"""
LeetCode Problem #1767: Find the Subtasks That Did Not Execute

Problem Statement:
You are given a table `Tasks` with the following structure:

| Column Name | Type    |
|-------------|---------|
| task_id     | int     |
| subtasks    | varchar |

The `task_id` column is the primary key for this table. Each row in the table represents a task, and the `subtasks` column contains a comma-separated list of subtasks that are part of the task.

You are also given a table `Execution` with the following structure:

| Column Name | Type    |
|-------------|---------|
| task_id     | int     |
| subtask     | varchar |

The `task_id` column is a foreign key referencing the `task_id` column in the `Tasks` table. Each row in the table represents a subtask that was executed.

Write an SQL query to find all the subtasks that did not execute for each task. Return the result table in any order.

The result table should have the following structure:

| Column Name | Type    |
|-------------|---------|
| task_id     | int     |
| subtask     | varchar |

Example:
Input:
Tasks table:
| task_id | subtasks       |
|---------|----------------|
| 1       | "a,b,c"        |
| 2       | "d,e,f"        |

Execution table:
| task_id | subtask        |
|---------|----------------|
| 1       | "a"            |
| 1       | "b"            |
| 2       | "d"            |

Output:
| task_id | subtask        |
|---------|----------------|
| 1       | "c"            |
| 2       | "e"            |
| 2       | "f"            |

Explanation:
For task_id = 1, subtasks are "a", "b", "c". Subtasks "a" and "b" were executed, so "c" did not execute.
For task_id = 2, subtasks are "d", "e", "f". Subtask "d" was executed, so "e" and "f" did not execute.

Note:
- The subtasks column in the `Tasks` table is a comma-separated list of subtasks.
"""

# Python Solution
def find_unexecuted_subtasks(tasks, execution):
    """
    Finds the subtasks that did not execute for each task.

    Args:
    tasks (List[Dict]): A list of dictionaries representing the Tasks table.
                        Each dictionary has keys 'task_id' and 'subtasks'.
    execution (List[Dict]): A list of dictionaries representing the Execution table.
                            Each dictionary has keys 'task_id' and 'subtask'.

    Returns:
    List[Dict]: A list of dictionaries representing the result table.
                Each dictionary has keys 'task_id' and 'subtask'.
    """
    # Step 1: Parse the subtasks column into individual subtasks
    task_subtasks = {}
    for task in tasks:
        task_id = task['task_id']
        subtasks = task['subtasks'].split(',')
        task_subtasks[task_id] = set(subtasks)

    # Step 2: Track executed subtasks
    executed_subtasks = {}
    for exec in execution:
        task_id = exec['task_id']
        subtask = exec['subtask']
        if task_id not in executed_subtasks:
            executed_subtasks[task_id] = set()
        executed_subtasks[task_id].add(subtask)

    # Step 3: Find unexecuted subtasks
    result = []
    for task_id, subtasks in task_subtasks.items():
        executed = executed_subtasks.get(task_id, set())
        unexecuted = subtasks - executed
        for subtask in unexecuted:
            result.append({'task_id': task_id, 'subtask': subtask})

    return result

# Example Test Cases
if __name__ == "__main__":
    tasks = [
        {'task_id': 1, 'subtasks': "a,b,c"},
        {'task_id': 2, 'subtasks': "d,e,f"}
    ]
    execution = [
        {'task_id': 1, 'subtask': "a"},
        {'task_id': 1, 'subtask': "b"},
        {'task_id': 2, 'subtask': "d"}
    ]

    # Expected Output:
    # [{'task_id': 1, 'subtask': 'c'}, {'task_id': 2, 'subtask': 'e'}, {'task_id': 2, 'subtask': 'f'}]
    print(find_unexecuted_subtasks(tasks, execution))

"""
Time and Space Complexity Analysis:

Time Complexity:
- Parsing the subtasks column: O(n), where n is the number of rows in the `Tasks` table.
- Tracking executed subtasks: O(m), where m is the number of rows in the `Execution` table.
- Finding unexecuted subtasks: O(n * k), where k is the average number of subtasks per task.
Overall: O(n * k + m)

Space Complexity:
- Storage for `task_subtasks`: O(n * k), where k is the average number of subtasks per task.
- Storage for `executed_subtasks`: O(m).
Overall: O(n * k + m)

Topic: Hash Table
"""