"""
LeetCode Problem #1815: Maximum Number of Groups Getting Fresh Donuts

Problem Statement:
There is a bakery that has a rule where they only serve customers if they can form a group of size `batchSize`. 
Customers come in groups of various sizes, and the bakery wants to maximize the number of groups that can get fresh donuts.

You are given an integer `batchSize` and an integer array `groups`, where `groups[i]` represents the size of the ith group of customers. 
Return the maximum number of groups that can get fresh donuts.

A group gets fresh donuts if the sum of the group sizes in the batch is divisible by `batchSize`. 
You can rearrange the groups in any order.

Constraints:
- 1 <= batchSize <= 9
- 1 <= groups.length <= 30
- 1 <= groups[i] <= 10^9
"""

from functools import lru_cache
from collections import Counter

def maxHappyGroups(batchSize: int, groups: list[int]) -> int:
    # Preprocess groups to calculate remainders
    remainders = [group % batchSize for group in groups]
    remainder_count = Counter(remainders)

    # Helper function for DFS with memoization
    @lru_cache(None)
    def dfs(state: tuple[int], current_sum: int) -> int:
        # Base case: if all groups are used
        if sum(state) == 0:
            return 0
        
        max_happy = 0
        for remainder in range(batchSize):
            if state[remainder] > 0:
                # Create new state by reducing the count of the current remainder
                new_state = list(state)
                new_state[remainder] -= 1
                new_state = tuple(new_state)
                
                # Calculate new sum and check if it forms a happy group
                new_sum = (current_sum + remainder) % batchSize
                happy_increment = 1 if new_sum == 0 else 0
                
                # Recursively calculate the maximum happy groups
                max_happy = max(max_happy, dfs(new_state, new_sum) + happy_increment)
        
        return max_happy

    # Convert remainder_count to a tuple for memoization
    state = tuple(remainder_count[i] for i in range(batchSize))
    
    # Start DFS with initial state and sum = 0
    return dfs(state, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    batchSize = 3
    groups = [1, 2, 3, 4, 5, 6]
    print(maxHappyGroups(batchSize, groups))  # Expected Output: 4

    # Test Case 2
    batchSize = 4
    groups = [1, 3, 2, 5, 2, 2, 1, 6]
    print(maxHappyGroups(batchSize, groups))  # Expected Output: 4

    # Test Case 3
    batchSize = 5
    groups = [1, 2, 3, 4, 5, 10, 15]
    print(maxHappyGroups(batchSize, groups))  # Expected Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The number of states in the DFS is bounded by `batchSize^batchSize` because we are tracking the count of each remainder (0 to batchSize-1).
- For each state, we iterate over `batchSize` remainders, leading to a complexity of O(batchSize * batchSize^batchSize).
- In practice, batchSize is small (<= 9), so this is computationally feasible.

Space Complexity:
- The space complexity is dominated by the memoization table, which stores up to `batchSize^batchSize` states.
- Additionally, the recursion stack can go up to O(batchSize^batchSize) in the worst case.

Primary Topic: Dynamic Programming (DP)
"""