"""
LeetCode Question #265: Paint House II

Problem Statement:
There are a row of `n` houses, each house can be painted with one of `k` colors. 
The cost of painting each house with a certain color is represented by a `n x k` cost matrix `costs`.

- costs[i][j] is the cost of painting house `i` with color `j`.
- You need to paint all the houses such that no two adjacent houses have the same color.

Return the minimum cost to paint all the houses.

If `costs` is empty, return 0.

Constraints:
- `costs.length == n`
- `costs[i].length == k`
- 1 <= n <= 100
- 1 <= k <= 20
- 1 <= costs[i][j] <= 20
"""

def minCostII(costs):
    """
    Function to calculate the minimum cost to paint all houses such that no two adjacent houses have the same color.
    
    :param costs: List[List[int]] - A 2D list where costs[i][j] represents the cost of painting house i with color j.
    :return: int - The minimum cost to paint all houses.
    """
    if not costs:
        return 0

    n, k = len(costs), len(costs[0])

    # Initialize the previous row to the costs of the first house
    prev_row = costs[0]

    for i in range(1, n):
        # Find the two smallest costs in the previous row
        min1, min2 = float('inf'), float('inf')
        for j in range(k):
            if prev_row[j] < min1:
                min2 = min1
                min1 = prev_row[j]
            elif prev_row[j] < min2:
                min2 = prev_row[j]

        # Update the current row based on the previous row
        curr_row = [0] * k
        for j in range(k):
            if prev_row[j] == min1:
                curr_row[j] = costs[i][j] + min2
            else:
                curr_row[j] = costs[i][j] + min1

        # Move to the next row
        prev_row = curr_row

    # The result is the minimum value in the last row
    return min(prev_row)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    costs1 = [
        [1, 5, 3],
        [2, 9, 4]
    ]
    print(minCostII(costs1))  # Output: 5

    # Test Case 2
    costs2 = [
        [8]
    ]
    print(minCostII(costs2))  # Output: 8

    # Test Case 3
    costs3 = [
        [1, 3, 5],
        [2, 4, 6],
        [3, 1, 7]
    ]
    print(minCostII(costs3))  # Output: 5

    # Test Case 4
    costs4 = []
    print(minCostII(costs4))  # Output: 0

    # Test Case 5
    costs5 = [
        [1, 2, 3],
        [10, 11, 12],
        [7, 8, 9]
    ]
    print(minCostII(costs5))  # Output: 18


"""
Time Complexity Analysis:
- Let `n` be the number of houses and `k` be the number of colors.
- For each house, we iterate through the `k` colors to find the two smallest costs, which takes O(k).
- Then, we update the costs for the current house, which also takes O(k).
- Total time complexity: O(n * k).

Space Complexity Analysis:
- We use a single array `prev_row` of size `k` to store the costs of the previous row.
- Total space complexity: O(k).

Topic: Dynamic Programming
"""