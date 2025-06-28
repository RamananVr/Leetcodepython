"""
LeetCode Problem 2781: Length of the Longest Valid Substring

You are given a string word and an array of strings forbidden.

A string is called valid if none of its substrings are present in forbidden.

Return the length of the longest valid substring of word.

A substring is a contiguous sequence of characters in a string, possibly empty.

Constraints:
- 1 <= word.length <= 10^5
- 1 <= forbidden.length <= 10^5
- 1 <= forbidden[i].length <= 10
- forbidden[i] and word consist only of lowercase English letters.

Example 1:
Input: word = "cbaaaabc", forbidden = ["aaa","cb"]
Output: 4
Explanation: There are 11 valid substrings in "cbaaaabc": "c", "b", "a", "a", "a", "a", "bc", "aa", "ba", "ab", "abc". The longest valid substring is "aaaa", which has length 4.

Example 2:
Input: word = "leetcode", forbidden = ["de","le","e"]
Output: 4
Explanation: There are 11 valid substrings in "leetcode": "l", "t", "c", "o", "d", "lt", "tc", "co", "od", "etc", "tco", "cod", "tcode". The longest valid substring is "tcod" which has length 4.

Topics: Array, Hash Table, String, Sliding Window
"""

class Solution:
    def longestValidSubstring(self, word: str, forbidden: list[str]) -> int:
        """
        Approach 1: Sliding Window with Early Termination
        
        Use sliding window and check for forbidden substrings.
        Key insight: since max forbidden length is 10, we only need to check
        the last few characters when extending the window.
        
        Time: O(n * min(10, max_forbidden_length))
        Space: O(total_forbidden_chars) for set storage
        """
        forbidden_set = set(forbidden)
        max_forbidden_len = max(len(f) for f in forbidden) if forbidden else 0
        
        n = len(word)
        left = 0
        max_length = 0
        
        for right in range(n):
            # Check all substrings ending at right with length up to max_forbidden_len
            for start in range(max(left, right - max_forbidden_len + 1), right + 1):
                substring = word[start:right + 1]
                if substring in forbidden_set:
                    # Found forbidden substring, move left pointer
                    left = start + 1
                    break
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    def longestValidSubstring_optimized(self, word: str, forbidden: list[str]) -> int:
        """
        Approach 2: Optimized sliding window
        
        More efficient checking by limiting the search range.
        
        Time: O(n * min(10, k)) where k is max forbidden string length
        Space: O(total_forbidden_chars)
        """
        forbidden_set = set(forbidden)
        if not forbidden_set:
            return len(word)
        
        max_len = min(10, max(len(f) for f in forbidden))
        n = len(word)
        left = 0
        result = 0
        
        for right in range(n):
            # Check substrings ending at position 'right'
            for length in range(1, min(max_len + 1, right - left + 2)):
                start = right - length + 1
                if start < left:
                    break
                
                if word[start:right + 1] in forbidden_set:
                    left = start + 1
                    break
            
            result = max(result, right - left + 1)
        
        return result
    
    def longestValidSubstring_bruteforce(self, word: str, forbidden: list[str]) -> int:
        """
        Approach 3: Brute force (for verification)
        
        Check all possible substrings and find the longest valid one.
        
        Time: O(n^3) - O(n^2) substrings, O(n) to check each
        Space: O(total_forbidden_chars)
        """
        forbidden_set = set(forbidden)
        n = len(word)
        max_length = 0
        
        for i in range(n):
            for j in range(i, n):
                substring = word[i:j + 1]
                
                # Check if this substring is valid
                is_valid = True
                for start in range(len(substring)):
                    for end in range(start + 1, len(substring) + 1):
                        if substring[start:end] in forbidden_set:
                            is_valid = False
                            break
                    if not is_valid:
                        break
                
                if is_valid:
                    max_length = max(max_length, len(substring))
        
        return max_length
    
    def longestValidSubstring_trie(self, word: str, forbidden: list[str]) -> int:
        """
        Approach 4: Using Trie for efficient forbidden string matching
        
        Build a trie of forbidden strings for faster lookup.
        
        Time: O(n * max_forbidden_length)
        Space: O(total_forbidden_chars) for trie
        """
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end = False
        
        # Build trie
        root = TrieNode()
        for word_forbidden in forbidden:
            node = root
            for char in word_forbidden:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
        
        n = len(word)
        left = 0
        max_length = 0
        
        for right in range(n):
            # Check for forbidden substrings ending at right
            node = root
            for start in range(right, max(left - 1, -1), -1):
                if word[start] not in node.children:
                    break
                node = node.children[word[start]]
                if node.is_end:
                    # Found forbidden substring word[start:right+1]
                    left = start + 1
                    break
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

def test_longest_valid_substring():
    """Test the longest valid substring solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.longestValidSubstring("cbaaaabc", ["aaa", "cb"]) == 4
    
    # Test case 2: Another example
    assert solution.longestValidSubstring("leetcode", ["de", "le", "e"]) == 4
    
    # Test case 3: No forbidden strings
    assert solution.longestValidSubstring("abcdef", []) == 6
    
    # Test case 4: Entire string is forbidden
    assert solution.longestValidSubstring("abc", ["abc"]) == 2
    
    # Test case 5: Single character
    assert solution.longestValidSubstring("a", ["a"]) == 0
    assert solution.longestValidSubstring("a", ["b"]) == 1
    
    # Test case 6: Overlapping forbidden strings
    assert solution.longestValidSubstring("abcdef", ["abc", "bcd"]) == 3
    
    # Test case 7: All single characters forbidden
    assert solution.longestValidSubstring("abcd", ["a", "b", "c", "d"]) == 0
    
    # Test case 8: Long valid substring
    assert solution.longestValidSubstring("aaabbbccc", ["ab"]) == 3
    
    # Test case 9: Forbidden string at the end
    assert solution.longestValidSubstring("abcdef", ["def"]) == 5
    
    # Test case 10: Multiple valid segments
    result10 = solution.longestValidSubstring("abcxyzpqr", ["abc", "pqr"])
    # Valid substrings include "xyz" and others, longest might be "cxyz" or similar
    
    # Compare approaches on smaller inputs
    small_test_cases = [
        ("cbaaaabc", ["aaa", "cb"]),
        ("abc", ["abc"]),
        ("a", ["a"]),
        ("a", ["b"]),
        ("abcd", ["a"]),
        ("abcdef", ["abc", "bcd"]),
        ("aaabbbccc", ["ab"])
    ]
    
    for word, forbidden in small_test_cases:
        result1 = solution.longestValidSubstring(word, forbidden)
        result2 = solution.longestValidSubstring_optimized(word, forbidden)
        result4 = solution.longestValidSubstring_trie(word, forbidden)
        
        # Only test brute force on very small inputs
        if len(word) <= 8:
            result3 = solution.longestValidSubstring_bruteforce(word, forbidden)
            assert result1 == result2 == result3 == result4, \
                f"Mismatch for word='{word}', forbidden={forbidden}: {result1}, {result2}, {result3}, {result4}"
        else:
            assert result1 == result2 == result4, \
                f"Mismatch for word='{word}', forbidden={forbidden}: {result1}, {result2}, {result4}"
    
    # Test edge cases
    assert solution.longestValidSubstring("", []) == 0
    assert solution.longestValidSubstring("a", []) == 1
    assert solution.longestValidSubstring("abcdefghij", ["k"]) == 10
    
    print("All longest valid substring tests passed!")

if __name__ == "__main__":
    test_longest_valid_substring()
