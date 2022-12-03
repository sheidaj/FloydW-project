# Test samples for Floyd Warshall Function

""" This file contains four different samples for the Floyd Warshall
algorithm function.
"""

# Use value for infinity to denote edges that do not exist
import itertools
import sys
#Npath is no direct path
NPATH = sys.maxsize


sample_a = [[0, 5, NPATH, 10], 
            [NPATH, 0, 3, NPATH], 
            [NPATH, NPATH, 0, 1], 
            [NPATH, NPATH, NPATH, 0]]

output_a = [[0, 5, 8, 9], 
            [NPATH, 0, 3, 4], 
            [NPATH, NPATH, 0, 1], 
            [NPATH, NPATH, NPATH, 0]]

# Test B: Negative Edges Graph (No Negative Cycles)
sample_b = [[0, 12, NPATH, 5], 
            [NPATH, 0, NPATH, 4], 
            [NPATH, NPATH, 0, -2], 
            [NPATH, NPATH, 5, 0]]

output_b = [[0, 12, 10, 5], 
            [NPATH, 0, 9, 4], 
            [NPATH, NPATH, 0, -2], 
            [NPATH, NPATH, 5, 0]]

# Test C: Small Graph (Three Vertices)
sample_c = [[0, NPATH, 10], 
            [NPATH, 0, NPATH], 
            [NPATH, 2, 0]]

output_c = [[0, 12, 10],
            [NPATH, 0, NPATH],
            [NPATH, 2, 0]]
