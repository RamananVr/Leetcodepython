"""
LeetCode Problem #1774: Closest Dessert Cost

Problem Statement:
You would like to make dessert and are preparing to buy the ingredients. You have `baseCosts`, an array of integers representing the price of the base ingredients. You also have `toppingCosts`, an array of integers representing the price of the topping ingredients.

You want to make a dessert with a total cost as close as possible to the `target` price. To do that, you can choose one of the base ingredients and add 0, 1, or 2 of each topping ingredient.

Return the closest possible cost of the dessert to the target. If there are multiple possible costs, return the smallest one.

Constraints:
- 1 <= baseCosts.length <= 10
- 1 <= toppingCosts.length <= 10
- 1 <= baseCosts[i], toppingCosts[i] <= 10^4
- 1 <= target <= 10^4
"""

from typing import List

def closestCost(baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
    def dfs(index, current_cost):
        # Base case: if we've considered all toppings
        if index == len(toppingCosts):
            return current_cost
        
        # Recursive case: try adding 0, 1, or 2 of the current topping
        without_topping = dfs(index + 1, current_cost)
        with_one_topping = dfs(index + 1, current_cost + toppingCosts[index])
        with_two_toppings = dfs(index + 1, current_cost + 2 * toppingCosts[index])
        
        # Return the closest cost among the three options
        return min(
            without_topping,
            with_one_topping,
            with_two_toppings,
            key=lambda x: (abs(x - target), x)
        )
    
    closest = float('inf')
    for base in baseCosts:
        closest = min(closest, dfs(0, base), key=lambda x: (abs(x - target), x))
    
    return closest

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    baseCosts = [1, 7]
    toppingCosts = [3, 4]
    target = 10
    print(closestCost(baseCosts, toppingCosts, target))  # Output: 10

    # Test Case 2
    baseCosts = [2, 3]
    toppingCosts = [4, 5, 100]
    target = 18
    print(closestCost(baseCosts, toppingCosts, target))  # Output: 17

    # Test Case 3
    baseCosts = [10]
    toppingCosts = [1]
    target = 1
    print(closestCost(baseCosts, toppingCosts, target))  # Output: 10

"""
Time Complexity:
- Let `n` be the length of `baseCosts` and `m` be the length of `toppingCosts`.
- For each base cost, we perform a depth-first search (DFS) over all possible combinations of toppings.
- Each topping can be added in 3 ways (0, 1, or 2 times), so there are 3^m combinations of toppings.
- Therefore, the time complexity is O(n * 3^m).

Space Complexity:
- The space complexity is O(m) due to the recursion stack in the DFS.

Topic: Backtracking
"""