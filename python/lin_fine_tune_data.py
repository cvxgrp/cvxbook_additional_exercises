"""
Data for linear fine tuning.

* x is a list of N numpy arrays of shape (d,). Each numpy array xi is an embedding
  of an exercise from Additional Exercises for Convex Optimization (March 2025)
* titles is a list of N strings. Each string is the title of the corresponding
  exercise. So, titles[i] is the title of the exercise with embedding embeddings[i].
* N is the number of embeddings
* d is the dimension of the embeddings.
* similar_pairs is a list of tuples of indices. Each tuple (i, j) represents a
  pair of exercises considered to be similar.
* dissimilar_pairs is a list of tuples of indices. Each tuple (i, j) represents a
  pair of exercises considered to be dissimilar.

Call the function compare_nearest_neighbors(F: np.ndarray) to compare the
nearest neighbors of two exercises before and after applying the linear fine
tuning F to the embeddings.
"""

import json
import urllib.request
import numpy as np

url = "https://raw.githubusercontent.com/cvxgrp/cvxbook_additional_exercises/main/python/ae_emb_data.txt"
with urllib.request.urlopen(url, timeout=10) as response:
    data = json.loads(response.read().decode("utf-8"))

# original N*d embedding vector x
x = [np.array(arr) for arr in data["embeddings"]]
titles = data["name"]
N = len(x)
d = len(x[0])


def find_nearest_neighbors(index: int, num_neighbors: int = 5, F=None) -> list[int]:
    """Find the nearest neighbors of the specified index. Apply the linear fine
    tuning F to the embeddings if F is not None."""
    query_embedding = x[index]
    if F is None:
        distances = np.linalg.norm(x - query_embedding, axis=1)
    else:
        distances = np.linalg.norm([F @ emb for emb in x] - F @ query_embedding, axis=1)
    nearest_indices = np.argsort(distances)[1 : num_neighbors + 1]
    return [int(k) for k in nearest_indices]


def compare_nearest_neighbors(F: np.ndarray) -> None:
    """print the nearest neighbors for the specified index."""
    for i in [138, 147]:
        print(f"'{titles[i]}' has")
        print("nearest neighbors before fine tuning:")
        for k, j in enumerate(find_nearest_neighbors(i, 5)):
            print(f"{k + 1}: {titles[j]}")
        print()
        print("nearest neighbors after fine tuning:")
        for k, j in enumerate(find_nearest_neighbors(i, 5, F)):
            print(f"{k + 1}: {titles[j]}")
        print()


# generate similar and dissimilar pairs
np.random.seed(0)
chapters = data["chapter"]

target_chapter_indices = [i for i in range(N) if chapters[i] == "finance"]

similar_pool = [k for k in range(N) if chapters[k] == "finance"]

similar_pairs = []
for i in similar_pool * 3:
    j = int(np.random.choice([k for k in similar_pool if k != i]))
    similar_pairs.append(tuple(sorted((i, j))))

dissimilar_pairs = []
for i in similar_pool:
    for j in find_nearest_neighbors(i, 10):
        if chapters[j] != chapters[i]:
            dissimilar_pairs.append(tuple(sorted((i, j))))

# similar_pairs (dissimilar_pairs) is a list of index pair (i,j)
similar_pairs = list(set(similar_pairs))
dissimilar_pairs = list(set(dissimilar_pairs))
