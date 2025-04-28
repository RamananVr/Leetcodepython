"""
LeetCode Question #1320: Minimum Distance to Type a Word Using Two Fingers

Problem Statement:
You have a keyboard layout as shown below:

    A B C D E F
    G H I J K L
    M N O P Q R
    S T U V W X
    Y Z

Each letter is placed at a specific position on the keyboard. For example, the letter 'A' is at position (0, 0), 
the letter 'B' is at position (0, 1), and so on.

You can use two fingers to type a word. Initially, both fingers are on the starting position (undefined). 
To type a character, you can move one of your fingers to the target character. The distance between two 
positions (r1, c1) and (r2, c2) is defined as |r1 - r2| + |c1 - c2|.

Given a string `word`, return the minimum distance to type the word using two fingers.

Constraints:
- 2 <= word.length <= 300
- word consists of uppercase English letters.

Example:
Input: word = "CAKE"
Output: 3
Explanation: 
Using two fingers, one optimal way is:
- Move one finger to 'C' (distance = 0)
- Move the other finger to 'A' (distance = 2)
- Move the first finger to 'K' (distance = 1)
- Move the second finger to 'E' (distance = 0)
The total distance is 3.
"""

# Python Solution
from functools import lru_cache

def minimumDistance(word: str) -> int:
    # Helper function to calculate Manhattan distance between two keys
    def get_distance(c1, c2):
        if c1 == c2:
            return 0
        r1, c1 = divmod(ord(c1) - ord('A'), 6)
        r2, c2 = divmod(ord(c2) - ord('A'), 6)
        return abs(r1 - r2) + abs(c1 - c2)

    @lru_cache(None)
    def dp(index, finger1, finger2):
        # Base case: if we've typed all characters
        if index == len(word):
            return 0

        # Current character to type
        current_char = word[index]

        # Option 1: Move finger1 to the current character
        cost1 = get_distance(finger1, current_char) + dp(index + 1, current_char, finger2)

        # Option 2: Move finger2 to the current character
        cost2 = get_distance(finger2, current_char) + dp(index + 1, finger1, current_char)

        # Return the minimum cost
        return min(cost1, cost2)

    # Start with both fingers at an undefined position ('*')
    return dp(0, '*', '*')

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "CAKE"
    print(f"Minimum distance to type '{word1}': {minimumDistance(word1)}")  # Expected Output: 3

    # Test Case 2
    word2 = "HAPPY"
    print(f"Minimum distance to type '{word2}': {minimumDistance(word2)}")  # Expected Output: 6

    # Test Case 3
    word3 = "NEW"
    print(f"Minimum distance to type '{word3}': {minimumDistance(word3)}")  # Expected Output: 3

    # Test Case 4
    word4 = "TYPE"
    print(f"Minimum distance to type '{word4}': {minimumDistance(word4)}")  # Expected Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function uses memoization to store results for each unique state (index, finger1, finger2).
- There are O(n * 26 * 26) states, where n is the length of the word and 26 represents the number of letters in the alphabet.
- Each state takes O(1) time to compute, so the overall time complexity is O(n * 26 * 26).

Space Complexity:
- The space complexity is determined by the memoization table, which stores O(n * 26 * 26) states.
- Additionally, the recursion stack can go up to O(n) depth.
- Thus, the overall space complexity is O(n * 26 * 26).
"""

# Topic: Dynamic Programming (DP)