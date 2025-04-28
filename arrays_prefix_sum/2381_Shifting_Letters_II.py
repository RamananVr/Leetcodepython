"""
LeetCode Problem #2381: Shifting Letters II

Problem Statement:
You are given a string `s` of lowercase English letters and a 2D integer array `shifts` where `shifts[i] = [start_i, end_i, direction_i]`. 
For every `i`, apply a shift to the substring `s[start_i...end_i]` (inclusive):
- If `direction_i == 1`, shift the characters to the right by 1.
- If `direction_i == 0`, shift the characters to the left by 1.

Shifting a character means:
- 'a' becomes 'b', 'b' becomes 'c', ..., 'z' becomes 'a' when shifting to the right.
- 'a' becomes 'z', 'b' becomes 'a', ..., 'z' becomes 'y' when shifting to the left.

Return the final string after all such shifts to `s` are applied.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- 1 <= shifts.length <= 10^5
- 0 <= start_i <= end_i < s.length
- direction_i is either 0 or 1.
"""

def shiftingLetters(s: str, shifts: list[list[int]]) -> str:
    """
    Function to apply the shifts to the string `s` as described in the problem statement.
    """
    n = len(s)
    shift_effect = [0] * (n + 1)  # Use a difference array to track shifts

    # Apply shifts using the difference array
    for start, end, direction in shifts:
        if direction == 1:  # Right shift
            shift_effect[start] += 1
            shift_effect[end + 1] -= 1
        else:  # Left shift
            shift_effect[start] -= 1
            shift_effect[end + 1] += 1

    # Compute the cumulative shift effect
    for i in range(1, n):
        shift_effect[i] += shift_effect[i - 1]

    # Apply the shifts to the string
    result = []
    for i in range(n):
        # Normalize the shift to be within the range [0, 26)
        shift = shift_effect[i] % 26
        # Calculate the new character
        new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
        result.append(new_char)

    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abc"
    shifts1 = [[0, 1, 0], [1, 2, 1]]
    print(shiftingLetters(s1, shifts1))  # Expected Output: "zac"

    # Test Case 2
    s2 = "dzt"
    shifts2 = [[0, 0, 1], [1, 1, 0], [2, 2, 1]]
    print(shiftingLetters(s2, shifts2))  # Expected Output: "eay"

    # Test Case 3
    s3 = "xyz"
    shifts3 = [[0, 2, 1], [0, 1, 0]]
    print(shiftingLetters(s3, shifts3))  # Expected Output: "yza"

"""
Time Complexity Analysis:
- Applying the shifts to the difference array takes O(m), where m is the number of shifts.
- Calculating the cumulative shift effect takes O(n), where n is the length of the string.
- Constructing the final string takes O(n).
- Overall time complexity: O(n + m).

Space Complexity Analysis:
- The difference array `shift_effect` takes O(n) space.
- The result array takes O(n) space.
- Overall space complexity: O(n).

Topic: Arrays, Prefix Sum
"""