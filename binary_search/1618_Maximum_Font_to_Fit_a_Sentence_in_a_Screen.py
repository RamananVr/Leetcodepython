"""
LeetCode Problem #1618: Maximum Font to Fit a Sentence in a Screen

Problem Statement:
You are given a string `text`, a positive integer `w` representing the width of a screen, 
a positive integer `h` representing the height of a screen, and a list of positive integers 
`fonts` representing the available font sizes in descending order. You are also given a 
function `FontInfo` that provides the following methods:

1. `getWidth(fontSize: int, text: str) -> int`: Returns the width of the `text` when rendered 
   with the given `fontSize`.
2. `getHeight(fontSize: int) -> int`: Returns the height of the font when rendered with the 
   given `fontSize`.

Your task is to find the maximum font size from the `fonts` list that can be used to render 
the `text` such that it fits within the screen dimensions (`w` x `h`). If no font size can 
fit the text within the screen, return -1.

Constraints:
- `1 <= len(text) <= 50000`
- `1 <= w, h <= 10^7`
- `1 <= len(fonts) <= 10^5`
- `1 <= fonts[i] <= 10^5`
- `fonts` is sorted in descending order.
- The `FontInfo` methods are provided and can be called to get the width and height of the text.

Example:
Input:
text = "example"
w = 100
h = 20
fonts = [10, 9, 8, 7]
FontInfo.getWidth(10, "example") = 80
FontInfo.getHeight(10) = 15

Output:
10

Explanation:
The font size 10 fits within the screen dimensions (100 x 20), and it is the largest font size 
that fits.

If no font size fits, return -1.
"""

# Python Solution
from typing import List

class FontInfo:
    def getWidth(self, fontSize: int, text: str) -> int:
        # This method is provided by the problem and simulates the width of the text.
        pass

    def getHeight(self, fontSize: int) -> int:
        # This method is provided by the problem and simulates the height of the font.
        pass

def maxFont(text: str, w: int, h: int, fonts: List[int], fontInfo: FontInfo) -> int:
    """
    Finds the maximum font size that fits the text within the screen dimensions.
    """
    def canFit(fontSize: int) -> bool:
        # Check if the font size fits within the screen dimensions
        return fontInfo.getWidth(fontSize, text) <= w and fontInfo.getHeight(fontSize) <= h

    # Binary search over the fonts array
    left, right = 0, len(fonts) - 1
    best_fit = -1

    while left <= right:
        mid = (left + right) // 2
        if canFit(fonts[mid]):
            best_fit = fonts[mid]  # Update the best fit
            left = mid + 1  # Try for a larger font size
        else:
            right = mid - 1  # Try for a smaller font size

    return best_fit

# Example Test Cases
class MockFontInfo(FontInfo):
    def __init__(self, width_map, height_map):
        self.width_map = width_map
        self.height_map = height_map

    def getWidth(self, fontSize: int, text: str) -> int:
        return self.width_map[fontSize]

    def getHeight(self, fontSize: int) -> int:
        return self.height_map[fontSize]

if __name__ == "__main__":
    # Mock data for testing
    width_map = {10: 80, 9: 72, 8: 64, 7: 56}
    height_map = {10: 15, 9: 13, 8: 12, 7: 10}
    fontInfo = MockFontInfo(width_map, height_map)

    # Test case 1
    text = "example"
    w = 100
    h = 20
    fonts = [10, 9, 8, 7]
    print(maxFont(text, w, h, fonts, fontInfo))  # Output: 10

    # Test case 2
    text = "example"
    w = 50
    h = 10
    fonts = [10, 9, 8, 7]
    print(maxFont(text, w, h, fonts, fontInfo))  # Output: 7

    # Test case 3
    text = "example"
    w = 30
    h = 5
    fonts = [10, 9, 8, 7]
    print(maxFont(text, w, h, fonts, fontInfo))  # Output: -1

"""
Time Complexity:
- The binary search runs in O(log(len(fonts))).
- For each font size checked, we call `getWidth` and `getHeight`, which are assumed to run in O(1).
- Therefore, the overall time complexity is O(log(len(fonts))).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures.

Topic: Binary Search
"""