"""
LeetCode Problem #2249: Count Lattice Points Inside a Circle

Problem Statement:
You are given an array `circles` where `circles[i] = [xi, yi, ri]` represents a circle centered at `(xi, yi)` with a radius of `ri`.
A lattice point is a point with integer coordinates.

Return the number of lattice points that are present inside at least one circle.

Notes:
- A point `(x, y)` is considered to be inside a circle with center `(xi, yi)` and radius `ri` if `(x - xi)^2 + (y - yi)^2 <= ri^2`.
- The circles may overlap.

Constraints:
- `1 <= circles.length <= 200`
- `circles[i].length == 3`
- `1 <= xi, yi <= 100`
- `1 <= ri <= 100`
"""

# Solution
def countLatticePoints(circles):
    """
    Counts the number of lattice points inside at least one circle.

    :param circles: List[List[int]] - List of circles where each circle is represented as [xi, yi, ri].
    :return: int - Number of lattice points inside at least one circle.
    """
    points = set()  # To store unique lattice points

    for x, y, r in circles:
        for i in range(x - r, x + r + 1):  # Iterate over x-coordinates in the bounding box
            for j in range(y - r, y + r + 1):  # Iterate over y-coordinates in the bounding box
                if (i - x) ** 2 + (j - y) ** 2 <= r ** 2:  # Check if the point is inside the circle
                    points.add((i, j))  # Add the point to the set

    return len(points)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    circles = [[2, 2, 1]]
    print(countLatticePoints(circles))  # Expected Output: 5

    # Test Case 2
    circles = [[2, 2, 2], [3, 4, 1]]
    print(countLatticePoints(circles))  # Expected Output: 16

    # Test Case 3
    circles = [[1, 1, 1], [4, 4, 1], [6, 6, 2]]
    print(countLatticePoints(circles))  # Expected Output: 29

    # Test Case 4
    circles = [[10, 10, 5]]
    print(countLatticePoints(circles))  # Expected Output: 81

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each circle, we iterate over a bounding box of size proportional to the square of the radius (r^2).
- In the worst case, we have 200 circles, each with a maximum radius of 100.
- The bounding box for a circle with radius 100 is 201 x 201 = 40401 points.
- Thus, the worst-case time complexity is O(n * r^2), where n is the number of circles and r is the maximum radius.

Space Complexity:
- We use a set to store unique lattice points. In the worst case, the number of unique points is proportional to the total area covered by the circles.
- The space complexity is O(k), where k is the number of unique lattice points.

Overall:
- Time Complexity: O(n * r^2)
- Space Complexity: O(k)
"""

# Topic: Geometry, Hashing, Simulation