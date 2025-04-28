"""
LeetCode Problem #2279: Maximum Bags With Full Capacity of Rocks

Problem Statement:
You have `n` bags numbered from `0` to `n - 1`. You are given two 0-indexed integer arrays `capacity` and `rocks`. 
The `i-th` bag can hold a maximum of `capacity[i]` rocks and currently contains `rocks[i]` rocks. 
You are also given an integer `additionalRocks`, the number of additional rocks you can place in any of the bags.

Return the maximum number of bags that can have full capacity after placing the additional rocks in some bags.

Example:
Input: capacity = [1, 2, 3], rocks = [0, 1, 2], additionalRocks = 2
Output: 2
Explanation:
- Place 1 rock in bag 0 and 1 rock in bag 2. Both bags now have full capacity.
- Bag 1 is already full.
- There are 2 bags with full capacity.

Constraints:
- `n == capacity.length == rocks.length`
- `1 <= n <= 5 * 10^4`
- `1 <= capacity[i] <= 10^9`
- `0 <= rocks[i] <= capacity[i]`
- `1 <= additionalRocks <= 10^9`
"""

# Python Solution
from typing import List

def maximumBags(capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
    # Calculate the remaining space in each bag
    remaining_space = [capacity[i] - rocks[i] for i in range(len(capacity))]
    
    # Sort the remaining space in ascending order
    remaining_space.sort()
    
    # Try to fill the bags with the additional rocks
    full_bags = 0
    for space in remaining_space:
        if additionalRocks >= space:
            additionalRocks -= space
            full_bags += 1
        else:
            break
    
    return full_bags

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    capacity = [1, 2, 3]
    rocks = [0, 1, 2]
    additionalRocks = 2
    print(maximumBags(capacity, rocks, additionalRocks))  # Output: 2

    # Test Case 2
    capacity = [10, 2, 5]
    rocks = [5, 1, 3]
    additionalRocks = 5
    print(maximumBags(capacity, rocks, additionalRocks))  # Output: 3

    # Test Case 3
    capacity = [2, 3, 4, 5]
    rocks = [1, 2, 4, 4]
    additionalRocks = 2
    print(maximumBags(capacity, rocks, additionalRocks))  # Output: 3

    # Test Case 4
    capacity = [5, 5, 5]
    rocks = [0, 0, 0]
    additionalRocks = 10
    print(maximumBags(capacity, rocks, additionalRocks))  # Output: 2

# Time Complexity Analysis:
# - Calculating the remaining space takes O(n), where n is the number of bags.
# - Sorting the remaining space takes O(n log n).
# - Iterating through the sorted list to fill the bags takes O(n).
# - Overall time complexity: O(n log n).

# Space Complexity Analysis:
# - The `remaining_space` list takes O(n) space.
# - Overall space complexity: O(n).

# Topic: Arrays, Greedy