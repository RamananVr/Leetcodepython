"""
LeetCode Question #391: Perfect Rectangle

Problem Statement:
Given an array `rectangles` where `rectangles[i] = [x1, y1, x2, y2]` represents the bottom-left corner 
(x1, y1) and the top-right corner (x2, y2) of a rectangle, return `true` if all the rectangles together 
form an exact cover of a rectangular region.

A rectangle can be represented as a set of four points: bottom-left, bottom-right, top-left, and top-right. 
The rectangles must form a perfect cover, meaning:
1. The union of all rectangles should form a single large rectangle.
2. There should be no overlaps or gaps between the rectangles.

Constraints:
- 1 <= rectangles.length <= 2 * 10^4
- rectangles[i].length == 4
- -10^5 <= x1, y1, x2, y2 <= 10^5
- x1 < x2 and y1 < y2
"""

def isRectangleCover(rectangles):
    """
    Determines if the given rectangles form a perfect rectangle.

    :param rectangles: List[List[int]] - List of rectangles represented as [x1, y1, x2, y2]
    :return: bool - True if the rectangles form a perfect rectangle, False otherwise
    """
    from collections import defaultdict

    # To track the corners and their counts
    corner_count = defaultdict(int)
    area = 0

    # Define a helper function to add corners
    def add_corner(corner):
        corner_count[corner] += 1

    # Iterate through all rectangles
    for x1, y1, x2, y2 in rectangles:
        # Calculate the area of the current rectangle
        area += (x2 - x1) * (y2 - y1)

        # Add the four corners of the rectangle
        add_corner((x1, y1))  # Bottom-left
        add_corner((x1, y2))  # Top-left
        add_corner((x2, y1))  # Bottom-right
        add_corner((x2, y2))  # Top-right

    # Find the bounding rectangle
    x1_min = min(rect[0] for rect in rectangles)
    y1_min = min(rect[1] for rect in rectangles)
    x2_max = max(rect[2] for rect in rectangles)
    y2_max = max(rect[3] for rect in rectangles)

    # Calculate the area of the bounding rectangle
    bounding_area = (x2_max - x1_min) * (y2_max - y1_min)

    # Check if the total area matches the bounding rectangle's area
    if area != bounding_area:
        return False

    # Check the corner counts
    # The four corners of the bounding rectangle should appear exactly once
    bounding_corners = {(x1_min, y1_min), (x1_min, y2_max), (x2_max, y1_min), (x2_max, y2_max)}
    for corner in bounding_corners:
        if corner_count[corner] != 1:
            return False
        del corner_count[corner]

    # All other corners should appear an even number of times
    for count in corner_count.values():
        if count % 2 != 0:
            return False

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Perfect rectangle
    rectangles1 = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
    print(isRectangleCover(rectangles1))  # Output: True

    # Test Case 2: Overlapping rectangles
    rectangles2 = [[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]
    print(isRectangleCover(rectangles2))  # Output: False

    # Test Case 3: Gaps between rectangles
    rectangles3 = [[1, 1, 2, 2], [2, 1, 3, 2], [1, 2, 2, 3], [2, 2, 3, 3], [4, 4, 5, 5]]
    print(isRectangleCover(rectangles3))  # Output: False

    # Test Case 4: Single rectangle
    rectangles4 = [[0, 0, 4, 4]]
    print(isRectangleCover(rectangles4))  # Output: True

# Time Complexity Analysis:
# - Calculating the bounding rectangle: O(n), where n is the number of rectangles.
# - Iterating through all rectangles to calculate the area and update corner counts: O(n).
# - Checking the corner counts: O(n).
# Overall: O(n).

# Space Complexity Analysis:
# - Space used by the `corner_count` dictionary: O(k), where k is the number of unique corners.
# In the worst case, k = 4n (each rectangle contributes 4 unique corners).
# Overall: O(k).

# Topic: Geometry, Hash Table