"""
LeetCode Problem #1503: Last Moment Before All Ants Fall Out of a Plank

Problem Statement:
We have a wooden plank of length `n` units. Some ants are walking on the plank, each with a speed of 1 unit per second. Some ants are moving to the left, and some are moving to the right. When two ants meet at some point, they turn around and start moving in the opposite direction. However, we can treat this as if the ants pass through each other without changing their direction.

Given two integer arrays `left` and `right`:
- `left[i]` represents the position of an ant moving to the left.
- `right[j]` represents the position of an ant moving to the right.

Return the **last moment** when any ant is still on the plank.

Constraints:
- 1 <= n <= 10^4
- 0 <= left.length, right.length <= 10^4
- 0 <= left[i] <= n
- 0 <= right[j] <= n

Note:
- Ants moving to the left will fall off the plank at position 0.
- Ants moving to the right will fall off the plank at position `n`.
"""

# Python Solution
def getLastMoment(n: int, left: list[int], right: list[int]) -> int:
    """
    Calculate the last moment before all ants fall off the plank.

    :param n: Length of the plank
    :param left: Positions of ants moving to the left
    :param right: Positions of ants moving to the right
    :return: The last moment before all ants fall off the plank
    """
    # The last moment for ants moving left is the maximum position in `left`.
    max_left = max(left) if left else 0
    
    # The last moment for ants moving right is `n - min(right)`.
    max_right = n - min(right) if right else 0
    
    # The last moment is the maximum of the two.
    return max(max_left, max_right)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    left = [4, 3]
    right = [0, 1]
    print(getLastMoment(n, left, right))  # Expected Output: 4

    # Test Case 2
    n = 7
    left = []
    right = [0, 1, 2, 3, 4, 5, 6, 7]
    print(getLastMoment(n, left, right))  # Expected Output: 7

    # Test Case 3
    n = 9
    left = [5]
    right = [4]
    print(getLastMoment(n, left, right))  # Expected Output: 5

    # Test Case 4
    n = 10
    left = [6, 7, 8]
    right = [2, 3, 4]
    print(getLastMoment(n, left, right))  # Expected Output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating `max(left)` takes O(L), where L is the length of the `left` array.
- Calculating `min(right)` takes O(R), where R is the length of the `right` array.
- Overall, the time complexity is O(L + R).

Space Complexity:
- The solution uses O(1) additional space, as we are only storing a few variables.
- The input arrays `left` and `right` are not modified, so no extra space is used.

Topic: Arrays
"""