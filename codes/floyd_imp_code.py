#labeles are changed from FLW algorithm
import sys
import itertools

NPATH = sys.maxsize
graphfl = [[0, 7, NPATH, 8],
         [NPATH, 0, 5, NPATH],
         [NPATH, NPATH, 0, 2],
         [NPATH, NPATH, NPATH, 0]]
MAXL = len(graphfl[0])


def floyd(dist):
    """
    A simple implementation of Floyd's algorithm
    """
    for mid, begin, end
    in itertools.product(range(MAXL), range(MAXL),
                         range(MAXL)):

        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if begin == end:
            dist[begin][end] = 0
            continue

        # return all possible paths and find the minimum
        dist[begin][end] = min(dist[begin][end],
                               dist[begin][mid] +
                               dist[mid][end])

    #Any value that have sys.maxsize has no path
    print(dist)
floyd(graphfl)
