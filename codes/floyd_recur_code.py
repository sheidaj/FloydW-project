# python3 using recursion

import sys
import itertools

from sys import maxsize
NPATH = sys.maxsize
graphfl = [[0, 7, NPATH, 8], [NPATH, 0, 5, NPATH], 
           [NPATH, NPATH, 0, 2], 
           [NPATH, NPATH, NPATH, 0]]
MAXL = len(graphfl[0])

# New function introduced here to claculate 
# the shortest distance using a recursive function
# 
def shortpath (begin, end, mid, dist):
    """
    An implementation of Floyd's algorithm using recursion
    """
    # When all nodes have been checked new function holds
    # the shortest direct paths and exits the recursion
    if mid < 0:
        return(dist[begin][end])
        
 # Return the min between two paths with a different nodes,
 # compares the distance of any possible paths, direct or
 # indirect path include middle node

    return min(shortpath(begin, end, mid - 1, dist), 
               shortpath(begin, mid, mid - 1, dist) + 
               shortpath(mid, end, mid - 1, dist))

# This function is followed from the imperative function code

def floyd(dist): 
    # Calculate the possible route combinations
    for begin, end in itertools.product(range(MAXL), 
                                        range(MAXL)):
        
        # Obviously if start point and end point are the same
        # then the distance is zero
        if begin == end:
            dist[begin][end] = 0
            continue
        dist[begin][end] = shortpath(begin, end, MAXL -1, dist)
    return dist


if __name__ == '__main__':
    #When all conditions been checked
    # Calls the function floyd and passes the definition of graph
    print(floyd(graphfl))

