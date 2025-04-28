"""
LeetCode Problem #1661: Average Time of Process per Machine

Problem Statement:
You are given a list of logs where each log is represented as a tuple (machine_id, process_time). 
Each log represents the time taken by a process on a specific machine. Your task is to calculate 
the average process time for each machine and return the result as a dictionary where the keys 
are machine IDs and the values are the average process times.

Example:
Input: logs = [(1, 10), (2, 5), (1, 20), (2, 15), (3, 30)]
Output: {1: 15.0, 2: 10.0, 3: 30.0}

Constraints:
- The machine IDs are positive integers.
- The process times are positive integers.
- The input list will contain at least one log.
"""

# Solution
def average_time_per_machine(logs):
    """
    Calculate the average process time for each machine.

    Args:
    logs (List[Tuple[int, int]]): A list of tuples where each tuple contains a machine ID and process time.

    Returns:
    Dict[int, float]: A dictionary where keys are machine IDs and values are the average process times.
    """
    from collections import defaultdict

    # Dictionary to store the total process time and count for each machine
    machine_data = defaultdict(lambda: [0, 0])  # [total_time, count]

    # Iterate through the logs and update machine_data
    for machine_id, process_time in logs:
        machine_data[machine_id][0] += process_time  # Add process time
        machine_data[machine_id][1] += 1  # Increment count

    # Calculate the average process time for each machine
    result = {machine_id: total_time / count for machine_id, (total_time, count) in machine_data.items()}

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    logs1 = [(1, 10), (2, 5), (1, 20), (2, 15), (3, 30)]
    print(average_time_per_machine(logs1))  # Expected Output: {1: 15.0, 2: 10.0, 3: 30.0}

    # Test Case 2
    logs2 = [(1, 50), (1, 50), (2, 100)]
    print(average_time_per_machine(logs2))  # Expected Output: {1: 50.0, 2: 100.0}

    # Test Case 3
    logs3 = [(1, 10)]
    print(average_time_per_machine(logs3))  # Expected Output: {1: 10.0}

    # Test Case 4
    logs4 = [(1, 10), (2, 20), (3, 30), (1, 40), (2, 60), (3, 90)]
    print(average_time_per_machine(logs4))  # Expected Output: {1: 25.0, 2: 40.0, 3: 60.0}

# Time and Space Complexity Analysis
"""
Time Complexity:
- Iterating through the logs takes O(n), where n is the number of logs.
- Calculating the averages takes O(m), where m is the number of unique machine IDs.
- Overall time complexity: O(n + m).

Space Complexity:
- The space used by the machine_data dictionary is O(m), where m is the number of unique machine IDs.
- Overall space complexity: O(m).
"""

# Topic: Hash Table