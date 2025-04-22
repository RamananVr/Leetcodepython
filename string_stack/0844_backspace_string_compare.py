"""
LeetCode Question #844: Backspace String Compare

Problem Statement:
Given two strings `s` and `t`, return true if they are equal when both are typed into empty text editors. 
`#` means a backspace character.

Note that after backspacing an empty text, the text will continue to be empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:
- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#' characters.

Follow up:
Can you solve it in O(n) time and O(1) space?
"""

def backspaceCompare(s: str, t: str) -> bool:
    """
    Function to determine if two strings are equal after processing backspaces.
    """
    def process_string(string: str) -> str:
        stack = []
        for char in string:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
    return process_string(s) == process_string(t)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1, t1 = "ab#c", "ad#c"
    print(backspaceCompare(s1, t1))  # Output: True

    # Test Case 2
    s2, t2 = "ab##", "c#d#"
    print(backspaceCompare(s2, t2))  # Output: True

    # Test Case 3
    s3, t3 = "a#c", "b"
    print(backspaceCompare(s3, t3))  # Output: False

    # Test Case 4
    s4, t4 = "a##c", "#a#c"
    print(backspaceCompare(s4, t4))  # Output: True

    # Test Case 5
    s5, t5 = "a#b#c", "c"
    print(backspaceCompare(s5, t5))  # Output: True

"""
Time Complexity Analysis:
- The `process_string` function iterates through the input string once, performing O(1) operations for each character.
- Since we call `process_string` for both `s` and `t`, the overall time complexity is O(n + m), where n and m are the lengths of `s` and `t`.

Space Complexity Analysis:
- The `process_string` function uses a stack to store characters. In the worst case, the stack size is proportional to the length of the input string.
- Therefore, the space complexity is O(n + m), where n and m are the lengths of `s` and `t`.

Topic: String, Stack
"""