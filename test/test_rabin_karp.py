import unittest
import sys

sys.path.append("/Users/ledan404/projects/labs_algo/lab6")
from src.rabin_karp import search


class TestSearchFunction(unittest.TestCase):
    """
    Test the search function in rabin_karp.py
    """

    def test_search_successful(self):
        """
        Test the search function when the pattern is found in the string.
        """
        haystack = "GEEKS FOR GEEKS"
        needle = "GEEK"
        expected_output = [0, 10]
        with self.subTest():
            self.assertListEqual(search(needle, haystack), expected_output)


if __name__ == "__main__":
    unittest.main()
