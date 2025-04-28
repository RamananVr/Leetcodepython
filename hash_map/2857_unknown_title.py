"""
LeetCode Problem #2857: Count Pairs of Points With Distance k

Problem Statement:
You are given an array `points` where `points[i] = [xi, yi]` represents a point in a 2D plane. 
You are also given an integer `k`. A pair of points `(i, j)` is considered valid if:
    - i < j
    - The Manhattan distance between the points is equal to `k`.

The Manhattan distance between two points `(xi, yi)` and `(xj, yj)` is defined as:
    |xi - xj| + |yi - yj|

Return the number of valid pairs of points.

Constraints:
    - 1 <= points.length <= 10^4
    - points[i].length == 2
    - 0 <= xi, yi <= 10^4
    - 1 <= k <= 10^4
"""

# Solution
from collections import defaultdict

def countPairs(points, k):
    """
    Counts the number of valid pairs of points with Manhattan distance k.

    :param points: List[List[int]] - List of points in the 2D plane.
    :param k: int - Target Manhattan distance.
    :return: int - Number of valid pairs.
    """
    count = 0
    freq = defaultdict(int)

    for x, y in points:
        # Check all possible points that could form a Manhattan distance of k
        candidates = [
            (x + k, y), (x - k, y),  # Horizontal shifts
            (x, y + k), (x, y - k)   # Vertical shifts
        ]
        
        # Count pairs with previously seen points
        for cx, cy in candidates:
            count += freq[(cx, cy)]
        
        # Add current point to the frequency map
        freq[(x, y)] += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points = [[1, 2], [3, 2], [2, 3], [4, 3]]
    k = 2
    print(countPairs(points, k))  # Expected Output: 2

    # Test Case 2
    points = [[0, 0], [0, 2], [2, 0], [2, 2]]
    k = 2
    print(countPairs(points, k))  # Expected Output: 4

    # Test Case 3
    points = [[1, 1], [2, 2], [3, 3]]
    k = 1
    print(countPairs(points, k))  # Expected Output: 2

    # Test Case 4
    points = [[0, 0], [1, 1], [2, 2], [3, 3]]
    k = 3
    print(countPairs(points, k))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
    - For each point in the `points` array, we generate 4 candidate points and check their frequency in the map.
    - This results in O(n) operations, where n is the number of points.
    - Thus, the overall time complexity is O(n).

Space Complexity:
    - We use a dictionary to store the frequency of points. In the worst case, the dictionary could store all n points.
    - Thus, the space complexity is O(n).

Topic: Hash Map
"""