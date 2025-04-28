"""
LeetCode Question #2594: Minimum Time to Repair Cars

Problem Statement:
You are given an integer array `ranks` representing the ranks of some mechanics. The ith mechanic has a rank `ranks[i]`, and can repair `cars` cars in `time` minutes according to the formula:
    time = cars^2 * ranks[i]
where `cars` is the number of cars the mechanic repairs and `time` is the time taken by the mechanic to repair those cars.

You are also given an integer `cars`, which represents the total number of cars that need to be repaired. Return the minimum time required to repair all the cars.

Constraints:
- 1 <= ranks.length <= 10^5
- 1 <= ranks[i] <= 100
- 1 <= cars <= 10^6
"""

# Solution
from math import isqrt

def repairCars(ranks, cars):
    def canRepairInTime(mid):
        total_cars = 0
        for rank in ranks:
            total_cars += isqrt(mid // rank)
            if total_cars >= cars:
                return True
        return total_cars >= cars

    left, right = 1, ranks[0] * cars * cars
    while left < right:
        mid = (left + right) // 2
        if canRepairInTime(mid):
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
    print(repairCars(ranks, cars))  # Expected Output: 9

    # Test Case 3
    ranks = [5, 1, 8]
    cars = 12
    print(repairCars(ranks, cars))  # Expected Output: 64

    # Test Case 4
    ranks = [10]
    cars = 5
    print(repairCars(ranks, cars))  # Expected Output: 250

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search runs in O(log(max_time)), where max_time is the maximum possible time (ranks[0] * cars^2).
- For each binary search iteration, we iterate through the ranks array to calculate the total number of cars repaired, which takes O(n), where n is the length of the ranks array.
- Therefore, the overall time complexity is O(n * log(max_time)).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures.

Topic: Binary Search
"""