"""
LeetCode Problem #1309: Decrypt String from Alphabet to Integer Mapping

Problem Statement:
You are given a string `s` formed by digits ('0' - '9') and '#' characters. 
We want to map `s` to English lowercase characters as follows:

- Characters ('a' to 'i') are represented by ('1' to '9') respectively.
- Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.

Return the string formed after mapping.

The test cases are guaranteed that a unique mapping will always exist.

Example 1:
Input: s = "10#11#12"
Output: "jkab"
Explanation: "10#" -> "j", "11#" -> "k", "1" -> "a", "2" -> "b".

Example 2:
Input: s = "1326#"
Output: "acz"

Example 3:
Input: s = "25#"
Output: "y"

Example 4:
Input: s = "123456789"
Output: "abcdefghi"

Constraints:
- 1 <= s.length <= 1000
- s consists of digits ('0'-'9') and '#' characters.
- `s` will be a valid string such that mapping is always possible.

"""

# Clean and Correct Python Solution
def freqAlphabets(s: str) -> str:
    result = []
    i = 0
    while i < len(s):
        # Check if the current character is part of a "10#" to "26#" mapping
        if i + 2 < len(s) and s[i + 2] == '#':
            # Convert the two-digit number to a character
            result.append(chr(int(s[i:i+2]) + 96))
            i += 3  # Skip the processed characters and the '#'
        else:
            # Convert the single-digit number to a character
            result.append(chr(int(s[i]) + 96))
            i += 1  # Move to the next character
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "10#11#12"
    print(freqAlphabets(s1))  # Output: "jkab"

    # Test Case 2
    s2 = "1326#"
    print(freqAlphabets(s2))  # Output: "acz"

    # Test Case 3
    s3 = "25#"
    print(freqAlphabets(s3))  # Output: "y"

    # Test Case 4
    s4 = "123456789"
    print(freqAlphabets(s4))  # Output: "abcdefghi"

    # Test Case 5
    s5 = "10#11#12#13#14#15#"
    print(freqAlphabets(s5))  # Output: "jklmnop"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm processes each character in the string `s` exactly once.
- For each character, we perform constant-time operations (e.g., slicing, integer conversion, and appending to a list).
- Therefore, the time complexity is O(n), where n is the length of the string `s`.

Space Complexity:
- The algorithm uses a list `result` to store the decoded characters.
- In the worst case, the size of `result` is proportional to the length of the input string `s`.
- Therefore, the space complexity is O(n), where n is the length of the string `s`.
"""

# Topic: String Manipulation