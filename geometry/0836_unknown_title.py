"""
LeetCode Problem #836: Rectangle Overlap

Problem Statement:
An axis-aligned rectangle is represented as a list `[x1, y1, x2, y2]`, where `(x1, y1)` is the coordinate of its bottom-left corner, and `(x2, y2)` is the coordinate of its top-right corner. 
Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles `rec1` and `rec2`, return `True` if they overlap, otherwise return `False`.

Constraints:
- `rec1.length == 4`
- `rec2.length == 4`
- `-10^9 <= rec1[i], rec2[i] <= 10^9`
- `rec1` and `rec2` represent a valid rectangle with a non-zero area.

Example:
Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: True

Input: rec1 = [0,0,1,1], rec2 = [1,1,2,2]
Output: False
"""

def isRectangleOverlap(rec1, rec2):
    """
    Determines if two rectangles overlap.

    :param rec1: List[int] - Coordinates of the first rectangle [x1, y1, x2, y2]
    :param rec2: List[int] - Coordinates of the second rectangle [x1, y1, x2, y2]
    :return: bool - True if the rectangles overlap, False otherwise
    """
    # Check if one rectangle is completely to the left, right, above, or below the other
    return not (
        rec1[2] <= rec2[0] or  # rec1 is to the left of rec2
        rec1[0] >= rec2[2] or  # rec1 is to the right of rec2
        rec1[3] <= rec2[1] or  # rec1 is below rec2
        rec1[1] >= rec2[3]     # rec1 is above rec2
    )

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Overlapping rectangles
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    print(isRectangleOverlap(rec1, rec2))  # Expected: True

    # Test Case 2: Touching rectangles (no overlap)
    rec1 = [0, 0, 1, 1]
    rec2 = [1, 1, 2, 2]
    print(isRectangleOverlap(rec1, rec2))  # Expected: False

    # Test Case 3: Completely separate rectangles
    rec1 = [0, 0, 1, 1]
    rec2 = [2, 2, 3, 3]
    print(isRectangleOverlap(rec1, rec2))  # Expected: False

    # Test Case 4: One rectangle inside another
    rec1 = [0, 0, 4, 4]
    rec2 = [1, 1, 2, 2]
    print(isRectangleOverlap(rec1, rec2))  # Expected: True

    # Test Case 5: Overlapping on one edge
    rec1 = [0, 0, 2, 2]
    rec2 = [1, -1, 3, 1]
    print(isRectangleOverlap(rec1, rec2))  # Expected: True

"""
Time Complexity Analysis:
- The solution performs a constant number of comparisons and logical operations.
- Time Complexity: O(1)

Space Complexity Analysis:
- The solution uses a constant amount of space.
- Space Complexity: O(1)

Topic: Geometry
"""