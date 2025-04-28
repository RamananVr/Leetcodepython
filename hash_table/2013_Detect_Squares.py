"""
LeetCode Problem #2013: Detect Squares

Problem Statement:
You are given a data structure that supports the following operations:
1. `add(point)`: Adds a new point with integer coordinates `point = [x, y]` to the data structure.
2. `count(point)`: Returns the number of squares that can be formed with `point = [x, y]` as one of the corners.

A square is valid if:
- The other three corners also exist in the data structure.
- The sides of the square are parallel to the x-axis and y-axis.

Implement the `DetectSquares` class:
- `DetectSquares()` Initializes the object.
- `add(point: List[int]) -> None` Adds a point to the data structure.
- `count(point: List[int]) -> int` Returns the number of squares with `point` as one of the corners.

Constraints:
- `point.length == 2`
- `0 <= point[0], point[1] <= 1000`
- At most 3000 calls in total will be made to `add` and `count`.

Example:
Input:
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output:
[null, null, null, null, 1, 0, null, 2]

Explanation:
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can form a square with corners (3, 10), (11, 10), (3, 2), (11, 2).
detectSquares.count([14, 8]); // return 0. No square can be formed.
detectSquares.add([11, 2]);
detectSquares.count([11, 10]); // return 2. You can form two squares with corners (3, 10), (11, 10), (3, 2), (11, 2) and (3, 10), (11, 10), (3, 2), (11, 2).
"""

from collections import defaultdict
from typing import List

class DetectSquares:
    def __init__(self):
        # Dictionary to store the count of points at each (x, y) coordinate
        self.point_count = defaultdict(int)
        # Dictionary to store all y-coordinates for each x-coordinate
        self.x_to_y = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.point_count[(x, y)] += 1
        self.x_to_y[x].add(y)

    def count(self, point: List[int]) -> int:
        x, y = point
        if x not in self.x_to_y:
            return 0

        total_squares = 0
        # Iterate through all y-coordinates for the given x-coordinate
        for other_y in self.x_to_y[x]:
            # Skip if the y-coordinate is the same as the current point
            if other_y == y:
                continue

            # Calculate the side length of the square
            side_length = abs(other_y - y)

            # Check for the other two corners of the square
            # (x + side_length, y) and (x + side_length, other_y)
            if (x + side_length, y) in self.point_count and (x + side_length, other_y) in self.point_count:
                total_squares += (
                    self.point_count[(x, y)] *
                    self.point_count[(x + side_length, y)] *
                    self.point_count[(x + side_length, other_y)]
                )

            # Check for the other two corners of the square
            # (x - side_length, y) and (x - side_length, other_y)
            if (x - side_length, y) in self.point_count and (x - side_length, other_y) in self.point_count:
                total_squares += (
                    self.point_count[(x, y)] *
                    self.point_count[(x - side_length, y)] *
                    self.point_count[(x - side_length, other_y)]
                )

        return total_squares


# Example Test Cases
if __name__ == "__main__":
    detectSquares = DetectSquares()
    detectSquares.add([3, 10])
    detectSquares.add([11, 2])
    detectSquares.add([3, 2])
    print(detectSquares.count([11, 10]))  # Output: 1
    print(detectSquares.count([14, 8]))  # Output: 0
    detectSquares.add([11, 2])
    print(detectSquares.count([11, 10]))  # Output: 2

"""
Time Complexity:
- `add`: O(1) - Adding a point involves updating two dictionaries, which is constant time.
- `count`: O(n) - For a given point, we iterate through all y-coordinates associated with its x-coordinate. In the worst case, there are n points added, so this operation is linear.

Space Complexity:
- O(n) - The space required to store the points and their counts in the dictionaries.

Topic: Hash Table
"""