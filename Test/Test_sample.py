# Sample test run
import unittest
import sys

"""
import a function from another file in the same directory
"""

# Import the shortpath and floyd function
from floyd_recur_code import shortpath
from floyd_recur_code import floyd


# Test the main finding the shortest path function
class testpathSample(unittest.TestCase):

    def test_shortpath_function(self):
        NPATH = sys.maxsize
        graphfl = [[0, 7, NPATH, 8],
                   [NPATH, 0, 5, NPATH],
                   [NPATH, NPATH, 0, 2],
                   [NPATH, NPATH, NPATH, 0]]
        result = shortpath(0, 1, 3, graphfl)
        self.assertEqual(result, 7, "should be 7")


# Test the implemantation of recursion in Floyd function
class ResultTest(unittest.TestCase):

    def test_fl_function(self):
        NPATH = sys.maxsize
        graphfl = [[0, 7, NPATH, 8],
                   [NPATH, 0, 5, NPATH],
                   [NPATH, NPATH, 0, 2],
                   [NPATH, NPATH, NPATH, 0]]
        MAXL = len(graphfl[0])
        result_graph = [[0, 7, 12, 8],
                        [NPATH, 0, 5, 7],
                        [NPATH, NPATH, 0, 2],
                        [NPATH, NPATH, NPATH, 0]]
        result = floyd(graphfl)
        self.assertEqual(result, result_graph,"matching output")

    # Test with wrong input
    # as a string or a character instead of a integer,
    # the test fails
    def test_wronginput(self):
        NPATH = sys.maxsize
        graphfl = [[0, "No_Path", "No_Path", 8],
                   [NPATH, 0, 5, NPATH],
                   [NPATH, NPATH, 0, 2],
                   [NPATH, NPATH, NPATH, 0]]
        with self.assertRaises(TypeError):
            result = shorttpath(0, 1, 3, graphfl)

 
    # Test non-exist node
    def test_wrongnode(self):
        NPATH = sys.maxsize
        graphfl = [[0, 7, NPATH, 8],
                   [NPATH, 0, 5, NPATH],
                   [NPATH, NPATH, 0, 2],
                   [NPATH, NPATH, NPATH, 0]]
        with self.assertRaises(IndexError):
            result = shortpath(0, 10, 0, graphfl)

    # Test non-exist intermediate node
    def test_wrongintermediate(self):
        NPATH = sys.maxsize
        graphfl = [[0, 7, NPATH, 8],
                   [NPATH, 0, 5, NPATH],
                   [NPATH, NPATH, 0, 2],
                   [NPATH, NPATH, NPATH, 0]]
        with self.assertRaises(IndexError):
            result = shortpath(0, 1, 4, graphfl)


# Unit Tests
class TestFloyd(unittest.TestCase):

    def test_floyda(self):
        self.assertEqual(floyd(sample_a), output_a, "Incorrect Output")

    def test_floydb(self):
        self.assertEqual(floyd(sample_b), output_b, "Incorrect Output")

    def test_floydc(self):
        self.assertEqual(floyd(sample_c), output_c, "Incorrect Output")


if __name__ == '__main__':
    unittest.main()
