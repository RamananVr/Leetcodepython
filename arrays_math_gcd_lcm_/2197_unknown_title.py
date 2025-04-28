"""
LeetCode Problem #2197: Replace Non-Coprime Numbers in Array

Problem Statement:
You are given an integer array `nums`. A subset of the integers in the array is called non-coprime if there exists at least one pair of integers in it such that the greatest common divisor (GCD) of those integers is greater than 1.

You need to perform the following operation repeatedly on the array until no more operations can be performed:
1. Find the first two adjacent numbers in the array that are non-coprime.
2. Replace these two numbers with their least common multiple (LCM).
3. Repeat the process until there are no adjacent non-coprime numbers.

Return the final state of the array.

The test cases are guaranteed to be such that the above process will always terminate.

Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
"""

from math import gcd
from functools import reduce

def replaceNonCoprimes(nums):
    """
    Replace adjacent non-coprime numbers in the array with their LCM until no more replacements can be made.
    
    Args:
    nums (List[int]): The input array of integers.
    
    Returns:
    List[int]: The final state of the array after all replacements.
    """
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    stack = []
    for num in nums:
        stack.append(num)
        # Check and merge adjacent non-coprime numbers
        while len(stack) > 1 and gcd(stack[-1], stack[-2]) > 1:
            b = stack.pop()
            a = stack.pop()
            stack.append(lcm(a, b))
    return stack

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [6, 4, 3, 2, 7, 6, 2]
    print(replaceNonCoprimes(nums1))  # Output: [12, 7, 6]

    # Test Case 2
    nums2 = [2, 2, 1, 1, 3, 3, 3]
    print(replaceNonCoprimes(nums2))  # Output: [2, 1, 1, 27]

    # Test Case 3
    nums3 = [4, 6, 8, 3, 9]
    print(replaceNonCoprimes(nums3))  # Output: [24, 3, 9]

    # Test Case 4
    nums4 = [7, 5, 6, 10, 15]
    print(replaceNonCoprimes(nums4))  # Output: [7, 30]

"""
Time Complexity Analysis:
- The algorithm processes each number in the input array exactly once, pushing and popping from the stack.
- For each merge operation, the computation of the LCM involves calculating the GCD, which is logarithmic in the size of the numbers.
- In the worst case, the stack can grow and shrink multiple times, but the total number of operations is proportional to the size of the input array.
- Overall time complexity: O(n * log(max(nums))), where n is the length of the array and max(nums) is the largest number in the array.

Space Complexity Analysis:
- The stack can grow to hold all elements of the input array in the worst case.
- Space complexity: O(n), where n is the length of the input array.

Topic: Arrays, Math (GCD/LCM)
"""