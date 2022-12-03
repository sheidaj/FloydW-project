# Compare between the imperative and recursive

import sys
import time

# Calling two codes to compare
import floyd_imper_code
import floyd_recur_code

# This function will run the code and record the time
def compare_performance():
    # helper script
    NPATH = sys.maxsize
    graphfl = [[0, 7, NPATH, 8],
               [NPATH, 0, 5, NPATH],
               [NPATH, NPATH, 0, 2],
               [NPATH, NPATH, NPATH, 0]]

    record_ing = time.time()
    for _ in range(2**12):
        floyd_recur_code.floyd(graphfl)
    elapsed_recur = time.time() - record_ing

    record_ing = time.time()
    for _ in range(2**12):
        floyd_imper_code.floyd(graphfl)
    elapsed_imper = time.time() - record_ing

    return (elapsed_recur, elapsed_imper)


if __name__ == '__main__':
    elapsed_recur, elapsed_imper = compare_performance()
    print('recursive: {}s'.format(round(elapsed_recur, 2)))
    print('imperative: {}s'.format(round(elapsed_imper, 2)))
