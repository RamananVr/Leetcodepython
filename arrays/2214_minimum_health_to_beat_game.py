"""
LeetCode Question #2214: Minimum Health to Beat Game

Problem Statement:
You are playing a game where you have to defeat n enemies in a row. Each enemy has a certain attack power represented by an integer array `damage`. 
You also have a shield that can block the attack of exactly one enemy. The shield can only be used once during the game.

Write a function `minimumHealth(damage: List[int], armor: int) -> int` that calculates the minimum health you need to start with to defeat all the enemies.

The function should return the minimum health required such that you can defeat all the enemies without dying. You can use the shield to block the attack of one enemy, reducing its damage by `armor`. If the enemy's attack power is less than or equal to `armor`, the shield will block all of its damage.

Constraints:
- `1 <= damage.length <= 10^5`
- `0 <= damage[i] <= 10^5`
- `0 <= armor <= 10^5`
"""

from typing import List

def minimumHealth(damage: List[int], armor: int) -> int:
    """
    Calculate the minimum health required to defeat all enemies.

    :param damage: List[int] - Attack power of each enemy.
    :param armor: int - Shield's blocking power.
    :return: int - Minimum health required to defeat all enemies.
    """
    # Total damage without using the shield
    total_damage = sum(damage)
    
    # Find the maximum damage from a single enemy
    max_damage = max(damage)
    
    # Use the shield to block the maximum damage, reducing it by armor
    shield_effect = min(max_damage, armor)
    
    # Minimum health required is total damage minus shield effect plus 1 (to survive)
    return total_damage - shield_effect + 1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    damage = [2, 7, 4, 3]
    armor = 5
    print(minimumHealth(damage, armor))  # Expected Output: 12

    # Test Case 2
    damage = [10, 20, 30]
    armor = 15
    print(minimumHealth(damage, armor))  # Expected Output: 46

    # Test Case 3
    damage = [1, 1, 1, 1]
    armor = 0
    print(minimumHealth(damage, armor))  # Expected Output: 5

    # Test Case 4
    damage = [100, 200, 300]
    armor = 250
    print(minimumHealth(damage, armor))  # Expected Output: 351

    # Test Case 5
    damage = [5]
    armor = 10
    print(minimumHealth(damage, armor))  # Expected Output: 1


"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the sum of the `damage` array takes O(n), where n is the length of the array.
- Finding the maximum value in the `damage` array also takes O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The function uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""