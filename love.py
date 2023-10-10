import unittest


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
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


def find_three_numbers(arr, p):
    arr = merge_sort(arr)
    N = len(arr)
    count = 0
    for i in range(N - 2):
        left = i + 1
        right = N - 1
        count += 1
        while left < right:
            count += 1
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == p:
                print(count)
                return True
            elif current_sum < p:
                left += 1
            else:
                right -= 1
    return False


class TestFindThreeNumbers(unittest.TestCase):
    def test_find_three_numbers(self):
        arr = [1, 2, 3]
        p = 6
        self.assertTrue(find_three_numbers(arr, p))


print(find_three_numbers(
    [1, 2, 3, 999_999_999, 1_000_000_000, 2], 2_000_000_002))
if __name__ == '__main__':
    unittest.main()
