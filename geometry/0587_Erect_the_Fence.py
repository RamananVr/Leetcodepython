"""
LeetCode Problem #587: Erect the Fence

Problem Statement:
You are given an array `trees` where `trees[i] = [xi, yi]` represents the location of a tree in the 2D space. 
You have to fence the entire forest using the minimum length of rope as it is expensive. The fence must be a 
convex polygon. You need to output the coordinates of trees that are exactly located on the fence's perimeter.

Input: An array of points `trees` where each point is represented as [xi, yi].
Output: A list of points that are on the convex hull in counter-clockwise order.

Notes:
- The convex hull is the smallest convex polygon that can enclose all the given points.
- If there are multiple valid outputs, return any of them.
- The input points are all unique.

Constraints:
- 1 <= trees.length <= 3000
- trees[i].length == 2
- 0 <= xi, yi <= 100
- All the given points are unique.
"""

from typing import List

def outerTrees(trees: List[List[int]]) -> List[List[int]]:
    def cross(o, a, b):
        """Calculate the cross product of vectors OA and OB."""
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Sort the points lexicographically (by x, then by y)
    trees.sort()

    # Build the lower hull
    lower = []
    for point in trees:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) < 0:
            lower.pop()
        lower.append(point)

    # Build the upper hull
    upper = []
    for point in reversed(trees):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) < 0:
            upper.pop()
        upper.append(point)

    # Remove the last point of each half because it's repeated at the beginning of the other half
    return list(set(lower[:-1] + upper[:-1]))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    print(outerTrees(trees))  # Expected output: [[1,1],[2,0],[4,2],[3,3],[2,4]]

    # Test Case 2
    trees = [[1,2],[2,2],[4,2]]
    print(outerTrees(trees))  # Expected output: [[1,2],[2,2],[4,2]]

    # Test Case 3
    trees = [[0,0],[4,2],[1,1],[3,3],[5,5],[6,0]]
    print(outerTrees(trees))  # Expected output: [[0,0],[6,0],[5,5],[3,3],[1,1]]

"""
Time Complexity:
- Sorting the points takes O(n log n), where n is the number of points.
- Constructing the convex hull (both lower and upper parts) takes O(n) because each point is added and removed at most once.
- Overall time complexity: O(n log n).

Space Complexity:
- The space complexity is O(n) for storing the lower and upper hulls.

Topic: Geometry
"""