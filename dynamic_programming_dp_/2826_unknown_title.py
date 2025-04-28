"""
LeetCode Problem #2826: Sorting Three Groups

Problem Statement:
You are given an array `nums` consisting of integers from 1 to 3, inclusive. You want to sort the array in non-decreasing order by performing the following operation any number of times:

- Choose any subarray of `nums` and reverse it.

Return the minimum number of operations required to sort the array.

Constraints:
- 1 <= nums.length <= 1000
- nums[i] is in the range [1, 3]
"""

def minimumOperations(nums):
    """
    This function calculates the minimum number of operations required to sort the array
    in non-decreasing order by reversing subarrays.

    Args:
    nums (List[int]): The input array consisting of integers from 1 to 3.

    Returns:
    int: The minimum number of operations required to sort the array.
    """
    n = len(nums)
    dp = [0] * 4  # dp[i] represents the minimum operations to make the array sorted up to group i (1, 2, or 3)

    for num in nums:
        for i in range(3, 0, -1):
            dp[i] = dp[i] + (num != i)
            if i > 1:
                dp[i] = min(dp[i], dp[i - 1])

    return min(dp[1:])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 1, 3, 1, 2, 2, 1]
    print(minimumOperations(nums1))  # Expected Output: 3

    # Test Case 2
    nums2 = [1, 3, 2, 1, 3, 2]
    print(minimumOperations(nums2))  # Expected Output: 3

    # Test Case 3
    nums3 = [1, 1, 1, 1]
    print(minimumOperations(nums3))  # Expected Output: 0

    # Test Case 4
    nums4 = [3, 3, 3, 3]
    print(minimumOperations(nums4))  # Expected Output: 0

    # Test Case 5
    nums5 = [1, 2, 3]
    print(minimumOperations(nums5))  # Expected Output: 0

"""
Time Complexity Analysis:
- The algorithm iterates through the input array `nums` once, and for each element, it updates the `dp` array in constant time.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The algorithm uses a fixed-size array `dp` of size 4, which does not depend on the input size.
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""