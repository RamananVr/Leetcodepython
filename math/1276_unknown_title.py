"""
LeetCode Problem #1276: Number of Burgers with No Waste of Ingredients

Problem Statement:
Given two integers `tomatoSlices` and `cheeseSlices`, return a list `[jumbo, small]` where:
- `jumbo` is the number of jumbo burgers.
- `small` is the number of small burgers.

Jumbo burgers require 4 tomato slices and 1 cheese slice.
Small burgers require 2 tomato slices and 1 cheese slice.

You need to use all the tomato slices and cheese slices without any waste. If there is no solution, return an empty list.

Constraints:
- 0 <= tomatoSlices, cheeseSlices <= 10^7
"""

def numOfBurgers(tomatoSlices: int, cheeseSlices: int) -> list[int]:
    """
    Calculate the number of jumbo and small burgers that can be made without waste.

    Args:
    tomatoSlices (int): Number of tomato slices available.
    cheeseSlices (int): Number of cheese slices available.

    Returns:
    list[int]: A list containing the number of jumbo and small burgers [jumbo, small].
               Returns an empty list if no solution exists.
    """
    # Jumbo burgers require 4 tomato slices and 1 cheese slice.
    # Small burgers require 2 tomato slices and 1 cheese slice.
    # Let jumbo = x and small = y.
    # We have two equations:
    # 4x + 2y = tomatoSlices
    # x + y = cheeseSlices

    # Solving the equations:
    # From the second equation: y = cheeseSlices - x
    # Substitute into the first equation:
    # 4x + 2(cheeseSlices - x) = tomatoSlices
    # 4x + 2cheeseSlices - 2x = tomatoSlices
    # 2x = tomatoSlices - 2cheeseSlices
    # x = (tomatoSlices - 2 * cheeseSlices) / 2

    # Calculate jumbo burgers (x)
    jumbo = (tomatoSlices - 2 * cheeseSlices) // 2

    # Calculate small burgers (y)
    small = cheeseSlices - jumbo

    # Check if the solution is valid
    if jumbo < 0 or small < 0 or 4 * jumbo + 2 * small != tomatoSlices or jumbo + small != cheeseSlices:
        return []

    return [jumbo, small]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tomatoSlices = 16
    cheeseSlices = 7
    print(numOfBurgers(tomatoSlices, cheeseSlices))  # Output: [4, 3]

    # Test Case 2
    tomatoSlices = 17
    cheeseSlices = 4
    print(numOfBurgers(tomatoSlices, cheeseSlices))  # Output: []

    # Test Case 3
    tomatoSlices = 0
    cheeseSlices = 0
    print(numOfBurgers(tomatoSlices, cheeseSlices))  # Output: [0, 0]

    # Test Case 4
    tomatoSlices = 2
    cheeseSlices = 1
    print(numOfBurgers(tomatoSlices, cheeseSlices))  # Output: [0, 1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves simple arithmetic operations, which take O(1) time.
- Therefore, the time complexity is O(1).

Space Complexity:
- The solution uses a constant amount of space for variables and calculations.
- Therefore, the space complexity is O(1).

Topic: Math
"""