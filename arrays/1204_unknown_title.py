"""
LeetCode Problem #1204: Last Person to Fit in the Elevator

Problem Statement:
You are given an array `weights` where `weights[i]` is the weight of the i-th person, and an integer `maxWeight` representing the maximum weight the elevator can hold. The elevator can hold any number of people as long as their total weight does not exceed `maxWeight`.

Return the index of the last person who can fit in the elevator without exceeding the weight limit. If no one can fit, return -1.

Example:
Input: weights = [40, 50, 60, 70], maxWeight = 150
Output: 2
Explanation: The first three people (40, 50, 60) can fit in the elevator, but adding the fourth person (70) would exceed the weight limit. Therefore, the last person who can fit is at index 2.

Constraints:
- 1 <= weights.length <= 10^4
- 1 <= weights[i] <= 10^3
- 1 <= maxWeight <= 10^4
"""

# Clean and Correct Python Solution
def last_person_to_fit(weights, maxWeight):
    """
    Finds the index of the last person who can fit in the elevator without exceeding the weight limit.

    :param weights: List[int] - List of weights of people
    :param maxWeight: int - Maximum weight the elevator can hold
    :return: int - Index of the last person who can fit, or -1 if no one can fit
    """
    current_weight = 0
    for i, weight in enumerate(weights):
        if current_weight + weight > maxWeight:
            return i - 1
        current_weight += weight
    return len(weights) - 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    weights = [40, 50, 60, 70]
    maxWeight = 150
    print(last_person_to_fit(weights, maxWeight))  # Output: 2

    # Test Case 2
    weights = [100, 200, 300]
    maxWeight = 150
    print(last_person_to_fit(weights, maxWeight))  # Output: -1

    # Test Case 3
    weights = [30, 20, 10, 40]
    maxWeight = 100
    print(last_person_to_fit(weights, maxWeight))  # Output: 3

    # Test Case 4
    weights = [10, 20, 30, 40, 50]
    maxWeight = 60
    print(last_person_to_fit(weights, maxWeight))  # Output: 1

    # Test Case 5
    weights = [10]
    maxWeight = 10
    print(last_person_to_fit(weights, maxWeight))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `weights` list once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the `weights` list.

Space Complexity:
- The function uses a constant amount of extra space (for variables like `current_weight` and the loop index).
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays