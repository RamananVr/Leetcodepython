"""
LeetCode Problem #1663: Smallest String With A Given Numeric Value

Problem Statement:
The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so 'a' has a numeric value of 1, 'b' has a numeric value of 2, ..., and 'z' has a numeric value of 26.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

Note that a string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, the string a has a character strictly smaller than the corresponding character in b. For example, "abc" is lexicographically smaller than "abd" because the first position they differ is at the third character, and 'c' is smaller than 'd'.

Constraints:
- 1 <= n <= 10^5
- n <= k <= 26 * n
"""

# Python Solution
def getSmallestString(n: int, k: int) -> str:
    # Initialize the result array with 'a' (value 1) for all positions
    result = ['a'] * n
    # Calculate the remaining value after assigning 'a' to all positions
    remaining = k - n
    
    # Start filling the string from the end to make it lexicographically smallest
    index = n - 1
    while remaining > 0:
        # Determine the maximum value we can add to the current position
        add_value = min(25, remaining)
        result[index] = chr(ord('a') + add_value)
        remaining -= add_value
        index -= 1
    
    # Join the result array into a string and return
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1 = 3, 27
    print(getSmallestString(n1, k1))  # Expected Output: "aay"

    # Test Case 2
    n2, k2 = 5, 73
    print(getSmallestString(n2, k2))  # Expected Output: "aaszz"

    # Test Case 3
    n3, k3 = 1, 26
    print(getSmallestString(n3, k3))  # Expected Output: "z"

    # Test Case 4
    n4, k4 = 4, 30
    print(getSmallestString(n4, k4))  # Expected Output: "aazz"

    # Test Case 5
    n5, k5 = 2, 52
    print(getSmallestString(n5, k5))  # Expected Output: "zz"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates over the string from the end, adjusting characters until the remaining value becomes 0.
- In the worst case, we iterate over all n positions, so the time complexity is O(n).

Space Complexity:
- The algorithm uses a list of size n to store the result, which is converted to a string at the end.
- Thus, the space complexity is O(n).
"""

# Topic: Greedy Algorithm