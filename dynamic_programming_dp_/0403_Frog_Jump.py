"""
LeetCode Problem #403: Frog Jump

Problem Statement:
A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. 
The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in sorted ascending order), where `stones[i]` represents the position of the ith stone, 
determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes 
the first jump must be 1 unit.

If the frog's last jump was `k` units, its next jump must be either `k - 1`, `k`, or `k + 1` units. The frog can only jump in 
the forward direction.

Return `True` if the frog can cross the river, otherwise return `False`.

Constraints:
- `2 <= stones.length <= 2000`
- `0 <= stones[i] <= 2^31 - 1`
- `stones[0] == 0`
- The stones are sorted in a strictly increasing order.
"""

def canCross(stones):
    """
    Determines if the frog can cross the river by landing on the last stone.

    :param stones: List[int] - The positions of the stones in sorted order.
    :return: bool - True if the frog can cross, False otherwise.
    """
    # Use a dictionary to store reachable positions and their possible jump sizes
    stone_positions = {stone: set() for stone in stones}
    stone_positions[0].add(0)  # The frog starts at position 0 with a jump size of 0

    for stone in stones:
        for jump in stone_positions[stone]:
            for next_jump in {jump - 1, jump, jump + 1}:
                if next_jump > 0 and stone + next_jump in stone_positions:
                    stone_positions[stone + next_jump].add(next_jump)

    # If the last stone has any reachable jumps, the frog can cross
    return bool(stone_positions[stones[-1]])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: The frog can cross
    stones1 = [0, 1, 3, 5, 6, 8, 12, 17]
    print(canCross(stones1))  # Expected output: True

    # Test Case 2: The frog cannot cross
    stones2 = [0, 1, 2, 3, 4, 8, 9, 11]
    print(canCross(stones2))  # Expected output: False

    # Test Case 3: Single jump to the last stone
    stones3 = [0, 1, 3, 6, 10, 15, 21]
    print(canCross(stones3))  # Expected output: True

    # Test Case 4: No possible jump to the last stone
    stones4 = [0, 1, 3, 6, 10, 15, 22]
    print(canCross(stones4))  # Expected output: False

"""
Time Complexity Analysis:
- Let `n` be the number of stones.
- For each stone, we iterate over all possible jump sizes stored in the dictionary. In the worst case, the number of jump sizes 
  for each stone can be proportional to `n` (though in practice, it is much smaller due to constraints on valid jumps).
- Thus, the time complexity is O(n^2).

Space Complexity Analysis:
- The space complexity is O(n^2) because we use a dictionary to store reachable positions and their possible jump sizes. 
  In the worst case, each stone can have up to `n` possible jump sizes.

Topic: Dynamic Programming (DP)
"""