using PyCall
py"""
import sys 
import os
sys.path.append(os.getcwd())
from allocate_memory_data import plot_memory, C, D, c, b
"""

function plot_memory(M)
    return py"""plot_memory($M, save_file="allocating_memory_jl.pdf")"""
end
C = py"""C"""
D = py"""D"""
c = py"""c"""
b = py"""b"""

