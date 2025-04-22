"""
LeetCode Question #739: Daily Temperatures

Problem Statement:
Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the i-th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

Example:
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
"""

# Python Solution
def dailyTemperatures(temperatures):
    """
    This function calculates the number of days to wait for a warmer temperature.

    :param temperatures: List[int] - List of daily temperatures
    :return: List[int] - List of days to wait for a warmer temperature
    """
    n = len(temperatures)
    answer = [0] * n
    stack = []  # Stack to store indices of temperatures

    for i in range(n):
        # While the stack is not empty and the current temperature is greater than the temperature
        # at the index stored at the top of the stack
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        stack.append(i)

    return answer

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(temperatures1))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]

    # Test Case 2
    temperatures2 = [30, 40, 50, 60]
    print(dailyTemperatures(temperatures2))  # Output: [1, 1, 1, 0]

    # Test Case 3
    temperatures3 = [30, 60, 90]
    print(dailyTemperatures(temperatures3))  # Output: [1, 1, 0]

    # Test Case 4
    temperatures4 = [90, 80, 70, 60]
    print(dailyTemperatures(temperatures4))  # Output: [0, 0, 0, 0]

    # Test Case 5
    temperatures5 = [70, 71, 70, 71, 70]
    print(dailyTemperatures(temperatures5))  # Output: [1, 0, 1, 0, 0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the `temperatures` array once (O(n)).
- Each index is pushed and popped from the stack at most once, so the stack operations are O(n) in total.
- Overall time complexity: O(n).

Space Complexity:
- The `answer` array takes O(n) space.
- The stack can hold at most n indices, so it also takes O(n) space.
- Overall space complexity: O(n).
"""

# Topic: Arrays, Monotonic Stack