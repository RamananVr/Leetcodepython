"""
LeetCode Problem #1182: Shortest Distance to Target Color

Problem Statement:
You are given an array `colors`, in which there are three colors: 1, 2, and 3.
You are also given some queries. Each query consists of two integers `i` and `c`,
where `i` is the index of the `colors` array, and `c` is the target color.

Return an array `answer`, where `answer[j]` is the shortest distance from index `i`
to any index `k` such that `colors[k] == c`. If there is no such index, set `answer[j] = -1`.

Example 1:
Input: colors = [1, 1, 2, 1, 3, 2, 2, 3, 3], queries = [[0, 3], [2, 2], [6, 1]]
Output: [3, 0, 3]

Example 2:
Input: colors = [1, 2], queries = [[0, 3]]
Output: [-1]

Constraints:
- `1 <= colors.length <= 5 * 10^4`
- `1 <= colors[i] <= 3`
- `1 <= queries.length <= 5 * 10^4`
- `queries[j].length == 2`
- `0 <= queries[j][0] < colors.length`
- `1 <= queries[j][1] <= 3`
"""

from collections import defaultdict
import bisect

def shortestDistanceColor(colors, queries):
    """
    Function to find the shortest distance to the target color for each query.

    :param colors: List[int] - The array of colors (1, 2, 3).
    :param queries: List[List[int]] - The list of queries, where each query is [i, c].
    :return: List[int] - The shortest distance for each query, or -1 if the target color is not found.
    """
    # Preprocess the indices of each color
    color_indices = defaultdict(list)
    for idx, color in enumerate(colors):
        color_indices[color].append(idx)

    result = []
    for i, c in queries:
        if c not in color_indices:
            # If the target color does not exist in the array
            result.append(-1)
            continue

        # Use binary search to find the closest index
        indices = color_indices[c]
        pos = bisect.bisect_left(indices, i)

        # Calculate the minimum distance
        left_distance = abs(indices[pos - 1] - i) if pos > 0 else float('inf')
        right_distance = abs(indices[pos] - i) if pos < len(indices) else float('inf')
        result.append(min(left_distance, right_distance))

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    colors = [1, 1, 2, 1, 3, 2, 2, 3, 3]
    queries = [[0, 3], [2, 2], [6, 1]]
    print(shortestDistanceColor(colors, queries))  # Output: [3, 0, 3]

    # Test Case 2
    colors = [1, 2]
    queries = [[0, 3]]
    print(shortestDistanceColor(colors, queries))  # Output: [-1]

    # Test Case 3
    colors = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    queries = [[4, 1], [7, 3], [8, 2]]
    print(shortestDistanceColor(colors, queries))  # Output: [3, 1, 1]

"""
Time Complexity:
- Preprocessing: O(n), where n is the length of the `colors` array. We iterate through the array once to store indices for each color.
- Query Processing: O(q * log(n)), where q is the number of queries. For each query, we perform a binary search on the indices of the target color.
- Overall: O(n + q * log(n)).

Space Complexity:
- O(n), where n is the length of the `colors` array. We store the indices of each color in a dictionary.

Topic: Arrays, Binary Search
"""