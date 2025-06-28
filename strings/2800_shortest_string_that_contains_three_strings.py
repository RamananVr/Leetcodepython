"""
LeetCode Problem 2800: Shortest String That Contains Three Strings

Given three strings a, b, and c, return the shortest string that contains all three as substrings.

If there are multiple answers of the same length, return the lexicographically smallest one.

If there are multiple ways to produce the same string, you can return any of them.

Constraints:
- 1 <= a.length, b.length, c.length <= 100
- a, b, and c consist only of lowercase English letters.
- No string is a substring of another among the three strings.

Example 1:
Input: a = "abc", b = "bca", c = "aab"
Output: "aaabca"
Explanation: We show that "aaabca" contains all the given strings: a = "abc" is substring "aaabca", b = "bca" is substring "aaabca", c = "aab" is substring "aaabca".
It can be shown that the length of the optimal string is 6.

Example 2:
Input: a = "a", b = "aa", c = "aaa"
Output: "aaa"
Explanation: The shortest string that contains the three given strings is "aaa".

Topics: String, Enumeration, Permutation
"""

class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        """
        Approach 1: Try all permutations and merge optimally
        
        Key insight: The optimal string is one of the 6 possible ways to
        arrange and merge the three strings. For each arrangement,
        we merge strings by finding maximum overlap.
        
        Time: O(n^2) where n is the total length of all strings
        Space: O(n) for storing result strings
        """
        def merge_two_strings(s1: str, s2: str) -> str:
            """Merge two strings with maximum overlap."""
            # Try to overlap s1 with s2
            max_overlap = 0
            best_merge = s1 + s2
            
            # Check if s2 is already contained in s1
            if s2 in s1:
                return s1
            
            # Check if s1 is already contained in s2
            if s1 in s2:
                return s2
            
            # Find maximum overlap where end of s1 matches start of s2
            for i in range(1, min(len(s1), len(s2)) + 1):
                if s1[-i:] == s2[:i]:
                    overlap_candidate = s1 + s2[i:]
                    if len(overlap_candidate) < len(best_merge):
                        best_merge = overlap_candidate
                        max_overlap = i
            
            # Find maximum overlap where end of s2 matches start of s1
            for i in range(1, min(len(s1), len(s2)) + 1):
                if s2[-i:] == s1[:i]:
                    overlap_candidate = s2 + s1[i:]
                    if len(overlap_candidate) < len(best_merge):
                        best_merge = overlap_candidate
            
            return best_merge
        
        def merge_three_strings(x: str, y: str, z: str) -> str:
            """Merge three strings optimally."""
            # Try merging x,y first then z
            temp1 = merge_two_strings(x, y)
            result1 = merge_two_strings(temp1, z)
            
            # Try merging x,z first then y
            temp2 = merge_two_strings(x, z)
            result2 = merge_two_strings(temp2, y)
            
            # Return the shorter result, or lexicographically smaller if same length
            if len(result1) < len(result2):
                return result1
            elif len(result1) > len(result2):
                return result2
            else:
                return min(result1, result2)
        
        # Try all 6 permutations of the three strings
        permutations = [
            (a, b, c), (a, c, b), (b, a, c),
            (b, c, a), (c, a, b), (c, b, a)
        ]
        
        best_result = None
        
        for perm in permutations:
            result = merge_three_strings(perm[0], perm[1], perm[2])
            
            if best_result is None:
                best_result = result
            elif len(result) < len(best_result):
                best_result = result
            elif len(result) == len(best_result):
                best_result = min(best_result, result)
        
        return best_result
    
    def minimumString_overlap_all_pairs(self, a: str, b: str, c: str) -> str:
        """
        Approach 2: Check all possible overlaps between pairs
        
        More systematic approach to find overlaps.
        
        Time: O(n^3)
        Space: O(n)
        """
        def find_overlap(s1: str, s2: str) -> str:
            """Find optimal merge of s1 and s2."""
            if s2 in s1:
                return s1
            if s1 in s2:
                return s2
            
            # Try s1 + suffix of s2
            best = s1 + s2
            for i in range(1, min(len(s1), len(s2)) + 1):
                if s1.endswith(s2[:i]):
                    candidate = s1 + s2[i:]
                    if len(candidate) < len(best):
                        best = candidate
            
            # Try s2 + suffix of s1
            for i in range(1, min(len(s1), len(s2)) + 1):
                if s2.endswith(s1[:i]):
                    candidate = s2 + s1[i:]
                    if len(candidate) < len(best):
                        best = candidate
            
            return best
        
        strings = [a, b, c]
        results = []
        
        # Try all 6 permutations
        import itertools
        for perm in itertools.permutations(strings):
            # Merge first two
            merged = find_overlap(perm[0], perm[1])
            # Merge result with third
            final = find_overlap(merged, perm[2])
            results.append(final)
        
        # Return shortest, lexicographically smallest
        results.sort(key=lambda x: (len(x), x))
        return results[0]
    
    def minimumString_bruteforce_merge(self, a: str, b: str, c: str) -> str:
        """
        Approach 3: Brute force all possible merges
        
        Try concatenating in all orders and find overlaps.
        
        Time: O(n^3)
        Space: O(n)
        """
        def get_overlap_length(s1: str, s2: str) -> int:
            """Get maximum overlap length where s1 suffix matches s2 prefix."""
            max_overlap = 0
            for i in range(1, min(len(s1), len(s2)) + 1):
                if s1[-i:] == s2[:i]:
                    max_overlap = i
            return max_overlap
        
        def merge_with_overlap(s1: str, s2: str) -> str:
            """Merge s1 and s2 with optimal overlap."""
            if s2 in s1:
                return s1
            if s1 in s2:
                return s2
            
            overlap1 = get_overlap_length(s1, s2)
            overlap2 = get_overlap_length(s2, s1)
            
            option1 = s1 + s2[overlap1:] if overlap1 > 0 else s1 + s2
            option2 = s2 + s1[overlap2:] if overlap2 > 0 else s2 + s1
            
            if len(option1) < len(option2):
                return option1
            elif len(option1) > len(option2):
                return option2
            else:
                return min(option1, option2)
        
        strings = [a, b, c]
        best = None
        
        # Try all permutations
        import itertools
        for perm in itertools.permutations(strings):
            result = perm[0]
            for s in perm[1:]:
                result = merge_with_overlap(result, s)
            
            if best is None or len(result) < len(best) or (len(result) == len(best) and result < best):
                best = result
        
        return best

