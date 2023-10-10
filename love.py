"""Algorithm to find three numbers in an array that sum up to a given value p."""
import unittest


def merge_sort(arr: list) -> list:
    """
    Sorts the given array using the merge sort algorithm.

    Args:
        arr: The array to be sorted.

    Returns:
        The sorted array.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left: list, right: list) -> list:
    """Merges two arrays into one sorted array"""
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def find_three_numbers(arr: list, p : int) -> bool:
    """
    Finds three numbers in the given array that sum up to the given value p.

    Args:
        arr: The array to search for three numbers.
        p: The target sum of three numbers.

    Returns:
        A list of three numbers that sum up to p, if found. Otherwise, returns None.
    """
    arr = merge_sort(arr)
    n = len(arr)
    count = 0
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        count += 1
        while left < right:
            count += 1
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == p:
                print(count)
                return True
            if current_sum < p:
                left += 1
            else:
                right -= 1
    return False


class TestFindThreeNumbers(unittest.TestCase):
    """Unit tests for find_three_numbers"""
    def test_find_three_numbers(self):
        """Test find_three_numbers"""
        arr = [1, 2, 3]
        p = 6
        self.assertTrue(find_three_numbers(arr, p))


print(find_three_numbers(
    [1, 2, 3, 999_999_999, 1_000_000_000, 2],
    2_000_000_002))
if __name__ == '__main__':
    unittest.main()
