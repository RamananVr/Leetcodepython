"""
LeetCode Problem #1221: Split a String in Balanced Strings

Problem Statement:
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string `s`, split it into the maximum number of balanced strings.

Return the maximum number of balanced strings you can obtain.

Constraints:
- 1 <= s.length <= 1000
- s[i] is either 'L' or 'R'.
- s is a balanced string.

Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains the same number of 'L' and 'R'.

Example 2:
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains the same number of 'L' and 'R'.

Example 3:
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Example 4:
Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", each substring contains the same number of 'L' and 'R'.

Follow-up:
Try to come up with a solution that has O(n) time complexity.
"""

# Python Solution
def balancedStringSplit(s: str) -> int:
    """
    This function takes a balanced string `s` and returns the maximum number of balanced strings
    that can be obtained by splitting `s`.
    """
    balance = 0
    count = 0

    for char in s:
        if char == 'L':
            balance += 1
        elif char == 'R':
            balance -= 1
        
        # When balance is zero, we have a balanced substring
        if balance == 0:
            count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "RLRRLLRLRL"
    print(f"Input: {s1} -> Output: {balancedStringSplit(s1)}")  # Expected Output: 4

    # Test Case 2
    s2 = "RLLLLRRRLR"
    print(f"Input: {s2} -> Output: {balancedStringSplit(s2)}")  # Expected Output: 3

    # Test Case 3
    s3 = "LLLLRRRR"
    print(f"Input: {s3} -> Output: {balancedStringSplit(s3)}")  # Expected Output: 1

    # Test Case 4
    s4 = "RLRRRLLRLL"
    print(f"Input: {s4} -> Output: {balancedStringSplit(s4)}")  # Expected Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity: O(n)
- We iterate through the string `s` once, where `n` is the length of the string.
- Each character is processed in O(1) time.

Space Complexity: O(1)
- We use a constant amount of extra space (two integer variables `balance` and `count`).

Overall, the solution is efficient with linear time complexity and constant space complexity.
"""

# Topic: String