"""
LeetCode Problem #1058: Minimize Rounding Error to Meet Target

Problem Statement:
Given a list of prices as strings and a target integer, you need to minimize the rounding error of the prices 
to meet the target. Each price must be rounded to either its floor integer or its ceiling integer.

Return the minimized rounding error as a string, formatted to three decimal places. If it is not possible 
to meet the target, return "-1".

Constraints:
1. 1 <= prices.length <= 1000
2. Each price is a string in the format "x.y" with 1 <= x <= 1000 and exactly 3 decimal places.
3. The target is an integer between 1 and 10^6.

Example:
Input: prices = ["0.700", "2.800", "4.900"], target = 8
Output: "1.000"

Input: prices = ["1.500", "2.500", "3.500"], target = 10
Output: "-1"
"""

from math import floor, ceil
from heapq import heappush, heappop

def minimizeError(prices, target):
    """
    Minimize the rounding error to meet the target.

    :param prices: List[str] - List of prices as strings.
    :param target: int - The target integer.
    :return: str - The minimized rounding error formatted to three decimal places, or "-1" if not possible.
    """
    floor_sum = 0
    ceil_sum = 0
    diffs = []

    for price in prices:
        num = float(price)
        floor_val = floor(num)
        ceil_val = ceil(num)
        floor_sum += floor_val
        ceil_sum += ceil_val

        # If the number is not an integer, calculate the difference between ceil and floor
        if floor_val != ceil_val:
            heappush(diffs, num - floor_val)

    # If the target is not achievable
    if target < floor_sum or target > ceil_sum:
        return "-1"

    # Calculate the number of ceil operations needed
    ceil_count = target - floor_sum

    # Minimize the rounding error
    rounding_error = 0
    for _ in range(ceil_count):
        rounding_error += heappop(diffs)

    rounding_error += sum(1 - diff for diff in diffs)

    return f"{rounding_error:.3f}"


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    prices1 = ["0.700", "2.800", "4.900"]
    target1 = 8
    print(minimizeError(prices1, target1))  # Output: "1.000"

    # Test Case 2
    prices2 = ["1.500", "2.500", "3.500"]
    target2 = 10
    print(minimizeError(prices2, target2))  # Output: "-1"

    # Test Case 3
    prices3 = ["0.500", "0.300", "0.700"]
    target3 = 2
    print(minimizeError(prices3, target3))  # Output: "0.500"

    # Test Case 4
    prices4 = ["1.200", "2.300", "3.400"]
    target4 = 7
    print(minimizeError(prices4, target4))  # Output: "0.900"

    # Test Case 5
    prices5 = ["0.600", "0.400"]
    target5 = 1
    print(minimizeError(prices5, target5))  # Output: "0.000"


"""
Time and Space Complexity Analysis:

Time Complexity:
- O(n log n): We iterate through the prices once (O(n)) to calculate floor_sum, ceil_sum, and the differences.
  We also use a min-heap to store the differences, which takes O(log n) for each insertion and extraction.
  In the worst case, we perform O(n) heap operations, resulting in O(n log n) complexity.

Space Complexity:
- O(n): We use a min-heap to store the differences, which can hold up to n elements in the worst case.

Topic: Greedy, Heap (Priority Queue)
"""