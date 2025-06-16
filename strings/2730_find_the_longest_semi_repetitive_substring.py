"""
2730. Find the Longest Semi-Repetitive Substring

You are given a 0-indexed string s that consists of digits from 0 to 9.

A string is called semi-repetitive if there is at most one adjacent pair of the same digit.
For example, "0010", "002020", "0123", "2002", and "54944" are semi-repetitive while 
"00101022", and "1101234" are not.

Return the length of the longest semi-repetitive substring of s.

A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
Input: s = "52233"
Output: 4
Explanation: The longest semi-repetitive substring is "5223", which starts at i = 0 and ends at i = 3.

Example 2:
Input: s = "5494"
Output: 4
Explanation: s is semi-repetitive, so the answer is 4.

Example 3:
Input: s = "1111111"
Output: 2
Explanation: The longest semi-repetitive substring is "11", which starts at i = 0 and ends at i = 1.

Constraints:
- 1 <= s.length <= 50
- s consists only of digits from 0 to 9.
"""

def longest_semi_repetitive_substring(s: str) -> int:
    """
    Find the length of the longest semi-repetitive substring using sliding window approach.
    
    Args:
        s: String consisting of digits 0-9
        
    Returns:
        int: Length of the longest semi-repetitive substring
        
    Time Complexity: O(n) - single pass with sliding window
    Space Complexity: O(1) - using constant extra space
    """
    n = len(s)
    if n <= 1:
        return n
    
    max_length = 1
    left = 0
    adjacent_pairs = 0
    
    for right in range(1, n):
        # Check if current position forms an adjacent pair
        if s[right] == s[right - 1]:
            adjacent_pairs += 1
        
        # If we have more than one adjacent pair, shrink window from left
        while adjacent_pairs > 1:
            if s[left] == s[left + 1]:
                adjacent_pairs -= 1
            left += 1
        
        # Update maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length

def longest_semi_repetitive_substring_brute_force(s: str) -> int:
    """
    Brute force solution checking all possible substrings.
    
    Args:
        s: String consisting of digits 0-9
        
    Returns:
        int: Length of the longest semi-repetitive substring
        
    Time Complexity: O(n^3) - checking all substrings
    Space Complexity: O(1) - using constant extra space
    """
    def is_semi_repetitive(substring):
        """Check if a substring is semi-repetitive."""
        adjacent_pairs = 0
        for i in range(1, len(substring)):
            if substring[i] == substring[i-1]:
                adjacent_pairs += 1
                if adjacent_pairs > 1:
                    return False
        return True
    
    n = len(s)
    max_length = 0
    
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if is_semi_repetitive(substring):
                max_length = max(max_length, len(substring))
    
    return max_length

def longest_semi_repetitive_substring_optimized(s: str) -> int:
    """
    Optimized sliding window with better tracking of adjacent pairs.
    
    Args:
        s: String consisting of digits 0-9
        
    Returns:
        int: Length of the longest semi-repetitive substring
        
    Time Complexity: O(n) - single pass
    Space Complexity: O(1) - constant space
    """
    n = len(s)
    if n <= 1:
        return n
    
    max_length = 1
    left = 0
    last_pair_pos = -1  # Position of the last adjacent pair
    
    for right in range(1, n):
        if s[right] == s[right - 1]:
            # Found an adjacent pair
            if last_pair_pos != -1:
                # We already have one pair, need to move left pointer
                left = last_pair_pos + 1
            last_pair_pos = right - 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test cases
def test_longest_semi_repetitive_substring():
    test_cases = [
        # Basic test cases
        ("52233", 4),      # "5223" is longest semi-repetitive
        ("5494", 4),       # Entire string is semi-repetitive
        ("1111111", 2),    # Only "11" is valid
        
        # Edge cases
        ("1", 1),          # Single character
        ("12", 2),         # Two different characters
        ("11", 2),         # Two same characters
        ("123", 3),        # All different characters
        
        # Complex cases
        ("0010", 4),       # Entire string is semi-repetitive
        ("002020", 6),     # Entire string is semi-repetitive
        ("0123", 4),       # All different digits
        ("2002", 4),       # One pair in middle
        ("54944", 5),      # Entire string is semi-repetitive
        
        # Invalid cases (more than one adjacent pair)
        ("001122", 4),     # "0011" or "1122" are longest
        ("1122334", 4),    # Multiple pairs
        ("1000", 3),       # "100" or "000" but "000" has 2 pairs, so "100"
        
        # Additional test cases
        ("112233", 4),     # "1122" or "2233"
        ("123321", 6),     # Entire string is semi-repetitive
        ("1001", 4),       # Entire string is semi-repetitive
    ]
    
    print("Testing longest_semi_repetitive_substring function:")
    for i, (s, expected) in enumerate(test_cases):
        result1 = longest_semi_repetitive_substring(s)
        result2 = longest_semi_repetitive_substring_brute_force(s)
        result3 = longest_semi_repetitive_substring_optimized(s)
        
        print(f"Test {i+1}: s='{s}'")
        print(f"  Expected: {expected}")
        print(f"  Sliding Window: {result1}")
        print(f"  Brute Force: {result2}")
        print(f"  Optimized: {result3}")
        
        assert result1 == expected, f"Sliding Window failed for s='{s}'"
        assert result2 == expected, f"Brute Force failed for s='{s}'"
        assert result3 == expected, f"Optimized failed for s='{s}'"
        print(f"  ✓ All passed\n")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_semi_repetitive_substring()

"""
Time Complexity Analysis:
- Sliding Window: O(n) - each character is visited at most twice
- Brute Force: O(n^3) - checking all O(n^2) substrings, each takes O(n)
- Optimized: O(n) - single pass with better tracking

Space Complexity Analysis:
- All solutions: O(1) - using constant extra space

Key Insights:
1. Sliding window technique is perfect for this constraint-based substring problem
2. We need to track at most one adjacent pair in a valid substring
3. When we encounter a second adjacent pair, we need to move the left boundary
4. The optimized version tracks the position of the last adjacent pair for efficiency

Topics: String, Sliding Window, Two Pointers
"""
