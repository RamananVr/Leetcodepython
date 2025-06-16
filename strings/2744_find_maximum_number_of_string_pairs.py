"""
LeetCode Problem 2744: Find Maximum Number of String Pairs

You are given a 0-indexed array words consisting of distinct strings.

The task is to find the maximum number of string pairs that can be formed from the array where:
- words[i] and words[j] form a pair if one string is the reverse of the other.
- Each string can be used in at most one pair.

Return the maximum number of string pairs that can be formed.

Example 1:
Input: words = ["cd","ac","dc","ca","zz"]
Output: 2
Explanation: 
In this example, we can form 2 pairs:
- ("cd", "dc")
- ("ac", "ca")
The string "zz" cannot form a pair because its reverse is itself, and each string can only be used once.

Example 2:
Input: words = ["ab","ba","cc"]
Output: 1
Explanation: 
In this example, we can form 1 pair:
- ("ab", "ba")
The string "cc" cannot form a pair because its reverse is itself.

Example 3:
Input: words = ["aa","ab"]
Output: 0
Explanation: 
In this example, we cannot form any pairs. "aa" reversed is "aa", and "ab" reversed is "ba" which is not in the array.

Constraints:
- 1 <= words.length <= 50
- 1 <= words[i].length <= 300
- words[i] consists of lowercase English letters.
- All the strings of words are unique.
"""

from typing import List, Set
from collections import Counter, defaultdict


def maximumNumberOfStringPairs(words: List[str]) -> int:
    """
    Find maximum number of string pairs using hash set for O(1) lookup.
    
    For each word, check if its reverse exists in remaining words.
    Use a set to track processed words to avoid double counting.
    
    Args:
        words: List of distinct strings
        
    Returns:
        Maximum number of string pairs
        
    Time Complexity: O(n * m) where n is number of words, m is average word length
    Space Complexity: O(n * m) for storing words in set
    """
    word_set = set(words)
    used = set()
    pairs = 0
    
    for word in words:
        if word in used:
            continue
            
        reversed_word = word[::-1]
        
        # Check if reverse exists and is different from current word
        if reversed_word in word_set and reversed_word != word and reversed_word not in used:
            pairs += 1
            used.add(word)
            used.add(reversed_word)
    
    return pairs


def maximumNumberOfStringPairsCounter(words: List[str]) -> int:
    """
    Use Counter to track word frequencies and handle palindromes.
    
    Args:
        words: List of distinct strings
        
    Returns:
        Maximum number of string pairs
        
    Time Complexity: O(n * m)
    Space Complexity: O(n * m)
    """
    word_count = Counter(words)
    pairs = 0
    processed = set()
    
    for word in words:
        if word in processed:
            continue
            
        reversed_word = word[::-1]
        
        if word == reversed_word:
            # Palindrome: can only pair with itself if count >= 2
            # But since all words are unique, this case won't contribute
            processed.add(word)
        elif reversed_word in word_count:
            # Found a pair
            pairs += 1
            processed.add(word)
            processed.add(reversed_word)
        else:
            processed.add(word)
    
    return pairs


def maximumNumberOfStringPairsGrouping(words: List[str]) -> int:
    """
    Group words by their canonical form (lexicographically smaller between word and reverse).
    
    Args:
        words: List of distinct strings
        
    Returns:
        Maximum number of string pairs
        
    Time Complexity: O(n * m)
    Space Complexity: O(n * m)
    """
    groups = defaultdict(list)
    
    for word in words:
        reversed_word = word[::-1]
        # Use lexicographically smaller as canonical form
        canonical = min(word, reversed_word)
        groups[canonical].append(word)
    
    pairs = 0
    for group in groups.values():
        if len(group) == 2:
            # Check if they are actually reverses of each other
            if group[0] == group[1][::-1]:
                pairs += 1
    
    return pairs


def maximumNumberOfStringPairsBruteForce(words: List[str]) -> int:
    """
    Brute force approach: check all pairs.
    
    Args:
        words: List of distinct strings
        
    Returns:
        Maximum number of string pairs
        
    Time Complexity: O(n^2 * m) where n is number of words, m is average word length
    Space Complexity: O(1)
    """
    n = len(words)
    used = [False] * n
    pairs = 0
    
    for i in range(n):
        if used[i]:
            continue
            
        for j in range(i + 1, n):
            if used[j]:
                continue
                
            if words[i] == words[j][::-1]:
                pairs += 1
                used[i] = True
                used[j] = True
                break
    
    return pairs


