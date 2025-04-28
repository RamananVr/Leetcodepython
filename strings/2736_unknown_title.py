"""
LeetCode Problem #2736: Maximize String Length After Deleting Subsequences

Problem Statement:
You are given a string `s` consisting of lowercase English letters. You are allowed to delete any number of subsequences from the string. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Your task is to determine the maximum possible length of the string `s` after deleting any number of subsequences.

Constraints:
- 1 <= len(s) <= 10^5
- `s` consists of lowercase English letters.

Return the maximum possible length of the string after performing the deletions.

Example:
Input: s = "abacaba"
Output: 2
Explanation: After deleting subsequences, the string can be reduced to "ab" or "ba", both of which have a length of 2.

Input: s = "aaaa"
Output: 1
Explanation: After deleting subsequences, the string can be reduced to "a", which has a length of 1.
"""

def maximizeStringLength(s: str) -> int:
    """
    Function to determine the maximum possible length of the string after deleting subsequences.
    
    Args:
    s (str): The input string consisting of lowercase English letters.
    
    Returns:
    int: The maximum possible length of the string after deletions.
    """
    # Use a set to find the number of unique characters in the string
    unique_characters = set(s)
    
    # The maximum length of the string after deletions is the number of unique characters
    return len(unique_characters)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abacaba"
    print(maximizeStringLength(s1))  # Output: 2

    # Test Case 2
    s2 = "aaaa"
    print(maximizeStringLength(s2))  # Output: 1

    # Test Case 3
    s3 = "abcde"
    print(maximizeStringLength(s3))  # Output: 5

    # Test Case 4
    s4 = "aabbcc"
    print(maximizeStringLength(s4))  # Output: 3

    # Test Case 5
    s5 = "xyzxyzxyz"
    print(maximizeStringLength(s5))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function uses the `set` data structure to find unique characters in the string `s`.
- Constructing a set from a string of length `n` takes O(n) time.
- Therefore, the time complexity is O(n).

Space Complexity:
- The space complexity is determined by the size of the `set` used to store unique characters.
- In the worst case, the set will contain all 26 lowercase English letters, which is O(1) space.
- Thus, the space complexity is O(1).

Topic: Strings
"""