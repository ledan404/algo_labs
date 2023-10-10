"""Zenyk and Maricka test"""
import unittest
from zig_zag import robot_gardener


class TestRobotGardener(unittest.TestCase):
    """
    Unit tests for robot_gardener
    """

    def test_case_1(self):
        """
        Test case 1
        """
        m = 5
        n = 5
        garden = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected_result = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11,
                           12, 13, 14, 15, 20, 19, 18, 17, 16, 21, 22, 23, 24, 25]
        self.assertEqual(robot_gardener(m, n, garden), expected_result)

    def test_case_2(self):
        """
        Test case 2
        """
        m = 2
        n = 4
        garden = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        expected_result = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(robot_gardener(m, n, garden), expected_result)

    def test_case_3(self):
        """
        Test case 3
        """
        m = 1
        n = 1
        garden = [[1]]
        expected_result = [1]
        self.assertEqual(robot_gardener(m, n, garden), expected_result)

    def test_case_4(self):
        """
        Test case 4
        """
        m = 6
        n = 6
        garden = [
            [1, 2, 3, 4, 5, 6],
            [12, 11, 10, 9, 8, 7],
            [13, 14, 15, 16, 17, 18],
            [24, 23, 22, 21, 20, 19],
            [25, 26, 27, 28, 29, 30],
            [36, 35, 34, 33, 32, 31]
        ]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                           13, 14, 15, 16, 17,18, 19, 20, 21, 22, 23, 24,
                           25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        self.assertEqual(robot_gardener(m, n, garden), expected_result)


if __name__ == '__main__':
    unittest.main()
