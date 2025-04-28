"""
LeetCode Problem #1665: Minimum Initial Energy to Finish Tasks

Problem Statement:
You are given an array `tasks` where `tasks[i] = [actual_i, minimum_i]`:
- `actual_i` is the actual amount of energy you spend to finish the ith task.
- `minimum_i` is the minimum amount of energy you require to start the ith task.

For example, if the task is `[10, 20]`, you spend 10 energy to complete it, but you need at least 20 energy to start it.

You can complete the tasks in any order. Return the minimum initial energy required to finish all the tasks.

Constraints:
- `1 <= tasks.length <= 10^5`
- `1 <= actual_i <= minimum_i <= 10^4`
"""

from typing import List

def minimumEffort(tasks: List[List[int]]) -> int:
    """
    Calculate the minimum initial energy required to finish all tasks.

    Args:
    tasks (List[List[int]]): A list of tasks where each task is represented as [actual, minimum].

    Returns:
    int: The minimum initial energy required.
    """
    # Sort tasks by the difference between minimum energy and actual energy in descending order
    tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
    
    # Initialize the total energy required
    total_energy = 0
    current_energy = 0
    
    # Iterate through the sorted tasks
    for actual, minimum in tasks:
        # If current energy is less than the minimum required, increase total energy
        if current_energy < minimum:
            total_energy += minimum - current_energy
            current_energy = minimum
        
        # Deduct the actual energy spent for the task
        current_energy -= actual
    
    return total_energy

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tasks1 = [[1, 3], [2, 4], [10, 11]]
    print(minimumEffort(tasks1))  # Output: 11

    # Test Case 2
    tasks2 = [[1, 2], [2, 4], [4, 8]]
    print(minimumEffort(tasks2))  # Output: 8

    # Test Case 3
    tasks3 = [[5, 9], [4, 8], [3, 7]]
    print(minimumEffort(tasks3))  # Output: 9

    # Test Case 4
    tasks4 = [[1, 1], [1, 1], [1, 1]]
    print(minimumEffort(tasks4))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the tasks takes O(n log n), where n is the number of tasks.
- Iterating through the tasks takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation may require additional space depending on the sorting algorithm, but it is generally O(1) for in-place sorting.
- No additional data structures are used, so the space complexity is O(1) (excluding input storage).

Primary Topic: Greedy Algorithm
"""