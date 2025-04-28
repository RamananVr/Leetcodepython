"""
LeetCode Problem #2769: Find the Maximum Achievable Number

Problem Statement:
You are given two integers, `num` and `t`. An integer `x` is called achievable if it can be obtained by adding or subtracting `t` from `num` any number of times (including zero times). Return the maximum achievable number.

Constraints:
- `1 <= num, t <= 100`

"""

# Solution
def theMaximumAchievableX(num: int, t: int) -> int:
    """
    Calculate the maximum achievable number by adding or subtracting t from num.

    Args:
    num (int): The starting number.
    t (int): The value to add or subtract.

    Returns:
    int: The maximum achievable number.
    """
    return num + 2 * t

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num = 4
    t = 2
    print(theMaximumAchievableX(num, t))  # Expected Output: 8

    # Test Case 2
    num = 10
    t = 5
    print(theMaximumAchievableX(num, t))  # Expected Output: 20

    # Test Case 3
    num = 1
    t = 1
    print(theMaximumAchievableX(num, t))  # Expected Output: 3

    # Test Case 4
    num = 50
    t = 25
    print(theMaximumAchievableX(num, t))  # Expected Output: 100

    # Test Case 5
    num = 100
    t = 100
    print(theMaximumAchievableX(num, t))  # Expected Output: 300

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function performs a single arithmetic operation, which takes O(1) time.
- Therefore, the time complexity is O(1).

Space Complexity:
- The function uses a constant amount of space to store the input and output variables.
- Therefore, the space complexity is O(1).

Topic: Math
"""