"""
LeetCode Problem #2296: Design a Text Editor

Problem Statement:
Design a text editor with a cursor that can do the following:
1. Add text to where the cursor is.
2. Delete text from where the cursor is (backspace).
3. Move the cursor either left or right.

Implement the `TextEditor` class:
- `TextEditor()`: Initializes the object with an empty text string.
- `void addText(string text)`: Appends `text` to where the cursor is. The cursor moves to the end of the added text.
- `int deleteText(int k)`: Deletes `k` characters to the left of the cursor. Returns the number of characters actually deleted.
- `string cursorLeft(int k)`: Moves the cursor `k` positions to the left. Returns the last 10 characters to the left of the cursor, or fewer if there are less than 10 characters.
- `string cursorRight(int k)`: Moves the cursor `k` positions to the right. Returns the last 10 characters to the left of the cursor, or fewer if there are less than 10 characters.

Constraints:
- `1 <= text.length, k <= 40`
- The sum of calls to all methods will not exceed `2 * 10^4`.

"""

class TextEditor:
    def __init__(self):
        # Use two stacks to manage text on the left and right of the cursor
        self.left = []  # Characters to the left of the cursor
        self.right = []  # Characters to the right of the cursor

    def addText(self, text: str) -> None:
        # Add text to the left of the cursor
        for char in text:
            self.left.append(char)

    def deleteText(self, k: int) -> int:
        # Delete up to k characters from the left of the cursor
        count = 0
        while self.left and count < k:
            self.left.pop()
            count += 1
        return count

    def cursorLeft(self, k: int) -> str:
        # Move the cursor k positions to the left
        for _ in range(min(k, len(self.left))):
            self.right.append(self.left.pop())
        # Return the last 10 characters to the left of the cursor
        return ''.join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        # Move the cursor k positions to the right
        for _ in range(min(k, len(self.right))):
            self.left.append(self.right.pop())
        # Return the last 10 characters to the left of the cursor
        return ''.join(self.left[-10:])


# Example Test Cases
if __name__ == "__main__":
    editor = TextEditor()
    
    # Test Case 1: Add text and move cursor
    editor.addText("leetcode")
    assert editor.cursorLeft(4) == "leet"  # Move cursor left by 4, last 10 chars: "leet"
    assert editor.cursorRight(2) == "leetc"  # Move cursor right by 2, last 10 chars: "leetc"
    
    # Test Case 2: Delete text
    assert editor.deleteText(4) == 4  # Delete 4 characters, returns 4
    assert editor.cursorLeft(2) == ""  # Move cursor left by 2, no characters left
    
    # Test Case 3: Add more text and move cursor
    editor.addText("practice")
    assert editor.cursorRight(3) == "pra"  # Move cursor right by 3, last 10 chars: "pra"
    assert editor.cursorLeft(8) == ""  # Move cursor left by 8, no characters left
    assert editor.cursorRight(10) == "practice"  # Move cursor right by 10, last 10 chars: "practice"

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. `addText(text)`:
   - Time Complexity: O(n), where n is the length of the text being added.
   - Space Complexity: O(n), as the text is stored in the `left` stack.

2. `deleteText(k)`:
   - Time Complexity: O(k), where k is the number of characters to delete.
   - Space Complexity: O(1), as we are only modifying the `left` stack.

3. `cursorLeft(k)`:
   - Time Complexity: O(k), where k is the number of positions to move the cursor.
   - Space Complexity: O(1), as we are transferring characters between stacks.

4. `cursorRight(k)`:
   - Time Complexity: O(k), where k is the number of positions to move the cursor.
   - Space Complexity: O(1), as we are transferring characters between stacks.

Overall:
- Time Complexity: O(n) per operation in the worst case.
- Space Complexity: O(n), where n is the total number of characters in the editor.

Topic: Stack
"""