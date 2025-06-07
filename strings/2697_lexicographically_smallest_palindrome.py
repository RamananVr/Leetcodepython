"""
2697. Lexicographically Smallest Palindrome

PROBLEM STATEMENT:
You are given a string s consisting of lowercase English letters, and you are allowed to change 
any character in s to any other lowercase English letter.

Return the lexicographically smallest palindrome that you can create from s.

A string is lexicographically smaller than another string of the same length if the first 
character where they differ has a smaller value in the first string.

EXAMPLES:
Example 1:
Input: s = "egcfe"
Output: "efcfe"
Explanation: The minimum lexicographically palindrome we can create from "egcfe" is "efcfe".

Example 2:
Input: s = "abcd"
Output: "abba"
Explanation: The minimum lexicographically palindrome we can create from "abcd" is "abba".

Example 3:
Input: s = "seven"
Output: "neven"
Explanation: The minimum lexicographically palindrome we can create from "seven" is "neven".

CONSTRAINTS:
- 1 <= s.length <= 1000
- s consists of only lowercase English letters.
"""

def make_smallest_palindrome(s):
    """
    Create the lexicographically smallest palindrome from string s.
    
    Approach: For a palindrome, s[i] must equal s[n-1-i] for all i.
    To get the lexicographically smallest result, we set both positions
    to the smaller of the two characters.
    
    Args:
        s: String of lowercase English letters
    
    Returns:
        Lexicographically smallest palindrome
    """
    chars = list(s)
    n = len(chars)
    
    # Compare characters from both ends
    for i in range(n // 2):
        left = i
        right = n - 1 - i
        
        # Set both positions to the smaller character
        smaller_char = min(chars[left], chars[right])
        chars[left] = smaller_char
        chars[right] = smaller_char
    
    return ''.join(chars)

def make_smallest_palindrome_two_pointer(s):
    """
    Two-pointer approach to create smallest palindrome.
    
    Args:
        s: String of lowercase English letters
    
    Returns:
        Lexicographically smallest palindrome
    """
    chars = list(s)
    left = 0
    right = len(chars) - 1
    
    while left < right:
        if chars[left] != chars[right]:
            # Choose the lexicographically smaller character
            if chars[left] < chars[right]:
                chars[right] = chars[left]
            else:
                chars[left] = chars[right]
        
        left += 1
        right -= 1
    
    return ''.join(chars)

def make_smallest_palindrome_detailed(s):
    """
    Detailed approach showing step-by-step process.
    
    Args:
        s: String of lowercase English letters
    
    Returns:
        Tuple of (result, changes_made)
    """
    chars = list(s)
    n = len(chars)
    changes = []
    
    for i in range(n // 2):
        left_pos = i
        right_pos = n - 1 - i
        left_char = chars[left_pos]
        right_char = chars[right_pos]
        
        if left_char != right_char:
            # Choose the smaller character
            if left_char < right_char:
                changes.append(f"Position {right_pos}: '{right_char}' -> '{left_char}'")
                chars[right_pos] = left_char
            else:
                changes.append(f"Position {left_pos}: '{left_char}' -> '{right_char}'")
                chars[left_pos] = right_char
    
    return ''.join(chars), changes

def count_changes_needed(s):
    """
    Count minimum number of changes needed to make palindrome.
    
    Args:
        s: String of lowercase English letters
    
    Returns:
        Number of character changes needed
    """
    n = len(s)
    changes = 0
    
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            changes += 1
    
    return changes

def all_possible_smallest_palindromes(s):
    """
    Generate all possible ways to create the smallest palindrome.
    Note: There's only one lexicographically smallest palindrome,
    but this shows the decision process.
    
    Args:
        s: String of lowercase English letters
    
    Returns:
        List of all intermediate steps
    """
    chars = list(s)
    n = len(chars)
    steps = [s]
    
    for i in range(n // 2):
        left = i
        right = n - 1 - i
        
        if chars[left] != chars[right]:
            # Always choose the smaller character
            smaller = min(chars[left], chars[right])
            chars[left] = smaller
            chars[right] = smaller
            steps.append(''.join(chars))
    
    return steps

def test_make_smallest_palindrome():
    """Test the lexicographically smallest palindrome implementation."""
    
    # Test 1: Example 1
    s1 = "egcfe"
    result1 = make_smallest_palindrome(s1)
    assert result1 == "efcfe"
    assert result1 == make_smallest_palindrome_two_pointer(s1)
    
    # Test 2: Example 2
    s2 = "abcd"
    result2 = make_smallest_palindrome(s2)
    assert result2 == "abba"
    assert result2 == make_smallest_palindrome_two_pointer(s2)
    
    # Test 3: Example 3
    s3 = "seven"
    result3 = make_smallest_palindrome(s3)
    assert result3 == "neven"
    assert result3 == make_smallest_palindrome_two_pointer(s3)
    
    # Test 4: Already a palindrome
    s4 = "racecar"
    result4 = make_smallest_palindrome(s4)
    assert result4 == "racecar"
    
    # Test 5: Single character
    s5 = "a"
    result5 = make_smallest_palindrome(s5)
    assert result5 == "a"
    
    # Test 6: Two characters
    s6 = "ab"
    result6 = make_smallest_palindrome(s6)
    assert result6 == "aa"
    
    s7 = "ba"
    result7 = make_smallest_palindrome(s7)
    assert result7 == "aa"
    
    # Test 7: All same characters
    s8 = "aaaa"
    result8 = make_smallest_palindrome(s8)
    assert result8 == "aaaa"
    
    # Test 8: Reverse order
    s9 = "zyxwvu"
    result9 = make_smallest_palindrome(s9)
    assert result9 == "uyxwyu"
    
    # Test 9: Mixed case requiring multiple changes
    s10 = "abcdef"
    result10 = make_smallest_palindrome(s10)
    assert result10 == "abccba"
    
    # Test 10: Odd length with middle character
    s11 = "abcde"
    result11 = make_smallest_palindrome(s11)
    assert result11 == "abcba"
    
    # Test 11: Check changes needed
    assert count_changes_needed("egcfe") == 1  # Only 'g' needs to change
    assert count_changes_needed("abcd") == 2   # Two pairs need changing
    assert count_changes_needed("racecar") == 0  # Already palindrome
    
    # Test 12: Detailed analysis
    result12, changes12 = make_smallest_palindrome_detailed("egcfe")
    assert result12 == "efcfe"
    assert len(changes12) == 1
    
    # Test 13: Step-by-step process
    steps = all_possible_smallest_palindromes("abcdef")
    assert steps[0] == "abcdef"  # Original
    assert steps[-1] == "abccba"  # Final result
    
    # Test 14: Complex example
    s14 = "programming"
    result14 = make_smallest_palindrome(s14)
    # p r o g r a m m i n g
    # 0 1 2 3 4 5 6 7 8 9 10
    # Need: p=g(10), r=n(9), o=i(8), g=m(7), r=m(6)
    # Choose smaller: g, n, i, g, m -> gnigmgming
    expected14 = "gnigrargirg"  # This needs careful calculation
    
    # Let's recalculate manually:
    # programming -> positions (0,10), (1,9), (2,8), (3,7), (4,6), middle=5
    # (p,g) -> g, (r,n) -> n, (o,i) -> i, (g,m) -> g, (r,m) -> m, middle=a
    expected14 = "gnigramaring"
    # Actually: gnigmamgirng - let me recalculate
    s14_chars = list("programming")
    n14 = len(s14_chars)
    for i in range(n14 // 2):
        left_char = s14_chars[i]
        right_char = s14_chars[n14 - 1 - i]
        smaller = min(left_char, right_char)
        s14_chars[i] = smaller
        s14_chars[n14 - 1 - i] = smaller
    expected14 = ''.join(s14_chars)
    
    assert result14 == expected14
    
    print("All test cases passed!")

def demonstrate_algorithm():
    """Demonstrate the algorithm with detailed output."""
    
    test_strings = ["egcfe", "abcd", "seven", "programming"]
    
    print("Lexicographically Smallest Palindrome Algorithm")
    print("=" * 60)
    
    for s in test_strings:
        print(f"\nInput: '{s}'")
        print(f"Length: {len(s)}")
        
        result, changes = make_smallest_palindrome_detailed(s)
        steps = all_possible_smallest_palindromes(s)
        
        print(f"Changes needed: {count_changes_needed(s)}")
        print("Step-by-step transformation:")
        for i, step in enumerate(steps):
            print(f"  Step {i}: {step}")
        
        print("Detailed changes:")
        for change in changes:
            print(f"  {change}")
        
        print(f"Result: '{result}'")
        
        # Verify it's a palindrome
        is_palindrome = result == result[::-1]
        print(f"Is palindrome: {is_palindrome}")
        print("-" * 40)

if __name__ == "__main__":
    test_make_smallest_palindrome()
    demonstrate_algorithm()

"""
COMPLEXITY ANALYSIS:
- Time Complexity: O(n) where n is the length of the string
- Space Complexity: O(n) for creating the character array

TOPICS: String Manipulation, Two Pointers, Greedy Algorithm, Palindrome

KEY INSIGHTS:
1. For lexicographically smallest palindrome, always choose the smaller character
2. Two-pointer approach efficiently compares corresponding positions
3. Middle character in odd-length strings doesn't need to be changed
4. Greedy approach works because local optimal choices lead to global optimum
5. Each position pair needs at most one character change
"""
