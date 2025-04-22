"""
LeetCode Question #214: Shortest Palindrome

Problem Statement:
You are given a string `s`. You can convert it to a palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation.

Example 1:
Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: s = "abcd"
Output: "dcbabcd"

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of lowercase English letters only.
"""

# Solution
def shortestPalindrome(s: str) -> str:
    """
    Finds the shortest palindrome by adding characters in front of the given string.

    :param s: Input string
    :return: Shortest palindrome
    """
    if not s:
        return s

    # Create a new string that combines s and its reverse with a separator
    temp = s + "#" + s[::-1]
    
    # Compute the prefix table for the combined string using KMP algorithm
    n = len(temp)
    lps = [0] * n  # Longest Prefix Suffix array
    j = 0  # Length of the previous longest prefix suffix

    for i in range(1, n):
        while j > 0 and temp[i] != temp[j]:
            j = lps[j - 1]
        if temp[i] == temp[j]:
            j += 1
        lps[i] = j

    # The length of the longest palindromic prefix in the original string
    longest_palindromic_prefix_length = lps[-1]

    # Add the necessary characters in front of the original string
    return s[longest_palindromic_prefix_length:][::-1] + s

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aacecaaa"
    print(shortestPalindrome(s1))  # Output: "aaacecaaa"

    # Test Case 2
    s2 = "abcd"
    print(shortestPalindrome(s2))  # Output: "dcbabcd"

    # Test Case 3
    s3 = ""
    print(shortestPalindrome(s3))  # Output: ""

    # Test Case 4
    s4 = "a"
    print(shortestPalindrome(s4))  # Output: "a"

    # Test Case 5
    s5 = "racecar"
    print(shortestPalindrome(s5))  # Output: "racecar"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Constructing the `temp` string takes O(n), where n is the length of the input string `s`.
- Computing the LPS array using the KMP algorithm takes O(n).
- The final step of constructing the result string takes O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The LPS array requires O(n) space.
- The `temp` string requires O(2n + 1) space, which is linear.
- Overall, the space complexity is O(n).

Topic: String, KMP Algorithm
"""