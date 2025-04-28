"""
LeetCode Problem #1217: Minimum Cost to Move Chips to The Same Position

Problem Statement:
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip by:
- Moving it to position[i] + 2 or position[i] - 2 with cost = 0.
- Moving it to position[i] + 1 or position[i] - 1 with cost = 1.

Return the minimum cost needed to move all the chips to the same position.

Constraints:
- 1 <= position.length <= 100
- 1 <= position[i] <= 10^9
"""

def minCostToMoveChips(position):
    """
    Calculate the minimum cost to move all chips to the same position.

    :param position: List[int] - List of positions of the chips
    :return: int - Minimum cost to move all chips to the same position
    """
    # Count the number of chips at even and odd positions
    even_count = sum(1 for p in position if p % 2 == 0)
    odd_count = len(position) - even_count

    # The cost is the minimum of moving all chips to even or odd positions
    return min(even_count, odd_count)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    position1 = [1, 2, 3]
    print(minCostToMoveChips(position1))  # Output: 1

    # Test Case 2
    position2 = [2, 2, 2, 3, 3]
    print(minCostToMoveChips(position2))  # Output: 2

    # Test Case 3
    position3 = [1, 1000000000]
    print(minCostToMoveChips(position3))  # Output: 1

    # Test Case 4
    position4 = [1, 1, 1, 1, 1]
    print(minCostToMoveChips(position4))  # Output: 0

    # Test Case 5
    position5 = [2, 4, 6, 8, 10]
    print(minCostToMoveChips(position5))  # Output: 0

"""
Time Complexity:
- Calculating the even_count takes O(n), where n is the length of the position array.
- Calculating the odd_count is derived from the total length, so it is O(1).
- Overall, the time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""