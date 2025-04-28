"""
LeetCode Problem #2611: Mice and Cheese

Problem Statement:
There are two types of cheese, type 1 and type 2, and `n` mice. You are given two arrays, `reward1` and `reward2`, both of length `n`, where:
- `reward1[i]` is the reward for the i-th mouse if it eats type 1 cheese.
- `reward2[i]` is the reward for the i-th mouse if it eats type 2 cheese.

You are also given an integer `k`. You need to assign exactly `k` mice to eat type 1 cheese, and the remaining `n - k` mice to eat type 2 cheese. Your goal is to maximize the total reward.

Return the maximum total reward that can be achieved.

Constraints:
- `1 <= n <= 10^5`
- `0 <= reward1[i], reward2[i] <= 10^5`
- `0 <= k <= n`
"""

# Python Solution
from typing import List

def miceAndCheese(reward1: List[int], reward2: List[int], k: int) -> int:
    # Calculate the difference between reward1 and reward2 for each mouse
    differences = [(reward1[i] - reward2[i], i) for i in range(len(reward1))]
    
    # Sort the differences in descending order
    differences.sort(reverse=True, key=lambda x: x[0])
    
    # Select the top k mice for type 1 cheese
    total_reward = 0
    selected_for_type1 = set()
    for i in range(k):
        total_reward += reward1[differences[i][1]]
        selected_for_type1.add(differences[i][1])
    
    # Assign the remaining mice to type 2 cheese
    for i in range(len(reward1)):
        if i not in selected_for_type1:
            total_reward += reward2[i]
    
    return total_reward

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    reward1 = [1, 4, 4, 6]
    reward2 = [2, 3, 5, 1]
    k = 2
    print(miceAndCheese(reward1, reward2, k))  # Expected Output: 15

    # Test Case 2
    reward1 = [5, 6, 7]
    reward2 = [3, 4, 5]
    k = 1
    print(miceAndCheese(reward1, reward2, k))  # Expected Output: 16

    # Test Case 3
    reward1 = [10, 20, 30]
    reward2 = [5, 15, 25]
    k = 2
    print(miceAndCheese(reward1, reward2, k))  # Expected Output: 65

    # Test Case 4
    reward1 = [1, 1, 1]
    reward2 = [1, 1, 1]
    k = 1
    print(miceAndCheese(reward1, reward2, k))  # Expected Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the differences: O(n)
- Sorting the differences: O(n log n)
- Selecting the top k mice: O(k)
- Assigning the remaining mice: O(n)
Overall: O(n log n)

Space Complexity:
- The differences list takes O(n) space.
- The set to track selected mice takes O(k) space.
Overall: O(n)
"""

# Topic: Arrays, Greedy Algorithm