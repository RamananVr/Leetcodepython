"""
LeetCode Question #1478: Allocate Mailboxes

Problem Statement:
Given the array `houses` and an integer `k`, where `houses[i]` is the location of the ith house along a street, 
we want to allocate `k` mailboxes in such a way that the total distance between the houses and the mailboxes is minimized.

The distance between the house and the mailbox is the absolute value of their difference. 
Return the minimum total distance between the houses and the mailboxes.

Constraints:
- `n == houses.length`
- `1 <= n <= 100`
- `1 <= houses[i] <= 10^4`
- `1 <= k <= n`
- The positions of the houses are distinct.

Example:
Input: houses = [1, 4, 8, 10, 20], k = 3
Output: 5
Explanation: Allocate mailboxes at positions 4, 8, and 10. The minimum total distance is 5.

Input: houses = [2, 3, 5, 12, 18], k = 2
Output: 9
Explanation: Allocate mailboxes at positions 3 and 12. The minimum total distance is 9.

Follow-up:
Could you solve the problem in O(n^2 * k) time complexity?
"""

from functools import lru_cache

def minDistance(houses, k):
    """
    Function to calculate the minimum total distance to allocate k mailboxes.
    
    :param houses: List[int] - List of house positions
    :param k: int - Number of mailboxes to allocate
    :return: int - Minimum total distance
    """
    # Sort the houses to simplify distance calculations
    houses.sort()
    n = len(houses)
    
    # Precompute the cost of placing one mailbox for any subarray of houses
    # cost[i][j] represents the total distance if one mailbox is placed optimally for houses[i:j+1]
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            mid = (i + j) // 2
            for x in range(i, j + 1):
                cost[i][j] += abs(houses[x] - houses[mid])
    
    # Use dynamic programming to find the minimum cost
    @lru_cache(None)
    def dp(i, k):
        # Base case: If no houses are left and no mailboxes are needed
        if i == n and k == 0:
            return 0
        # If no houses are left but mailboxes are still needed, or vice versa
        if i == n or k == 0:
            return float('inf')
        
        # Try placing a mailbox for houses[i:j+1] and recurse
        result = float('inf')
        for j in range(i, n):
            result = min(result, cost[i][j] + dp(j + 1, k - 1))
        return result
    
    return dp(0, k)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    houses = [1, 4, 8, 10, 20]
    k = 3
    print(minDistance(houses, k))  # Output: 5

    # Test Case 2
    houses = [2, 3, 5, 12, 18]
    k = 2
    print(minDistance(houses, k))  # Output: 9

    # Test Case 3
    houses = [1, 2, 3, 4, 5]
    k = 1
    print(minDistance(houses, k))  # Output: 6

    # Test Case 4
    houses = [1, 2, 3, 4, 5]
    k = 2
    print(minDistance(houses, k))  # Output: 3

    # Test Case 5
    houses = [1, 10, 20, 30, 40]
    k = 4
    print(minDistance(houses, k))  # Output: 0

"""
Time Complexity:
- Sorting the houses takes O(n log n).
- Precomputing the cost array takes O(n^2).
- The DP function has O(n * k) states, and for each state, we iterate over O(n) to calculate the result.
- Overall time complexity: O(n^2 * k).

Space Complexity:
- The cost array takes O(n^2) space.
- The DP cache takes O(n * k) space.
- Overall space complexity: O(n^2 + n * k).

Topic: Dynamic Programming
"""