"""
LeetCode Problem #1876: Substrings of Size Three with Distinct Characters

Problem Statement:
A string is good if there are no repeated characters. Given a string `s`, return the number of good substrings of length three in `s`.

A substring is a contiguous sequence of characters in a string.

Example 1:
Input: s = "xyzzaz"
Output: 1
Explanation: There are four substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".

Example 2:
Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".

Constraints:
- 1 <= s.length <= 100
- s consists of lowercase English letters.
"""

def countGoodSubstrings(s: str) -> int:
    """
    Counts the number of substrings of size three with distinct characters.

    :param s: Input string
    :return: Number of good substrings of length 3
    """
    count = 0
    for i in range(len(s) - 2):
        # Extract the substring of length 3
        substring = s[i:i+3]
        # Check if all characters in the substring are unique
        if len(set(substring)) == 3:
            count += 1
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "xyzzaz"
    print(f"Input: {s1} -> Output: {countGoodSubstrings(s1)}")  # Expected: 1

    # Test Case 2
    s2 = "aababcabc"
    print(f"Input: {s2} -> Output: {countGoodSubstrings(s2)}")  # Expected: 4

    # Test Case 3
    s3 = "abc"
    print(f"Input: {s3} -> Output: {countGoodSubstrings(s3)}")  # Expected: 1

    # Test Case 4
    s4 = "aaa"
    print(f"Input: {s4} -> Output: {countGoodSubstrings(s4)}")  # Expected: 0

    # Test Case 5
    s5 = "abcdef"
    print(f"Input: {s5} -> Output: {countGoodSubstrings(s5)}")  # Expected: 4

"""
Time Complexity Analysis:
- The loop iterates through the string `s` with a sliding window of size 3.
- For each window, we extract a substring of size 3 and check its uniqueness using a set.
- Extracting a substring and creating a set both take O(1) time for a fixed size of 3.
- Therefore, the overall time complexity is O(n), where n is the length of the string.

Space Complexity Analysis:
- The space complexity is O(1) because the set used to check uniqueness has a fixed size of at most 3 elements.

Topic: Sliding Window
"""