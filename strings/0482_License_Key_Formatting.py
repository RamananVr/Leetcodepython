"""
LeetCode Problem #482: License Key Formatting

Problem Statement:
You are given a license key represented as a string `s` that consists of only alphanumeric characters and dashes. 
The string is separated into `n + 1` groups by `n` dashes. You are also given an integer `k`.

We want to reformat the string `s` such that each group contains exactly `k` characters, except for the first group, 
which could be shorter than `k` but still must contain at least one character. Furthermore, there must be a dash ('-') 
inserted between two groups, and you should convert all lowercase letters to uppercase.

Given the string `s` and the integer `k`, return the reformatted license key.

Example 1:
Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each with 4 characters: "5F3Z" and "2E9W".

Example 2:
Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into four parts, each with 2 characters: "2", "5G", "3J".

Constraints:
- 1 <= s.length <= 10^5
- s consists of English letters, digits, and dashes '-'.
- 1 <= k <= 10^4
"""

# Python Solution
def licenseKeyFormatting(s: str, k: int) -> str:
    # Remove all dashes and convert to uppercase
    s = s.replace("-", "").upper()
    
    # Initialize the result list
    result = []
    
    # Start from the end of the string and group characters in chunks of size k
    for i in range(len(s), 0, -k):
        result.append(s[max(0, i - k):i])
    
    # Join the groups with dashes and return the result
    return "-".join(reversed(result))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "5F3Z-2e-9-w"
    k1 = 4
    print(licenseKeyFormatting(s1, k1))  # Output: "5F3Z-2E9W"

    # Test Case 2
    s2 = "2-5g-3-J"
    k2 = 2
    print(licenseKeyFormatting(s2, k2))  # Output: "2-5G-3J"

    # Test Case 3
    s3 = "abc-def-ghij"
    k3 = 3
    print(licenseKeyFormatting(s3, k3))  # Output: "AB-CDE-FGH-IJ"

    # Test Case 4
    s4 = "a"
    k4 = 1
    print(licenseKeyFormatting(s4, k4))  # Output: "A"

    # Test Case 5
    s5 = "----"
    k5 = 2
    print(licenseKeyFormatting(s5, k5))  # Output: ""

# Time and Space Complexity Analysis
# Time Complexity: O(n)
# - Removing dashes and converting to uppercase takes O(n), where n is the length of the string `s`.
# - Iterating through the string in chunks of size `k` also takes O(n).
# - Joining the groups with dashes takes O(n).
# Overall, the time complexity is O(n).

# Space Complexity: O(n)
# - The result list stores the reformatted string, which can be at most the size of the input string `s` (excluding dashes).
# - The space complexity is therefore O(n).

# Topic: Strings