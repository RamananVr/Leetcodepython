"""
LeetCode Question #2650: Design a Text Editor

Problem Statement:
You are tasked with designing a simple text editor that supports the following operations:
1. Insert a character at the current cursor position.
2. Delete the character at the current cursor position.
3. Move the cursor left or right.
4. Retrieve the current state of the text.

Implement a class `TextEditor` with the following methods:
- `__init__()`: Initializes the text editor.
- `insert(char: str) -> None`: Inserts the character `char` at the current cursor position.
- `delete() -> None`: Deletes the character at the current cursor position if there is one.
- `moveCursorLeft() -> None`: Moves the cursor one position to the left if possible.
- `moveCursorRight() -> None`: Moves the cursor one position to the right if possible.
- `getText() -> str`: Returns the current state of the text.

Constraints:
- The text editor should handle up to 10^5 operations efficiently.
- The cursor position is always valid.
"""

# Python Solution
class TextEditor:
    def __init__(self):
        self.left_stack = []  # Characters to the left of the cursor
        self.right_stack = []  # Characters to the right of the cursor

    def insert(self, char: str) -> None:
        self.left_stack.append(char)

    def delete(self) -> None:
        if self.left_stack:
            self.left_stack.pop()

    def moveCursorLeft(self) -> None:
        if self.left_stack:
            self.right_stack.append(self.left_stack.pop())

    def moveCursorRight(self) -> None:
        if self.right_stack:
            self.left_stack.append(self.right_stack.pop())

    def getText(self) -> str:
        return ''.join(self.left_stack) + ''.join(reversed(self.right_stack))


# Example Test Cases
if __name__ == "__main__":
    editor = TextEditor()

    # Test Case 1: Basic insert and getText
    editor.insert('a')
    editor.insert('b')
    editor.insert('c')
    print(editor.getText())  # Output: "abc"

    # Test Case 2: Move cursor left and insert
    editor.moveCursorLeft()
    editor.insert('x')
    print(editor.getText())  # Output: "abxc"

    # Test Case 3: Delete and move cursor right
    editor.delete()
    editor.moveCursorRight()
    print(editor.getText())  # Output: "abc"

    # Test Case 4: Move cursor left multiple times
    editor.moveCursorLeft()
    editor.moveCursorLeft()
    editor.insert('y')
    print(editor.getText())  # Output: "aybc"

    # Test Case 5: Edge case - delete at the beginning
    editor.moveCursorLeft()
    editor.moveCursorLeft()
    editor.delete()
    print(editor.getText())  # Output: "ybc"


"""
Time and Space Complexity Analysis:

1. `insert(char)`:
   - Time Complexity: O(1) (appending to a stack is constant time).
   - Space Complexity: O(1) (no additional space used).

2. `delete()`:
   - Time Complexity: O(1) (popping from a stack is constant time).
   - Space Complexity: O(1) (no additional space used).

3. `moveCursorLeft()` and `moveCursorRight()`:
   - Time Complexity: O(1) (moving elements between stacks is constant time).
   - Space Complexity: O(1) (no additional space used).

4. `getText()`:
   - Time Complexity: O(n), where n is the total number of characters in the text (concatenating stacks requires iterating through all elements).
   - Space Complexity: O(n) (temporary space used for concatenation).

Overall:
- Time Complexity per operation: O(1) for all operations except `getText()`, which is O(n).
- Space Complexity: O(n), where n is the total number of characters in the text.

Topic: Data Structures (Stacks)
"""