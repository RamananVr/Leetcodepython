"""
LeetCode Problem #2991: Minimum Rounds to Complete All Tasks

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
        
        # Calculate the minimum rounds for the current task difficulty
        # Use integer division and modulo to determine the number of 3-task and 2-task rounds
        total_rounds += count // 3
        if count % 3 != 0:
            total_rounds += 1
    
    return total_rounds

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Example from the problem statement
    tasks1 = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
    print(minimumRounds(tasks1))  # Output: 4

    # Test Case 2: All tasks can be grouped into 3-task rounds
    tasks2 = [1, 1, 1, 1, 1, 1]
    print(minimumRounds(tasks2))  # Output: 2

    # Test Case 3: A task appears only once, making it impossible
    tasks3 = [1, 2, 2]
    print(minimumRounds(tasks3))  # Output: -1

    # Test Case 4: Mixed grouping of 2-task and 3-task rounds
    tasks4 = [5, 5, 5, 5, 5, 5, 5]
    print(minimumRounds(tasks4))  # Output: 3

    # Test Case 5: Single task type with a count of 2
    tasks5 = [7, 7]
    print(minimumRounds(tasks5))  # Output: 1

"""
Time Complexity Analysis:
- Counting the frequency of tasks using `Counter` takes O(n), where n is the length of the `tasks` array.
- Iterating through the unique task difficulties and calculating the rounds takes O(k), where k is the number of unique task difficulties.
- In the worst case, k = n (all tasks have unique difficulties), so the overall time complexity is O(n).

Space Complexity Analysis:
- The `Counter` object stores the frequency of each task difficulty, which requires O(k) space, where k is the number of unique task difficulties.
- In the worst case, k = n, so the space complexity is O(n).

Topic: Greedy Algorithm
"""