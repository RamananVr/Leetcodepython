"""
2738. Count Occurrences in Text

Given a string text and a string pattern, return the number of times pattern occurs in text.

Overlapping occurrences count as separate occurrences.

Example 1:
Input: text = "abcabc", pattern = "abc"
Output: 2
Explanation: The pattern "abc" occurs at indices 0 and 3.

Example 2:
Input: text = "aaaa", pattern = "aa"
Output: 3
Explanation: The pattern "aa" occurs at indices 0, 1, and 2 (overlapping occurrences).

Example 3:
Input: text = "abc", pattern = "def"
Output: 0
Explanation: The pattern "def" does not occur in "abc".

Constraints:
- 1 <= text.length <= 1000
- 1 <= pattern.length <= 100
- text and pattern consist of only lowercase English letters.
"""

def count_occurrences_in_text(text: str, pattern: str) -> int:
    """
    Count overlapping occurrences of pattern in text using naive approach.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        
    Returns:
        int: Number of occurrences (including overlapping)
        
    Time Complexity: O(n * m) where n = len(text), m = len(pattern)
    Space Complexity: O(1) - constant extra space
    """
    if len(pattern) > len(text):
        return 0
    
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    
    return count

def count_occurrences_kmp(text: str, pattern: str) -> int:
    """
    Count occurrences using KMP (Knuth-Morris-Pratt) algorithm for efficiency.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        
    Returns:
        int: Number of occurrences
        
    Time Complexity: O(n + m) - linear time preprocessing and searching
    Space Complexity: O(m) - for the LPS (Longest Prefix Suffix) array
    """
    if len(pattern) > len(text):
        return 0
    
    def compute_lps(pattern):
        """Compute Longest Prefix Suffix array for KMP algorithm."""
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    lps = compute_lps(pattern)
    count = 0
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            count += 1
            j = lps[j - 1]  # Continue searching for overlapping matches
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return count

def count_occurrences_rolling_hash(text: str, pattern: str) -> int:
    """
    Count occurrences using rolling hash (Rabin-Karp algorithm).
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        
    Returns:
        int: Number of occurrences
        
    Time Complexity: O(n + m) average case, O(n * m) worst case
    Space Complexity: O(1) - constant extra space
    """
    if len(pattern) > len(text):
        return 0
    
    n, m = len(text), len(pattern)
    base = 256  # Number of characters in the input alphabet
    prime = 101  # A prime number for hashing
    
    pattern_hash = 0
    text_hash = 0
    h = 1
    count = 0
    
    # Calculate h = pow(base, m-1) % prime
    for i in range(m - 1):
        h = (h * base) % prime
    
    # Calculate hash value of pattern and first window of text
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime
    
    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check if hash values match
        if pattern_hash == text_hash:
            # Check for actual match (to handle hash collisions)
            if text[i:i + m] == pattern:
                count += 1
        
        # Calculate hash value for next window
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            # Handle negative hash values
            if text_hash < 0:
                text_hash += prime
    
    return count

def count_occurrences_z_algorithm(text: str, pattern: str) -> int:
    """
    Count occurrences using Z algorithm.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        
    Returns:
        int: Number of occurrences
        
    Time Complexity: O(n + m) - linear time
    Space Complexity: O(n + m) - for the combined string and Z array
    """
    if len(pattern) > len(text):
        return 0
    
    # Create combined string: pattern + '$' + text
    combined = pattern + '$' + text
    n = len(combined)
    
    # Compute Z array
    z = [0] * n
    left, right = 0, 0
    
    for i in range(1, n):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        
        while i + z[i] < n and combined[z[i]] == combined[i + z[i]]:
            z[i] += 1
        
        if i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1
    
    # Count occurrences
    count = 0
    pattern_len = len(pattern)
    
    for i in range(pattern_len + 1, n):
        if z[i] == pattern_len:
            count += 1
    
    return count

# Test cases
def test_count_occurrences_in_text():
    test_cases = [
        # Basic test cases
        ("abcabc", "abc", 2),
        ("aaaa", "aa", 3),
        ("abc", "def", 0),
        
        # Edge cases
        ("", "a", 0),              # Empty text
        ("a", "", 0),              # Empty pattern (handled as 0 matches)
        ("a", "a", 1),             # Single character match
        ("a", "b", 0),             # Single character no match
        
        # Overlapping patterns
        ("aaaa", "aaa", 2),        # "aaa" at positions 0 and 1
        ("ababa", "aba", 2),       # "aba" at positions 0 and 2
        ("ababab", "abab", 2),     # "abab" at positions 0 and 2
        
        # No matches
        ("xyz", "abc", 0),
        ("hello", "world", 0),
        
        # Pattern longer than text
        ("abc", "abcd", 0),
        
        # Exact match
        ("abc", "abc", 1),
        
        # Multiple non-overlapping matches
        ("abcdefabc", "abc", 2),
        
        # Complex patterns
        ("aabaacaadaabaaba", "aaba", 4),   # Pattern "aaba" appears 4 times
        ("mississippi", "issi", 1),        # Pattern in middle
        ("mississippi", "ss", 2),          # Overlapping "ss"
        
        # Repeated characters
        ("aaaaaa", "aa", 5),       # Five overlapping "aa"
        ("bbbbb", "bb", 4),        # Four overlapping "bb"
    ]
    
    print("Testing count_occurrences_in_text function:")
    for i, (text, pattern, expected) in enumerate(test_cases):
        result1 = count_occurrences_in_text(text, pattern)
        result2 = count_occurrences_kmp(text, pattern)
        result3 = count_occurrences_rolling_hash(text, pattern)
        result4 = count_occurrences_z_algorithm(text, pattern)
        
        print(f"Test {i+1}: text='{text}', pattern='{pattern}'")
        print(f"  Expected: {expected}")
        print(f"  Naive: {result1}")
        print(f"  KMP: {result2}")
        print(f"  Rolling Hash: {result3}")
        print(f"  Z Algorithm: {result4}")
        
        assert result1 == expected, f"Naive failed for test case {i+1}"
        assert result2 == expected, f"KMP failed for test case {i+1}"
        assert result3 == expected, f"Rolling Hash failed for test case {i+1}"
        assert result4 == expected, f"Z Algorithm failed for test case {i+1}"
        print(f"  ✓ All passed\n")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_count_occurrences_in_text()

"""
Time Complexity Analysis:
- Naive Solution: O(n * m) - checking each position with pattern comparison
- KMP Algorithm: O(n + m) - linear preprocessing and searching
- Rolling Hash: O(n + m) average, O(n * m) worst case due to hash collisions
- Z Algorithm: O(n + m) - linear time construction and search

Space Complexity Analysis:
- Naive: O(1) - constant extra space
- KMP: O(m) - LPS array for pattern
- Rolling Hash: O(1) - constant extra space
- Z Algorithm: O(n + m) - combined string and Z array

Key Insights:
1. Overlapping occurrences must be counted separately
2. Naive approach is simple but can be slow for large inputs
3. KMP provides optimal time complexity with reasonable space usage
4. Rolling hash offers good average-case performance
5. Z algorithm is elegant and provides linear time guarantees
6. The choice of algorithm depends on the expected input characteristics

Topics: String, Pattern Matching, KMP Algorithm, Rolling Hash, Z Algorithm
"""
