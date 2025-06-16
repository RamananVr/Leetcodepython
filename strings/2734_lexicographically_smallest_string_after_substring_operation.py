"""
2734. Lexicographically Smallest String After Substring Operation

You are given a string s consisting of only lowercase English letters. In one operation, you can:
- Select any non-empty substring of s.
- Replace every letter in the substring with the previous letter in the English alphabet. For example 'b' becomes 'a', 'c' becomes 'b', and so on. The letter 'a' becomes 'z'.

Return the lexicographically smallest string you can obtain after performing exactly one operation.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "cbabc"
Output: "baabc"
Explanation: We apply the operation on the substring starting at index 0, and ending at index 1 inclusive.
It can be shown that the resulting string is the lexicographically smallest.

Example 2:
Input: s = "acbbc"
Output: "aabbc"
Explanation: We apply the operation on the substring starting at index 1, and ending at index 1 inclusive.
It can be shown that the resulting string is the lexicographically smallest.

Example 3:
Input: s = "aaa"
Output: "aaz"
Explanation: We apply the operation on the substring starting at index 2, and ending at index 2 inclusive.
It can be shown that the resulting string is the lexicographically smallest.

Constraints:
- 1 <= s.length <= 1000
- s consists of only lowercase English letters.
"""

def smallest_string_after_operation(s: str) -> str:
    """
    Find lexicographically smallest string after exactly one substring operation.
    
    Args:
        s: String consisting of lowercase English letters
        
    Returns:
        str: Lexicographically smallest string after one operation
        
    Time Complexity: O(n) - single pass through string
    Space Complexity: O(n) - creating result string
    """
    n = len(s)
    s_list = list(s)
    
    # Find the first non-'a' character and convert consecutive non-'a' characters
    for i in range(n):
        if s_list[i] != 'a':
            # Convert consecutive non-'a' characters starting from position i
            j = i
            while j < n and s_list[j] != 'a':
                s_list[j] = chr(ord(s_list[j]) - 1)
                j += 1
            return ''.join(s_list)
    
    # If all characters are 'a', convert the last one to 'z'
    s_list[-1] = 'z'
    return ''.join(s_list)

def smallest_string_after_operation_greedy(s: str) -> str:
    """
    Greedy approach: convert the first sequence of non-'a' characters.
    
    Args:
        s: String consisting of lowercase English letters
        
    Returns:
        str: Lexicographically smallest string after one operation
        
    Time Complexity: O(n) - single pass
    Space Complexity: O(n) - result string
    """
    s_chars = list(s)
    n = len(s_chars)
    
    # Strategy: Find leftmost non-'a' character and convert consecutive non-'a's
    start = -1
    for i in range(n):
        if s_chars[i] != 'a':
            start = i
            break
    
    if start == -1:
        # All characters are 'a', convert last one
        s_chars[-1] = 'z'
    else:
        # Convert consecutive non-'a' characters starting from start
        i = start
        while i < n and s_chars[i] != 'a':
            s_chars[i] = chr(ord(s_chars[i]) - 1)
            i += 1
    
    return ''.join(s_chars)

def smallest_string_after_operation_optimal(s: str) -> str:
    """
    Optimal solution with early termination and minimal operations.
    
    Args:
        s: String consisting of lowercase English letters
        
    Returns:
        str: Lexicographically smallest string after one operation
        
    Time Complexity: O(n) - single pass with potential early termination
    Space Complexity: O(n) - result string
    """
    chars = list(s)
    n = len(chars)
    
    # Find first non-'a' character
    for i in range(n):
        if chars[i] != 'a':
            # Convert this character and continue until we hit 'a' or end
            while i < n and chars[i] != 'a':
                chars[i] = chr(ord(chars[i]) - 1)
                i += 1
            return ''.join(chars)
    
    # All are 'a', change last to 'z'
    chars[-1] = 'z'
    return ''.join(chars)

def smallest_string_after_operation_brute_force(s: str) -> str:
    """
    Brute force approach: try all possible substrings and find the best result.
    
    Args:
        s: String consisting of lowercase English letters
        
    Returns:
        str: Lexicographically smallest string after one operation
        
    Time Complexity: O(n^3) - trying all substrings
    Space Complexity: O(n) - result string
    """
    n = len(s)
    best_result = None
    
    for i in range(n):
        for j in range(i, n):
            # Try operation on substring s[i:j+1]
            result = list(s)
            for k in range(i, j + 1):
                if result[k] == 'a':
                    result[k] = 'z'
                else:
                    result[k] = chr(ord(result[k]) - 1)
            
            result_str = ''.join(result)
            if best_result is None or result_str < best_result:
                best_result = result_str
    
    return best_result

# Test cases
def test_smallest_string_after_operation():
    test_cases = [
        # Basic test cases
        ("cbabc", "baabc"),
        ("acbbc", "aabbc"),
        ("aaa", "aaz"),
        
        # Edge cases
        ("a", "z"),           # Single 'a'
        ("b", "a"),           # Single non-'a'
        ("z", "y"),           # Single 'z'
        ("ab", "aa"),         # Mixed with 'a' at start
        ("ba", "aa"),         # Mixed with 'a' at end
        
        # Complex cases
        ("dcba", "ccba"),     # Decreasing sequence
        ("abcd", "aacd"),     # Increasing sequence
        ("aaabbb", "aaabaa"), # Multiple 'a's followed by non-'a's
        ("bbbaaaccc", "aaaaaacc"), # Non-'a's, then 'a's, then non-'a's
        
        # All same character cases
        ("bbbb", "aaaa"),     # All same non-'a'
        ("aaaa", "aaaz"),     # All 'a's
        
        # Mixed patterns
        ("abcabc", "aacabc"), # Alternating pattern
        ("zabc", "yabc"),     # Starting with 'z'
        ("abcz", "aacz"),     # Ending with 'z'
    ]
    
    print("Testing smallest_string_after_operation function:")
    for i, (s, expected) in enumerate(test_cases):
        result1 = smallest_string_after_operation(s)
        result2 = smallest_string_after_operation_greedy(s)
        result3 = smallest_string_after_operation_optimal(s)
        result4 = smallest_string_after_operation_brute_force(s)
        
        print(f"Test {i+1}: s='{s}'")
        print(f"  Expected: '{expected}'")
        print(f"  Basic: '{result1}'")
        print(f"  Greedy: '{result2}'")
        print(f"  Optimal: '{result3}'")
        print(f"  Brute Force: '{result4}'")
        
        assert result1 == expected, f"Basic failed for s='{s}'"
        assert result2 == expected, f"Greedy failed for s='{s}'"
        assert result3 == expected, f"Optimal failed for s='{s}'"
        assert result4 == expected, f"Brute Force failed for s='{s}'"
        print(f"  ✓ All passed\n")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_smallest_string_after_operation()

"""
Time Complexity Analysis:
- Basic/Greedy/Optimal: O(n) - single pass through string
- Brute Force: O(n^3) - trying all O(n^2) substrings, each requiring O(n) operations

Space Complexity Analysis:
- All solutions: O(n) - creating result string

Key Insights:
1. To get lexicographically smallest result, we should make changes as early as possible
2. Converting 'a' to 'z' makes the string larger, so avoid if possible
3. The optimal strategy is to find the first non-'a' character and convert consecutive non-'a' characters
4. If all characters are 'a', we must convert exactly one, so convert the last one to minimize impact
5. Greedy approach works because earlier positions have higher priority in lexicographic comparison

Topics: String, Greedy
"""
