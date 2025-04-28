"""
LeetCode Question #2465: Number of Distinct Averages

Problem Statement:
You are given a 0-indexed integer array `nums` of even length.

For example, if `nums = [1, 2, 3, 4]`, the averages of pairs `(1, 4)` and `(2, 3)` are `(1 + 4) / 2 = 2.5` and `(2 + 3) / 2 = 2.5`.

Return the number of distinct averages that can be obtained from `nums`.

Note:
- The length of `nums` is guaranteed to be even.
- Each element in `nums` is an integer.

Constraints:
- `2 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

"""

# Solution
def distinctAverages(nums):
    """
    Calculate the number of distinct averages that can be obtained from the array.

    :param nums: List[int] - A list of integers of even length
    :return: int - The number of distinct averages
    """
    nums.sort()
    distinct_averages = set()
    left, right = 0, len(nums) - 1

    while left < right:
        avg = (nums[left] + nums[right]) / 2
        distinct_averages.add(avg)
        left += 1
        right -= 1

    return len(distinct_averages)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(distinctAverages(nums1))  # Output: 2

    # Test Case 2
    nums2 = [1, 100]
    print(distinctAverages(nums2))  # Output: 1

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5, 6]
    print(distinctAverages(nums3))  # Output: 3

    # Test Case 4
    nums4 = [10, 20, 30, 40, 50, 60]
    print(distinctAverages(nums4))  # Output: 3

    # Test Case 5
    nums5 = [1, 1, 1, 1]
    print(distinctAverages(nums5))  # Output: 1


# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The while loop runs for n/2 iterations, which is O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The space used by the `distinct_averages` set is O(k), where k is the number of distinct averages.
- Sorting the array may require O(n) space depending on the sorting algorithm.
- Overall space complexity: O(n).
"""

# Topic: Arrays