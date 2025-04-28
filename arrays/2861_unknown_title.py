"""
LeetCode Problem #2861: Maximum Number of Alloys

Problem Statement:
You are given `n` types of machines, each capable of producing a specific type of alloy. Each machine has a fixed production rate, and you are given the number of units of each alloy that can be produced per unit time. Additionally, you are given the cost of producing each alloy and the budget available to you.

Your task is to determine the maximum number of alloys that can be produced within the given budget.

Input:
- `n` (int): The number of types of machines.
- `production_rates` (List[int]): A list of integers where `production_rates[i]` represents the production rate of the i-th machine.
- `costs` (List[int]): A list of integers where `costs[i]` represents the cost of producing one unit of alloy using the i-th machine.
- `budget` (int): The total budget available.

Output:
- Return the maximum number of alloys that can be produced within the given budget.

Constraints:
- 1 <= n <= 10^5
- 1 <= production_rates[i], costs[i] <= 10^5
- 1 <= budget <= 10^9
"""

# Solution
def max_alloys(n, production_rates, costs, budget):
    """
    Calculate the maximum number of alloys that can be produced within the given budget.

    :param n: int - Number of types of machines.
    :param production_rates: List[int] - Production rates of each machine.
    :param costs: List[int] - Costs of producing one unit of alloy for each machine.
    :param budget: int - Total budget available.
    :return: int - Maximum number of alloys that can be produced.
    """
    max_alloys = 0

    for rate, cost in zip(production_rates, costs):
        # Calculate the maximum number of units that can be produced by this machine within the budget
        max_units = budget // cost
        max_alloys = max(max_alloys, max_units * rate)

    return max_alloys

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    production_rates = [5, 10, 15]
    costs = [2, 3, 5]
    budget = 20
    print(max_alloys(n, production_rates, costs, budget))  # Expected Output: 50

    # Test Case 2
    n = 2
    production_rates = [8, 12]
    costs = [4, 6]
    budget = 24
    print(max_alloys(n, production_rates, costs, budget))  # Expected Output: 48

    # Test Case 3
    n = 4
    production_rates = [3, 6, 9, 12]
    costs = [1, 2, 3, 4]
    budget = 10
    print(max_alloys(n, production_rates, costs, budget))  # Expected Output: 30

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the `production_rates` and `costs` lists once, which takes O(n) time.
- Therefore, the time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space for variables like `max_alloys` and `max_units`.
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays