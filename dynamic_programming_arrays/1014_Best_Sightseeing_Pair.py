"""
LeetCode Problem #1014: Best Sightseeing Pair

Problem Statement:
You are given an integer array `values` where values[i] represents the value of the i-th sightseeing spot. 
Two sightseeing spots i and j have a distance of `j - i` between them.

The score of a pair (i < j) of sightseeing spots is `values[i] + values[j] + i - j`: 
the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Constraints:
- 2 <= values.length <= 5 * 10^4
- 1 <= values[i] <= 10^3
"""

# Solution
def maxScoreSightseeingPair(values):
    """
    Function to calculate the maximum score of a pair of sightseeing spots.

    :param values: List[int] - List of sightseeing spot values
    :return: int - Maximum score of a pair
    """
    max_score = 0
    max_i = values[0]  # Initialize max_i as values[0] + 0

    for j in range(1, len(values)):
        # Calculate the score for the current pair (i, j)
        max_score = max(max_score, max_i + values[j] - j)
        # Update max_i for the next iteration
        max_i = max(max_i, values[j] + j)

    return max_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    values1 = [8, 1, 5, 2, 6]
    print(maxScoreSightseeingPair(values1))  # Expected Output: 11

    # Test Case 2
    values2 = [1, 2]
    print(maxScoreSightseeingPair(values2))  # Expected Output: 2

    # Test Case 3
    values3 = [4, 7, 5, 8]
    print(maxScoreSightseeingPair(values3))  # Expected Output: 13

    # Test Case 4
    values4 = [10, 4, 3, 2, 1]
    print(maxScoreSightseeingPair(values4))  # Expected Output: 13

    # Test Case 5
    values5 = [1, 3, 5, 7, 9]
    print(maxScoreSightseeingPair(values5))  # Expected Output: 15

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the `values` array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the `values` array.

Space Complexity:
- The algorithm uses a constant amount of extra space (variables `max_score` and `max_i`).
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming, Arrays
"""