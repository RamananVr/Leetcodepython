"""
LeetCode Problem #818: Race Car

Problem Statement:
Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. 
Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

- 'A': Instructs your car to accelerate by increasing its speed by 1 unit and moving forward by the speed.
- 'R': Instructs your car to reverse its direction. After reversing, your speed changes to -1 * current_speed.

For example, after executing the instructions "AAR", your car goes to positions 1, 3, and 2 respectively.

Given a target position `target`, return the length of the shortest sequence of instructions to reach the target position.

Constraints:
- 1 <= target <= 10^4
"""

from collections import deque

def racecar(target: int) -> int:
    """
    Finds the minimum number of instructions to reach the target position.
    """
    # BFS queue: (position, speed, steps)
    queue = deque([(0, 1, 0)])
    visited = set((0, 1))  # To avoid revisiting the same state

    while queue:
        position, speed, steps = queue.popleft()

        # If we reach the target, return the number of steps
        if position == target:
            return steps

        # Accelerate: Move to the next position with increased speed
        next_position, next_speed = position + speed, speed * 2
        if (next_position, next_speed) not in visited and 0 <= next_position <= 2 * target:
            visited.add((next_position, next_speed))
            queue.append((next_position, next_speed, steps + 1))

        # Reverse: Change direction and reset speed to ±1
        reverse_speed = -1 if speed > 0 else 1
        if (position, reverse_speed) not in visited:
            visited.add((position, reverse_speed))
            queue.append((position, reverse_speed, steps + 1))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    target = 3
    print(f"Minimum steps to reach {target}: {racecar(target)}")  # Expected: 2

    # Test Case 2
    target = 6
    print(f"Minimum steps to reach {target}: {racecar(target)}")  # Expected: 5

    # Test Case 3
    target = 10
    print(f"Minimum steps to reach {target}: {racecar(target)}")  # Expected: 7

"""
Time Complexity:
- The BFS explores all possible states (position, speed) until the target is reached.
- The number of states is bounded by O(target * log(target)) because the speed doubles or halves, and the position is limited to 2 * target.
- Therefore, the time complexity is O(target * log(target)).

Space Complexity:
- The space complexity is determined by the size of the queue and the visited set, which is also O(target * log(target)).

Topic: Breadth-First Search (BFS)
"""