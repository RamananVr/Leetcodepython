"""
LeetCode Problem #1018: Binary Prefix Divisible By 5

Problem Statement:
You are given a binary array `nums` (a list of 0s and 1s).

A binary prefix is a subarray of the binary array starting at index 0. For example, if `nums = [0, 1, 1]`, then the prefixes are:
- [0] (binary 0)
- [0, 1] (binary 01 or decimal 1)
- [0, 1, 1] (binary 011 or decimal 3)

Return a list of booleans `answer`, where `answer[i]` is `True` if the binary number represented by the prefix `nums[0]` to `nums[i]` is divisible by 5.

Example:
Input: nums = [0, 1, 1]
Output: [True, False, False]
Explanation:
- The binary number "0" is 0 in decimal, which is divisible by 5.
- The binary number "01" is 1 in decimal, which is not divisible by 5.
- The binary number "011" is 3 in decimal, which is not divisible by 5.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
"""

# Python Solution
from typing import List

def prefixesDivBy5(nums: List[int]) -> List[bool]:
    result = []
    current_number = 0

    for num in nums:
        # Update the current number in binary
        current_number = (current_number * 2 + num) % 5
        # Check divisibility by 5
        result.append(current_number == 0)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [0, 1, 1]
    print(prefixesDivBy5(nums1))  # Output: [True, False, False]

    # Test Case 2
    nums2 = [1, 0, 1, 1, 1]
    print(prefixesDivBy5(nums2))  # Output: [False, False, False, False, False]

    # Test Case 3
    nums3 = [0, 0, 0]
    print(prefixesDivBy5(nums3))  # Output: [True, True, True]

    # Test Case 4
    nums4 = [1, 1, 1, 0, 1]
    print(prefixesDivBy5(nums4))  # Output: [False, False, False, False, False]

    # Test Case 5
    nums5 = [1, 0, 0, 0, 0]
    print(prefixesDivBy5(nums5))  # Output: [False, False, False, False, True]

"""
Time Complexity Analysis:
- The algorithm iterates through the `nums` array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array `nums`.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space to store the `current_number` and the `result` list.
- Therefore, the space complexity is O(n) for the output list, but the algorithm itself uses O(1) additional space.

Topic: Arrays, Bit Manipulation
"""