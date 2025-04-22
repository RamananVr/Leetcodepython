"""
LeetCode Question #17: Letter Combinations of a Phone Number

Problem Statement:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

    2 -> "abc"
    3 -> "def"
    4 -> "ghi"
    5 -> "jkl"
    6 -> "mno"
    7 -> "pqrs"
    8 -> "tuv"
    9 -> "wxyz"

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].
"""

# Solution
from typing import List

def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []
    
    # Mapping of digits to letters
    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    
    # Helper function for backtracking
    def backtrack(index: int, path: str):
        # If the current combination is complete, add it to the result
        if index == len(digits):
            combinations.append(path)
            return
        
        # Get the letters corresponding to the current digit
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            # Append the letter to the current path and move to the next digit
            backtrack(index + 1, path + letter)
    
    # List to store the combinations
    combinations = []
    backtrack(0, "")
    return combinations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    digits = "23"
    print(letterCombinations(digits))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    # Test Case 2
    digits = ""
    print(letterCombinations(digits))  # Output: []

    # Test Case 3
    digits = "2"
    print(letterCombinations(digits))  # Output: ["a","b","c"]

# Topic: Backtracking