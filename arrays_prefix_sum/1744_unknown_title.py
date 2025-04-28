"""
LeetCode Problem #1744: Can You Eat Your Favorite Candy on Your Favorite Day?

Problem Statement:
You are given a 0-indexed array `candiesCount` of size `n`, where `candiesCount[i]` represents the number of candies of the `i-th` type you have. 
You are also given a 2D array `queries` where `queries[i] = [favoriteTypei, favoriteDayi, dailyCapi]`.

You want to know if you can eat at least one candy of type `favoriteTypei` on day `favoriteDayi` without eating more than `dailyCapi` candies per day.

Note that you:
- Start eating candies on day 0.
- You can only eat at most `dailyCapi` candies each day.
- You must eat exactly one candy per day before eating a candy of the next type.

Return a boolean array `result` of length `m`, where `result[i]` is `true` if you can eat a candy of type `favoriteTypei` on day `favoriteDayi` under the given constraints, and `false` otherwise.

Constraints:
- `1 <= candiesCount.length <= 10^5`
- `1 <= candiesCount[i] <= 10^12`
- `1 <= queries.length <= 10^5`
- `queries[i].length == 3`
- `0 <= favoriteTypei < candiesCount.length`
- `0 <= favoriteDayi < 10^9`
- `1 <= dailyCapi <= 10^9`

Example:
Input: candiesCount = [7, 4, 5, 3, 8], queries = [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]
Output: [true, false, true]
"""

# Solution
from itertools import accumulate
from typing import List

def canEat(candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
    # Calculate the prefix sum of candiesCount
    prefix_sum = list(accumulate(candiesCount))
    
    result = []
    for favoriteType, favoriteDay, dailyCap in queries:
        # Calculate the range of days when you can eat the favorite type of candy
        min_candies_needed = favoriteDay + 1  # Minimum candies needed to reach favoriteDay
        max_candies_possible = (favoriteDay + 1) * dailyCap  # Maximum candies you can eat by favoriteDay
        
        # Calculate the range of candies available for the favorite type
        candies_before = prefix_sum[favoriteType - 1] if favoriteType > 0 else 0
        candies_available = prefix_sum[favoriteType]
        
        # Check if the ranges overlap
        can_eat = not (max_candies_possible <= candies_before or min_candies_needed > candies_available)
        result.append(can_eat)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    candiesCount = [7, 4, 5, 3, 8]
    queries = [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]
    print(canEat(candiesCount, queries))  # Output: [True, False, True]

    # Test Case 2
    candiesCount = [5, 2, 6, 4, 1]
    queries = [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]]
    print(canEat(candiesCount, queries))  # Output: [False, True, True, False, False]

# Time Complexity Analysis:
# - Calculating the prefix sum takes O(n), where n is the length of candiesCount.
# - For each query, we perform constant-time calculations, so processing all queries takes O(m), where m is the number of queries.
# - Overall time complexity: O(n + m).

# Space Complexity Analysis:
# - The prefix sum array takes O(n) space.
# - The result array takes O(m) space.
# - Overall space complexity: O(n + m).

# Topic: Arrays, Prefix Sum