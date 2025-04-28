"""
LeetCode Problem #2403: Minimum Time to Kill All Monsters

Problem Statement:
You are given an array `monsters` where `monsters[i]` represents the health of the i-th monster. 
You are also given an integer `damage` which represents the amount of health you can reduce from a monster in one attack.

Your task is to determine the minimum time required to kill all the monsters. You can attack any monster in any order, 
but you must completely kill one monster before moving to the next. The time required to kill a monster is equal to 
the ceiling of its health divided by `damage`.

Return the total minimum time required to kill all the monsters.

Constraints:
- 1 <= monsters.length <= 10^5
- 1 <= monsters[i] <= 10^9
- 1 <= damage <= 10^9
"""

# Solution
import math
from typing import List

def minimumTimeToKillMonsters(monsters: List[int], damage: int) -> int:
    """
    Calculate the minimum time required to kill all monsters.

    Args:
    monsters (List[int]): List of health values of monsters.
    damage (int): Damage dealt per attack.

    Returns:
    int: Minimum time required to kill all monsters.
    """
    total_time = 0
    for health in monsters:
        total_time += math.ceil(health / damage)
    return total_time

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    monsters = [10, 20, 30]
    damage = 10
    print(minimumTimeToKillMonsters(monsters, damage))  # Expected Output: 6

    # Test Case 2
    monsters = [15, 25, 35]
    damage = 10
    print(minimumTimeToKillMonsters(monsters, damage))  # Expected Output: 8

    # Test Case 3
    monsters = [1, 1, 1, 1]
    damage = 1
    print(minimumTimeToKillMonsters(monsters, damage))  # Expected Output: 4

    # Test Case 4
    monsters = [1000000000]
    damage = 1000000000
    print(minimumTimeToKillMonsters(monsters, damage))  # Expected Output: 1

    # Test Case 5
    monsters = [9, 18, 27]
    damage = 9
    print(minimumTimeToKillMonsters(monsters, damage))  # Expected Output: 6

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `monsters` list once, performing a constant-time operation (math.ceil) for each element.
- Let n be the length of the `monsters` list. The time complexity is O(n).

Space Complexity:
- The function uses a constant amount of extra space (for the `total_time` variable and the loop iterator).
- The space complexity is O(1).
"""

# Topic: Arrays