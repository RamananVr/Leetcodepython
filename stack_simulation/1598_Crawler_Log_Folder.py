"""
LeetCode Problem #1598: Crawler Log Folder

Problem Statement:
The LeetCode file system keeps a log of every operation performed. The operations are represented as a list of strings `logs` where:

- `"../"`: Move to the parent folder. If you are already in the main folder, remain in the same folder.
- `"./"`: Remain in the current folder.
- `"x/"`: Move to the child folder named `x`. It is guaranteed that `x` consists of lowercase English letters.

You are in the main folder initially, which is also the root folder. Return the minimum number of operations needed to go back to the main folder after performing all the operations in the `logs`.

Constraints:
- `1 <= logs.length <= 100`
- `2 <= logs[i].length <= 10`
- `logs[i]` contains `"../"`, `"./"`, or `"x/"`.

Example:
Input: logs = ["d1/", "d2/", "../", "d21/", "./"]
Output: 2

Explanation:
- Move into folder "d1".
- Move into folder "d2".
- Move back to the parent folder.
- Move into folder "d21".
- Stay in the same folder.
The minimum steps required to return to the main folder is 2.

Follow-up:
Can you solve it in O(n) time complexity?
"""

# Python Solution
def minOperations(logs):
    """
    Calculate the minimum number of operations to return to the main folder.

    :param logs: List[str] - List of operations performed in the file system.
    :return: int - Minimum number of operations to return to the main folder.
    """
    depth = 0
    for log in logs:
        if log == "../":
            if depth > 0:
                depth -= 1
        elif log == "./":
            continue
        else:
            depth += 1
    return depth

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    logs1 = ["d1/", "d2/", "../", "d21/", "./"]
    print(minOperations(logs1))  # Output: 2

    # Test Case 2
    logs2 = ["d1/", "d2/", "./", "d3/", "../", "../"]
    print(minOperations(logs2))  # Output: 1

    # Test Case 3
    logs3 = ["d1/", "../", "../", "../"]
    print(minOperations(logs3))  # Output: 0

    # Test Case 4
    logs4 = ["./", "../", "./"]
    print(minOperations(logs4))  # Output: 0

    # Test Case 5
    logs5 = ["d1/", "d2/", "d3/", "../", "d4/"]
    print(minOperations(logs5))  # Output: 3

"""
Time Complexity Analysis:
- The solution iterates through the `logs` list once, performing constant-time operations for each log entry.
- Therefore, the time complexity is O(n), where n is the length of the `logs` list.

Space Complexity Analysis:
- The solution uses a single integer variable `depth` to track the current folder depth.
- No additional data structures are used, so the space complexity is O(1).

Topic: Stack Simulation
"""