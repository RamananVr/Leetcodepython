"""
LeetCode Problem #478: Generate Random Point in a Circle

Problem Statement:
You are given the radius `radius` and the coordinates of the center `x_center`, `y_center` of a circle. 
Implement the `Solution` class:

- `Solution(double radius, double x_center, double y_center)` Initializes the object with the radius of the circle `radius` and the coordinates of the center `(x_center, y_center)`.
- `randPoint()` Returns a random point inside the circle. A point on the circumference of the circle is considered to be in the circle. The answer is returned as an array `[x, y]`.

Any point inside the circle must be uniformly distributed.

Constraints:
- `0 < radius <= 10^8`
- `-10^7 <= x_center, y_center <= 10^7`
- At most `3 * 10^4` calls will be made to `randPoint`.

"""

import random
import math

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        """
        Initializes the circle with the given radius and center coordinates.
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> list[float]:
        """
        Generates a random point inside the circle.
        """
        while True:
            # Generate random x and y offsets in the range [-radius, radius]
            x_offset = random.uniform(-self.radius, self.radius)
            y_offset = random.uniform(-self.radius, self.radius)
            
            # Check if the point lies within the circle
            if x_offset**2 + y_offset**2 <= self.radius**2:
                # Translate the point to the circle's center
                return [self.x_center + x_offset, self.y_center + y_offset]

# Example Test Cases
if __name__ == "__main__":
    # Initialize the circle with radius 1 and center (0, 0)
    solution = Solution(1.0, 0.0, 0.0)
    
    # Generate 5 random points inside the circle
    for _ in range(5):
        print(solution.randPoint())

"""
Time Complexity Analysis:
- The `randPoint` method generates random x and y offsets and checks if the point lies within the circle.
  The probability of a random point being inside the circle is proportional to the area of the circle 
  divided by the area of the bounding square (πr² / (2r)² = π/4 ≈ 0.785). On average, the loop will run 
  approximately 1 / 0.785 ≈ 1.27 times per call. Thus, the expected time complexity is O(1).

Space Complexity Analysis:
- The space complexity is O(1) since no additional data structures are used.

Topic: Randomization
"""