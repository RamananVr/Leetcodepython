"""
LeetCode Problem #922: Sort Array By Parity II

Problem Statement:
Given an array of integers `nums` of size `n`, where `n` is even. The array is 
composed of `n / 2` even integers and `n / 2` odd integers.

Sort the array such that whenever `nums[i]` is at an even index `i`, `nums[i]` 
is even, and whenever `nums[i]` is at an odd index `i`, `nums[i]` is odd.

Return any array that satisfies this condition.

Constraints:
1. 2 <= nums.length <= 2 * 10^4
2. nums.length is even.
3. Half of the integers in nums are even.
4. 0 <= nums[i] <= 1000

Example 1:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example 2:
Input: nums = [2,3]
Output: [2,3]

Follow-Up:
Can you do it in-place without using extra space?
"""

def sortArrayByParityII(nums):
    """
    Sorts the array such that even indices contain even numbers and odd indices contain odd numbers.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    List[int]: The sorted array satisfying the parity condition.
    """
    n = len(nums)
    even_index, odd_index = 0, 1
    result = [0] * n

    for num in nums:
        if num % 2 == 0:  # Even number
            result[even_index] = num
            even_index += 2
        else:  # Odd number
            result[odd_index] = num
            odd_index += 2

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 2, 5, 7]
    print(sortArrayByParityII(nums1))  # Output: [4, 5, 2, 7] or other valid outputs

    # Test Case 2
    nums2 = [2, 3]
    print(sortArrayByParityII(nums2))  # Output: [2, 3]

    # Test Case 3
    nums3 = [10, 3, 8, 5, 2, 7]
    print(sortArrayByParityII(nums3))  # Output: [10, 3, 8, 5, 2, 7] or other valid outputs

    # Test Case 4
    nums4 = [6, 1, 4, 3]
    print(sortArrayByParityII(nums4))  # Output: [6, 1, 4, 3] or other valid outputs

"""
Time Complexity:
- O(n): We iterate through the input array `nums` once, where `n` is the length of the array.

Space Complexity:
- O(n): We use an additional array `result` of size `n` to store the output.

Topic: Arrays
"""