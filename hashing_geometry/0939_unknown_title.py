"""
LeetCode Problem #939: Minimum Area Rectangle

Problem Statement:
You are given an array of points in the X-Y plane `points` where `points[i] = [xi, yi]`.
Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. 
If there is no such rectangle, return 0.

Example 1:
Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:
Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

Constraints:
- 1 <= points.length <= 500
- 0 <= xi, yi <= 4 * 10^4
- All the given points are unique.
"""

def minAreaRect(points):
    """
    Finds the minimum area of a rectangle formed by points with sides parallel to the X and Y axes.

    :param points: List[List[int]] - List of points in the X-Y plane
    :return: int - Minimum area of the rectangle, or 0 if no rectangle can be formed
    """
    # Convert points to a set for O(1) lookups
    point_set = set(map(tuple, points))
    min_area = float('inf')

    # Iterate through all pairs of points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]

            # Check if the points form a diagonal of a rectangle
            if x1 != x2 and y1 != y2:
                # Check if the other two corners of the rectangle exist
                if (x1, y2) in point_set and (x2, y1) in point_set:
                    # Calculate the area of the rectangle
                    area = abs(x2 - x1) * abs(y2 - y1)
                    min_area = min(min_area, area)

    # If no rectangle was found, return 0
    return 0 if min_area == float('inf') else min_area

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
    print(minAreaRect(points1))  # Output: 4

    # Test Case 2
    points2 = [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
    print(minAreaRect(points2))  # Output: 2

    # Test Case 3
    points3 = [[1, 1], [2, 2], [3, 3]]
    print(minAreaRect(points3))  # Output: 0 (No rectangle can be formed)

    # Test Case 4
    points4 = [[1, 1], [1, 2], [2, 1], [2, 2]]
    print(minAreaRect(points4))  # Output: 1

"""
Time Complexity:
- The outer loop iterates through all pairs of points, so the time complexity is O(n^2), where n is the number of points.
- Checking if the other two corners exist in the set is O(1) for each pair.
- Overall time complexity: O(n^2).

Space Complexity:
- The space complexity is O(n) due to the set used to store the points.

Topic: Hashing, Geometry
"""