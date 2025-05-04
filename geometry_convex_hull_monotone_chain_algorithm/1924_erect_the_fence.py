"""
LeetCode Question #1924: Erect the Fence

Problem Statement:
You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden. 
You are asked to enclose all the trees with a fence. The fence should be a convex polygon. 
The convex polygon must enclose all the given trees. Return the coordinates of trees that are on the 
convex polygon's boundary.

The answer is guaranteed to be unique. You can return the vertices of the convex polygon in any order.

Constraints:
- 1 <= trees.length <= 3000
- trees[i].length == 2
- 0 <= xi, yi <= 100
- All the given positions are unique.
"""

from typing import List

def outerTrees(trees: List[List[int]]) -> List[List[int]]:
    """
    Function to find the convex hull of a set of points using the Monotone Chain algorithm.
    """
    # Helper function to calculate the cross product of vectors
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Sort the points lexicographically (by x, then by y)
    trees = sorted(trees)

    # Build the lower hull
    lower = []
    for p in trees:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)

    # Build the upper hull
    upper = []
    for p in reversed(trees):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
            upper.pop()
        upper.append(p)

    # Remove the last point of each half because it's repeated at the beginning of the other half
    return list(set(lower + upper))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    trees1 = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    print(outerTrees(trees1))  # Expected Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]

    # Test Case 2
    trees2 = [[1,2],[2,2],[4,2]]
    print(outerTrees(trees2))  # Expected Output: [[1,2],[2,2],[4,2]]

    # Test Case 3
    trees3 = [[0,0],[4,2],[1,1],[3,3],[5,5],[6,0]]
    print(outerTrees(trees3))  # Expected Output: [[0,0],[6,0],[5,5],[3,3],[1,1],[4,2]]


"""
Time Complexity Analysis:
- Sorting the points takes O(n log n), where n is the number of points.
- Constructing the lower and upper hulls involves iterating through the points, 
  and each point is added and removed from the hull at most once, which is O(n).
- Combining the hulls and removing duplicates takes O(n).
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- The space complexity is O(n) to store the hull points.

Topic: Geometry, Convex Hull, Monotone Chain Algorithm
"""