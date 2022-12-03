# Performance Tests for floyd Function

import sys

# Import Floyd Warshall function
from floyd_recur_code import floyd

# Import Floyd sample cases
from samples import (sample_a, sample_b, sample_c)

# Import testing package
import cProfile

# Performance Tests
cProfile.run("floyd(sample_a)")

cProfile.run("floyd(sample_b)")

cProfile.run("floyd(sample_c)")
