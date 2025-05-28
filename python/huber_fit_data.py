"""
Data for fitting a 2D Huber distribution.

* Y: numpy array of data points with shape (N, n)
* n: dimension of the data points
* N: number of data points

* plot_fits(A, mu, savepath): function for plotting the density of the data points
    along with the density of the Huber and Gaussian fits. The plot is saved to the
    path specified by save_path.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Y.shape = (N, n)
N = 200
n = 2


# Generate the data Y
def randcov(n):
    """Generate a random covariance matrix."""
    A = np.random.randn(n, n)
    A = A @ A.T
    return A / np.max(np.abs(np.linalg.eigvals(A)))


np.random.seed(1)
Y = np.sqrt(0.6) * np.random.multivariate_normal(np.random.randn(n), randcov(n), N)
sel = np.random.choice(Y.shape[0], Y.shape[0] // 10, replace=False)
Y[sel] = np.sqrt(5) * np.random.randn(*Y[sel].shape)


def huber_function(x, M):
    """Huber function.

    Args:
        x (np.ndarray): Input array. Shape (N, n), where N is the number of data
            points and n is the dimension of the data.
        M (float): Huber threshold parameter.
    """
    res = np.zeros(x.shape[0])
    norms = np.linalg.norm(x, axis=1)
    res[norms <= M] = 0.5 * norms[norms <= M] ** 2
    res[norms > M] = M * (norms[norms > M] - 0.5 * M)
    return res


def log_likelihood(data, A, mu, M):
    """Data log likelihood for the 2D Huber distribution.

    Args:
        data (np.ndarray): data points. Shape (N, n), where N is the number of
            data points and n is the dimension of the data.
        A (np.ndarray): parameter matrix.
        mu (np.ndarray): parameter vector.
        M (float): Huber threshold parameter.

    Returns:
        float: The log likelihood of the data given the parameters.
    """
    A_inv = np.linalg.inv(A)
    if np.isfinite(M):
        # standard Huber integral for dimension n = 2, M = 1
        C = 0.09906747943445049
    else:
        # standard Gaussian integral for dimension n = 2
        C = 1.0 / (2 * np.pi)

    _, logabsdet = np.linalg.slogdet(A_inv)
    return np.sum(np.log(C) + logabsdet - huber_function((data - mu) @ A_inv.T, M))


def data_log_likelihood(A, mu):
    """Data log likelihood for the 2D Huber distribution with M = 1.

    Args:
        A (np.ndarray): parameter matrix.
        mu (np.ndarray): parameter vector.

    Returns:
        float: The log likelihood of the data given the parameters.
    """
    return log_likelihood(Y, A, mu, 1.0)


def plot_fits(A, mu, save_path=None):
    """
    Plots the density of a 2D Huber distribution along with the data. Also plots
    against the density of a 2D Gaussian distribution fit to the data.

    Parameters:
    A (numpy.ndarray): Parameter matrix.
    mu (numpy.ndarray): Parameter vector.
    M (float): The Huber distribution threshold. Corresponds to a Gaussian
        distribution if set to np.inf.
    save_path (str, optional): The path to save the plot. If None, the plot is not saved. Default is None.
    """
    resolution = 100

    # Gaussian fit
    mu_gaussian = np.mean(Y, axis=0)
    cov_gaussian = np.cov(Y, rowvar=False, bias=True)
    A_gaussian = np.linalg.cholesky(cov_gaussian)
    print(
        "Gaussian fit has log likelihood:",
        log_likelihood(Y, A_gaussian, mu_gaussian, np.inf),
    )

    def plot_density(ax, M, title, gaussian=False):
        x_min, x_max = np.min(Y[:, 0]), np.max(Y[:, 0])
        y_min, y_max = np.min(Y[:, 1]), np.max(Y[:, 1])
        x_grid = np.linspace(x_min, x_max, resolution)
        y_grid = np.linspace(y_min, y_max, resolution)
        X_mesh, Y_mesh = np.meshgrid(x_grid, y_grid)
        Z = np.zeros_like(X_mesh)
        for i in range(resolution):
            for j in range(resolution):
                z = np.array([[X_mesh[i, j], Y_mesh[i, j]]])
                if gaussian:
                    Z[i, j] = np.exp(log_likelihood(z, A_gaussian, mu_gaussian, np.inf))
                else:
                    Z[i, j] = np.exp(log_likelihood(z, A, mu, M))

        ax.scatter(Y[:, 0], Y[:, 1], c="red", s=4)
        ax.set_xlabel("y1")
        ax.set_ylabel("y2")
        ax.set_title(title)

        # Add contour lines for some confidence ellipsoids
        confidence_levels = [0.9]
        if gaussian:
            # compute 90% confidence level for Gaussian fit
            C = 1.0 / (2 * np.pi)
            detA = np.linalg.det(A_gaussian)
            chi2_values = chi2.ppf(confidence_levels, df=2)
            contour_levels = C / detA * np.exp(-0.5 * chi2_values)
            contour_levels.sort()
            contours = ax.contour(
                X_mesh,
                Y_mesh,
                Z,
                levels=contour_levels,
                colors="blue",
                linestyles="dashed",
            )
            data_ll = data_log_likelihood(A_gaussian, mu_gaussian)
        else:
            # compute 90% confidence level for Huber fit
            C = 0.09906747943445049
            detA = np.linalg.det(A)
            norm_values = [3.95]
            contour_levels = [
                C / detA * np.exp(-huber_function(np.array([r]).reshape(1, 1), 1)[0])
                for r in norm_values
            ]
            contour_levels.sort()
            contours = ax.contour(
                X_mesh,
                Y_mesh,
                Z,
                levels=contour_levels,
                colors="blue",
                linestyles="dashed",
            )
            data_ll = data_log_likelihood(A, mu)

        # Add labels to the contour lines
        fmt = {
            level: f"{int(conf * 100)}%"
            for level, conf in zip(contour_levels, confidence_levels)
        }
        ax.clabel(contours, fmt=fmt, inline=True, fontsize=12, colors="blue")
        ax.text(
            0.05,
            0.05,
            f"Data log-likelihood: {data_ll:.2f}",
            fontsize=12,
            color="black",
            transform=ax.transAxes,
            bbox=dict(facecolor="white", alpha=0.5),
        )

    # Plot the density of the Huber and Gaussian fits
    _, axs = plt.subplots(1, 2, figsize=(9, 4.5))

    plot_density(axs[0], np.inf, "Gaussian fit", gaussian=True)
    plot_density(axs[1], 1, "Huber fit")

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
        plt.close()
    plt.show()
