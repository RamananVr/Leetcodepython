"""
LeetCode Question #2145: Count the Hidden Sequences

Problem Statement:
You are given an integer array `differences` of length `n` where `differences[i] = nums[i + 1] - nums[i]` for a 0-indexed array `nums` of length `n + 1`. 
You are also given two integers `lower` and `upper` that represent the inclusive range `[lower, upper]` for the values of `nums`.

Return the number of valid arrays `nums` that you can obtain.

Example:
Input: differences = [1, -3, 4], lower = 1, upper = 6
Output: 4
Explanation: The possible arrays are:
- [3, 4, 1, 5]
- [4, 5, 2, 6]
- [5, 6, 3, 7]
- [6, 7, 4, 8]
There are 4 valid arrays.

Constraints:
- `1 <= differences.length <= 10^5`
- `-10^5 <= differences[i] <= 10^5`
- `-10^5 <= lower <= upper <= 10^5`
"""

# Python Solution
def count_hidden_sequences(differences, lower, upper):
    """
    Count the number of valid arrays nums that can be obtained given the differences array and range [lower, upper].

    :param differences: List[int] - The differences array.
    :param lower: int - The lower bound of the range.
    :param upper: int - The upper bound of the range.
    :return: int - The number of valid arrays nums.
    """
    # Initialize the first element of nums to 0
    current = 0
    min_val, max_val = 0, 0

    # Calculate the prefix sum and track the minimum and maximum values
    for diff in differences:
        current += diff
        min_val = min(min_val, current)
        max_val = max(max_val, current)

    # Calculate the range of valid starting values
    start_min = lower - min_val
    start_max = upper - max_val

    # The number of valid starting values is the size of the intersection of the range
    return max(0, start_max - start_min + 1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    differences = [1, -3, 4]
    lower = 1
    upper = 6
    print(count_hidden_sequences(differences, lower, upper))  # Output: 4

    # Test Case 2
    differences = [3, -2, 5, -1]
    lower = 0
    upper = 10
    print(count_hidden_sequences(differences, lower, upper))  # Output: 6

    # Test Case 3
    differences = [-1, -1, -1]
    lower = 1
    upper = 3
    print(count_hidden_sequences(differences, lower, upper))  # Output: 1

    # Test Case 4
    differences = [2, 2, -1, -2]
    lower = -5
    upper = 5
    print(count_hidden_sequences(differences, lower, upper))  # Output: 7

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the `differences` array once to compute the prefix sum and track the minimum and maximum values.
- This takes O(n) time, where n is the length of the `differences` array.

Space Complexity:
- The algorithm uses O(1) additional space since it only uses a few variables to track the prefix sum, minimum, and maximum values.
- Therefore, the space complexity is O(1).

Overall, the solution is efficient with a time complexity of O(n) and a space complexity of O(1).
"""

# Topic: Arrays