"""
LeetCode Problem #1647: Minimum Deletions to Make Character Frequencies Unique

Problem Statement:
A string s is called good if there are no two different characters in s that have the same frequency.
Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. 
For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:
Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the string "aaabcc".
The frequency of each character is now unique.

Example 3:
Input: s = "ceabaacb"
Output: 2
Explanation: You can delete two characters. For example, delete one 'c' and one 'e' resulting in "ceabacb".
The frequencies of characters are now 'a': 2, 'b': 2, 'c': 2, 'e': 1.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters.
"""

from collections import Counter

def minDeletions(s: str) -> int:
    """
    Function to calculate the minimum number of deletions required to make character frequencies unique.
    """
    # Count the frequency of each character
    freq = Counter(s)
    
    # Use a set to track used frequencies
    used_frequencies = set()
    deletions = 0

    for char, count in freq.items():
        # Reduce the frequency until it becomes unique or zero
        while count > 0 and count in used_frequencies:
            count -= 1
            deletions += 1
        # Add the unique frequency to the set
        if count > 0:
            used_frequencies.add(count)
    
    return deletions

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aab"
    print(f"Input: {s1}, Output: {minDeletions(s1)}")  # Expected Output: 0

    # Test Case 2
    s2 = "aaabbbcc"
    print(f"Input: {s2}, Output: {minDeletions(s2)}")  # Expected Output: 2

    # Test Case 3
    s3 = "ceabaacb"
    print(f"Input: {s3}, Output: {minDeletions(s3)}")  # Expected Output: 2

    # Test Case 4
    s4 = "abcabc"
    print(f"Input: {s4}, Output: {minDeletions(s4)}")  # Expected Output: 3

    # Test Case 5
    s5 = "aabbccddeeff"
    print(f"Input: {s5}, Output: {minDeletions(s5)}")  # Expected Output: 6

"""
Time Complexity Analysis:
- Counting the frequency of characters takes O(n), where n is the length of the string.
- Iterating through the frequency dictionary takes O(k), where k is the number of unique characters (at most 26 for lowercase English letters).
- Adjusting the frequency for uniqueness involves at most O(n) operations in total (since we can only delete characters up to the total length of the string).
- Overall time complexity: O(n).

Space Complexity Analysis:
- The frequency dictionary and the set of used frequencies both require O(k) space, where k is the number of unique characters (at most 26).
- Overall space complexity: O(k), which is effectively O(1) for this problem due to the fixed alphabet size.

Topic: Greedy
"""