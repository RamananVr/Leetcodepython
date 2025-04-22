"""
LeetCode Question #925: Long Pressed Name

Problem Statement:
Your friend is typing their name into a keyboard. Sometimes, when typing a character, the key might get long pressed, 
and the character will be typed one or more times.

You examine the typed characters and the original name. Return True if the typed string is a valid long-pressed version 
of the name.

Example 1:
Input: name = "alex", typed = "aaleex"
Output: True
Explanation: 'a' and 'e' in "alex" were long pressed.

Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: False
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Constraints:
- 1 <= name.length, typed.length <= 1000
- name and typed consist of only lowercase English letters.
"""

# Solution
def isLongPressedName(name: str, typed: str) -> bool:
    """
    Determines if the typed string is a valid long-pressed version of the name.

    :param name: Original name string.
    :param typed: Typed string that may include long presses.
    :return: True if typed is a valid long-pressed version of name, False otherwise.
    """
    i, j = 0, 0  # Pointers for name and typed strings
    
    while i < len(name) and j < len(typed):
        if name[i] == typed[j]:
            i += 1
            j += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            j += 1
        else:
            return False
    
    # Check if remaining characters in `typed` are valid long presses
    while j < len(typed):
        if typed[j] != typed[j - 1]:
            return False
        j += 1
    
    # Ensure all characters in `name` were matched
    return i == len(name)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    name = "alex"
    typed = "aaleex"
    print(isLongPressedName(name, typed))  # Output: True

    # Test Case 2
    name = "saeed"
    typed = "ssaaedd"
    print(isLongPressedName(name, typed))  # Output: False

    # Test Case 3
    name = "leelee"
    typed = "lleeelee"
    print(isLongPressedName(name, typed))  # Output: True

    # Test Case 4
    name = "laiden"
    typed = "laiden"
    print(isLongPressedName(name, typed))  # Output: True

    # Test Case 5
    name = "py"
    typed = "ppyy"
    print(isLongPressedName(name, typed))  # Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through both `name` and `typed` strings once.
- In the worst case, we traverse both strings fully, so the time complexity is O(n + m), 
  where n is the length of `name` and m is the length of `typed`.

Space Complexity:
- The algorithm uses a constant amount of extra space (two pointers i and j).
- Therefore, the space complexity is O(1).
"""

# Topic: Two Pointers