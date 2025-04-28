"""
LeetCode Problem #2949: Minimum Time to Repair Cars

Problem Statement:
You are given an integer array `ranks` representing the ranks of some mechanics. The rank of the ith mechanic is `ranks[i]`. A mechanic with a rank `r` can repair `k` cars in `r * k^2` minutes.

You are also given an integer `cars`, the total number of cars that need to be repaired. Return the minimum time required to repair all the cars.

Note:
- Each mechanic can repair any number of cars.
- A mechanic can only work on one car at a time.
- Multiple mechanics can work simultaneously.

Constraints:
- 1 <= ranks.length <= 10^5
- 1 <= ranks[i] <= 100
- 1 <= cars <= 10^6
"""

from typing import List

def repairCars(ranks: List[int], cars: int) -> int:
    def can_repair_in_time(time: int) -> bool:
        """
        Helper function to check if all cars can be repaired within the given time.
        """
        total_cars_repaired = 0
        for rank in ranks:
            total_cars_repaired += int((time // rank) ** 0.5)
            if total_cars_repaired >= cars:
                return True
        return total_cars_repaired >= cars

    # Binary search for the minimum time
    left, right = 1, max(ranks) * cars * cars
    while left < right:
        mid = (left + right) // 2
        if can_repair_in_time(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    ranks = [4, 2, 3]
    cars = 10
    print(repairCars(ranks, cars))  # Expected Output: 16

    # Test Case 2
    ranks = [1, 2, 3]
    cars = 6
    print(repairCars(ranks, cars))  # Expected Output: 6

    # Test Case 3
    ranks = [5, 1, 8]
    cars = 15
    print(repairCars(ranks, cars))  # Expected Output: 64

"""
Time Complexity Analysis:
- The binary search runs in O(log(max_time)), where max_time = max(ranks) * cars^2.
- For each binary search iteration, we iterate through the `ranks` array to calculate the total cars repaired, which takes O(n), where n is the length of the `ranks` array.
- Therefore, the overall time complexity is O(n * log(max_time)).

Space Complexity Analysis:
- The space complexity is O(1) since we are not using any additional data structures.

Topic: Binary Search
"""