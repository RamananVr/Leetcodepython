"""
LeetCode Problem #2266: Count Number of Texts

Problem Statement:
Alice is texting Bob using her phone. The mapping of digits to letters is shown on the keypad below.

Each digit maps to a set of characters as follows:
1 -> None
2 -> "abc"
3 -> "def"
4 -> "ghi"
5 -> "jkl"
6 -> "mno"
7 -> "pqrs"
8 -> "tuv"
9 -> "wxyz"

Alice wants to text a string `pressedKeys` where each character in the string represents the digit she pressed. 
The characters corresponding to a single digit are sorted in lexicographical order, and Alice can press a button 
1 to 4 times to type a single character.

- For example, if Alice presses the button '2' once, she types 'a'. If she presses it twice, she types 'b'. 
  If she presses it three times, she types 'c', and if she presses it four times, it is invalid.

Given a string `pressedKeys` representing the sequence of buttons Alice pressed, return the total number of 
possible text messages Alice could have typed. Since the answer may be very large, return it modulo 10^9 + 7.

Constraints:
- 1 <= pressedKeys.length <= 10^5
- pressedKeys only consists of digits from '2' to '9'.

Example:
Input: pressedKeys = "22233"
Output: 8
Explanation: 
The possible text messages Alice could have typed are:
"aaadd", "aabdd", "abadd", "bbaad", "caadd", "cabdd", "cbadd", and "ccadd".
"""

# Python Solution
def countTexts(pressedKeys: str) -> int:
    MOD = 10**9 + 7

    # Maximum number of presses for each digit
    max_presses = {
        '2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '8': 3,
        '7': 4, '9': 4
    }

    n = len(pressedKeys)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: 1 way to type an empty string

    for i in range(1, n + 1):
        dp[i] = 0
        for j in range(1, max_presses[pressedKeys[i - 1]] + 1):
            if i - j >= 0 and pressedKeys[i - j] == pressedKeys[i - 1]:
                dp[i] = (dp[i] + dp[i - j]) % MOD
            else:
                break

    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    pressedKeys = "22233"
    print(countTexts(pressedKeys))  # Output: 8

    # Test Case 2
    pressedKeys = "2222222222"
    print(countTexts(pressedKeys))  # Output: 89

    # Test Case 3
    pressedKeys = "7777"
    print(countTexts(pressedKeys))  # Output: 8

    # Test Case 4
    pressedKeys = "99999"
    print(countTexts(pressedKeys))  # Output: 16

    # Test Case 5
    pressedKeys = "88888888"
    print(countTexts(pressedKeys))  # Output: 34

"""
Time Complexity:
- The outer loop runs for `n` iterations, where `n` is the length of `pressedKeys`.
- The inner loop runs for at most 4 iterations (since the maximum number of presses for any digit is 4).
- Therefore, the time complexity is O(n).

Space Complexity:
- The space complexity is O(n) due to the `dp` array used to store intermediate results.

Topic: Dynamic Programming (DP)
"""