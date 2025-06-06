"""
LeetCode Problem #2645: Minimum Additions to Make Valid String

Problem Statement:
Given a string word, you can insert any letter any number of times to make word valid.

Return the minimum number of letters that must be added to make word valid.

A string is considered valid if it can be formed by concatenating the string "abc" zero or more times.

Example 1:
Input: word = "b"
Output: 2
Explanation: Insert "a" to the right of "b", and "c" to the right of "ab" to obtain "abc".

Example 2:
Input: word = "aaa"
Output: 6
Explanation: Insert "bc" after each "a" to obtain "abcabcabc".

Example 3:
Input: word = "abc"
Output: 0
Explanation: word is already valid. No insertions are needed.

Constraints:
- 1 <= word.length <= 50
- word consists of letters 'a', 'b', and 'c' only.
"""

def addMinimum(word: str) -> int:
    """
    Find minimum number of characters to add to make string valid.
    A valid string is formed by concatenating "abc" zero or more times.
    
    Args:
    word: String containing only 'a', 'b', 'c'
    
    Returns:
    Minimum number of characters to add
    """
    n = len(word)
    additions = 0
    i = 0
    
    while i < n:
        # Start of a new "abc" group
        expected = 'a'
        group_additions = 0
        
        # Process one complete "abc" group
        for expected_char in ['a', 'b', 'c']:
            if i < n and word[i] == expected_char:
                i += 1  # Character matches, move to next
            else:
                group_additions += 1  # Character missing, need to add
        
        additions += group_additions
    
    return additions

def addMinimumAlternative(word: str) -> int:
    """
    Alternative approach using state tracking.
    
    Args:
    word: String containing only 'a', 'b', 'c'
    
    Returns:
    Minimum number of characters to add
    """
    additions = 0
    expected = 'a'  # Next expected character in the pattern
    
    for char in word:
        # If current character matches expected, advance
        if char == expected:
            if expected == 'a':
                expected = 'b'
            elif expected == 'b':
                expected = 'c'
            else:  # expected == 'c'
                expected = 'a'
        else:
            # Character doesn't match expected, we need to add missing characters
            while expected != char:
                additions += 1
                if expected == 'a':
                    expected = 'b'
                elif expected == 'b':
                    expected = 'c'
                else:  # expected == 'c'
                    expected = 'a'
            
            # Now process the current character
            if expected == 'a':
                expected = 'b'
            elif expected == 'b':
                expected = 'c'
            else:  # expected == 'c'
                expected = 'a'
    
    # Add remaining characters to complete the last group
    while expected != 'a':
        additions += 1
        if expected == 'b':
            expected = 'c'
        else:  # expected == 'c'
            expected = 'a'
    
    return additions

def addMinimumCounting(word: str) -> int:
    """
    Approach using counting of complete groups.
    
    Args:
    word: String containing only 'a', 'b', 'c'
    
    Returns:
    Minimum number of characters to add
    """
    # Count how many complete "abc" groups we need
    groups = 0
    i = 0
    n = len(word)
    
    while i < n:
        if word[i] == 'a':
            groups += 1
            i += 1
            # Skip 'b' if present
            if i < n and word[i] == 'b':
                i += 1
                # Skip 'c' if present
                if i < n and word[i] == 'c':
                    i += 1
        elif word[i] == 'b':
            groups += 1
            i += 1
            # Skip 'c' if present
            if i < n and word[i] == 'c':
                i += 1
        else:  # word[i] == 'c'
            groups += 1
            i += 1
    
    # Total characters needed = groups * 3
    # Characters we have = len(word)
    return groups * 3 - len(word)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "b"
    print(addMinimum(word1))  # Output: 2
    
    # Test Case 2
    word2 = "aaa"
    print(addMinimum(word2))  # Output: 6
    
    # Test Case 3
    word3 = "abc"
    print(addMinimum(word3))  # Output: 0
    
    # Test Case 4: Mixed patterns
    word4 = "abab"
    print(addMinimum(word4))  # Output: 2 (need "c" after first "ab" and "c" after second "ab")
    
    # Test Case 5: Only 'c' characters
    word5 = "ccc"
    print(addMinimum(word5))  # Output: 6 (need "ab" before each "c")
    
    # Test Case 6: Complex pattern
    word6 = "aabcbc"
    print(addMinimum(word6))  # Output: 3 (a[bc]abc[a]bc -> abcabcabc)
    
    # Test Case 7: Already complete
    word7 = "abcabc"
    print(addMinimum(word7))  # Output: 0
    
    # Test Case 8: Reverse order
    word8 = "cba"
    print(addMinimum(word8))  # Output: 6 (need abc + abc for each character)
    
    # Test alternative approaches
    print("\nAlternative approach results:")
    print(addMinimumAlternative(word1))  # Output: 2
    print(addMinimumAlternative(word2))  # Output: 6
    print(addMinimumAlternative(word3))  # Output: 0
    
    print("\nCounting approach results:")
    print(addMinimumCounting(word1))  # Output: 2
    print(addMinimumCounting(word2))  # Output: 6
    print(addMinimumCounting(word3))  # Output: 0

"""
Time Complexity:
- We iterate through the string once: O(n) where n = len(word)
- For each character, we do constant time operations
- Overall time complexity: O(n)

Space Complexity:
- We use only a constant amount of extra space for variables
- Space complexity: O(1)

Algorithm Explanation:
1. We process the string character by character, expecting the pattern "abc" to repeat
2. For each position, we check if the current character matches what we expect
3. If it matches, we advance to the next expected character
4. If it doesn't match, we count how many characters we need to insert to reach the current character
5. At the end, we add any remaining characters needed to complete the final group

The counting approach works by determining how many complete "abc" groups we need,
then subtracting the length of the input string from the total characters required.
"""

# Topic: Strings
