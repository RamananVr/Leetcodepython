"""
LeetCode Problem #2110: Number of Smooth Descent Periods of a Stock

Problem Statement:
You are given an integer array `prices` representing the daily price history of a stock, where `prices[i]` is the price of the stock on the ith day.

A smooth descent period is defined as a subarray of `prices` such that:
- For every `j` in the subarray, `prices[j] - prices[j+1] = 1` (0 <= j < subarray.length - 1).

Return the total number of smooth descent periods.

A single day is also considered a smooth descent period.

Example 1:
Input: prices = [3, 2, 1, 4]
Output: 7
Explanation: There are 7 smooth descent periods:
- [3], [2], [1], [4] (single days)
- [3, 2], [2, 1] (two-day periods)
- [3, 2, 1] (three-day period)

Example 2:
Input: prices = [8, 6, 7, 7]
Output: 4
Explanation: There are 4 smooth descent periods:
- [8], [6], [7], [7] (single days)

Constraints:
- 1 <= prices.length <= 10^5
- 1 <= prices[i] <= 10^5
"""

def getDescentPeriods(prices):
    """
    Calculate the total number of smooth descent periods in the given stock prices.

    :param prices: List[int] - List of stock prices
    :return: int - Total number of smooth descent periods
    """
    n = len(prices)
    total_periods = 0
    current_length = 1  # A single day is always a smooth descent period

    for i in range(1, n):
        if prices[i - 1] - prices[i] == 1:
            current_length += 1
        else:
            current_length = 1  # Reset the length for a new descent period
        total_periods += current_length

    return total_periods

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    prices1 = [3, 2, 1, 4]
    print(getDescentPeriods(prices1))  # Output: 7

    # Test Case 2
    prices2 = [8, 6, 7, 7]
    print(getDescentPeriods(prices2))  # Output: 4

    # Test Case 3
    prices3 = [1, 2, 3, 4]
    print(getDescentPeriods(prices3))  # Output: 4

    # Test Case 4
    prices4 = [10, 9, 8, 7, 6]
    print(getDescentPeriods(prices4))  # Output: 15

    # Test Case 5
    prices5 = [5]
    print(getDescentPeriods(prices5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the `prices` array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the `prices` array.

Space Complexity:
- The algorithm uses a constant amount of extra space (variables `total_periods` and `current_length`).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""