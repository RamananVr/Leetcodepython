"""
LeetCode Problem #421: Maximum XOR of Two Numbers in an Array

Problem Statement:
Given an integer array `nums`, return the maximum result of `nums[i] XOR nums[j]`, where `0 <= i, j < nums.length` and `i != j`.

Example 1:
Input: nums = [3, 10, 5, 25, 2, 8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:
Input: nums = [0]
Output: 0

Example 3:
Input: nums = [2, 4]
Output: 6
Explanation: The maximum result is 2 XOR 4 = 6.

Example 4:
Input: nums = [8, 10, 2]
Output: 10

Example 5:
Input: nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
Output: 127

Constraints:
- 1 <= nums.length <= 2 * 10^5
- 0 <= nums[i] <= 2^31 - 1
"""

# Clean and Correct Python Solution
class Solution:
    def findMaximumXOR(self, nums):
        """
        Finds the maximum XOR of two numbers in the array.

        :param nums: List[int] - The input array of integers.
        :return: int - The maximum XOR value.
        """
        # Initialize the maximum XOR and the mask
        max_xor = 0
        mask = 0

        # Iterate over the bits from the most significant to the least significant
        for i in range(31, -1, -1):
            # Update the mask to include the current bit
            mask |= (1 << i)
            # Store prefixes of all numbers with the current mask
            prefixes = {num & mask for num in nums}

            # Assume the current bit in max_xor is 1
            candidate = max_xor | (1 << i)

            # Check if there are two prefixes that can achieve the candidate XOR
            for prefix in prefixes:
                if candidate ^ prefix in prefixes:
                    max_xor = candidate
                    break

        return max_xor

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1 = [3, 10, 5, 25, 2, 8]
    print("Test Case 1 Output:", solution.findMaximumXOR(nums1))  # Expected: 28

    # Test Case 2
    nums2 = [0]
    print("Test Case 2 Output:", solution.findMaximumXOR(nums2))  # Expected: 0

    # Test Case 3
    nums3 = [2, 4]
    print("Test Case 3 Output:", solution.findMaximumXOR(nums3))  # Expected: 6

    # Test Case 4
    nums4 = [8, 10, 2]
    print("Test Case 4 Output:", solution.findMaximumXOR(nums4))  # Expected: 10

    # Test Case 5
    nums5 = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
    print("Test Case 5 Output:", solution.findMaximumXOR(nums5))  # Expected: 127

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop runs for 32 iterations (since integers are at most 32 bits).
- For each iteration, we iterate through the `nums` array to compute prefixes, which takes O(n) time.
- Checking for the candidate XOR in the set of prefixes is O(1) for each prefix.
- Overall time complexity: O(32 * n) = O(n).

Space Complexity:
- We use a set to store prefixes, which requires O(n) space.
- Overall space complexity: O(n).
"""

# Topic: Bit Manipulation