def maximumNumberOfStringPairsOptimal(words: List[str]) -> int:
    """
    Most optimal approach using single pass with set.
    
    Args:
        words: List of distinct strings
        
    Returns:
        Maximum number of string pairs
        
    Time Complexity: O(n * m)
    Space Complexity: O(n * m)
    """
    seen = set()
    pairs = 0
    
    for word in words:
        reversed_word = word[::-1]
        
        if reversed_word in seen:
            pairs += 1
            seen.remove(reversed_word)  # Remove to avoid reuse
        else:
            seen.add(word)
    
    return pairs


# Test cases
def test_maximumNumberOfStringPairs():
    """Test the maximumNumberOfStringPairs function with various inputs."""
    
    test_cases = [
        {
            "words": ["cd", "ac", "dc", "ca", "zz"],
            "expected": 2,
            "description": "Example 1: cd-dc and ac-ca pairs, zz is palindrome"
        },
        {
            "words": ["ab", "ba", "cc"],
            "expected": 1,
            "description": "Example 2: ab-ba pair, cc is palindrome"
        },
        {
            "words": ["aa", "ab"],
            "expected": 0,
            "description": "Example 3: no valid pairs"
        },
        {
            "words": ["abc", "cba", "def", "fed"],
            "expected": 2,
            "description": "Two pairs: abc-cba and def-fed"
        },
        {
            "words": ["a"],
            "expected": 0,
            "description": "Single word, no pairs possible"
        },
        {
            "words": ["ab", "cd", "ef"],
            "expected": 0,
            "description": "No reverses present"
        },
        {
            "words": ["abc", "def", "cba", "ghi", "fed"],
            "expected": 2,
            "description": "Mixed case with some pairs"
        },
        {
            "words": ["abcd", "dcba", "xy", "yx", "pq"],
            "expected": 2,
            "description": "Different length words with pairs"
        }
    ]
    
    for i, test in enumerate(test_cases):
        words = test["words"]
        expected = test["expected"]
        
        # Test main solution
        result1 = maximumNumberOfStringPairs(words)
        print(f"Test {i+1}: {test['description']}")
        print(f"  Input: words = {words}")
        print(f"  Expected: {expected}")
        print(f"  Hash set approach: {result1}")
        
        # Test counter solution
        result2 = maximumNumberOfStringPairsCounter(words)
        print(f"  Counter approach: {result2}")
        
        # Test grouping solution
        result3 = maximumNumberOfStringPairsGrouping(words)
        print(f"  Grouping approach: {result3}")
        
        # Test optimal solution
        result4 = maximumNumberOfStringPairsOptimal(words)
        print(f"  Optimal approach: {result4}")
        
        # Test brute force for verification
        result5 = maximumNumberOfStringPairsBruteForce(words)
        print(f"  Brute force: {result5}")
        
        # Verify results
        assert result1 == expected, f"Hash set approach failed for test {i+1}"
        assert result2 == expected, f"Counter approach failed for test {i+1}"
        assert result3 == expected, f"Grouping approach failed for test {i+1}"
        assert result4 == expected, f"Optimal approach failed for test {i+1}"
        assert result5 == expected, f"Brute force failed for test {i+1}"
        
        print(f"  ✓ All solutions passed!")
        print()


if __name__ == "__main__":
    test_maximumNumberOfStringPairs()

"""
Complexity Analysis:

1. Hash Set Approach (maximumNumberOfStringPairs):
   - Time Complexity: O(n * m) - iterate through words, reverse each word
   - Space Complexity: O(n * m) - store all words and used set

2. Counter Approach (maximumNumberOfStringPairsCounter):
   - Time Complexity: O(n * m) - similar to hash set approach
   - Space Complexity: O(n * m) - counter and processed set

3. Grouping Approach (maximumNumberOfStringPairsGrouping):
   - Time Complexity: O(n * m) - group words by canonical form
   - Space Complexity: O(n * m) - store groups

4. Optimal Approach (maximumNumberOfStringPairsOptimal):
   - Time Complexity: O(n * m) - single pass through words
   - Space Complexity: O(n * m) - seen set (but removes paired words)

5. Brute Force (maximumNumberOfStringPairsBruteForce):
   - Time Complexity: O(n^2 * m) - check all pairs
   - Space Complexity: O(n) - used array

Key Insights:
- Each word can be used at most once
- A word pairs with its reverse if both exist and are different
- Palindromes cannot form pairs with themselves (would violate "each string used once" rule)
- The optimal approach processes words in one pass, removing paired words immediately

Edge Cases:
- Palindromic words (cannot pair with themselves)
- Single character words
- Empty input
- All words are unique (no duplicates to worry about)

Topics: Arrays, Strings, Hash Table, String Manipulation
"""
