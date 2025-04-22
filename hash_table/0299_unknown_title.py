"""
LeetCode Problem #299: Bulls and Cows

Problem Statement:
You are playing the "Bulls and Cows" game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:
- The number of "bulls", which are digits in the guess that are in the correct position.
- The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Note that "bulls" take precedence over "cows".

Given the secret number `secret` and your friend's guess `guess`, return the hint as a string formatted as `"xAyB"`, where:
- `x` is the number of bulls.
- `y` is the number of cows.

Note:
- Both `secret` and `guess` contain only digits and have the same length.
- Both `secret` and `guess` may contain duplicate digits.

Example 1:
Input: secret = "1807", guess = "7810"
Output: "1A3B"

Example 2:
Input: secret = "1123", guess = "0111"
Output: "1A1B"

Constraints:
- 1 <= secret.length <= 1000
- secret.length == guess.length
- secret and guess consist of digits only.
"""

def getHint(secret: str, guess: str) -> str:
    """
    Function to calculate the number of bulls and cows in the Bulls and Cows game.
    """
    bulls = 0
    cows = 0
    secret_count = {}
    guess_count = {}

    # First pass: Count bulls and track unmatched characters
    for s, g in zip(secret, guess):
        if s == g:
            bulls += 1
        else:
            secret_count[s] = secret_count.get(s, 0) + 1
            guess_count[g] = guess_count.get(g, 0) + 1

    # Second pass: Count cows based on unmatched characters
    for digit in guess_count:
        if digit in secret_count:
            cows += min(secret_count[digit], guess_count[digit])

    return f"{bulls}A{cows}B"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    secret = "1807"
    guess = "7810"
    print(getHint(secret, guess))  # Output: "1A3B"

    # Test Case 2
    secret = "1123"
    guess = "0111"
    print(getHint(secret, guess))  # Output: "1A1B"

    # Test Case 3
    secret = "1234"
    guess = "5678"
    print(getHint(secret, guess))  # Output: "0A0B"

    # Test Case 4
    secret = "1122"
    guess = "2211"
    print(getHint(secret, guess))  # Output: "0A4B"

"""
Time Complexity Analysis:
- The function iterates through the `secret` and `guess` strings twice:
  - First pass: O(n), where n is the length of the strings, to count bulls and populate the dictionaries.
  - Second pass: O(1) for each digit (since there are at most 10 digits), which is effectively O(1).
- Overall time complexity: O(n).

Space Complexity Analysis:
- The function uses two dictionaries (`secret_count` and `guess_count`) to store counts of unmatched characters.
- The space complexity is O(1) because the dictionaries store at most 10 keys (digits 0-9).
- Overall space complexity: O(1).

Topic: Hash Table
"""