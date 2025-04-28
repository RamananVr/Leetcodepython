"""
LeetCode Problem #2870: Minimum Number of Operations to Make Array Equal

Problem Statement:
You are given two integer arrays `nums1` and `nums2` of length `n`.

In one operation, you can:
- Choose any index `i` (0 <= i < n) and increment `nums1[i]` by 1.
- Choose any index `i` (0 <= i < n) and decrement `nums1[i]` by 1.

Your goal is to make `nums1` equal to `nums2`. Return the minimum number of operations required to achieve this. If it is impossible to make `nums1` equal to `nums2`, return -1.

Example:
Input: nums1 = [1, 2, 3], nums2 = [2, 2, 2]
Output: 2
Explanation: Increment nums1[0] once and decrement nums1[2] once.

Constraints:
- `nums1.length == nums2.length == n`
- `1 <= n <= 10^5`
- `1 <= nums1[i], nums2[i] <= 10^9`
"""

# Solution
def minOperations(nums1, nums2):
    """
    Calculate the minimum number of operations to make nums1 equal to nums2.

    Args:
    nums1 (List[int]): The first array.
    nums2 (List[int]): The second array.

    Returns:
    int: The minimum number of operations required, or -1 if impossible.
    """
    # Calculate the total difference between nums1 and nums2
    total_diff = sum(nums2) - sum(nums1)
    
    # If the total difference is not zero, it's impossible to make the arrays equal
    if total_diff != 0:
        return -1
    
    # Calculate the absolute differences for each index
    abs_diff = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
    
    # Return the sum of absolute differences as the minimum number of operations
    return sum(abs_diff)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    nums2 = [2, 2, 2]
    print(minOperations(nums1, nums2))  # Output: 2

    # Test Case 2
    nums1 = [1, 1, 1]
    nums2 = [1, 1, 1]
    print(minOperations(nums1, nums2))  # Output: 0

    # Test Case 3
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print(minOperations(nums1, nums2))  # Output: -1

    # Test Case 4
    nums1 = [10, 20, 30]
    nums2 = [30, 20, 10]
    print(minOperations(nums1, nums2))  # Output: 40

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the sum of nums1 and nums2 takes O(n).
- Calculating the absolute differences takes O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(n) due to the `abs_diff` list.

Topic: Arrays
"""