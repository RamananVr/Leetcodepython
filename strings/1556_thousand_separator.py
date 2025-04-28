"""
LeetCode Question #1556: Thousand Separator

Problem Statement:
Given an integer `n`, add a dot (".") as the thousands separator and return it in string format.

Example 1:
Input: n = 987
Output: "987"

Example 2:
Input: n = 1234
Output: "1.234"

Example 3:
Input: n = 123456789
Output: "123.456.789"

Example 4:
Input: n = 0
Output: "0"

Constraints:
- 0 <= n <= 2^31 - 1
"""

# Solution
def thousandSeparator(n: int) -> str:
    """
    Adds a dot as the thousands separator to the given integer `n`.

    :param n: Integer input
    :return: String representation of `n` with thousands separators
    """
    # Convert the integer to a string
    n_str = str(n)
    # Reverse the string to process in groups of 3
    reversed_n = n_str[::-1]
    # Group the reversed string into chunks of 3 characters
    grouped = [reversed_n[i:i+3] for i in range(0, len(reversed_n), 3)]
    # Join the groups with a dot and reverse the result back
    return '.'.join(grouped)[::-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 987
    print(thousandSeparator(n1))  # Output: "987"

    # Test Case 2
    n2 = 1234
    print(thousandSeparator(n2))  # Output: "1.234"

    # Test Case 3
    n3 = 123456789
    print(thousandSeparator(n3))  # Output: "123.456.789"

    # Test Case 4
    n4 = 0
    print(thousandSeparator(n4))  # Output: "0"

    # Test Case 5
    n5 = 1000000
    print(thousandSeparator(n5))  # Output: "1.000.000"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Converting the integer to a string takes O(d), where d is the number of digits in `n`.
- Reversing the string takes O(d).
- Grouping the reversed string into chunks of 3 takes O(d).
- Joining the groups with a dot and reversing the result back takes O(d).
- Overall, the time complexity is O(d), where d is the number of digits in `n`.

Space Complexity:
- The space complexity is O(d) due to the storage of the reversed string and grouped chunks.
- No additional data structures are used beyond the input size.
- Overall, the space complexity is O(d).

Topic: Strings
"""