"""
LeetCode Problem #2237: Count Positions on Street With Required Brightness

Problem Statement:
A street is represented as an array `lights` of length `n`, where `lights[i]` represents the brightness of the street at position `i`. 
You are given an integer `required_brightness`, which represents the minimum brightness required at each position on the street.

Your task is to count the number of positions on the street that meet or exceed the required brightness.

Write a function `count_positions_with_brightness(lights: List[int], required_brightness: int) -> int` that returns the count of positions 
on the street that meet or exceed the required brightness.

Constraints:
- 1 <= n <= 10^5
- 0 <= lights[i] <= 10^9
- 0 <= required_brightness <= 10^9
"""

from typing import List

def count_positions_with_brightness(lights: List[int], required_brightness: int) -> int:
    """
    Counts the number of positions on the street that meet or exceed the required brightness.

    Args:
    lights (List[int]): List of integers representing the brightness at each position on the street.
    required_brightness (int): Minimum brightness required at each position.

    Returns:
    int: Count of positions meeting or exceeding the required brightness.
    """
    return sum(1 for brightness in lights if brightness >= required_brightness)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    lights = [1, 2, 3, 4, 5]
    required_brightness = 3
    print(count_positions_with_brightness(lights, required_brightness))  # Output: 3

    # Test Case 2
    lights = [10, 20, 30, 40, 50]
    required_brightness = 25
    print(count_positions_with_brightness(lights, required_brightness))  # Output: 3

    # Test Case 3
    lights = [0, 0, 0, 0, 0]
    required_brightness = 1
    print(count_positions_with_brightness(lights, required_brightness))  # Output: 0

    # Test Case 4
    lights = [100, 200, 300, 400, 500]
    required_brightness = 100
    print(count_positions_with_brightness(lights, required_brightness))  # Output: 5

    # Test Case 5
    lights = [5, 5, 5, 5, 5]
    required_brightness = 5
    print(count_positions_with_brightness(lights, required_brightness))  # Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the `lights` list once, performing a comparison for each element.
- Therefore, the time complexity is O(n), where n is the length of the `lights` list.

Space Complexity:
- The function uses a generator expression to count the positions, which does not require additional space proportional to the input size.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""