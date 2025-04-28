"""
LeetCode Problem #1375: Bulb Switcher III

Problem Statement:
There is a room with n bulbs, numbered from 1 to n, arranged in a row from left to right. Initially, all the bulbs are turned off. At moment k (for k from 0 to n - 1), you turn on the light[k] bulb. A bulb changes color to blue only if it is on and all the previous bulbs (to the left) are turned on as well. Return the number of moments in which all turned-on bulbs are blue.

Example:
Input: light = [2, 1, 3, 5, 4]
Output: 3
Explanation: 
- At moment 0: The light[0] = 2 is turned on (not blue).
- At moment 1: The light[1] = 1 is turned on (blue).
- At moment 2: The light[2] = 3 is turned on (blue).
- At moment 3: The light[3] = 5 is turned on (not blue).
- At moment 4: The light[4] = 4 is turned on (blue).
There are 3 moments when all turned-on bulbs are blue.

Constraints:
- n == light.length
- 1 <= n <= 5 * 10^4
- light is a permutation of [1, 2, ..., n]
"""

# Python Solution
def numTimesAllBlue(light):
    """
    Function to calculate the number of moments when all turned-on bulbs are blue.

    :param light: List[int] - The order in which bulbs are turned on.
    :return: int - The number of moments when all turned-on bulbs are blue.
    """
    max_on = 0
    moments = 0

    for i, bulb in enumerate(light):
        max_on = max(max_on, bulb)
        if max_on == i + 1:
            moments += 1

    return moments

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    light = [2, 1, 3, 5, 4]
    print(numTimesAllBlue(light))  # Output: 3

    # Test Case 2
    light = [3, 2, 4, 1, 5]
    print(numTimesAllBlue(light))  # Output: 2

    # Test Case 3
    light = [4, 1, 2, 3]
    print(numTimesAllBlue(light))  # Output: 1

    # Test Case 4
    light = [1, 2, 3, 4, 5]
    print(numTimesAllBlue(light))  # Output: 5

    # Test Case 5
    light = [5, 4, 3, 2, 1]
    print(numTimesAllBlue(light))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the `light` array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the `light` array.

Space Complexity:
- The algorithm uses a constant amount of extra space, as it only maintains a few variables (`max_on` and `moments`).
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays