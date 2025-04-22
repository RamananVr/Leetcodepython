"""
LeetCode Question #636: Exclusive Time of Functions

Problem Statement:
You are given the number of functions `n` and a list of logs, where each log is a string with the format "{function_id}:start|end:{timestamp}". 
The logs represent the start and end times of functions running in a single-threaded CPU. Each function has a unique ID between 0 and n-1.

The CPU can only run one function at a time. When a function starts, it may interrupt another function that is currently running. 
The interrupted function will resume once the function that interrupted it finishes.

Return an array `result` of length `n` where `result[i]` is the exclusive time of the function with ID `i`. 
The exclusive time of a function is the time spent running the function itself, excluding the time spent by other functions that interrupted it.

Constraints:
- 1 <= n <= 100
- 1 <= logs.length <= 10^4
- 0 <= function_id < n
- 0 <= timestamp <= 10^9
- The input is guaranteed to be valid and the events in the logs are properly ordered.

Example:
Input: n = 2, logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
Output: [3, 4]
Explanation:
Function 0 starts at time 0 and runs for 2 units of time before being interrupted by function 1.
Function 1 runs for 4 units of time and then function 0 resumes at time 6 for 1 unit of time.

"""

# Solution
def exclusiveTime(n, logs):
    """
    Calculate the exclusive time of functions based on logs.

    :param n: int - Number of functions
    :param logs: List[str] - List of logs in the format "{function_id}:start|end:{timestamp}"
    :return: List[int] - Exclusive time of each function
    """
    result = [0] * n
    stack = []  # Stack to keep track of active functions
    prev_time = 0  # Previous timestamp

    for log in logs:
        func_id, event, timestamp = log.split(":")
        func_id, timestamp = int(func_id), int(timestamp)

        if event == "start":
            if stack:
                # Add the time spent by the function at the top of the stack
                result[stack[-1]] += timestamp - prev_time
            stack.append(func_id)
            prev_time = timestamp
        else:  # event == "end"
            # Add the time spent by the function at the top of the stack
            result[stack.pop()] += timestamp - prev_time + 1
            prev_time = timestamp + 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 2
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    print(exclusiveTime(n, logs))  # Output: [3, 4]

    # Test Case 2
    n = 1
    logs = ["0:start:0", "0:end:1"]
    print(exclusiveTime(n, logs))  # Output: [2]

    # Test Case 3
    n = 3
    logs = ["0:start:0", "1:start:2", "1:end:5", "2:start:6", "2:end:7", "0:end:8"]
    print(exclusiveTime(n, logs))  # Output: [3, 4, 2]

    # Test Case 4
    n = 2
    logs = ["0:start:0", "0:end:1", "1:start:2", "1:end:3"]
    print(exclusiveTime(n, logs))  # Output: [2, 2]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the logs once, performing constant-time operations for each log.
- Therefore, the time complexity is O(logs.length).

Space Complexity:
- The stack can hold at most n function IDs at any time, and the result array has a size of n.
- Therefore, the space complexity is O(n).
"""

# Topic: Stack