"""
LeetCode Problem #447: Number of Boomerangs

Problem Statement:
You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. 
A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals 
the distance between i and k (the order of the tuple matters).

Return the number of boomerangs.

Example:
Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[0,0],[1,0],[2,0]] and [[2,0],[1,0],[0,0]].

Constraints:
- n == points.length
- 1 <= n <= 500
- points[i].length == 2
- -10^4 <= xi, yi <= 10^4
- All the points are unique.
"""

from collections import defaultdict
from typing import List

def numberOfBoomerangs(points: List[List[int]]) -> int:
    def squared_distance(p1, p2):
        """Helper function to calculate squared distance between two points."""
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    count = 0
    for i in points:
        distance_map = defaultdict(int)
        for j in points:
            if i != j:
                dist = squared_distance(i, j)
                distance_map[dist] += 1
        for freq in distance_map.values():
            if freq > 1:
                count += freq * (freq - 1)  # Permutations: P(freq, 2) = freq * (freq - 1)
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[0, 0], [1, 0], [2, 0]]
    print(numberOfBoomerangs(points1))  # Output: 2

    # Test Case 2
    points2 = [[1, 1], [2, 2], [3, 3]]
    print(numberOfBoomerangs(points2))  # Output: 2

    # Test Case 3
    points3 = [[1, 1]]
    print(numberOfBoomerangs(points3))  # Output: 0

    # Test Case 4
    points4 = [[0, 0], [1, 0], [2, 0], [3, 0]]
    print(numberOfBoomerangs(points4))  # Output: 8

"""
Time Complexity:
- The outer loop iterates over each point, so O(n).
- The inner loop iterates over all points to calculate distances, so O(n).
- Calculating the squared distance is O(1).
- Thus, the overall time complexity is O(n^2).

Space Complexity:
- We use a defaultdict to store distances for each point, which can have at most O(n) entries.
- Therefore, the space complexity is O(n).

Topic: Hash Table
"""