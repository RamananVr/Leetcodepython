"""
LeetCode Problem #136: Single Number

Problem Statement:
Given a non-empty array of integers `nums`, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element in the array appears twice except for one element which appears only once.
"""

# Solution
def singleNumber(nums):
    """
    Finds the single number in the array where every other number appears twice.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The single number that appears only once.
    """
    result = 0
    for num in nums:
        result ^= num  # XOR operation
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 2, 1]
    print(f"Input: {nums1} -> Output: {singleNumber(nums1)}")  # Expected Output: 1

    # Test Case 2
    nums2 = [4, 1, 2, 1, 2]
    print(f"Input: {nums2} -> Output: {singleNumber(nums2)}")  # Expected Output: 4

    # Test Case 3
    nums3 = [1]
    print(f"Input: {nums3} -> Output: {singleNumber(nums3)}")  # Expected Output: 1

    # Test Case 4
    nums4 = [0, 1, 0]
    print(f"Input: {nums4} -> Output: {singleNumber(nums4)}")  # Expected Output: 1

    # Test Case 5
    nums5 = [7, 3, 5, 3, 5]
    print(f"Input: {nums5} -> Output: {singleNumber(nums5)}")  # Expected Output: 7

"""
Time Complexity Analysis:
- The solution iterates through the array once, performing an XOR operation for each element.
- XOR is a constant-time operation, so the time complexity is O(n), where n is the length of the array.

Space Complexity Analysis:
- The solution uses a single variable `result` to store intermediate XOR results.
- No additional data structures are used, so the space complexity is O(1).

Topic: Arrays, Bit Manipulation
"""