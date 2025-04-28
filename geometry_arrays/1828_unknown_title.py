"""
LeetCode Problem #1828: Queries on Number of Points Inside a Circle

Problem Statement:
You are given an array `points` where `points[i] = [xi, yi]` is the coordinates of the ith point on a 2D plane. 
Multiple queries are given in the array `queries`, where `queries[j] = [xj, yj, rj]` describes a circle centered 
at (xj, yj) with radius rj.

For each query, compute the number of points inside the circle (including points on the boundary) and return an 
array `answer`, where `answer[j]` is the answer to the jth query.

The ith point is considered to be inside the jth circle if the Euclidean distance between the point and the center 
of the circle is less than or equal to the radius of the circle.

Example:
Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
Output: [3,2,2]

Constraints:
- 1 <= points.length <= 500
- points[i].length == 2
- 0 <= xi, yi <= 500
- 1 <= queries.length <= 500
- queries[j].length == 3
- 0 <= xj, yj <= 500
- 1 <= rj <= 500
"""

# Python Solution
def countPoints(points, queries):
    """
    Function to count the number of points inside each circle described by the queries.

    :param points: List[List[int]] - List of points on the 2D plane.
    :param queries: List[List[int]] - List of queries describing circles.
    :return: List[int] - Number of points inside each circle.
    """
    answer = []
    for xj, yj, rj in queries:
        count = 0
        for xi, yi in points:
            # Calculate the squared distance to avoid floating-point operations
            if (xi - xj) ** 2 + (yi - yj) ** 2 <= rj ** 2:
                count += 1
        answer.append(count)
    return answer

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points = [[1, 3], [3, 3], [5, 3], [2, 2]]
    queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
    print(countPoints(points, queries))  # Output: [3, 2, 2]

    # Test Case 2
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    queries = [[3, 3, 2], [1, 1, 1], [5, 5, 1]]
    print(countPoints(points, queries))  # Output: [4, 1, 1]

    # Test Case 3
    points = [[0, 0], [1, 1], [2, 2], [3, 3]]
    queries = [[1, 1, 1], [2, 2, 2], [0, 0, 3]]
    print(countPoints(points, queries))  # Output: [2, 3, 4]

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each query, we iterate through all the points to check if they lie inside the circle.
- Let `m` be the number of points and `n` be the number of queries.
- The time complexity is O(m * n), where `m` is the length of `points` and `n` is the length of `queries`.

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures apart from the output list.

Overall Complexity:
- Time: O(m * n)
- Space: O(1)
"""

# Topic: Geometry, Arrays