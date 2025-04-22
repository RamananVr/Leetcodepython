"""
LeetCode Problem #624: Maximum Distance in Arrays

Problem Statement:
Given m arrays, where each array is sorted in ascending order, you can pick up two integers from two different arrays (each array must contribute one integer) to form a pair. Return the maximum distance between these pairs.

The distance between two integers `a` and `b` is defined as `|a - b|`, where `|x|` denotes the absolute value of `x`.

Example:
Input: arrays = [[1,2,3], [4,5], [1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 from the first array and 5 from the second array.

Constraints:
- m == arrays.length
- 2 <= m <= 10^4
- 1 <= arrays[i].length <= 500
- -10^4 <= arrays[i][j] <= 10^4
- arrays[i] is sorted in ascending order.
"""

# Python Solution
def maxDistance(arrays):
    """
    Finds the maximum distance between integers from two different arrays.

    :param arrays: List[List[int]] - List of sorted arrays
    :return: int - Maximum distance
    """
    # Initialize variables to track the minimum and maximum values
    # from the first array
    min_val = arrays[0][0]
    max_val = arrays[0][-1]
    max_distance = 0

    # Iterate through the rest of the arrays
    for i in range(1, len(arrays)):
        # Calculate the potential maximum distance using the current array
        current_min = arrays[i][0]
        current_max = arrays[i][-1]
        max_distance = max(max_distance, abs(current_max - min_val), abs(max_val - current_min))

        # Update the global minimum and maximum values
        min_val = min(min_val, current_min)
        max_val = max(max_val, current_max)

    return max_distance

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arrays1 = [[1, 2, 3], [4, 5], [1, 2, 3]]
    print(maxDistance(arrays1))  # Output: 4

    # Test Case 2
    arrays2 = [[-10, -5, 0], [5, 10, 15], [20, 25, 30]]
    print(maxDistance(arrays2))  # Output: 40

    # Test Case 3
    arrays3 = [[1, 2], [3, 4], [5, 6]]
    print(maxDistance(arrays3))  # Output: 5

    # Test Case 4
    arrays4 = [[1, 5], [3, 8], [2, 6]]
    print(maxDistance(arrays4))  # Output: 7

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through all arrays once, performing constant-time operations for each array.
- Let m be the number of arrays. The time complexity is O(m).

Space Complexity:
- The solution uses a constant amount of extra space for variables (min_val, max_val, max_distance).
- The space complexity is O(1).
"""

# Topic: Arrays