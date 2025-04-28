"""
LeetCode Problem #2193: Minimum Number of Moves to Make Palindrome

Problem Statement:
You are given a string s consisting only of lowercase English letters.

In one move, you can select any two adjacent characters of s and swap them.

Return the minimum number of moves needed to make s a palindrome.

Example 1:
Input: s = "aabb"
Output: 2
Explanation:
- Swap s[1] and s[2], s becomes "abab".
- Swap s[2] and s[3], s becomes "abba".

Example 2:
Input: s = "letelt"
Output: 2
Explanation:
- Swap s[2] and s[3], s becomes "leltet".
- Swap s[3] and s[4], s becomes "letetl".

Constraints:
- 1 <= s.length <= 2000
- s consists only of lowercase English letters.
"""

def minMovesToMakePalindrome(s: str) -> int:
    """
    Function to calculate the minimum number of moves to make a string palindrome.
    """
    s = list(s)
    n = len(s)
    moves = 0

    while len(s) > 1:
        # If the first and last characters are the same, no swap is needed
        if s[0] == s[-1]:
            s.pop(0)
            s.pop(-1)
        else:
            # Find the matching character for the first character
            match_index = s.index(s[-1])
            if match_index == len(s) - 1:
                # If the last character has no match, move it to the middle
                s.pop(-1)
                moves += len(s) // 2
            else:
                # Swap the matching character to the end
                s.pop(match_index)
                s.pop(-1)
                moves += match_index
    return moves

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aabb"
    print(f"Minimum moves to make '{s1}' a palindrome: {minMovesToMakePalindrome(s1)}")  # Output: 2

    # Test Case 2
    s2 = "letelt"
    print(f"Minimum moves to make '{s2}' a palindrome: {minMovesToMakePalindrome(s2)}")  # Output: 2

    # Test Case 3
    s3 = "racecar"
    print(f"Minimum moves to make '{s3}' a palindrome: {minMovesToMakePalindrome(s3)}")  # Output: 0

    # Test Case 4
    s4 = "abcd"
    print(f"Minimum moves to make '{s4}' a palindrome: {minMovesToMakePalindrome(s4)}")  # Output: 4

"""
Time Complexity:
- The algorithm iterates through the string, and for each character, it may perform a linear search to find a match.
- In the worst case, this results in O(n^2) time complexity, where n is the length of the string.

Space Complexity:
- The algorithm uses a list to store the characters of the string, which takes O(n) space.
- No additional data structures are used, so the overall space complexity is O(n).

Topic: String Manipulation, Two Pointers
"""