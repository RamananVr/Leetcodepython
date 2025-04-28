"""
LeetCode Question #1071: Greatest Common Divisor of Strings

Problem Statement:
For two strings `s1` and `s2`, we say `s2` divides `s1` if and only if `s1 = s2 + s2 + ... + s2` (i.e., `s2` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.

Constraints:
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of English uppercase letters.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

"""

# Solution
def gcd_of_strings(str1: str, str2: str) -> str:
    """
    Finds the greatest common divisor (GCD) of two strings.
    """
    def gcd(a: int, b: int) -> int:
        # Helper function to compute the GCD of two integers
        while b:
            a, b = b, a % b
        return a

    # Check if str1 + str2 == str2 + str1 (necessary condition for a common divisor string)
    if str1 + str2 != str2 + str1:
        return ""

    # Compute the GCD of the lengths of the two strings
    length_gcd = gcd(len(str1), len(str2))

    # Return the prefix of str1 with length equal to the GCD of the lengths
    return str1[:length_gcd]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    str1 = "ABCABC"
    str2 = "ABC"
    print(gcd_of_strings(str1, str2))  # Output: "ABC"

    # Test Case 2
    str1 = "ABABAB"
    str2 = "ABAB"
    print(gcd_of_strings(str1, str2))  # Output: "AB"

    # Test Case 3
    str1 = "LEET"
    str2 = "CODE"
    print(gcd_of_strings(str1, str2))  # Output: ""

    # Test Case 4
    str1 = "AAAAAA"
    str2 = "AAA"
    print(gcd_of_strings(str1, str2))  # Output: "AAA"

    # Test Case 5
    str1 = "ABCDEF"
    str2 = "ABC"
    print(gcd_of_strings(str1, str2))  # Output: ""

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `gcd` function runs in O(log(min(len(str1), len(str2)))) due to the Euclidean algorithm.
- The string concatenation check (`str1 + str2 != str2 + str1`) takes O(len(str1) + len(str2)).
- Extracting the prefix (`str1[:length_gcd]`) takes O(length_gcd), where `length_gcd` is the GCD of the lengths of the two strings.
- Overall, the time complexity is O(len(str1) + len(str2)).

Space Complexity:
- The space complexity is O(1) since we are only using a few variables and no additional data structures.

Topic: Strings
"""