"""
Maximum Subarray (Kadane's Algorithm)
Find the contiguous subarray with the largest sum.

Approach: track the best sum ending at the current index, and the best
seen so far. Reset the running sum when it drops below zero.
Time: O(n)   Space: O(1)
"""


def max_subarray(nums):
    best = current = nums[0]
    for n in nums[1:]:
        current = max(n, current + n)
        best = max(best, current)
    return best


if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([-1, -2, -3]) == -1
    print("All tests passed.")
