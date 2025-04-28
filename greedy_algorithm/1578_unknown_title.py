"""
LeetCode Problem #1578: Minimum Time to Make Rope Colorful

Problem Statement:
Alice has `n` balloons arranged on a rope. You are given a string `colors` where `colors[i]` is the color of the `i-th` balloon. 
Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. 
Bob can remove some balloons from the rope to make it colorful. The cost of removing the `i-th` balloon is given by an integer array `neededTime` 
where `neededTime[i]` is the time (in seconds) needed to remove the `i-th` balloon.

Return the minimum time Bob needs to make the rope colorful.

Constraints:
- `n == colors.length == neededTime.length`
- `1 <= n <= 10^5`
- `1 <= neededTime[i] <= 10^4`
- `colors` contains only lowercase English letters.
"""

# Solution
def minCost(colors: str, neededTime: list[int]) -> int:
    """
    This function calculates the minimum time required to make the rope colorful.
    """
    n = len(colors)
    total_time = 0
    i = 0

    while i < n:
        # Group balloons with the same color
        max_time = 0
        group_sum = 0
        while i < n - 1 and colors[i] == colors[i + 1]:
            group_sum += neededTime[i]
            max_time = max(max_time, neededTime[i])
            i += 1
        # Add the last balloon in the group
        group_sum += neededTime[i]
        max_time = max(max_time, neededTime[i])
        # Remove all but the most expensive balloon in the group
        total_time += group_sum - max_time
        i += 1

    return total_time

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    colors = "abaac"
    neededTime = [1, 2, 3, 4, 5]
    print(minCost(colors, neededTime))  # Output: 3

    # Test Case 2
    colors = "abc"
    neededTime = [1, 2, 3]
    print(minCost(colors, neededTime))  # Output: 0

    # Test Case 3
    colors = "aabaa"
    neededTime = [1, 2, 3, 4, 1]
    print(minCost(colors, neededTime))  # Output: 2

    # Test Case 4
    colors = "aaabbb"
    neededTime = [3, 5, 10, 7, 5, 3]
    print(minCost(colors, neededTime))  # Output: 15

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the `colors` string once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the `colors` string.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables like `total_time`, `max_time`, and `group_sum`.
- Therefore, the space complexity is O(1).
"""

# Topic: Greedy Algorithm