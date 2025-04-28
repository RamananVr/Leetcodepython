"""
LeetCode Problem #1176: Diet Plan Performance

Problem Statement:
A dieter consumes calories[i] calories on the i-th day. Given an integer k, for every consecutive sequence of k days 
(calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k), they look at T, the total calories consumed 
during that sequence of k days:

- If T < lower, they lose 1 point.
- If T > upper, they gain 1 point.
- Otherwise, they earn 0 points.

Return the total number of points the dieter has after all consecutive sequences of k days have been considered.

Note:
- 1 <= k <= calories.length <= 10^5
- 0 <= calories[i] <= 20000
- 0 <= lower <= upper

Example:
Input: calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
Output: 0

Input: calories = [3,2], k = 2, lower = 0, upper = 1
Output: 1

Input: calories = [6,5,0,0], k = 2, lower = 1, upper = 5
Output: 0
"""

def dietPlanPerformance(calories, k, lower, upper):
    """
    Calculate the total points based on the diet plan performance.

    :param calories: List[int] - List of calories consumed each day.
    :param k: int - Number of consecutive days to consider.
    :param lower: int - Lower threshold for calorie sum.
    :param upper: int - Upper threshold for calorie sum.
    :return: int - Total points.
    """
    n = len(calories)
    total_points = 0
    current_window_sum = sum(calories[:k])  # Initial sum of the first window

    # Evaluate the first window
    if current_window_sum < lower:
        total_points -= 1
    elif current_window_sum > upper:
        total_points += 1

    # Slide the window across the array
    for i in range(k, n):
        current_window_sum += calories[i] - calories[i - k]  # Update the sliding window sum
        if current_window_sum < lower:
            total_points -= 1
        elif current_window_sum > upper:
            total_points += 1

    return total_points

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    calories = [1, 2, 3, 4, 5]
    k = 1
    lower = 3
    upper = 3
    print(dietPlanPerformance(calories, k, lower, upper))  # Output: 0

    # Test Case 2
    calories = [3, 2]
    k = 2
    lower = 0
    upper = 1
    print(dietPlanPerformance(calories, k, lower, upper))  # Output: 1

    # Test Case 3
    calories = [6, 5, 0, 0]
    k = 2
    lower = 1
    upper = 5
    print(dietPlanPerformance(calories, k, lower, upper))  # Output: 0

    # Test Case 4
    calories = [10, 20, 30, 40, 50]
    k = 3
    lower = 50
    upper = 100
    print(dietPlanPerformance(calories, k, lower, upper))  # Output: 1

    # Test Case 5
    calories = [5, 5, 5, 5, 5]
    k = 2
    lower = 8
    upper = 12
    print(dietPlanPerformance(calories, k, lower, upper))  # Output: 5

"""
Time Complexity:
- The algorithm processes the array in O(n) time, where n is the length of the `calories` array.
- The sliding window ensures that each element is added and removed from the window exactly once.

Space Complexity:
- The algorithm uses O(1) additional space, as it only maintains a few variables (e.g., `current_window_sum` and `total_points`).

Topic: Sliding Window
"""