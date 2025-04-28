"""
LeetCode Problem #1664: Ways to Make a Fair Array

Problem Statement:
You are given an integer array `nums`. You can choose exactly one index (0-indexed) and remove the element at that index. 
An array is fair if the sum of the elements at even indices equals the sum of the elements at odd indices.

Return the number of indices that you could remove to make the array fair.

Example 1:
Input: nums = [2,1,6,4]
Output: 1
Explanation:
Remove index 1: [2,6,4] -> Even indices sum = 2 + 4 = 6, Odd indices sum = 6.

Example 2:
Input: nums = [1,1,1]
Output: 3
Explanation:
You can remove any index and the array will be fair.

Example 3:
Input: nums = [1,2,3]
Output: 0
Explanation:
No index can be removed to make the array fair.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
"""

def waysToMakeFair(nums):
    """
    Function to calculate the number of indices that can be removed to make the array fair.
    
    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The number of indices that can be removed to make the array fair.
    """
    n = len(nums)
    total_even, total_odd = 0, 0
    for i in range(n):
        if i % 2 == 0:
            total_even += nums[i]
        else:
            total_odd += nums[i]
    
    left_even, left_odd = 0, 0
    count = 0
    
    for i in range(n):
        # Remove nums[i], calculate new even and odd sums
        if i % 2 == 0:
            total_even -= nums[i]
        else:
            total_odd -= nums[i]
        
        # Check if the array is fair after removing nums[i]
        if left_even + total_odd == left_odd + total_even:
            count += 1
        
        # Update left sums
        if i % 2 == 0:
            left_even += nums[i]
        else:
            left_odd += nums[i]
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 1, 6, 4]
    print(waysToMakeFair(nums1))  # Output: 1

    # Test Case 2
    nums2 = [1, 1, 1]
    print(waysToMakeFair(nums2))  # Output: 3

    # Test Case 3
    nums3 = [1, 2, 3]
    print(waysToMakeFair(nums3))  # Output: 0

    # Test Case 4
    nums4 = [1]
    print(waysToMakeFair(nums4))  # Output: 1

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5, 6]
    print(waysToMakeFair(nums5))  # Output: 0

"""
Time Complexity:
- The solution iterates through the array twice: once to calculate the total sums of even and odd indices, 
  and once to check each index for fairness. Thus, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The solution uses a constant amount of extra space for variables (e.g., total_even, total_odd, left_even, left_odd). 
  Therefore, the space complexity is O(1).

Topic: Arrays
"""