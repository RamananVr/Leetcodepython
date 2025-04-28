"""
LeetCode Problem #2361: Minimum Costs Using the Train Line

Problem Statement:
You are given two arrays `cost1` and `cost2` of size `n`, where `cost1[i]` and `cost2[i]` represent the cost of traveling to station `i` using train line 1 and train line 2, respectively. You can switch between the two train lines at any station, but switching incurs an additional cost `switchCost`.

Your task is to determine the minimum cost to travel from station 0 to station `n-1`.

Constraints:
- `1 <= n <= 10^5`
- `1 <= cost1[i], cost2[i], switchCost <= 10^4`

Example:
Input: cost1 = [1, 3, 5], cost2 = [2, 1, 4], switchCost = 2
Output: 6
Explanation:
- Start at station 0 using train line 1 (cost = 1).
- Switch to train line 2 at station 1 (cost = 1 + 2 = 3).
- Continue on train line 2 to station 2 (cost = 3 + 4 = 6).
The total cost is 6.

Your goal is to implement a function `minimumCosts(cost1, cost2, switchCost)` that returns the minimum cost to travel from station 0 to station `n-1`.
"""

def minimumCosts(cost1, cost2, switchCost):
    """
    Calculate the minimum cost to travel from station 0 to station n-1.

    :param cost1: List[int] - Costs for train line 1
    :param cost2: List[int] - Costs for train line 2
    :param switchCost: int - Cost to switch between train lines
    :return: int - Minimum cost to travel
    """
    n = len(cost1)
    
    # Initialize the minimum costs for the first station
    prev_cost1 = cost1[0]
    prev_cost2 = cost2[0]
    
    # Iterate through the stations
    for i in range(1, n):
        # Calculate the cost of staying on the same line or switching lines
        curr_cost1 = min(prev_cost1 + cost1[i], prev_cost2 + switchCost + cost1[i])
        curr_cost2 = min(prev_cost2 + cost2[i], prev_cost1 + switchCost + cost2[i])
        
        # Update the previous costs for the next iteration
        prev_cost1, prev_cost2 = curr_cost1, curr_cost2
    
    # Return the minimum cost to reach the last station
    return min(prev_cost1, prev_cost2)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cost1 = [1, 3, 5]
    cost2 = [2, 1, 4]
    switchCost = 2
    print(minimumCosts(cost1, cost2, switchCost))  # Output: 6

    # Test Case 2
    cost1 = [10, 10, 10]
    cost2 = [1, 1, 1]
    switchCost = 5
    print(minimumCosts(cost1, cost2, switchCost))  # Output: 3

    # Test Case 3
    cost1 = [5, 8, 6]
    cost2 = [7, 3, 4]
    switchCost = 3
    print(minimumCosts(cost1, cost2, switchCost))  # Output: 14

    # Test Case 4
    cost1 = [1]
    cost2 = [2]
    switchCost = 10
    print(minimumCosts(cost1, cost2, switchCost))  # Output: 1

    # Test Case 5
    cost1 = [1, 2, 3, 4, 5]
    cost2 = [5, 4, 3, 2, 1]
    switchCost = 1
    print(minimumCosts(cost1, cost2, switchCost))  # Output: 9

"""
Time Complexity Analysis:
- The algorithm iterates through the `n` stations once, performing constant-time calculations at each step.
- Therefore, the time complexity is O(n).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space to store the previous costs for the two train lines.
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming
"""