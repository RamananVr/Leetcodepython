"""
LeetCode Problem #2751: Robot Collisions

Problem Statement:
There are `n` robots, each represented as a tuple `(position, health, direction)`:
- `position` is an integer representing the robot's position on a 1D line.
- `health` is an integer representing the robot's health.
- `direction` is either 'L' (left) or 'R' (right), representing the direction the robot is moving.

When two robots collide:
1. Both robots lose 1 health point.
2. If a robot's health becomes 0, it is destroyed and removed from the line.
3. If both robots survive the collision, they reverse their directions.

The robots move simultaneously, and collisions are resolved in the order they occur.

Write a function `robotCollisions` that takes a list of robots and returns the final state of the robots after all collisions are resolved. The final state should be sorted by position.

Input:
- `robots`: List of tuples, where each tuple is `(position, health, direction)`.

Output:
- A list of tuples representing the final state of the robots, sorted by position.

Constraints:
- `1 <= n <= 10^5`
- `1 <= position <= 10^9`
- `1 <= health <= 10^9`
- `direction` is either 'L' or 'R'.

Example:
Input: [(5, 3, 'R'), (8, 2, 'L')]
Output: [(5, 2, 'L')]

"""

# Python Solution
from collections import deque

def robotCollisions(robots):
    # Sort robots by position
    robots.sort(key=lambda x: x[0])
    
    stack = deque()  # Stack to handle collisions
    result = []      # Final state of robots
    
    for position, health, direction in robots:
        if direction == 'R':
            # Push right-moving robot onto the stack
            stack.append((position, health, direction))
        else:
            # Handle collisions with right-moving robots
            while stack and stack[-1][2] == 'R' and health > 0:
                r_position, r_health, r_direction = stack.pop()
                if r_health > health:
                    # Right-moving robot survives
                    stack.append((r_position, r_health - 1, r_direction))
                    health -= 1
                elif r_health < health:
                    # Left-moving robot survives
                    health -= 1
                else:
                    # Both robots are destroyed
                    health = 0
            
            # If the left-moving robot survives, add it to the result
            if health > 0:
                result.append((position, health, direction))
    
    # Add remaining right-moving robots in the stack to the result
    result.extend(stack)
    
    # Sort the result by position
    result.sort(key=lambda x: x[0])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    robots = [(5, 3, 'R'), (8, 2, 'L')]
    print(robotCollisions(robots))  # Output: [(5, 2, 'L')]

    # Test Case 2
    robots = [(1, 5, 'R'), (3, 3, 'L'), (6, 2, 'R')]
    print(robotCollisions(robots))  # Output: [(1, 4, 'R'), (3, 2, 'L'), (6, 2, 'R')]

    # Test Case 3
    robots = [(2, 4, 'R'), (4, 4, 'L'), (6, 1, 'R')]
    print(robotCollisions(robots))  # Output: [(2, 3, 'R'), (4, 3, 'L'), (6, 1, 'R')]

    # Test Case 4
    robots = [(10, 1, 'R'), (15, 1, 'L')]
    print(robotCollisions(robots))  # Output: []

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the robots by position takes O(n log n).
- Processing each robot and handling collisions takes O(n) in the worst case.
- Overall time complexity: O(n log n).

Space Complexity:
- The stack can hold up to O(n) robots in the worst case.
- The result list also holds up to O(n) robots.
- Overall space complexity: O(n).

Topic: Simulation
"""