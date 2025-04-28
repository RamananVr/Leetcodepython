"""
LeetCode Problem #469: Convex Polygon

Problem Statement:
You are given an array of points in the 2D plane `points` where `points[i] = [xi, yi]`. 
A polygon is convex if it has no points that are "turned inward." More formally, every 
internal angle of the polygon must be strictly less than 180 degrees.

Return `True` if the given polygon is convex. Otherwise, return `False`.

The given polygon is represented as a list of points in counter-clockwise order. 
Each point in the polygon is represented as a list of two integers.

Constraints:
- 3 <= points.length <= 10^4
- points[i].length == 2
- -10^4 <= xi, yi <= 10^4
- All the points are unique.
- The given points form a simple polygon (no self-intersecting edges).

Example:
Input: points = [[0,0],[0,1],[1,1],[1,0]]
Output: true

Input: points = [[0,0],[0,10],[10,10],[10,0],[5,5]]
Output: false
"""

def isConvex(points):
    """
    Determines if a given polygon is convex.

    :param points: List[List[int]] - List of points representing the polygon in counter-clockwise order.
    :return: bool - True if the polygon is convex, False otherwise.
    """
    def cross_product(p1, p2, p3):
        """
        Computes the cross product of vectors (p2 - p1) and (p3 - p2).
        """
        x1, y1 = p2[0] - p1[0], p2[1] - p1[1]
        x2, y2 = p3[0] - p2[0], p3[1] - p2[1]
        return x1 * y2 - x2 * y1

    n = len(points)
    prev_sign = 0

    for i in range(n):
        p1, p2, p3 = points[i], points[(i + 1) % n], points[(i + 2) % n]
        cross = cross_product(p1, p2, p3)

        if cross != 0:
            curr_sign = 1 if cross > 0 else -1
            if prev_sign != 0 and curr_sign != prev_sign:
                return False
            prev_sign = curr_sign

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple square (convex)
    points1 = [[0, 0], [0, 1], [1, 1], [1, 0]]
    print(isConvex(points1))  # Output: True

    # Test Case 2: Self-intersecting polygon (not convex)
    points2 = [[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]]
    print(isConvex(points2))  # Output: False

    # Test Case 3: Triangle (convex)
    points3 = [[0, 0], [1, 1], [2, 0]]
    print(isConvex(points3))  # Output: True

    # Test Case 4: Concave polygon
    points4 = [[0, 0], [4, 0], [4, 4], [2, 2], [0, 4]]
    print(isConvex(points4))  # Output: False

    # Test Case 5: Large convex polygon
    points5 = [[0, 0], [0, 5], [5, 5], [5, 0]]
    print(isConvex(points5))  # Output: True

"""
Time Complexity:
- The algorithm iterates through all the points in the polygon once, performing constant-time operations for each triplet of points.
- Let `n` be the number of points in the polygon. The time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables and computations.
- The space complexity is O(1).

Topic: Geometry
"""