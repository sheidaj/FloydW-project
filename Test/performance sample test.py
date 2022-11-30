#Sample test run
import unittest
import sys


from floyd_recur_code import shorttpath
from floyd_recur_code import floyd


# Test the main Recursive function
class ShortpathSample(unittest.Sample):

    def test_to_shortpath_function(self):
        NPATH = sys.maxsize
        graphfl = [[0, 7, NPATH, 8],
                 [NPATH, 0, 5, NPATH],
                 [NPATH, NPATH, 0, 2],
                 [NPATH, NPATH, NPATH, 0]]
        result = shortpath(0, 1, 3, graphfl)
        self.assertEqual(result, 7, "hint if needed")


# Test the Floyd function known as FLW
class FloydOutputTest(unittest.Testn):

    def test_flw_function(self):
        NPATH = sys.maxsize
        graphfl = [[0, 7, NPATH, 8],
                 [NPATH, 0, 5, NPATH],
                 [NPATH, NPATH, 0, 2],
                 [NPATH, NPATH, NPATH, 0]]
        MAXL = len(graphfl[0])
        shortest_graph = [[0, 7, 12, 8],
                          [NPATH, 0, 5, 7],
                          [NPATH, NPATH, 0, 2],
                          [NPATH, NPATH, NPATH, 0]]
        result = floyd(graphfl)
        self.assertEqual(result, shortest_graph,"hint if needed")

    # Test the function failures with incorrect input
    # If you pass a string or a character instead of a integer
    # the test fails
    def test_inputfailure_function(self):
        NPATH = sys.maxsize
        graphfl = [[0, "x", NPATH, 8],
                 [NPATH, 0, 5, NPATH],
                 [NPATH, NPATH, 0, 2],
                 [NPATH, NPATH, NPATH, 0]]
        with self.assertRaises(TypeError):
            result = shorttpath(0, 1, 3, graphfl)

    # testing a use case where there is only one node
    def test_testonenode_function(self):
        NPATH = sys.maxsize
        graphfl = [[0]]
        result = shortpath(0, 0, 0, graphfl)
        self.assertEqual(result, 0)

    # Test non-existent node
    def test_nodepath_function(self):
        NPATH = sys.maxsize
        graphfl = [[0, 7, NPATH, 8],
                 [NPATH, 0, 5, NPATH],
                 [NPATH, NPATH, 0, 2],
                 [NPATH, NPATH, NPATH, 0]]
        with self.assertRaises(IndexError):
            result = shortpath(0, 4, 0, graphfl)

    # Test non-existent intermediary node
    def test_noninternode_function(self):
        NPATH = sys.maxsize
        graphfl = [[0, 7, NPATH, 8],
                 [NPATH, 0, 5, NPATH],
                 [NPATH, NPATH, 0, 2],
                 [NPATH, NPATH, NPATH, 0]]
        with self.assertRaises(IndexError):
            result = shortpath(0, 1, 4, graphfl)

