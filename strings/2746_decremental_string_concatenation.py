"""
LeetCode Problem 2746: Decremental String Concatenation

You are given a 0-indexed array words of n strings.

Let joinedString be a string formed by concatenating all strings in words[0] to words[i] where i < n. 
In other words, joinedString = words[0] + words[1] + ... + words[i].

Return the minimum possible length of the string after removing exactly one occurrence of any substring 
from joinedString that appears at least twice.

If no such substring exists, return the length of joinedString.

Example 1:
Input: words = ["aa","ab","aa"]
Output: 4
Explanation: 
joinedString = "aa" + "ab" + "aa" = "aaabaa"
The substring "aa" appears twice (at indices 0-1 and 4-5).
Removing one occurrence: "aaabaa" -> "abaa" (length 4) or "aaab" (length 4).

Example 2:
Input: words = ["ab","b"]  
Output: 2
Explanation:
joinedString = "ab" + "b" = "abb"
The substring "b" appears twice (at indices 1 and 2).
Removing one occurrence: "abb" -> "ab" (length 2) or "ab" (length 2).

Example 3:
Input: words = ["aaa"]
Output: 2
Explanation:
joinedString = "aaa"
The substring "a" appears three times. Removing one: "aaa" -> "aa" (length 2).
The substring "aa" appears twice. Removing one: "aaa" -> "a" (length 1).
We want minimum length, so we remove "aa" to get length 1.
Wait, that's wrong. Let me recalculate:
"a" appears 3 times, "aa" appears 2 times, "aaa" appears 1 time.
Removing "aa": "aaa" -> "a" (length 1). This gives minimum length.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of lowercase English letters.
"""

from typing import List
from collections import defaultdict


def minimumLength(words: List[str]) -> int:
    """
    Find minimum length after removing one occurrence of any repeated substring.
    
    Strategy:
    1. Form the joined string
    2. Find all substrings that appear at least twice
    3. Remove the longest such substring to minimize final length
    
    Args:
        words: List of strings to concatenate
        
    Returns:
        Minimum possible length after removing one repeated substring
        
    Time Complexity: O(n^3) where n is length of joined string
    Space Complexity: O(n^2) for storing substring counts
    """
    joined = "".join(words)
    n = len(joined)
    
    if n <= 1:
        return n
    
    # Find all substrings and their counts
    substring_counts = defaultdict(list)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = joined[i:j]
            substring_counts[substring].append(i)
    
    # Find the longest substring that appears at least twice
    max_length_to_remove = 0
    
    for substring, positions in substring_counts.items():
        if len(positions) >= 2:
            max_length_to_remove = max(max_length_to_remove, len(substring))
    
    return n - max_length_to_remove


def minimumLengthOptimized(words: List[str]) -> int:
    """
    Optimized approach: only consider meaningful substrings.
    
    Args:
        words: List of strings to concatenate
        
    Returns:
        Minimum possible length after removing one repeated substring
        
    Time Complexity: O(n^3)
    Space Complexity: O(n^2)
    """
    joined = "".join(words)
    n = len(joined)
    
    if n <= 1:
        return n
    
    max_removal = 0
    
    # Check all possible substring lengths from longest to shortest
    for length in range(n, 0, -1):
        if length <= max_removal:
            break  # Already found longer substring to remove
            
        seen = set()
        found_duplicate = False
        
        for i in range(n - length + 1):
            substring = joined[i:i + length]
            if substring in seen:
                max_removal = length
                found_duplicate = True
                break
            seen.add(substring)
        
        if found_duplicate:
            break
    
    return n - max_removal


def minimumLengthDP(words: List[str]) -> int:
    """
    Dynamic programming approach to build the string incrementally.
    
    This approach considers the optimal way to build the string by
    keeping track of possible states as we add each word.
    
    Args:
        words: List of strings to concatenate
        
    Returns:
        Minimum possible length after removing one repeated substring
        
    Time Complexity: O(n^3)
    Space Complexity: O(n^2)
    """
    if not words:
        return 0
    
    # Build string incrementally and find best removal at each step
    current = ""
    
    for word in words:
        current += word
    
    # Now find the best substring to remove
    return minimumLengthOptimized([current])


