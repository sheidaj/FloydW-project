# Test samples for Floyd Warshall Function

""" This file contains four different samples for 
the Floyd Warshall algorithm function.
"""

# Use value for infinity to denote edges that do not exist
INF = 999999

# Test A: Control Graph
""" Title: Floyd Warshall Algorithm | DP-16
Author: GeeksforGeeks
Availability: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
"""
sample_a = [[0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]]

output_a = [[0, 5, 8, 9],
            [INF, 0, 3, 4],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]]

# Test B: Negative Edges Graph (No Negative Cycles)
sample_b = [[0, 12, INF, 5],
            [INF, 0, INF, 4],
            [INF, INF, 0, -2],
            [INF, INF, 5, 0]]

output_b = [[0, 12, 10, 5],
            [INF, 0, 9, 4],
            [INF, INF, 0, -2],
            [INF, INF, 5, 0]]

# Test C: Small Graph (Three Vertices)
sample_c = [[0, INF, 10],
            [INF, 0, INF],
            [INF, 2, 0]]

output_c = [[0, 12, 10],
            [INF, 0, INF],
            [INF, 2, 0]]
