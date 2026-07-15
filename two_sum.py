"""
Two Sum
Given an array of integers and a target, return indices of the two numbers
that add up to the target.

Approach: single pass with a hash map of value -> index.
Time: O(n)   Space: O(n)
"""


def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    print("All tests passed.")
