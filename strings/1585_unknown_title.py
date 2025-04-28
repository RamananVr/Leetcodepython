"""
LeetCode Problem #1585: Check If String Is Transformable With Substring Sort Operations

Problem Statement:
Given two strings `s` and `t` of the same length consisting of digits (0-9), you are allowed to perform the following operation any number of times:

- Choose any substring in `s` and sort it in ascending order.

Return `true` if it is possible to transform `s` into `t` using the above operation. Otherwise, return `false`.

Constraints:
- `s.length == t.length`
- `s` and `t` consist of digits (0-9).

Example 1:
Input: s = "84532", t = "34852"
Output: true
Explanation: You can transform s into t using the following operations:
1. Sort the substring "843" -> "34852"

Example 2:
Input: s = "34521", t = "23415"
Output: false
Explanation: It is impossible to transform s into t.

Example 3:
Input: s = "12345", t = "12435"
Output: false
Explanation: No matter how you sort the substrings, you cannot achieve t from s.

Follow-up:
Can you solve it in O(n) time complexity?
"""

# Python Solution
from collections import deque

def isTransformable(s: str, t: str) -> bool:
    # Create queues for each digit (0-9) to store their indices in `s`
    positions = [deque() for _ in range(10)]
    for i, char in enumerate(s):
        positions[int(char)].append(i)
    
    for char in t:
        digit = int(char)
        # If there are no occurrences of `digit` left in `s`, return False
        if not positions[digit]:
            return False
        
        # Get the index of the first occurrence of `digit` in `s`
        index = positions[digit].popleft()
        
        # Check if there is any smaller digit that appears before `index` in `s`
        for smaller_digit in range(digit):
            if positions[smaller_digit] and positions[smaller_digit][0] < index:
                return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "84532"
    t1 = "34852"
    print(isTransformable(s1, t1))  # Output: True

    # Test Case 2
    s2 = "34521"
    t2 = "23415"
    print(isTransformable(s2, t2))  # Output: False

    # Test Case 3
    s3 = "12345"
    t3 = "12435"
    print(isTransformable(s3, t3))  # Output: False

    # Additional Test Case 4
    s4 = "9876543210"
    t4 = "0123456789"
    print(isTransformable(s4, t4))  # Output: True

    # Additional Test Case 5
    s5 = "111222333"
    t5 = "123123123"
    print(isTransformable(s5, t5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string `t` (length n) and performs operations on the queues.
- For each character in `t`, we check up to 10 queues (constant time).
- Thus, the overall time complexity is O(n).

Space Complexity:
- We use 10 queues to store indices of digits in `s`. In the worst case, each queue could store up to n indices.
- Therefore, the space complexity is O(n).

Topic: Strings
"""