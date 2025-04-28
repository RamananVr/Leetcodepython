"""
LeetCode Problem #1620: Coordinate With Maximum Network Quality

Problem Statement:
You are given an array of network towers `towers`, where `towers[i] = [xi, yi, qi]` denotes the location `(xi, yi)` and quality factor `qi` of the ith tower. All coordinates are integral coordinates on the X-Y plane, and the distance between two coordinates is the Euclidean distance.

You are also given an integer `radius`, where a tower is only reachable if the distance is less than or equal to `radius`. If the ith tower is reachable, the signal quality of the tower is calculated as:
    floor(qi / (1 + d))
where `d` is the distance between the tower and the point.

The network quality at a coordinate `(x, y)` is the sum of the signal qualities from all reachable towers.

Return the integral coordinate `(x, y)` where the network quality is maximum. If there are multiple coordinates with the same network quality, return the lexicographically smallest coordinate.

Constraints:
- `1 <= towers.length <= 50`
- `1 <= xi, yi, qi <= 50`
- `1 <= radius <= 50`

"""

# Solution
from math import sqrt, floor

def bestCoordinate(towers, radius):
    def signal_quality(x, y):
        """Calculate the total network quality at coordinate (x, y)."""
        total_quality = 0
        for tx, ty, q in towers:
            distance = sqrt((tx - x) ** 2 + (ty - y) ** 2)
            if distance <= radius:
                total_quality += floor(q / (1 + distance))
        return total_quality

    # Determine the bounds for the search space
    max_x = max(tower[0] for tower in towers)
    max_y = max(tower[1] for tower in towers)

    best_quality = 0
    best_coordinate = (0, 0)

    # Iterate over all possible integral coordinates within the bounds
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            quality = signal_quality(x, y)
            if quality > best_quality or (quality == best_quality and (x, y) < best_coordinate):
                best_quality = quality
                best_coordinate = (x, y)

    return best_coordinate

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    towers1 = [[1, 2, 5], [2, 1, 7], [3, 1, 9]]
    radius1 = 2
    print(bestCoordinate(towers1, radius1))  # Expected Output: (2, 1)

    # Test Case 2
    towers2 = [[23, 11, 21]]
    radius2 = 9
    print(bestCoordinate(towers2, radius2))  # Expected Output: (23, 11)

    # Test Case 3
    towers3 = [[1, 2, 13], [2, 1, 7], [0, 1, 9]]
    radius3 = 2
    print(bestCoordinate(towers3, radius3))  # Expected Output: (1, 2)

    # Test Case 4
    towers4 = [[0, 0, 1], [2, 2, 1], [3, 3, 1]]
    radius4 = 1
    print(bestCoordinate(towers4, radius4))  # Expected Output: (0, 0)

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates over all possible integral coordinates within the bounds defined by the maximum x and y values of the towers.
- For each coordinate, it calculates the signal quality by iterating over all towers.
- Let `n` be the number of towers and `m` be the maximum value of x or y in the towers.
- The time complexity is O(m^2 * n), where m^2 is the number of coordinates to check and n is the number of towers.

Space Complexity:
- The space complexity is O(1) since we are only using a few variables to store intermediate results.

Overall: Time Complexity = O(m^2 * n), Space Complexity = O(1)
"""

# Topic: Geometry, Brute Force