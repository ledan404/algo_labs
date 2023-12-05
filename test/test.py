import unittest
import sys

sys.path.append("/Users/ledan404/projects/labs_algo/6lab1")
from src.rabin_karp import rabin_karp


class TestRabinKarpAlgorithm(unittest.TestCase):
    def test_rabin_karp(self):
        # Test case 1
        haystack_1 = "abracadabraabra"
        needle_1 = "abra"
        output_1 = rabin_karp(haystack_1, needle_1)
        self.assertEqual(output_1, [0, 7, 11])

        # Test case 2
        haystack_2 = "abcdabcdabcd"
        needle_2 = "abc"
        output_2 = rabin_karp(haystack_2, needle_2)
        self.assertEqual(output_2, [0, 4, 8])

        # Test case 3
        haystack_3 = "aaaaa"
        needle_3 = "aa"
        output_3 = rabin_karp(haystack_3, needle_3)
        self.assertEqual(output_3, [0, 1, 2, 3])

        # Add more test cases as needed


if __name__ == "__main__":
    unittest.main()
