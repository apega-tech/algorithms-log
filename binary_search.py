"""
Binary Search
Find the index of a target value in a sorted array, or -1 if not present.

Approach: classic divide-and-conquer binary search.
Time: O(log n)   Space: O(1)
"""


def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(data, 7) == 3
    assert binary_search(data, 1) == 0
    assert binary_search(data, 100) == -1
    print("All tests passed.")
