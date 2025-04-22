"""
LeetCode Problem #256: Paint House

Problem Statement:
There is a row of `n` houses, where each house can be painted one of three colors: red, blue, or green. 
The cost of painting each house with a certain color is represented by a `n x 3` cost matrix `costs`.

- `costs[i][0]` is the cost of painting house `i` red.
- `costs[i][1]` is the cost of painting house `i` blue.
- `costs[i][2]` is the cost of painting house `i` green.

You want to paint all the houses such that no two adjacent houses have the same color.

Return the minimum cost to paint all the houses.

If there are no houses, return 0.

Constraints:
- `costs.length == n`
- `costs[i].length == 3`
- `1 <= n <= 100`
- `1 <= costs[i][j] <= 20`
"""

def minCost(costs):
    """
    Function to calculate the minimum cost to paint all houses such that no two adjacent houses
    have the same color.

    :param costs: List[List[int]] - A 2D list where costs[i][j] represents the cost of painting
                                    house i with color j (0: red, 1: blue, 2: green).
    :return: int - The minimum cost to paint all houses.
    """
    if not costs:
        return 0

    n = len(costs)
    # Iterate from the second-to-last house to the first house
    for i in range(n - 2, -1, -1):
        # Update the cost of painting the current house with each color
        costs[i][0] += min(costs[i + 1][1], costs[i + 1][2])  # Red
        costs[i][1] += min(costs[i + 1][0], costs[i + 1][2])  # Blue
        costs[i][2] += min(costs[i + 1][0], costs[i + 1][1])  # Green

    # The minimum cost to paint all houses will be the minimum of the costs for the first house
    return min(costs[0][0], costs[0][1], costs[0][2])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    costs1 = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    print(minCost(costs1))  # Expected Output: 10

    # Test Case 2
    costs2 = [[7, 6, 2]]
    print(minCost(costs2))  # Expected Output: 2

    # Test Case 3
    costs3 = []
    print(minCost(costs3))  # Expected Output: 0

    # Test Case 4
    costs4 = [[1, 5, 3], [2, 9, 4]]
    print(minCost(costs4))  # Expected Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the list of houses once, updating the costs for each house.
- This results in a time complexity of O(n), where n is the number of houses.

Space Complexity:
- The algorithm modifies the input `costs` list in place and does not use any additional space.
- Thus, the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""