"""
LeetCode Question #1575: Count All Possible Routes

Problem Statement:
You are given an array of distinct positive integers `locations` where `locations[i]` represents the position of city `i`. 
You are also given integers `start`, `finish`, and `fuel` representing the starting city, the destination city, and the 
initial amount of fuel you have, respectively.

At each step, if you are at city `i`, you can pick any city `j` such that `j != i` and move to city `j`. 
Moving from city `i` to city `j` reduces the amount of fuel you have by `|locations[i] - locations[j]|`, 
where `|x|` denotes the absolute value of `x`. Please notice that `|locations[i] - locations[j]|` is the distance 
between the two cities.

Return the count of all possible routes from the starting city `start` to the destination city `finish`. 
Since the answer may be too large, return it modulo `10^9 + 7`.

Constraints:
1. 2 <= locations.length <= 100
2. 1 <= locations[i] <= 10^9
3. All integers in `locations` are distinct.
4. 0 <= start, finish < locations.length
5. 0 <= fuel <= 200

"""

# Python Solution
from functools import lru_cache

def countRoutes(locations, start, finish, fuel):
    MOD = 10**9 + 7

    @lru_cache(None)
    def dfs(city, remaining_fuel):
        # If we run out of fuel, no routes are possible
        if remaining_fuel < 0:
            return 0
        
        # Start with 1 if we are at the destination city
        routes = 1 if city == finish else 0
        
        # Try moving to all other cities
        for next_city in range(len(locations)):
            if next_city != city:
                cost = abs(locations[city] - locations[next_city])
                if remaining_fuel >= cost:
                    routes += dfs(next_city, remaining_fuel - cost)
                    routes %= MOD
        
        return routes

    return dfs(start, fuel)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    locations = [2, 3, 6, 8, 4]
    start = 1
    finish = 3
    fuel = 5
    print(countRoutes(locations, start, finish, fuel))  # Output: 4

    # Test Case 2
    locations = [4, 3, 1]
    start = 1
    finish = 0
    fuel = 6
    print(countRoutes(locations, start, finish, fuel))  # Output: 5

    # Test Case 3
    locations = [5, 2, 1]
    start = 0
    finish = 2
    fuel = 3
    print(countRoutes(locations, start, finish, fuel))  # Output: 0

    # Test Case 4
    locations = [1, 2, 3]
    start = 0
    finish = 2
    fuel = 40
    print(countRoutes(locations, start, finish, fuel))  # Output: 615

"""
Time and Space Complexity Analysis:

Time Complexity:
- Let `n` be the number of cities (length of `locations`) and `f` be the amount of fuel.
- The `dfs` function is called for each combination of city and remaining fuel, resulting in O(n * f) states.
- For each state, we iterate over all `n` cities, leading to a total time complexity of O(n^2 * f).

Space Complexity:
- The space complexity is O(n * f) due to the memoization table used by `lru_cache`.
- Additionally, the recursion stack can go up to O(n) in the worst case.

Overall:
Time Complexity: O(n^2 * f)
Space Complexity: O(n * f)

Topic: Dynamic Programming (DP)
"""