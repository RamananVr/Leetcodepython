"""
LeetCode Question #260: Single Number III

Problem Statement:
Given an integer array `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice, 
find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation: [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]

Example 3:
Input: nums = [0,1]
Output: [1,0]

Constraints:
- 2 <= nums.length <= 3 * 10^4
- -2^31 <= nums[i] <= 2^31 - 1
- Each integer in `nums` will appear exactly twice, except for two integers which will appear only once.
"""

# Clean, Correct Python Solution
def singleNumber(nums):
    """
    Find the two numbers that appear only once in the array.

    Args:
    nums (List[int]): The input array.

    Returns:
    List[int]: A list containing the two numbers that appear only once.
    """
    # Step 1: XOR all numbers to get the XOR of the two unique numbers
    xor_result = 0
    for num in nums:
        xor_result ^= num

    # Step 2: Find the rightmost set bit in xor_result
    # This bit differentiates the two unique numbers
    diff_bit = xor_result & -xor_result

    # Step 3: Divide numbers into two groups based on the diff_bit
    num1, num2 = 0, 0
    for num in nums:
        if num & diff_bit:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 1, 3, 2, 5]
    print(singleNumber(nums1))  # Output: [3, 5] or [5, 3]

    # Test Case 2
    nums2 = [-1, 0]
    print(singleNumber(nums2))  # Output: [-1, 0] or [0, -1]

    # Test Case 3
    nums3 = [0, 1]
    print(singleNumber(nums3))  # Output: [1, 0] or [0, 1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm performs a single pass to XOR all elements (O(n)).
- Then, it performs another pass to divide the elements into two groups based on the diff_bit (O(n)).
- Overall, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses constant extra space (O(1)).
- No additional data structures are used, and the space usage does not depend on the input size.

Topic: Bit Manipulation
"""