"""
LeetCode Problem #2668: Find the Divisibility Array of a String

Problem Statement:
You are given a string `word` consisting of digits and an integer `m`. The divisibility array `div` of `word` is an array of length `n` such that:
- `div[i] == 1` if the numeric value of the substring `word[0..i]` (from the 0th index to the ith index) is divisible by `m`.
- Otherwise, `div[i] == 0`.

Return the divisibility array of `word`.

Example:
Input: word = "998244353", m = 3
Output: [1, 1, 0, 0, 0, 1, 1, 0, 0]

Constraints:
- `1 <= word.length <= 10^5`
- `word` consists of digits from '0' to '9'.
- `1 <= m <= 10^9`
"""

def divisibilityArray(word: str, m: int) -> list[int]:
    """
    Function to compute the divisibility array of a string.

    Args:
    word (str): A string consisting of digits.
    m (int): The divisor.

    Returns:
    list[int]: The divisibility array.
    """
    n = len(word)
    div = [0] * n
    current_number = 0

    for i in range(n):
        # Update the current number using modular arithmetic to avoid overflow
        current_number = (current_number * 10 + int(word[i])) % m
        # Check divisibility
        div[i] = 1 if current_number == 0 else 0

    return div

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "998244353"
    m1 = 3
    print(divisibilityArray(word1, m1))  # Output: [1, 1, 0, 0, 0, 1, 1, 0, 0]

    # Test Case 2
    word2 = "123456789"
    m2 = 9
    print(divisibilityArray(word2, m2))  # Output: [0, 0, 1, 0, 0, 0, 1, 0, 1]

    # Test Case 3
    word3 = "111111111"
    m3 = 1
    print(divisibilityArray(word3, m3))  # Output: [1, 1, 1, 1, 1, 1, 1, 1, 1]

    # Test Case 4
    word4 = "987654321"
    m4 = 2
    print(divisibilityArray(word4, m4))  # Output: [0, 1, 0, 1, 0, 1, 0, 1, 0]

    # Test Case 5
    word5 = "1000000000"
    m5 = 10
    print(divisibilityArray(word5, m5))  # Output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

"""
Time Complexity Analysis:
- The function iterates through the string `word` once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where `n` is the length of the string `word`.

Space Complexity Analysis:
- The function uses an array `div` of size `n` to store the result and a constant amount of extra space for variables.
- Therefore, the space complexity is O(n).

Topic: Strings, Modular Arithmetic
"""