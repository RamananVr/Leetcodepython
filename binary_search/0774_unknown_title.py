"""
LeetCode Problem #774: Minimize Max Distance to Gas Station

Problem Statement:
You are given an array `stations` that represents the positions of gas stations along a highway. You are also given an integer `K`, which represents the number of additional gas stations you can add. You want to minimize the maximum distance between adjacent gas stations after adding the `K` gas stations.

Return the smallest possible value of the maximum distance between adjacent gas stations.

Example:
Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9], K = 3
Output: 0.5

Constraints:
- `stations.length >= 2`
- `1 <= stations[i] <= 10^9`
- `stations` are sorted in ascending order.
- `0 <= K <= 10^6`
- The answer should be within 10^-6 of the true value.

"""

# Solution
def minimizeMaxDistance(stations, K):
    def is_possible(mid):
        # Check if we can achieve a maximum distance of `mid` with K additional stations
        count = 0
        for i in range(len(stations) - 1):
            distance = stations[i + 1] - stations[i]
            count += int(distance // mid)
        return count <= K

    # Binary search for the smallest possible maximum distance
    left, right = 0, stations[-1] - stations[0]
    while right - left > 1e-6:  # Precision up to 10^-6
        mid = (left + right) / 2
        if is_possible(mid):
            right = mid
        else:
            left = mid
    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    stations = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    K = 3
    print(minimizeMaxDistance(stations, K))  # Expected Output: 0.5

    # Test Case 2
    stations = [10, 20, 30, 40]
    K = 2
    print(minimizeMaxDistance(stations, K))  # Expected Output: 10.0

    # Test Case 3
    stations = [1, 5, 10]
    K = 1
    print(minimizeMaxDistance(stations, K))  # Expected Output: 4.0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search runs for O(log((right - left) / precision)), where precision is 10^-6.
- For each binary search iteration, we iterate through the `stations` array to calculate the number of additional stations needed, which takes O(n).
- Therefore, the overall time complexity is O(n * log((right - left) / precision)).

Space Complexity:
- The space complexity is O(1) since we are only using a few variables for calculations.

Topic: Binary Search
"""