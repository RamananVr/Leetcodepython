"""
LeetCode Problem #1165: Single-Row Keyboard

Problem Statement:
There is a special keyboard with all keys in a single row. You are given a string `keyboard` of length 26 indicating the layout of the keyboard (indexed from 0 to 25). Initially, your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.

You want to type a string `word`. Write a function to calculate how much time it takes to type the string `word` with this keyboard.

Example 1:
Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
Output: 4
Explanation:
The index moves are as follows:
- From 'a' to 'c': |0 - 2| = 2
- From 'c' to 'b': |2 - 1| = 1
- From 'b' to 'a': |1 - 0| = 1
Total time = 2 + 1 + 1 = 4.

Example 2:
Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
Output: 73

Constraints:
- `keyboard.length == 26`
- `keyboard` contains each English lowercase letter exactly once in some order.
- `1 <= word.length <= 10^4`
- `word[i]` is an English lowercase letter.
"""

# Python Solution
def calculateTime(keyboard: str, word: str) -> int:
    # Create a dictionary to map each character to its index in the keyboard
    char_to_index = {char: idx for idx, char in enumerate(keyboard)}
    
    # Initialize the total time and the starting position
    total_time = 0
    current_position = 0
    
    # Iterate through each character in the word
    for char in word:
        # Calculate the time to move to the current character
        target_position = char_to_index[char]
        total_time += abs(target_position - current_position)
        # Update the current position
        current_position = target_position
    
    return total_time

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    keyboard1 = "abcdefghijklmnopqrstuvwxyz"
    word1 = "cba"
    print(calculateTime(keyboard1, word1))  # Output: 4

    # Test Case 2
    keyboard2 = "pqrstuvwxyzabcdefghijklmno"
    word2 = "leetcode"
    print(calculateTime(keyboard2, word2))  # Output: 73

    # Test Case 3
    keyboard3 = "abcdefghijklmnopqrstuvwxyz"
    word3 = "a"
    print(calculateTime(keyboard3, word3))  # Output: 0

    # Test Case 4
    keyboard4 = "abcdefghijklmnopqrstuvwxyz"
    word4 = "z"
    print(calculateTime(keyboard4, word4))  # Output: 25

# Time and Space Complexity Analysis
# Time Complexity:
# - Constructing the `char_to_index` dictionary takes O(26) = O(1) since the keyboard has a fixed length of 26.
# - Iterating through the `word` takes O(n), where n is the length of the word.
# - Overall time complexity: O(n).

# Space Complexity:
# - The `char_to_index` dictionary requires O(26) = O(1) space.
# - Other variables use O(1) space.
# - Overall space complexity: O(1).

# Topic: Hash Table, String