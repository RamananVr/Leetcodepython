"""
LeetCode Problem #752: Open the Lock

Problem Statement:
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', ..., '9'. 
The wheels can rotate freely and wrap around: for example, the wheel that starts at '0' can rotate 
clockwise to '1', or counterclockwise to '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends, meaning if the lock displays any of these codes, the lock will 
become stuck and you cannot rotate it anymore. You are also given a target code, and you want to 
know the minimum number of turns required to unlock the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "0201" -> "0202".
Note that a wheel can rotate clockwise or counterclockwise.

Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel clockwise to move from "0000" -> "0009".

Example 3:
Input: deadends = ["8888","0000"], target = "0009"
Output: -1
Explanation: The lock is stuck at the initial state "0000", and we cannot unlock it.

Constraints:
- 1 <= deadends.length <= 500
- deadends[i].length == 4
- target.length == 4
- target is a string of digits from '0' to '9'.
- The input strings are unique.
"""

from collections import deque

def openLock(deadends, target):
    def get_neighbors(state):
        """Generate all possible states by turning one wheel."""
        neighbors = []
        for i in range(4):
            digit = int(state[i])
            # Turn the wheel clockwise
            neighbors.append(state[:i] + str((digit + 1) % 10) + state[i+1:])
            # Turn the wheel counterclockwise
            neighbors.append(state[:i] + str((digit - 1) % 10) + state[i+1:])
        return neighbors

    dead_set = set(deadends)
    if "0000" in dead_set:
        return -1

    queue = deque([("0000", 0)])  # (current state, number of moves)
    visited = set("0000")

    while queue:
        current, moves = queue.popleft()
        if current == target:
            return moves
        for neighbor in get_neighbors(current):
            if neighbor not in visited and neighbor not in dead_set:
                visited.add(neighbor)
                queue.append((neighbor, moves + 1))
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    print(openLock(deadends, target))  # Output: 6

    # Test Case 2
    deadends = ["8888"]
    target = "0009"
    print(openLock(deadends, target))  # Output: 1

    # Test Case 3
    deadends = ["8888", "0000"]
    target = "0009"
    print(openLock(deadends, target))  # Output: -1

    # Test Case 4
    deadends = []
    target = "0001"
    print(openLock(deadends, target))  # Output: 1

    # Test Case 5
    deadends = ["0001"]
    target = "0001"
    print(openLock(deadends, target))  # Output: -1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each state has up to 8 neighbors (4 wheels, each with 2 possible rotations).
- In the worst case, we explore all 10,000 possible states (0000 to 9999).
- Thus, the time complexity is O(10,000 * 8) = O(80,000), which simplifies to O(10,000).

Space Complexity:
- The `visited` set can store up to 10,000 states.
- The queue can also hold up to 10,000 states in the worst case.
- Thus, the space complexity is O(10,000).

Topic: Breadth-First Search (BFS)
"""