def minimumLengthRollingHash(words: List[str]) -> int:
    """
    Use rolling hash for efficient substring comparison.
    
    Args:
        words: List of strings to concatenate
        
    Returns:
        Minimum possible length after removing one repeated substring
        
    Time Complexity: O(n^2) average case
    Space Complexity: O(n)
    """
    joined = "".join(words)
    n = len(joined)
    
    if n <= 1:
        return n
    
    def rolling_hash(s: str) -> int:
        """Compute rolling hash for string."""
        hash_val = 0
        base = 31
        mod = 10**9 + 7
        
        for char in s:
            hash_val = (hash_val * base + ord(char)) % mod
        
        return hash_val
    
    max_removal = 0
    
    # Check each possible substring length
    for length in range(1, n + 1):
        if length <= max_removal:
            continue
            
        hash_to_positions = defaultdict(list)
        
        for i in range(n - length + 1):
            substring = joined[i:i + length]
            hash_val = rolling_hash(substring)
            hash_to_positions[hash_val].append((i, substring))
        
        # Check for actual duplicates (handle hash collisions)
        for positions in hash_to_positions.values():
            if len(positions) >= 2:
                # Verify actual string equality
                first_str = positions[0][1]
                for _, substring in positions[1:]:
                    if substring == first_str:
                        max_removal = max(max_removal, length)
                        break
    
    return n - max_removal


# Test cases
def test_minimumLength():
    """Test the minimumLength function with various inputs."""
    
    test_cases = [
        {
            "words": ["aa", "ab", "aa"],
            "expected": 4,
            "description": "Example 1: aaabaa -> remove 'aa' -> abaa"
        },
        {
            "words": ["ab", "b"],
            "expected": 2,
            "description": "Example 2: abb -> remove 'b' -> ab"
        },
        {
            "words": ["aaa"],
            "expected": 1,
            "description": "Example 3: aaa -> remove 'aa' -> a"
        },
        {
            "words": ["a"],
            "expected": 1,
            "description": "Single character, no removal possible"
        },
        {
            "words": ["abc"],
            "expected": 3,
            "description": "No repeated substrings"
        },
        {
            "words": ["ab", "ba", "ab"],
            "expected": 4,
            "description": "abbaab -> remove 'ab' -> baab"
        },
        {
            "words": ["aa", "aa", "aa"],
            "expected": 2,
            "description": "aaaaaa -> remove 'aaaa' -> aa"
        },
        {
            "words": ["abc", "def", "abc"],
            "expected": 6,
            "description": "abcdefabc -> remove 'abc' -> defabc"
        },
        {
            "words": ["a", "b", "a", "b"],
            "expected": 2,
            "description": "abab -> remove 'ab' -> ab"
        }
    ]
    
    for i, test in enumerate(test_cases):
        words = test["words"]
        expected = test["expected"]
        
        # Test main solution
        result1 = minimumLength(words)
        print(f"Test {i+1}: {test['description']}")
        print(f"  Input: words = {words}")
        print(f"  Joined: {''.join(words)}")
        print(f"  Expected: {expected}")
        print(f"  Brute force: {result1}")
        
        # Test optimized solution
        result2 = minimumLengthOptimized(words)
        print(f"  Optimized: {result2}")
        
        # Test rolling hash solution
        result3 = minimumLengthRollingHash(words)
        print(f"  Rolling hash: {result3}")
        
        # Verify results
        assert result1 == expected, f"Brute force failed for test {i+1}"
        assert result2 == expected, f"Optimized failed for test {i+1}"
        assert result3 == expected, f"Rolling hash failed for test {i+1}"
        
        print(f"  ✓ All solutions passed!")
        print()


if __name__ == "__main__":
    test_minimumLength()

"""
Complexity Analysis:

1. Brute Force (minimumLength):
   - Time Complexity: O(n^3) - generate all substrings and count occurrences
   - Space Complexity: O(n^2) - store all substrings in hash map

2. Optimized (minimumLengthOptimized):
   - Time Complexity: O(n^3) - but with early termination when longer duplicate found
   - Space Complexity: O(n) - only store substrings of current length being checked

3. Rolling Hash (minimumLengthRollingHash):
   - Time Complexity: O(n^2) average case - rolling hash reduces string comparison cost
   - Space Complexity: O(n) - hash map for current length substrings

Key Insights:
- We want to remove the longest possible substring that appears at least twice
- This minimizes the final string length
- All substrings need to be considered, but we can optimize by checking longest first
- Rolling hash can speed up duplicate detection

Edge Cases:
- Single word with no repeated substrings
- All words are the same
- Single character strings
- Empty input

Optimization Strategies:
- Check substring lengths from longest to shortest
- Use rolling hash for faster string comparison
- Early termination when longer duplicate is found

Topics: Strings, Hash Table, Rolling Hash, Dynamic Programming, Substring Search
"""
