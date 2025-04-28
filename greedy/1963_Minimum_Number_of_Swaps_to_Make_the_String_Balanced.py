"""
LeetCode Problem #1963: Minimum Number of Swaps to Make the String Balanced

Problem Statement:
You are given a string `s` of length `n` consisting only of the characters '[' and ']'. 
A string is considered balanced if:
- It is the empty string, or
- It can be written as `AB`, where both `A` and `B` are balanced strings, or
- It can be written as `[C]`, where `C` is a balanced string.

You can swap any two characters in the string. Return the minimum number of swaps required to make the string balanced.

Constraints:
- `n == s.length`
- `2 <= n <= 10^6`
- `s[i]` is either '[' or ']'.
- The number of '[' and ']' are equal.

Example:
Input: s = "][]["
Output: 1
Explanation: Swap the first and last characters to make the string balanced.

Input: s = "]]][[["
Output: 2
Explanation: Swap the second and fourth characters to make the string balanced.

Input: s = "[]"
Output: 0
Explanation: The string is already balanced.
"""

# Python Solution
def minSwaps(s: str) -> int:
    """
    Calculate the minimum number of swaps required to make the string balanced.

    :param s: A string consisting of '[' and ']'
    :return: Minimum number of swaps required
    """
    imbalance = 0
    max_imbalance = 0

    # Traverse the string to calculate the maximum imbalance
    for char in s:
        if char == '[':
            imbalance += 1
        else:  # char == ']'
            imbalance -= 1
        
        # Track the maximum imbalance encountered
        max_imbalance = max(max_imbalance, -imbalance)

    # The number of swaps required is the ceiling of max_imbalance / 2
    return (max_imbalance + 1) // 2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "][]["
    print(minSwaps(s1))  # Output: 1

    # Test Case 2
    s2 = "]]][[["
    print(minSwaps(s2))  # Output: 2

    # Test Case 3
    s3 = "[]"
    print(minSwaps(s3))  # Output: 0

    # Test Case 4
    s4 = "[[[[]]]]"
    print(minSwaps(s4))  # Output: 0

    # Test Case 5
    s5 = "][[[[[]]]]]][["
    print(minSwaps(s5))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves a single traversal of the string `s`, which has a length of `n`.
- Therefore, the time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space to store variables like `imbalance` and `max_imbalance`.
- Therefore, the space complexity is O(1).

Topic: Greedy
"""