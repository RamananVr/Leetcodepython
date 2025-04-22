"""
LeetCode Question #973: K Closest Points to Origin

Problem Statement:
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane 
and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance 
(i.e., √(x1 - x2)^2 + (y1 - y2)^2).

You may return the answer in any order. The answer is guaranteed to be unique 
(except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance of the point [1,3] from the origin is √10.
The distance of the point [-2,2] from the origin is √8.
Since √8 < √10, [-2,2] is closer to the origin.

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The distances are √18, √26, and √20 respectively.
The two closest points are [3,3] and [-2,4].

Constraints:
- 1 <= k <= points.length <= 10^4
- -10^4 < xi, yi < 10^4
"""

# Solution
from heapq import nsmallest

def kClosest(points, k):
    """
    Find the k closest points to the origin.

    :param points: List[List[int]] - List of points on the X-Y plane.
    :param k: int - Number of closest points to return.
    :return: List[List[int]] - k closest points to the origin.
    """
    # Use a heap to find the k smallest distances
    return nsmallest(k, points, key=lambda point: point[0]**2 + point[1]**2)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[1, 3], [-2, 2]]
    k1 = 1
    print(kClosest(points1, k1))  # Expected Output: [[-2, 2]]

    # Test Case 2
    points2 = [[3, 3], [5, -1], [-2, 4]]
    k2 = 2
    print(kClosest(points2, k2))  # Expected Output: [[3, 3], [-2, 4]]

    # Test Case 3
    points3 = [[1, 1], [2, 2], [3, 3]]
    k3 = 2
    print(kClosest(points3, k3))  # Expected Output: [[1, 1], [2, 2]]

    # Test Case 4
    points4 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    k4 = 3
    print(kClosest(points4, k4))  # Expected Output: [[0, 1], [1, 0], [0, -1]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the squared distance for each point takes O(1).
- Using `heapq.nsmallest` to find the k smallest distances takes O(n log k), 
  where n is the number of points and k is the number of closest points to return.
- Overall time complexity: O(n log k).

Space Complexity:
- The heap used by `heapq.nsmallest` requires O(k) space.
- Overall space complexity: O(k).
"""

# Topic: Arrays, Sorting, Heap