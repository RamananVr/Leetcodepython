"""
LeetCode Problem #910: Smallest Range II

Problem Statement:
You are given an integer array `nums` and an integer `k`. For each index `i` where `0 <= i < nums.length`, 
change `nums[i]` to be either `nums[i] + k` or `nums[i] - k`. The score of `nums` is the difference between 
the maximum and minimum elements in `nums`.

Return the minimum score of `nums` after changing the values at each index.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^4
- 0 <= k <= 10^4
"""

# Solution
def smallestRangeII(nums, k):
    """
    Finds the minimum score of nums after modifying each element by either +k or -k.

    :param nums: List[int] - The input array of integers.
    :param k: int - The value to add or subtract from each element.
    :return: int - The minimum score of nums after modification.
    """
    nums.sort()
    n = len(nums)
    result = nums[-1] - nums[0]  # Initial range without any modification

    for i in range(n - 1):
        high = max(nums[-1] - k, nums[i] + k)
        low = min(nums[0] + k, nums[i + 1] - k)
        result = min(result, high - low)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1]
    k1 = 0
    print(smallestRangeII(nums1, k1))  # Expected Output: 0

    # Test Case 2
    nums2 = [0, 10]
    k2 = 2
    print(smallestRangeII(nums2, k2))  # Expected Output: 6

    # Test Case 3
    nums3 = [1, 3, 6]
    k3 = 3
    print(smallestRangeII(nums3, k3))  # Expected Output: 3

    # Test Case 4
    nums4 = [7, 8, 8]
    k4 = 5
    print(smallestRangeII(nums4, k4))  # Expected Output: 1

    # Test Case 5
    nums5 = [4, 8, 2, 7, 3]
    k5 = 5
    print(smallestRangeII(nums5, k5))  # Expected Output: 6

"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The loop iterates through the array once, which is O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation is in-place, and we use a constant amount of extra space.
- Overall space complexity: O(1).

Topic: Arrays, Greedy
"""