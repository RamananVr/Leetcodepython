"""
LeetCode Problem #2398: Maximum Number of Robots Within Budget

Problem Statement:
You are given two integer arrays, `chargeTimes` and `runningCosts`, both of length `n`, and an integer `budget`.

The `i-th` robot costs `chargeTimes[i]` to charge and `runningCosts[i]` to run. You can run multiple robots simultaneously, but the total cost of running them must not exceed the budget. The total cost of running `k` robots is defined as:

    max(chargeTimes[i]) + k * sum(runningCosts[i])

where `max(chargeTimes[i])` is the maximum charge time among the selected robots, and `sum(runningCosts[i])` is the sum of their running costs.

Return the maximum number of robots you can run simultaneously without exceeding the budget.

Constraints:
- `chargeTimes.length == runningCosts.length == n`
- `1 <= n <= 10^5`
- `1 <= chargeTimes[i], runningCosts[i] <= 10^5`
- `1 <= budget <= 10^9`
"""

from collections import deque

def maximumRobots(chargeTimes, runningCosts, budget):
    """
    Finds the maximum number of robots that can be run simultaneously within the given budget.

    Args:
    chargeTimes (List[int]): List of charge times for each robot.
    runningCosts (List[int]): List of running costs for each robot.
    budget (int): Maximum budget allowed.

    Returns:
    int: Maximum number of robots that can be run simultaneously.
    """
    n = len(chargeTimes)
    max_deque = deque()  # Stores indices of chargeTimes in decreasing order
    total_running_cost = 0
    left = 0
    max_robots = 0

    for right in range(n):
        # Add the current chargeTime to the deque
        while max_deque and chargeTimes[max_deque[-1]] <= chargeTimes[right]:
            max_deque.pop()
        max_deque.append(right)

        # Add the current running cost to the total
        total_running_cost += runningCosts[right]

        # Calculate the total cost for the current window
        max_charge_time = chargeTimes[max_deque[0]]
        num_robots = right - left + 1
        total_cost = max_charge_time + num_robots * total_running_cost

        # If the total cost exceeds the budget, shrink the window from the left
        while total_cost > budget:
            if max_deque[0] == left:
                max_deque.popleft()
            total_running_cost -= runningCosts[left]
            left += 1
            num_robots = right - left + 1
            if num_robots > 0:
                max_charge_time = chargeTimes[max_deque[0]]
                total_cost = max_charge_time + num_robots * total_running_cost
            else:
                total_cost = 0

        # Update the maximum number of robots
        max_robots = max(max_robots, num_robots)

    return max_robots

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    chargeTimes = [3, 6, 1, 3, 4]
    runningCosts = [2, 1, 3, 4, 5]
    budget = 25
    print(maximumRobots(chargeTimes, runningCosts, budget))  # Expected Output: 3

    # Test Case 2
    chargeTimes = [10, 20, 30]
    runningCosts = [1, 2, 3]
    budget = 15
    print(maximumRobots(chargeTimes, runningCosts, budget))  # Expected Output: 1

    # Test Case 3
    chargeTimes = [1, 1, 1, 1]
    runningCosts = [1, 1, 1, 1]
    budget = 10
    print(maximumRobots(chargeTimes, runningCosts, budget))  # Expected Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the `chargeTimes` and `runningCosts` arrays once, making it O(n).
- The deque operations (append, pop, popleft) are O(1) each, and each element is added and removed from the deque at most once.
- Overall time complexity: O(n).

Space Complexity:
- The deque used to store indices of `chargeTimes` can hold at most `n` elements, making its space complexity O(n).
- Other variables use constant space.
- Overall space complexity: O(n).

Topic: Sliding Window, Monotonic Queue
"""