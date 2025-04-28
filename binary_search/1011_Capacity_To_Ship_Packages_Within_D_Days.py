"""
LeetCode Problem #1011: Capacity To Ship Packages Within D Days

Problem Statement:
A conveyor belt has packages that must be shipped from one port to another within `D` days.

The `i-th` package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages in the order given by `weights`. We may not load more weight than the ship's capacity.

Return the least weight capacity of the ship that will result in all the packages being shipped within `D` days.

Constraints:
- 1 <= len(weights) <= 5 * 10^4
- 1 <= weights[i] <= 500
- 1 <= D <= len(weights)
"""

def shipWithinDays(weights, D):
    """
    Finds the minimum ship capacity to ship all packages within D days.

    :param weights: List[int] - List of package weights
    :param D: int - Number of days to ship all packages
    :return: int - Minimum ship capacity
    """
    def canShip(capacity):
        days = 1
        current_weight = 0
        for weight in weights:
            if current_weight + weight > capacity:
                days += 1
                current_weight = 0
            current_weight += weight
            if days > D:
                return False
        return True

    left, right = max(weights), sum(weights)
    while left < right:
        mid = (left + right) // 2
        if canShip(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    weights1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    D1 = 5
    print(shipWithinDays(weights1, D1))  # Expected Output: 15

    # Test Case 2
    weights2 = [3, 2, 2, 4, 1, 4]
    D2 = 3
    print(shipWithinDays(weights2, D2))  # Expected Output: 6

    # Test Case 3
    weights3 = [1, 2, 3, 1, 1]
    D3 = 4
    print(shipWithinDays(weights3, D3))  # Expected Output: 3

"""
Time Complexity Analysis:
- The binary search runs in O(log(sum(weights) - max(weights))).
- The `canShip` function iterates through the `weights` array, which takes O(n).
- Therefore, the overall time complexity is O(n * log(sum(weights) - max(weights))).

Space Complexity Analysis:
- The algorithm uses O(1) additional space since it only uses a few variables for computation.

Topic: Binary Search
"""