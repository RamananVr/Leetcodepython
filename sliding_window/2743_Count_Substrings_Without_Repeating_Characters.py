"""
LeetCode Problem #2743: Count Substrings Without Repeating Characters

Problem Statement:
Given a string `s`, return the number of substrings of `s` that contain no repeated characters.

A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
Input: s = "abc"
Output: 6
Explanation: The substrings are "a", "b", "c", "ab", "bc", and "abc". All of them have no repeated characters.

Example 2:
Input: s = "aaa"
Output: 3
Explanation: The substrings are "a", "a", "a". Only these substrings have no repeated characters.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
"""

def countSubstringsWithoutRepeatingCharacters(s: str) -> int:
    """
    Returns the number of substrings of `s` that contain no repeated characters.
    """
    n = len(s)
    left = 0
    char_set = set()
    count = 0

    for right in range(n):
        # Slide the window to ensure no repeated characters
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add the current character to the set
        char_set.add(s[right])
        
        # Count substrings ending at `right`
        count += (right - left + 1)
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abc"
    print(countSubstringsWithoutRepeatingCharacters(s1))  # Output: 6

    # Test Case 2
    s2 = "aaa"
    print(countSubstringsWithoutRepeatingCharacters(s2))  # Output: 3

    # Test Case 3
    s3 = "abac"
    print(countSubstringsWithoutRepeatingCharacters(s3))  # Output: 7

    # Test Case 4
    s4 = "abcd"
    print(countSubstringsWithoutRepeatingCharacters(s4))  # Output: 10

    # Test Case 5
    s5 = "a"
    print(countSubstringsWithoutRepeatingCharacters(s5))  # Output: 1

"""
Time Complexity Analysis:
- The algorithm uses a sliding window approach, where each character is added to and removed from the set at most once.
- Therefore, the time complexity is O(n), where n is the length of the string `s`.

Space Complexity Analysis:
- The space complexity is O(k), where k is the size of the character set (in this case, at most 26 for lowercase English letters).

Topic: Sliding Window
"""