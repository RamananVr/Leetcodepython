"""
LeetCode Problem 2743: Count Substrings Without Repeating Character

Given a string s, return the number of substrings that do not have any repeating character.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "abcabc"
Output: 21
Explanation: 
The substrings without repeating characters are:
"a" (appears 2 times), "b" (appears 2 times), "c" (appears 2 times),
"ab" (appears 2 times), "bc" (appears 2 times), "ca" (appears 1 time),
"abc" (appears 2 times), "bca" (appears 1 time), "cab" (appears 1 time)
Total: 2*3 + 2*3 + 1 + 2*3 + 1 + 1 = 21

Example 2:
Input: s = "aba"
Output: 4
Explanation: 
The substrings without repeating characters are:
"a" (appears 2 times), "b" (appears 1 time), "ab" (appears 1 time)
Total: 2 + 1 + 1 = 4

Example 3:
Input: s = "aaa"
Output: 3
Explanation: 
The substrings without repeating characters are:
"a" (appears 3 times)
Total: 3

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
"""

from typing import Dict


def numberOfUniqueSubstrings(s: str) -> int:
    """
    Count the number of substrings without repeating characters using sliding window.
    
    For each position, we find the longest substring ending at that position
    without repeating characters. All prefixes of this substring are valid.
    
    Args:
        s: Input string
        
    Returns:
        Number of substrings without repeating characters
        
    Time Complexity: O(n)
    Space Complexity: O(min(m, n)) where m is size of character set
    """
    n = len(s)
    if n == 0:
        return 0
    
    count = 0
    char_index = {}  # Character -> last seen index
    start = 0  # Start of current window
    
    for end in range(n):
        char = s[end]
        
        # If character seen before and within current window
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        # Update last seen index
        char_index[char] = end
        
        # All substrings ending at 'end' and starting from 'start' to 'end'
        # are valid (no repeating characters)
        count += end - start + 1
    
    return count


def numberOfUniqueSubstringsBrute(s: str) -> int:
    """
    Brute force approach: check all possible substrings.
    
    Args:
        s: Input string
        
    Returns:
        Number of substrings without repeating characters
        
    Time Complexity: O(n^3)
    Space Complexity: O(min(m, n)) where m is size of character set
    """
    n = len(s)
    count = 0
    
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if len(set(substring)) == len(substring):
                count += 1
    
    return count


def numberOfUniqueSubstringsOptimized(s: str) -> int:
    """
    Optimized approach using two pointers and set.
    
    Args:
        s: Input string
        
    Returns:
        Number of substrings without repeating characters
        
    Time Complexity: O(n)
    Space Complexity: O(min(m, n)) where m is size of character set
    """
    n = len(s)
    if n == 0:
        return 0
    
    count = 0
    left = 0
    char_set = set()
    
    for right in range(n):
        # Shrink window from left until no duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character
        char_set.add(s[right])
        
        # All substrings ending at 'right' and starting from 'left' to 'right'
        count += right - left + 1
    
    return count


def numberOfUniqueSubstringsWithLastSeen(s: str) -> int:
    """
    Track last seen position of each character for efficient window management.
    
    Args:
        s: Input string
        
    Returns:
        Number of substrings without repeating characters
        
    Time Complexity: O(n)
    Space Complexity: O(1) - at most 26 characters
    """
    n = len(s)
    count = 0
    last_seen = [-1] * 26  # For lowercase letters a-z
    start = 0
    
    for end in range(n):
        char_idx = ord(s[end]) - ord('a')
        
        # Update start to avoid repeating character
        start = max(start, last_seen[char_idx] + 1)
        
        # Update last seen position
        last_seen[char_idx] = end
        
        # Count valid substrings ending at current position
        count += end - start + 1
    
    return count


# Test cases
def test_numberOfUniqueSubstrings():
    """Test the numberOfUniqueSubstrings function with various inputs."""
    
    test_cases = [
        {
            "s": "abcabc",
            "expected": 21,
            "description": "Example 1: repeating pattern"
        },
        {
            "s": "aba",
            "expected": 4,
            "description": "Example 2: simple case with repetition"
        },
        {
            "s": "aaa",
            "expected": 3,
            "description": "Example 3: all same characters"
        },
        {
            "s": "a",
            "expected": 1,
            "description": "Single character"
        },
        {
            "s": "abc",
            "expected": 6,
            "description": "No repeating characters: a, b, c, ab, bc, abc"
        },
        {
            "s": "abba",
            "expected": 7,
            "description": "Palindrome: a, b, b, a, ab, bb, ba"
        },
        {
            "s": "pwwkew",
            "expected": 12,
            "description": "Complex case with multiple repetitions"
        },
        {
            "s": "",
            "expected": 0,
            "description": "Empty string"
        }
    ]
    
    for i, test in enumerate(test_cases):
        s = test["s"]
        expected = test["expected"]
        
        # Test main solution
        result1 = numberOfUniqueSubstrings(s)
        print(f"Test {i+1}: {test['description']}")
        print(f"  Input: s = '{s}'")
        print(f"  Expected: {expected}")
        print(f"  Sliding window: {result1}")
        
        # Test optimized solution
        result2 = numberOfUniqueSubstringsOptimized(s)
        print(f"  Two pointers: {result2}")
        
        # Test with last seen array
        result3 = numberOfUniqueSubstringsWithLastSeen(s)
        print(f"  Last seen array: {result3}")
        
        # Test brute force for smaller inputs
        if len(s) <= 10:
            result4 = numberOfUniqueSubstringsBrute(s)
            print(f"  Brute force: {result4}")
            assert result4 == expected, f"Brute force failed for test {i+1}"
        
        # Verify results
        assert result1 == expected, f"Sliding window failed for test {i+1}"
        assert result2 == expected, f"Two pointers failed for test {i+1}"
        assert result3 == expected, f"Last seen array failed for test {i+1}"
        
        print(f"  ✓ All solutions passed!")
        print()


if __name__ == "__main__":
    test_numberOfUniqueSubstrings()

"""
Complexity Analysis:

1. Sliding Window (numberOfUniqueSubstrings):
   - Time Complexity: O(n) - each character processed at most twice
   - Space Complexity: O(min(m, n)) - hash map for character positions

2. Two Pointers (numberOfUniqueSubstringsOptimized):
   - Time Complexity: O(n) - each character added/removed from set at most once
   - Space Complexity: O(min(m, n)) - set for tracking characters

3. Last Seen Array (numberOfUniqueSubstringsWithLastSeen):
   - Time Complexity: O(n) - single pass through string
   - Space Complexity: O(1) - fixed size array for 26 lowercase letters

4. Brute Force (numberOfUniqueSubstringsBrute):
   - Time Complexity: O(n^3) - check all substrings and validate each
   - Space Complexity: O(min(m, n)) - for substring character checking

Key Insights:
- For each ending position, count how many valid starting positions exist
- Use sliding window to maintain substring without repeating characters
- When duplicate found, move start pointer to position after last occurrence
- Total substrings ending at position i = (i - start + 1)

Similar Problems:
- Longest Substring Without Repeating Characters
- Subarrays with K Different Integers
- Fruit Into Baskets

Topics: Strings, Sliding Window, Two Pointers, Hash Table
"""
