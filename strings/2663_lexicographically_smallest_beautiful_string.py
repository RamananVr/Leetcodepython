"""
LeetCode Question #2663: Lexicographically Smallest Beautiful String

Problem Statement:
A string is beautiful if:
- It consists of the first k letters of the English alphabet.
- It does not contain any substring of length 2 or more which is a palindrome.

You are given a beautiful string s of length n and a positive integer k.

Return the lexicographically smallest string of length n, which is larger than s, that is beautiful. If there is no such string, return an empty string.

A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b.

Examples:
Example 1:
Input: s = "abcz", k = 4
Output: "abda"
Explanation: The string "abda" is beautiful and lexicographically larger than the string "abcz".
It can be shown that there is no string that is lexicographically larger than "abcz", beautiful, and lexicographically smaller than "abda".

Example 2:
Input: s = "dc", k = 4
Output: ""
Explanation: It can be shown that there is no beautiful string lexicographically larger than "dc".

Constraints:
- 1 <= n <= 10^5
- 4 <= k <= 26
- s is a beautiful string.
"""

def smallestBeautifulString(s: str, k: int) -> str:
    """
    Find the lexicographically smallest beautiful string larger than s.
    
    Strategy:
    1. Start from the rightmost character and try to increment it
    2. For each position, find the smallest valid character that:
       - Is larger than current character (for increment)
       - Doesn't form palindromes with previous characters
    3. Fill remaining positions with smallest valid characters
    """
    n = len(s)
    s_list = list(s)
    
    # Helper function to check if placing char at position i is valid
    def is_valid_char(char, pos):
        # Check if it forms palindrome with previous character
        if pos > 0 and s_list[pos - 1] == char:
            return False
        # Check if it forms palindrome with character two positions back
        if pos > 1 and s_list[pos - 2] == char:
            return False
        return True
    
    # Try to increment from right to left
    for i in range(n - 1, -1, -1):
        # Try characters larger than current
        for next_char_ord in range(ord(s_list[i]) + 1, ord('a') + k):
            next_char = chr(next_char_ord)
            
            if is_valid_char(next_char, i):
                s_list[i] = next_char
                
                # Fill remaining positions to the right with smallest valid characters
                for j in range(i + 1, n):
                    for fill_char_ord in range(ord('a'), ord('a') + k):
                        fill_char = chr(fill_char_ord)
                        if is_valid_char(fill_char, j):
                            s_list[j] = fill_char
                            break
                
                return ''.join(s_list)
    
    # No valid string found
    return ""

def smallestBeautifulStringOptimized(s: str, k: int) -> str:
    """
    Optimized version with cleaner logic.
    """
    n = len(s)
    s_arr = list(s)
    
    def get_next_valid_char(pos, start_char='a'):
        """Get the next valid character for position pos starting from start_char."""
        for c in range(ord(start_char), ord('a') + k):
            char = chr(c)
            # Check constraints
            valid = True
            if pos > 0 and s_arr[pos - 1] == char:
                valid = False
            if pos > 1 and s_arr[pos - 2] == char:
                valid = False
            if valid:
                return char
        return None
    
    # Find rightmost position that can be incremented
    for i in range(n - 1, -1, -1):
        # Try to increment current character
        current_char_ord = ord(s_arr[i])
        next_char = get_next_valid_char(i, chr(current_char_ord + 1))
        
        if next_char:
            s_arr[i] = next_char
            
            # Fill remaining positions with smallest valid characters
            for j in range(i + 1, n):
                s_arr[j] = get_next_valid_char(j, 'a')
            
            return ''.join(s_arr)
    
    return ""

def smallestBeautifulStringBruteForce(s: str, k: int) -> str:
    """
    Brute force approach for validation (works for small inputs).
    """
    def is_beautiful(string):
        """Check if string is beautiful."""
        # Check if all characters are within first k letters
        for char in string:
            if ord(char) >= ord('a') + k:
                return False
        
        # Check for palindromic substrings of length >= 2
        n = len(string)
        for i in range(n):
            for j in range(i + 2, n + 1):
                substring = string[i:j]
                if substring == substring[::-1]:
                    return False
        return True
    
    def next_string(string):
        """Generate next lexicographically larger string."""
        s_list = list(string)
        n = len(s_list)
        
        # Find rightmost character that can be incremented
        for i in range(n - 1, -1, -1):
            if ord(s_list[i]) < ord('a') + k - 1:
                s_list[i] = chr(ord(s_list[i]) + 1)
                # Reset all characters to the right to 'a'
                for j in range(i + 1, n):
                    s_list[j] = 'a'
                return ''.join(s_list)
        
        return None
    
    # Generate next strings until we find a beautiful one
    current = s
    for _ in range(10000):  # Limit iterations to avoid infinite loop
        current = next_string(current)
        if current is None:
            return ""
        if is_beautiful(current):
            return current
    
    return ""

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ("abcz", 4, "abda"),
        ("dc", 4, ""),
        ("abc", 4, "abd"),
        ("abd", 4, "aba"),
        ("abdc", 4, "abaca"),
        ("a", 4, "b"),
        ("d", 4, "")
    ]
    
    print("Testing main approach:")
    for s, k, expected in test_cases:
        result = smallestBeautifulString(s, k)
        print(f"smallestBeautifulString('{s}', {k}) = '{result}', expected = '{expected}', {'✓' if result == expected else '✗'}")
    
    print("\nTesting optimized approach:")
    for s, k, expected in test_cases:
        result = smallestBeautifulStringOptimized(s, k)
        print(f"smallestBeautifulStringOptimized('{s}', {k}) = '{result}', expected = '{expected}', {'✓' if result == expected else '✗'}")
    
    # Note: Brute force approach might be too slow for larger inputs
    print("\nTesting brute force approach (small inputs only):")
    small_test_cases = [case for case in test_cases if len(case[0]) <= 4]
    for s, k, expected in small_test_cases:
        result = smallestBeautifulStringBruteForce(s, k)
        print(f"smallestBeautifulStringBruteForce('{s}', {k}) = '{result}', expected = '{expected}', {'✓' if result == expected else '✗'}")

"""
Time and Space Complexity Analysis:

Main Approach:
Time Complexity: O(n * k) where n = length of string, k = alphabet size
- For each position (O(n)), we try at most k characters
- For each character, we do O(1) validation
Space Complexity: O(n) - for storing the string as list

Optimized Approach:
Time Complexity: O(n * k) - same as main approach but with cleaner code
Space Complexity: O(n) - for storing the string as list

Brute Force Approach:
Time Complexity: O(exponential) - generates many strings and checks each
Space Complexity: O(n) - for storing strings
Note: Not practical for large inputs

Key Insights:
1. Beautiful string constraints:
   - Only first k letters of alphabet
   - No palindromic substrings of length ≥ 2
2. To avoid palindromes, character at position i should differ from:
   - Character at position i-1 (length 2 palindrome)
   - Character at position i-2 (length 3 palindrome)
3. Greedy approach: increment rightmost possible position, then fill with smallest valid chars

Algorithm Steps:
1. From right to left, find first position that can be incremented
2. Increment that position to next valid character
3. Fill all positions to the right with smallest valid characters
4. Return result or empty string if impossible

Topic: Strings, Greedy, Lexicographic Order, Constraint Satisfaction
"""
