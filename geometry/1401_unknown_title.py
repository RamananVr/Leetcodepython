"""
LeetCode Problem #1401: Circle and Rectangle Overlapping

Problem Statement:
You are given a circle represented as (radius, x_center, y_center) and an axis-aligned rectangle represented as 
(x1, y1, x2, y2), where (x1, y1) is the bottom-left corner and (x2, y2) is the top-right corner of the rectangle.

Return True if the circle and rectangle are overlapped otherwise return False.

In other words, check if there is any point (x, y) such that it lies inside the circle and the rectangle simultaneously.

Constraints:
- 1 <= radius <= 2000
- -10^4 <= x_center, y_center <= 10^4
- -10^4 <= x1 < x2 <= 10^4
- -10^4 <= y1 < y2 <= 10^4
"""

def checkOverlap(radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    """
    Determines if a circle and rectangle overlap.

    Args:
    radius (int): Radius of the circle.
    x_center (int): X-coordinate of the circle's center.
    y_center (int): Y-coordinate of the circle's center.
    x1 (int): X-coordinate of the rectangle's bottom-left corner.
    y1 (int): Y-coordinate of the rectangle's bottom-left corner.
    x2 (int): X-coordinate of the rectangle's top-right corner.
    y2 (int): Y-coordinate of the rectangle's top-right corner.

    Returns:
    bool: True if the circle and rectangle overlap, False otherwise.
    """
    # Find the closest point on the rectangle to the circle's center
    closest_x = max(x1, min(x_center, x2))
    closest_y = max(y1, min(y_center, y2))
    
    # Calculate the distance from the circle's center to this closest point
    distance_squared = (closest_x - x_center) ** 2 + (closest_y - y_center) ** 2
    
    # Check if the distance is less than or equal to the circle's radius squared
    return distance_squared <= radius ** 2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Circle overlaps with the rectangle
    print(checkOverlap(1, 0, 0, -1, -1, 1, 1))  # Expected: True

    # Test Case 2: Circle is completely outside the rectangle
    print(checkOverlap(1, 2, 2, -1, -1, 1, 1))  # Expected: False

    # Test Case 3: Circle is completely inside the rectangle
    print(checkOverlap(1, 0, 0, -2, -2, 2, 2))  # Expected: True

    # Test Case 4: Circle just touches the rectangle
    print(checkOverlap(1, 1, 1, 0, 0, 2, 2))  # Expected: True

    # Test Case 5: Circle and rectangle are far apart
    print(checkOverlap(1, 10, 10, -1, -1, 1, 1))  # Expected: False

"""
Time Complexity Analysis:
- Finding the closest point on the rectangle involves constant time operations (max and min), so it is O(1).
- Calculating the squared distance and comparing it to the radius squared is also O(1).
- Overall, the time complexity is O(1).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space for variables, so the space complexity is O(1).

Topic: Geometry
"""