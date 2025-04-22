"""
LeetCode Problem #344: Reverse String

Problem Statement:
Write a function that reverses a string. The input string is given as an array of characters `s`.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
- 1 <= s.length <= 10^5
- `s[i]` is a printable ASCII character.
"""

# Clean, Correct Python Solution
def reverseString(s):
    """
    Reverses the input list of characters in-place.

    :param s: List[str] - The input list of characters
    :return: None - The input list is modified in-place
    """
    left, right = 0, len(s) - 1
    while left < right:
        # Swap characters at the left and right pointers
        s[left], s[right] = s[right], s[left]
        # Move the pointers closer to the center
        left += 1
        right -= 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = ["h", "e", "l", "l", "o"]
    reverseString(s1)
    print(s1)  # Expected Output: ["o", "l", "l", "e", "h"]

    # Test Case 2
    s2 = ["H", "a", "n", "n", "a", "h"]
    reverseString(s2)
    print(s2)  # Expected Output: ["h", "a", "n", "n", "a", "H"]

    # Test Case 3
    s3 = ["a"]
    reverseString(s3)
    print(s3)  # Expected Output: ["a"]

    # Test Case 4
    s4 = ["A", "B", "C", "D", "E"]
    reverseString(s4)
    print(s4)  # Expected Output: ["E", "D", "C", "B", "A"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through half of the list, performing a constant-time swap operation for each pair of characters.
- Therefore, the time complexity is O(n), where n is the length of the input list.

Space Complexity:
- The function uses only a constant amount of extra space (two pointers: `left` and `right`).
- Therefore, the space complexity is O(1).
"""

# Topic: Two Pointers