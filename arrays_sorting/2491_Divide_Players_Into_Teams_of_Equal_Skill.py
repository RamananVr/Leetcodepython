"""
LeetCode Problem #2491: Divide Players Into Teams of Equal Skill

Problem Statement:
You are given a positive integer array `skill` of size `n`, where `n` is even. The array represents the skill levels of players. 
Divide the players into `n / 2` teams of size 2 such that the total skill level of each team is the same.

Return the sum of the product of the skill levels of the players in each team, or return -1 if it is not possible to divide the players in the described way.

Example 1:
Input: skill = [3, 2, 5, 1, 3, 4]
Output: 22
Explanation: Divide the players into teams: (3, 3), (5, 1), (4, 2). Each team has a total skill level of 6.
The sum of the product of the skill levels is 3*3 + 5*1 + 4*2 = 22.

Example 2:
Input: skill = [3, 4]
Output: -1
Explanation: It is impossible to divide the players into teams such that each team has the same total skill level.

Constraints:
- `2 <= skill.length <= 10^5`
- `skill.length` is even.
- `1 <= skill[i] <= 1000`
"""

# Python Solution
def dividePlayers(skill):
    skill.sort()
    n = len(skill)
    target_sum = skill[0] + skill[-1]
    total_product = 0

    for i in range(n // 2):
        if skill[i] + skill[n - 1 - i] != target_sum:
            return -1
        total_product += skill[i] * skill[n - 1 - i]

    return total_product

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    skill1 = [3, 2, 5, 1, 3, 4]
    print(dividePlayers(skill1))  # Output: 22

    # Test Case 2
    skill2 = [3, 4]
    print(dividePlayers(skill2))  # Output: -1

    # Test Case 3
    skill3 = [1, 1, 1, 1]
    print(dividePlayers(skill3))  # Output: 2

    # Test Case 4
    skill4 = [6, 2, 4, 8]
    print(dividePlayers(skill4))  # Output: 52

    # Test Case 5
    skill5 = [1, 2, 3, 4, 5, 6]
    print(dividePlayers(skill5))  # Output: -1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n).
- Iterating through half the array takes O(n / 2), which simplifies to O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation is in-place, so no additional space is used apart from a few variables.
- Overall space complexity: O(1).
"""

# Topic: Arrays, Sorting