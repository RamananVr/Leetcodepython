"""
LeetCode Problem #621: Task Scheduler

Problem Statement:
You are given a char array `tasks` representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer `n` that represents the cooldown period between two same tasks (the same task can only be executed again after at least `n` units of time have passed).

Return the least number of units of times that the CPU will take to finish all the given tasks.

Constraints:
- `1 <= tasks.length <= 10^4`
- `tasks[i]` is an uppercase English letter.
- The integer `n` is in the range `[0, 100]`.
"""

from collections import Counter

def leastInterval(tasks, n):
    """
    Calculate the minimum time required to complete all tasks with a cooldown period.

    :param tasks: List[str] - List of tasks represented as uppercase English letters.
    :param n: int - Cooldown period between two same tasks.
    :return: int - Minimum time required to complete all tasks.
    """
    # Count the frequency of each task
    task_counts = Counter(tasks)
    max_freq = max(task_counts.values())
    
    # Count how many tasks have the maximum frequency
    max_freq_count = sum(1 for count in task_counts.values() if count == max_freq)
    
    # Calculate the minimum time using the formula
    part_count = max_freq - 1
    part_length = n - (max_freq_count - 1)
    empty_slots = part_count * part_length
    available_tasks = len(tasks) - max_freq * max_freq_count
    idles = max(0, empty_slots - available_tasks)
    
    return len(tasks) + idles

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tasks1 = ["A", "A", "A", "B", "B", "B"]
    n1 = 2
    print(leastInterval(tasks1, n1))  # Expected Output: 8

    # Test Case 2
    tasks2 = ["A", "A", "A", "B", "B", "B"]
    n2 = 0
    print(leastInterval(tasks2, n2))  # Expected Output: 6

    # Test Case 3
    tasks3 = ["A", "A", "A", "B", "B", "B", "C", "C", "D", "D", "E", "E"]
    n3 = 2
    print(leastInterval(tasks3, n3))  # Expected Output: 12

    # Test Case 4
    tasks4 = ["A", "A", "A", "A", "B", "B", "C", "C"]
    n4 = 3
    print(leastInterval(tasks4, n4))  # Expected Output: 10

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of tasks takes O(tasks.length).
- Calculating the maximum frequency and its count takes O(26) since there are at most 26 unique tasks (uppercase English letters).
- Overall, the time complexity is O(tasks.length).

Space Complexity:
- The space complexity is O(1) for the Counter since there are at most 26 unique tasks.

Topic: Greedy
"""