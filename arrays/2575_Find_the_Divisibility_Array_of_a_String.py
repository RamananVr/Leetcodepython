"""
LeetCode Problem #2575: Find the Divisibility Array of a String

Problem Statement:
You are given a string `word` of length `n` consisting of digits, and an integer `m`.
The divisibility array `div` of `word` is an integer array of length `n` such that:

- `div[i] = 1` if the numeric value of the substring `word[0...i]` (from the 0th index to the ith index) is divisible by `m`.
- Otherwise, `div[i] = 0`.

Return the divisibility array `div` of `word`.

Example:
Input: word = "998244353", m = 3
Output: [1, 1, 0, 0, 0, 1, 0, 0, 0]

Constraints:
- `1 <= n <= 10^5`
- `word.length == n`
- `word` consists of digits ('0' to '9').
- `1 <= m <= 10^9`
"""

# Solution
def divisibilityArray(word: str, m: int) -> list[int]:
    """
    Computes the divisibility array for the given string `word` and integer `m`.

    Args:
    word (str): A string consisting of digits.
    m (int): The divisor.

    Returns:
    list[int]: The divisibility array.
    """
    div = []
    current_number = 0

    for char in word:
        current_number = (current_number * 10 + int(char)) % m
        div.append(1 if current_number == 0 else 0)

    return div

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word = "998244353"
    m = 3
    print(divisibilityArray(word, m))  # Output: [1, 1, 0, 0, 0, 1, 0, 0, 0]

    # Test Case 2
    word = "123456789"
    m = 9
    print(divisibilityArray(word, m))  # Output: [0, 0, 0, 0, 0, 0, 0, 0, 1]

    # Test Case 3
    word = "111111111"
    m = 1
    print(divisibilityArray(word, m))  # Output: [1, 1, 1, 1, 1, 1, 1, 1, 1]

    # Test Case 4
    word = "987654321"
    m = 7
    print(divisibilityArray(word, m))  # Output: [0, 0, 0, 0, 0, 0, 1, 0, 0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through each character in the string `word` once.
- For each character, it performs constant-time operations (multiplication, addition, modulo).
- Therefore, the time complexity is O(n), where `n` is the length of the string `word`.

Space Complexity:
- The algorithm uses a list `div` of size `n` to store the divisibility array.
- Additionally, it uses a single integer variable `current_number` for intermediate calculations.
- Therefore, the space complexity is O(n), where `n` is the length of the string `word`.
"""

# Topic: Arrays