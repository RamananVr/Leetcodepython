"""
LeetCode Question #848: Shifting Letters

Problem Statement:
You are given a string `s` of lowercase English letters and an integer array `shifts` of the same length.

Each element `shifts[i]` indicates the total number of times the `i-th` character of `s` should be shifted. A shift means increasing the character's value by one (e.g., 'a' becomes 'b', 'z' becomes 'a').

Return the final string after all the shifts have been applied to `s`.

Constraints:
- `1 <= s.length <= 10^5`
- `shifts.length == s.length`
- `0 <= shifts[i] <= 10^9`
"""

# Solution
def shiftingLetters(s: str, shifts: list[int]) -> str:
    # Calculate the cumulative shifts from the end of the array
    n = len(shifts)
    cumulative_shift = 0
    result = []

    for i in range(n - 1, -1, -1):
        cumulative_shift += shifts[i]
        # Apply the shift to the current character
        new_char = chr((ord(s[i]) - ord('a') + cumulative_shift) % 26 + ord('a'))
        result.append(new_char)

    # Reverse the result list to get the final string
    return ''.join(result[::-1])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abc"
    shifts1 = [3, 5, 9]
    print(shiftingLetters(s1, shifts1))  # Expected Output: "rpl"

    # Test Case 2
    s2 = "aaa"
    shifts2 = [1, 2, 3]
    print(shiftingLetters(s2, shifts2))  # Expected Output: "gfd"

    # Test Case 3
    s3 = "xyz"
    shifts3 = [1, 1, 1]
    print(shiftingLetters(s3, shifts3))  # Expected Output: "yza"

    # Test Case 4
    s4 = "z"
    shifts4 = [26]
    print(shiftingLetters(s4, shifts4))  # Expected Output: "z"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the `shifts` array once in reverse order, which takes O(n) time.
- Constructing the result string also takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- The solution uses a list `result` to store the shifted characters, which takes O(n) space.
- Other variables (e.g., `cumulative_shift`) use O(1) space.
- Overall space complexity: O(n).
"""

# Topic: Strings