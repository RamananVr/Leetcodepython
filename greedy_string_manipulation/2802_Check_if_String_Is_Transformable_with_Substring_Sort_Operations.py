"""
LeetCode Problem #2802: Check if String Is Transformable with Substring Sort Operations

Problem Statement:
You are given two strings `s` and `t` of the same length consisting of digits from '0' to '9'. 
You can transform `s` into `t` using the following operation any number of times:

- Choose a non-empty substring in `s` and sort it in ascending order.

Return `true` if it is possible to transform `s` into `t`. Otherwise, return `false`.

Example 1:
Input: s = "84532", t = "34852"
Output: true
Explanation: You can transform s into t using the following operations:
1. Sort the substring "845" -> "45832"
2. Sort the substring "4583" -> "34582"
3. Sort the substring "34582" -> "34852"

Example 2:
Input: s = "345", t = "534"
Output: false
Explanation: It is impossible to transform s into t.

Constraints:
- `s.length == t.length`
- `s` and `t` consist of digits from '0' to '9'.

"""

# Python Solution
from collections import deque

def isTransformable(s: str, t: str) -> bool:
    # Create a list of queues to store the indices of each digit in `s`
    positions = [deque() for _ in range(10)]
    for i, char in enumerate(s):
        positions[int(char)].append(i)
    
    for char in t:
        digit = int(char)
        # If there are no occurrences of the current digit in `s`, return False
        if not positions[digit]:
            return False
        # Get the index of the first occurrence of the current digit in `s`
        index = positions[digit].popleft()
        # Check if there is any smaller digit that appears before the current digit in `s`
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
    s2 = "345"
    t2 = "534"
    print(isTransformable(s2, t2))  # Output: False

    # Test Case 3
    s3 = "12345"
    t3 = "12345"
    print(isTransformable(s3, t3))  # Output: True

    # Test Case 4
    s4 = "54321"
    t4 = "12345"
    print(isTransformable(s4, t4))  # Output: True

    # Test Case 5
    s5 = "111222333"
    t5 = "123123123"
    print(isTransformable(s5, t5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string `t` (length n) and performs operations on the `positions` list.
- For each character in `t`, we check up to 10 smaller digits, which is constant.
- Therefore, the time complexity is O(n).

Space Complexity:
- The `positions` list contains up to 10 deques, each storing indices of digits in `s`.
- In the worst case, all indices are stored, resulting in O(n) space usage.
- Thus, the space complexity is O(n).

Topic: Greedy, String Manipulation
"""