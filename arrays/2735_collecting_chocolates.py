"""
LeetCode Question #2735: Collecting Chocolates

Problem Statement:
You are given an array `chocolates` of length `n`, where `chocolates[i]` represents the cost of the chocolate at index `i`. 
You can perform the following operation any number of times:

- Choose an integer `k` (1 <= k <= n - 1) and rotate the array to the right by `k` positions. 
  For example, if `k = 2` and the array is `[1, 2, 3, 4]`, after rotating the array to the right by `k`, it becomes `[3, 4, 1, 2]`.

Your goal is to collect one chocolate from each index of the array. To collect a chocolate from index `i`, 
you must pay the cost of the chocolate at that index. You can rotate the array any number of times to minimize the total cost.

Return the minimum total cost to collect all chocolates.

Constraints:
- `1 <= n <= 1000`
- `1 <= chocolates[i] <= 10^6`
"""

# Python Solution
def minCostToCollectChocolates(chocolates):
    """
    Calculate the minimum cost to collect all chocolates from the array.

    :param chocolates: List[int] - Array of chocolate costs
    :return: int - Minimum total cost
    """
    n = len(chocolates)
    min_cost = float('inf')

    # Iterate over all possible rotations
    for k in range(n):
        rotated_cost = 0
        for i in range(n):
            rotated_cost += chocolates[(i + k) % n]
        min_cost = min(min_cost, rotated_cost)

    return min_cost

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    chocolates = [1, 2, 3, 4]
    print(minCostToCollectChocolates(chocolates))  # Expected Output: 10

    # Test Case 2
    chocolates = [5, 1, 2, 3]
    print(minCostToCollectChocolates(chocolates))  # Expected Output: 11

    # Test Case 3
    chocolates = [10, 20, 30]
    print(minCostToCollectChocolates(chocolates))  # Expected Output: 60

    # Test Case 4
    chocolates = [1]
    print(minCostToCollectChocolates(chocolates))  # Expected Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop iterates over all possible rotations (n times).
- The inner loop calculates the cost for each rotation, which takes O(n) time.
- Therefore, the total time complexity is O(n^2).

Space Complexity:
- We use a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Arrays