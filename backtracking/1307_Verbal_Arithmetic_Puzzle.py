"""
LeetCode Problem #1307: Verbal Arithmetic Puzzle

Problem Statement:
Given an equation, represented by words on the left side and the result on the right side, 
find if the equation is solvable under the following rules:

1. Each character is assigned a digit from 0 to 9.
2. No two characters can map to the same digit.
3. Each word must be interpreted as a number without leading zeros.
4. The equation is valid if the sum of the numbers on the left side equals the number on the right side.

You are given an array `words` and a string `result` that represent the equation. Return `true` if the equation is solvable, otherwise return `false`.

Example:
Input: words = ["SEND", "MORE"], result = "MONEY"
Output: true

Explanation:
One possible solution is:
'S' -> 9, 'E' -> 5, 'N' -> 6, 'D' -> 7, 'M' -> 1, 'O' -> 0, 'R' -> 8, 'Y' -> 2
SEND + MORE = MONEY
9567 + 1089 = 10656
"""

from itertools import permutations

def is_solvable(words, result):
    """
    Determines if the given verbal arithmetic puzzle is solvable.

    :param words: List[str] - List of words on the left side of the equation.
    :param result: str - The result word on the right side of the equation.
    :return: bool - True if the equation is solvable, False otherwise.
    """
    # Combine all unique characters from words and result
    unique_chars = set("".join(words) + result)
    
    # If there are more than 10 unique characters, it's impossible to assign digits
    if len(unique_chars) > 10:
        return False
    
    # Convert the unique characters into a list for easier indexing
    unique_chars = list(unique_chars)
    
    # Helper function to convert a word into its numeric value based on the mapping
    def word_to_number(word, char_to_digit):
        num = 0
        for char in word:
            num = num * 10 + char_to_digit[char]
        return num
    
    # Try all permutations of digits for the unique characters
    for perm in permutations(range(10), len(unique_chars)):
        char_to_digit = {char: digit for char, digit in zip(unique_chars, perm)}
        
        # Check for leading zeros
        if any(char_to_digit[word[0]] == 0 for word in words + [result]):
            continue
        
        # Calculate the sum of the left side and the value of the result
        left_sum = sum(word_to_number(word, char_to_digit) for word in words)
        right_value = word_to_number(result, char_to_digit)
        
        # Check if the equation is valid
        if left_sum == right_value:
            return True
    
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words = ["SEND", "MORE"]
    result = "MONEY"
    print(is_solvable(words, result))  # Output: True

    # Test Case 2
    words = ["LEET", "CODE"]
    result = "POINT"
    print(is_solvable(words, result))  # Output: False

    # Test Case 3
    words = ["A", "B"]
    result = "C"
    print(is_solvable(words, result))  # Output: True

    # Test Case 4
    words = ["ABC", "DEF"]
    result = "GHI"
    print(is_solvable(words, result))  # Output: False

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The number of unique characters is at most 10.
   - We generate all permutations of digits for these characters, which is O(10!).
   - For each permutation, we calculate the numeric values of the words and the result, which is O(n * m), 
     where n is the number of words and m is the average length of the words.
   - Overall time complexity: O(10! * n * m), which is feasible for small inputs.

2. Space Complexity:
   - The space required for storing the character-to-digit mapping is O(10).
   - The space required for generating permutations is O(10!).
   - Overall space complexity: O(10!).

Topic: Backtracking
"""