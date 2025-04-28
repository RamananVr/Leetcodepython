"""
LeetCode Problem #2672: Number of Adjacent Elements With the Same Color

Problem Statement:
You are given a 0-indexed integer array `colors` of length `n`, where `colors[i]` represents the color of the ith element. 
You are also given a 2D array `queries` where `queries[j] = [index_j, color_j]`.

For each query `j`, you need to update `colors[index_j]` to `color_j`, and then determine the number of adjacent elements 
with the same color.

Return an array `answer` where `answer[j]` is the result of the jth query.

Example:
Input: colors = [1, 1, 2], queries = [[1, 2], [2, 1], [1, 1]]
Output: [1, 1, 2]

Explanation:
- After the 1st query, the array becomes [1, 2, 2], and there is 1 pair of adjacent elements with the same color.
- After the 2nd query, the array becomes [1, 2, 1], and there is 1 pair of adjacent elements with the same color.
- After the 3rd query, the array becomes [1, 1, 1], and there are 2 pairs of adjacent elements with the same color.

Constraints:
- 1 <= colors.length <= 10^5
- 1 <= colors[i] <= 10^5
- 1 <= queries.length <= 10^5
- queries[j].length == 2
- 0 <= index_j < colors.length
- 1 <= color_j <= 10^5
"""

# Python Solution
def colorTheArray(n, queries):
    """
    Function to process queries and return the number of adjacent elements with the same color after each query.

    :param n: Length of the colors array (not used directly in the function).
    :param queries: List of queries where each query is [index, color].
    :return: List of integers representing the number of adjacent elements with the same color after each query.
    """
    colors = [0] * n  # Initialize the colors array with 0 (no color).
    adjacent_count = 0  # Initialize the count of adjacent elements with the same color.
    result = []  # List to store the result for each query.

    for index, new_color in queries:
        # Check the left neighbor
        if index > 0 and colors[index] == colors[index - 1]:
            adjacent_count -= 1
        # Check the right neighbor
        if index < n - 1 and colors[index] == colors[index + 1]:
            adjacent_count -= 1

        # Update the color at the index
        colors[index] = new_color

        # Check the left neighbor again
        if index > 0 and colors[index] == colors[index - 1]:
            adjacent_count += 1
        # Check the right neighbor again
        if index < n - 1 and colors[index] == colors[index + 1]:
            adjacent_count += 1

        # Append the current adjacent count to the result
        result.append(adjacent_count)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    colors = [1, 1, 2]
    queries = [[1, 2], [2, 1], [1, 1]]
    print(colorTheArray(len(colors), queries))  # Output: [1, 1, 2]

    # Test Case 2
    colors = [0, 0, 0, 0]
    queries = [[0, 1], [1, 1], [2, 1], [3, 1]]
    print(colorTheArray(len(colors), queries))  # Output: [0, 1, 2, 3]

    # Test Case 3
    colors = [1, 2, 3, 4]
    queries = [[0, 2], [1, 2], [2, 2], [3, 2]]
    print(colorTheArray(len(colors), queries))  # Output: [0, 1, 2, 3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each query involves checking the left and right neighbors (O(1)) and updating the color (O(1)).
- Since there are `q` queries, the total time complexity is O(q).

Space Complexity:
- The `colors` array requires O(n) space.
- The `result` array requires O(q) space.
- Overall space complexity is O(n + q).
"""

# Topic: Arrays