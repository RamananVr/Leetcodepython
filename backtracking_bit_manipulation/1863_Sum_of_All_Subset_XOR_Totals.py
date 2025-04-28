"""
LeetCode Problem #1863: Sum of All Subset XOR Totals

Problem Statement:
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

- For example, the XOR total of the array [2, 5, 6] is 2 XOR 5 XOR 6 = 1.

Given an array nums, return the sum of all XOR totals for every subset of nums.

Note: Subsets with the same elements should be counted multiple times as different subsets.

Example 1:
Input: nums = [1,3]
Output: 6
Explanation: The 4 subsets of [1,3] are:
- The empty subset has an XOR total of 0.
- [1] has an XOR total of 1.
- [3] has an XOR total of 3.
- [1,3] has an XOR total of 1 XOR 3 = 2.
0 + 1 + 3 + 2 = 6

Example 2:
Input: nums = [5,1,6]
Output: 28
Explanation: The 8 subsets of [5,1,6] are:
- The empty subset has an XOR total of 0.
- [5] has an XOR total of 5.
- [1] has an XOR total of 1.
- [6] has an XOR total of 6.
- [5,1] has an XOR total of 5 XOR 1 = 4.
- [5,6] has an XOR total of 5 XOR 6 = 3.
- [1,6] has an XOR total of 1 XOR 6 = 7.
- [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28

Example 3:
Input: nums = [0]
Output: 0

Constraints:
- 1 <= nums.length <= 12
- 0 <= nums[i] <= 20
"""

# Clean and Correct Python Solution
def subsetXORSum(nums):
    def dfs(index, current_xor):
        # Base case: if we've processed all elements
        if index == len(nums):
            return current_xor
        
        # Recursive case: include or exclude the current element
        include = dfs(index + 1, current_xor ^ nums[index])  # Include nums[index]
        exclude = dfs(index + 1, current_xor)               # Exclude nums[index]
        
        return include + exclude

    # Start DFS from index 0 with an initial XOR of 0
    return dfs(0, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3]
    print(f"Input: {nums1}, Output: {subsetXORSum(nums1)}")  # Expected Output: 6

    # Test Case 2
    nums2 = [5, 1, 6]
    print(f"Input: {nums2}, Output: {subsetXORSum(nums2)}")  # Expected Output: 28

    # Test Case 3
    nums3 = [0]
    print(f"Input: {nums3}, Output: {subsetXORSum(nums3)}")  # Expected Output: 0

    # Test Case 4
    nums4 = [2, 4, 6]
    print(f"Input: {nums4}, Output: {subsetXORSum(nums4)}")  # Expected Output: 28

    # Test Case 5
    nums5 = [1, 2, 3]
    print(f"Input: {nums5}, Output: {subsetXORSum(nums5)}")  # Expected Output: 24

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function explores all subsets of the input array. For an array of size n, there are 2^n subsets.
- For each subset, we perform a constant amount of work (computing XOR).
- Therefore, the time complexity is O(2^n).

Space Complexity:
- The space complexity is O(n) due to the recursion stack, where n is the length of the input array.

Overall:
Time Complexity: O(2^n)
Space Complexity: O(n)
"""

# Topic: Backtracking, Bit Manipulation