def test_minimum_string():
    """Test the minimum string solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    result1 = solution.minimumString("abc", "bca", "aab")
    # Expected: something like "aaabca" or similar with length 6
    assert len(result1) <= 9  # At most concatenation length
    assert "abc" in result1
    assert "bca" in result1
    assert "aab" in result1
    
    # Test case 2: One string contains others as substrings
    assert solution.minimumString("a", "aa", "aaa") == "aaa"
    
    # Test case 3: No overlap possible
    result3 = solution.minimumString("abc", "def", "ghi")
    assert len(result3) == 9  # Just concatenation
    assert "abc" in result3
    assert "def" in result3
    assert "ghi" in result3
    
    # Test case 4: Significant overlap
    result4 = solution.minimumString("ab", "bc", "cd")
    # Could be "abcd" with overlaps
    assert "ab" in result4
    assert "bc" in result4
    assert "cd" in result4
    assert len(result4) <= 6
    
    # Test case 5: Single characters
    result5 = solution.minimumString("a", "b", "c")
    assert len(result5) == 3
    assert "a" in result5
    assert "b" in result5
    assert "c" in result5
    
    # Test case 6: Identical strings
    result6 = solution.minimumString("abc", "abc", "abc")
    assert result6 == "abc"
    
    # Test case 7: Two identical, one different
    result7 = solution.minimumString("ab", "ab", "cd")
    assert "ab" in result7
    assert "cd" in result7
    assert len(result7) <= 4
    
    # Test case 8: Complex overlaps
    result8 = solution.minimumString("abcd", "cdab", "bcda")
    # These have circular overlap patterns
    assert "abcd" in result8
    assert "cdab" in result8
    assert "bcda" in result8
    
    # Compare approaches on smaller inputs
    small_test_cases = [
        ("abc", "bca", "aab"),
        ("a", "aa", "aaa"),
        ("abc", "def", "ghi"),
        ("ab", "bc", "cd"),
        ("a", "b", "c"),
        ("abc", "abc", "abc"),
        ("ab", "ab", "cd")
    ]
    
    for a, b, c in small_test_cases:
        result1 = solution.minimumString(a, b, c)
        result2 = solution.minimumString_overlap_all_pairs(a, b, c)
        result3 = solution.minimumString_bruteforce_merge(a, b, c)
        
        # All should have same length and contain all strings
        assert len(result1) == len(result2) == len(result3), \
            f"Length mismatch for {a}, {b}, {c}: {len(result1)}, {len(result2)}, {len(result3)}"
        
        for result in [result1, result2, result3]:
            assert a in result and b in result and c in result, \
                f"Missing substring in {result} for {a}, {b}, {c}"
    
    print("All minimum string tests passed!")

if __name__ == "__main__":
    test_minimum_string()
