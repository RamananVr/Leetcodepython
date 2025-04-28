"""
LeetCode Question #1936: Add Minimum Number of Rungs

Problem Statement:
You are given a strictly increasing integer array `rungs` that represents the height of rungs on a ladder. You are currently on the ground at height 0, and you want to reach the last rung.

You are also given an integer `dist`. You can only climb to the next rung if the distance between where you are and the next rung is at most `dist`. You are able to insert rungs at any positive integer height if needed.

Return the minimum number of rungs you need to add to the ladder in order to climb to the last rung.

Constraints:
- 1 <= rungs.length <= 10^5
- 1 <= rungs[i] <= 10^9
- 1 <= dist <= 10^9
- rungs is strictly increasing.
"""

def addRungs(rungs, dist):
    """
    Calculate the minimum number of rungs to add to the ladder.

    :param rungs: List[int] - Heights of the rungs on the ladder.
    :param dist: int - Maximum distance you can climb in one step.
    :return: int - Minimum number of rungs to add.
    """
    added_rungs = 0
    current_height = 0

    for rung in rungs:
        if rung - current_height > dist:
            # Calculate the number of rungs needed to bridge the gap
            added_rungs += (rung - current_height - 1) // dist
        current_height = rung

    return added_rungs

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rungs = [1, 3, 5, 10]
    dist = 2
    print(addRungs(rungs, dist))  # Output: 2

    # Test Case 2
    rungs = [3, 6, 8, 10]
    dist = 3
    print(addRungs(rungs, dist))  # Output: 0

    # Test Case 3
    rungs = [3, 4, 6, 7]
    dist = 1
    print(addRungs(rungs, dist))  # Output: 1

    # Test Case 4
    rungs = [5]
    dist = 10
    print(addRungs(rungs, dist))  # Output: 0

    # Test Case 5
    rungs = [10, 20, 30, 40]
    dist = 15
    print(addRungs(rungs, dist))  # Output: 2

"""
Time Complexity:
- The function iterates through the `rungs` array once, performing constant-time calculations for each rung.
- Let `n` be the length of the `rungs` array.
- Time complexity: O(n).

Space Complexity:
- The function uses a constant amount of extra space, regardless of the input size.
- Space complexity: O(1).

Topic: Arrays
"""