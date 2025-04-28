"""
LeetCode Problem #672: Bulb Switcher II

Problem Statement:
There is a room with `n` bulbs, numbered from 1 to `n`, arranged in a row. Initially, all the bulbs are turned off. 
You are given an integer `n` and an integer `presses`, describing the number of times you are allowed to press a 
button to toggle the bulbs. There are four buttons that can be pressed:

1. Toggle all the bulbs.
2. Toggle bulbs with even indices.
3. Toggle bulbs with odd indices.
4. Toggle bulbs with indices that are multiples of 3.

You need to return the number of different possible states of the bulbs after `presses` button presses.

Constraints:
- 1 <= n <= 1000
- 0 <= presses <= 1000
"""

def bulbSwitch(n: int, presses: int) -> int:
    """
    Returns the number of different possible states of the bulbs after `presses` button presses.
    """
    if presses == 0:
        return 1  # No presses, only the initial state is possible.
    if n == 1:
        return 2  # Only one bulb, it can be either ON or OFF.
    if n == 2:
        return 3 if presses > 1 else 2  # Two bulbs, limited states based on presses.
    if presses == 1:
        return 4  # Four possible states with one press.
    if presses == 2:
        return 7  # Seven possible states with two presses.
    return 8  # Maximum of 8 states for n >= 3 and presses >= 3.

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: No presses, only the initial state is possible.
    print(bulbSwitch(3, 0))  # Expected output: 1

    # Test Case 2: One bulb, it can be either ON or OFF.
    print(bulbSwitch(1, 1))  # Expected output: 2

    # Test Case 3: Two bulbs, limited states based on presses.
    print(bulbSwitch(2, 1))  # Expected output: 2
    print(bulbSwitch(2, 2))  # Expected output: 3

    # Test Case 4: Three bulbs, maximum states depend on presses.
    print(bulbSwitch(3, 1))  # Expected output: 4
    print(bulbSwitch(3, 2))  # Expected output: 7
    print(bulbSwitch(3, 3))  # Expected output: 8

    # Test Case 5: Large number of bulbs and presses.
    print(bulbSwitch(1000, 1000))  # Expected output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution is constant time O(1) because the number of possible states is determined by the constraints 
  and does not depend on the size of `n` or `presses`.

Space Complexity:
- The solution uses O(1) space as no additional data structures are used.

Topic: Bit Manipulation / Simulation
"""