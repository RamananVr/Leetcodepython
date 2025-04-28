"""
LeetCode Problem #2029: Stone Game IX

Problem Statement:
Alice and Bob take turns playing a game, with Alice starting first. There are n stones in a pile. Each stone has a value that is either 0, 1, or 2. On each player's turn, they can remove any stone from the pile. The game ends when there are no stones left to remove.

The score of a player is the sum of the values of the stones they have removed. The winner is the player whose score is not divisible by 3. If both players' scores are divisible by 3, the game is a draw.

Given an integer array `stones` where `stones[i]` is the value of the ith stone, return `true` if Alice wins the game, otherwise return `false`. If the game results in a draw, return `false`.

Constraints:
- 1 <= stones.length <= 10^5
- stones[i] is either 0, 1, or 2.

"""

# Solution
def stoneGameIX(stones):
    """
    Determines if Alice wins the Stone Game IX.

    :param stones: List[int] - List of stone values (0, 1, or 2).
    :return: bool - True if Alice wins, False otherwise.
    """
    count = [0, 0, 0]
    for stone in stones:
        count[stone % 3] += 1

    # Count of stones with values 0, 1, and 2 modulo 3
    zero_count, one_count, two_count = count[0], count[1], count[2]

    # If there are an even number of stones with value 0, the game depends on counts of 1 and 2
    if zero_count % 2 == 0:
        return one_count >= 1 and two_count >= 1
    else:
        return abs(one_count - two_count) > 2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    stones = [2, 1]
    print(stoneGameIX(stones))  # Output: True

    # Test Case 2
    stones = [2, 1, 1, 2]
    print(stoneGameIX(stones))  # Output: False

    # Test Case 3
    stones = [0, 0, 0]
    print(stoneGameIX(stones))  # Output: False

    # Test Case 4
    stones = [1, 1, 1, 2, 2, 2, 0, 0]
    print(stoneGameIX(stones))  # Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the `stones` array once to count the occurrences of values modulo 3.
- This takes O(n) time, where n is the length of the `stones` array.

Space Complexity:
- The solution uses a fixed-size array `count` of size 3 to store counts of stones modulo 3.
- This takes O(1) space.

Overall, the time complexity is O(n), and the space complexity is O(1).
"""

# Topic: Game Theory