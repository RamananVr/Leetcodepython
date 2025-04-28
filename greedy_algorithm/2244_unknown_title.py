"""
LeetCode Problem #2244: Minimum Rounds to Complete All Tasks

Problem Statement:
You are given a 0-indexed integer array `tasks`, where `tasks[i]` represents the difficulty level of a task. 
In each round, you can complete either:
- Exactly 2 tasks of the same difficulty level, or
- Exactly 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

Constraints:
1. 1 <= tasks.length <= 10^5
2. 1 <= tasks[i] <= 10^9
"""

from collections import Counter
from math import ceil

def minimumRounds(tasks):
    """
    Function to calculate the minimum number of rounds required to complete all tasks.

    :param tasks: List[int] - List of task difficulties
    :return: int - Minimum number of rounds required, or -1 if not possible
    """
    # Count the frequency of each task difficulty
    task_counts = Counter(tasks)
    
    # Initialize the total rounds
    total_rounds = 0
    
    # Iterate through each task difficulty and its count
    for task, count in task_counts.items():
        # If a task appears only once, it's impossible to complete it
        if count == 1:
            return -1
        
        # Calculate the minimum rounds for this task
        # Use ceil(count / 3) to determine the number of rounds
        total_rounds += ceil(count / 3)
    
    return total_rounds

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Example from the problem statement
    tasks1 = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
    print(minimumRounds(tasks1))  # Output: 4

    # Test Case 2: All tasks can be grouped into rounds of 3
    tasks2 = [1, 1, 1, 1, 1, 1]
    print(minimumRounds(tasks2))  # Output: 2

    # Test Case 3: A task appears only once, making it impossible
    tasks3 = [1, 2, 2]
    print(minimumRounds(tasks3))  # Output: -1

    # Test Case 4: Large input with multiple groupings
    tasks4 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    print(minimumRounds(tasks4))  # Output: 4

    # Test Case 5: Single task type with count divisible by 3
    tasks5 = [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print(minimumRounds(tasks5))  # Output: 3

"""
Time Complexity:
- Counting the frequencies of tasks takes O(n), where n is the length of the `tasks` array.
- Iterating through the unique task difficulties and calculating the rounds takes O(m), where m is the number of unique task difficulties.
- Overall, the time complexity is O(n + m). Since m <= n, this simplifies to O(n).

Space Complexity:
- The space complexity is O(m) due to the storage of task frequencies in the Counter object, where m is the number of unique task difficulties.

Topic: Greedy Algorithm
"""