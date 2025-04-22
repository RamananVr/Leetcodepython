"""
LeetCode Problem #638: Shopping Offers

Problem Statement:
In LeetCode Question #638, you are given the following:

- `price` (List[int]): An array where `price[i]` is the price of the `i-th` item.
- `special` (List[List[int]]): A 2D list where each `special[j]` contains a list of integers. 
  The first `n` integers represent the number of each item included in the offer, and the last integer is the price of the offer.
- `needs` (List[int]): A list where `needs[i]` is the number of items of the `i-th` type that you want to buy.

The goal is to find the minimum cost to satisfy the shopping list `needs`. You can use each special offer any number of times, as long as the offer does not exceed the required number of items.

Constraints:
1. `n == len(price) == len(needs)`
2. `0 <= price[i] <= 10`
3. `0 <= needs[i] <= 10`
4. `1 <= len(special) <= 100`
5. `0 <= special[j][i] <= 10` for `0 <= i < n`
6. `0 <= special[j][n] <= 200`

Write a function `shoppingOffers(price: List[int], special: List[List[int]], needs: List[int]) -> int` to solve the problem.
"""

from typing import List

def shoppingOffers(price: List[int], special: List[List[int]], needs: List[int]) -> int:
    def dfs(current_needs):
        # If the current state has been computed before, return the cached result
        if tuple(current_needs) in memo:
            return memo[tuple(current_needs)]
        
        # Calculate the cost without using any special offers
        cost_without_offer = sum(current_needs[i] * price[i] for i in range(len(needs)))
        min_cost = cost_without_offer
        
        # Try each special offer
        for offer in special:
            new_needs = []
            for i in range(len(needs)):
                if current_needs[i] < offer[i]:  # If the offer exceeds the needs, skip it
                    break
                new_needs.append(current_needs[i] - offer[i])
            else:  # If the offer is valid, calculate the cost recursively
                min_cost = min(min_cost, offer[-1] + dfs(new_needs))
        
        # Cache the result for the current state
        memo[tuple(current_needs)] = min_cost
        return min_cost
    
    # Memoization dictionary
    memo = {}
    return dfs(needs)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    price = [2, 5]
    special = [[3, 0, 5], [1, 2, 10]]
    needs = [3, 2]
    print(shoppingOffers(price, special, needs))  # Output: 14

    # Test Case 2
    price = [2, 3, 4]
    special = [[1, 1, 0, 4], [2, 2, 1, 9]]
    needs = [1, 2, 1]
    print(shoppingOffers(price, special, needs))  # Output: 11

    # Test Case 3
    price = [2, 3]
    special = [[1, 1, 5]]
    needs = [2, 2]
    print(shoppingOffers(price, special, needs))  # Output: 10

"""
Time and Space Complexity Analysis:

Time Complexity:
- Let `n` be the number of items and `m` be the number of special offers.
- The total number of states in the `needs` space is at most `(max_needs + 1)^n`, where `max_needs` is the maximum value in `needs`.
- For each state, we iterate through all `m` special offers.
- Thus, the time complexity is O(m * (max_needs + 1)^n).

Space Complexity:
- The space complexity is O((max_needs + 1)^n) due to the memoization dictionary.

Topic: Dynamic Programming (DP)
"""