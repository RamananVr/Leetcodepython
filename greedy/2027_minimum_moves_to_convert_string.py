"""
LeetCode Question #2027: Minimum Moves to Convert String

Problem Statement:
You are given a string s consisting of n characters which are either 'X' or 'O'.

A move consists of selecting three consecutive characters of s and converting them to 'O'. 
Note that if a move is applied to the character 'O', it will stay the same.

Return the minimum number of moves required to convert s to a string consisting of only 'O' characters.

Example 1:
Input: s = "XXX"
Output: 1
Explanation: XXX -> OOO

Example 2:
Input: s = "XXOX"
Output: 2
Explanation: XXOX -> OOOX -> OOOO

Example 3:
Input: s = "OOOO"
Output: 0
Explanation: There are no 'X' characters to convert.

Constraints:
- 3 <= s.length <= 1000
- s[i] is either 'X' or 'O'.
"""

def minimumMoves(s: str) -> int:
    """
    Calculate the minimum number of moves required to convert the string s to all 'O's.
    
    :param s: A string consisting of 'X' and 'O'.
    :return: The minimum number of moves required.
    """
    moves = 0
    i = 0
    
    while i < len(s):
        if s[i] == 'X':
            # Apply a move to convert three consecutive characters to 'O'
            moves += 1
            i += 3  # Skip the next two characters as they are converted to 'O'
        else:
            i += 1  # Move to the next character
    
    return moves

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "XXX"
    print(minimumMoves(s1))  # Output: 1

    # Test Case 2
    s2 = "XXOX"
    print(minimumMoves(s2))  # Output: 2

    # Test Case 3
    s3 = "OOOO"
    print(minimumMoves(s3))  # Output: 0

    # Test Case 4
    s4 = "XOXOXOXO"
    print(minimumMoves(s4))  # Output: 3

    # Test Case 5
    s5 = "XOOX"
    print(minimumMoves(s5))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string s once, processing each character.
- In the worst case, we skip 3 characters for every 'X' encountered.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The algorithm uses a constant amount of extra space (variables `moves` and `i`).
- No additional data structures are used.
- Therefore, the space complexity is O(1).

Topic: Greedy
"""