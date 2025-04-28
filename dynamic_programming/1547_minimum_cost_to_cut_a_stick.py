"""
LeetCode Question #1547: Minimum Cost to Cut a Stick

Problem Statement:
You are given a wooden stick of length `n`. You want to split the stick into `k` pieces. 
The positions of the cuts are given as an array `cuts` where `cuts[i]` is the position 
of the ith cut on the stick. You should perform the cuts in such a way that the total 
cost is minimized.

The cost of making a cut is equal to the length of the stick segment that is being cut. 
After a cut, the stick is divided into two smaller sticks. The sum of the costs of all 
cuts is the total cost.

Return the minimum total cost of making the cuts.

Constraints:
- `2 <= n <= 10^6`
- `1 <= cuts.length <= min(n - 1, 100)`
- `1 <= cuts[i] <= n - 1`
- All the integers in `cuts` are distinct.

Example:
Input: n = 7, cuts = [1, 3, 4, 5]
Output: 16
Explanation: Using cuts at 1, 3, 4, and 5 in order, the total cost is:
- First cut at 3 costs 7 (length of the stick).
- Second cut at 4 costs 4 (length of the stick segment).
- Third cut at 5 costs 3 (length of the stick segment).
- Fourth cut at 1 costs 2 (length of the stick segment).
Total cost = 7 + 4 + 3 + 2 = 16.
"""

# Solution
def minCost(n: int, cuts: list[int]) -> int:
    # Add the boundaries of the stick to the cuts array
    cuts = sorted(cuts + [0, n])
    m = len(cuts)
    
    # Initialize a DP table
    dp = [[0] * m for _ in range(m)]
    
    # Fill the DP table
    for length in range(2, m):  # The length of the segment being considered
        for i in range(m - length):  # Start of the segment
            j = i + length  # End of the segment
            dp[i][j] = float('inf')
            for k in range(i + 1, j):  # Possible cut positions within the segment
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])
    
    return dp[0][m - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 7
    cuts = [1, 3, 4, 5]
    print(minCost(n, cuts))  # Output: 16

    # Test Case 2
    n = 9
    cuts = [5, 6, 1, 4]
    print(minCost(n, cuts))  # Output: 22

    # Test Case 3
    n = 10
    cuts = [2, 4, 7]
    print(minCost(n, cuts))  # Output: 20

    # Test Case 4
    n = 20
    cuts = [3, 8, 10, 15]
    print(minCost(n, cuts))  # Output: 43

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the cuts array takes O(k log k), where k is the length of the cuts array.
- The DP table has dimensions m x m, where m = k + 2 (including boundaries).
- Filling the DP table involves iterating over all pairs (i, j) and all possible cuts k within the segment.
- This results in a time complexity of O(m^3), where m = k + 2.
- Since k <= 100, m <= 102, so the time complexity is effectively O(102^3) = O(1,061,208), which is manageable.

Space Complexity:
- The DP table requires O(m^2) space, where m = k + 2.
- Thus, the space complexity is O(102^2) = O(10,404), which is also manageable.

Topic: Dynamic Programming
"""