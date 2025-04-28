"""
LeetCode Problem #874: Walking Robot Simulation

Problem Statement:
A robot on an infinite XY-plane starts at point (0, 0) and faces north. The robot can receive a sequence of commands:
- `-2`: Turn left 90 degrees.
- `-1`: Turn right 90 degrees.
- `1 <= x <= 9`: Move forward `x` units in the direction it is currently facing.

The robot can also encounter obstacles on the plane, represented as a list of points `obstacles` where each point is a tuple `(xi, yi)`.

The robot performs the commands in order and stops if it tries to move into an obstacle. Return the maximum Euclidean distance squared from the origin `(0, 0)` to the farthest point the robot reaches.

Note:
- The Euclidean distance squared between two points `(x1, y1)` and `(x2, y2)` is `(x1 - x2)^2 + (y1 - y2)^2`.
- Obstacles are stationary and do not block the robot's path unless the robot tries to land on them.

Constraints:
- `1 <= commands.length <= 10^4`
- `0 <= obstacles.length <= 10^4`
- `-3 * 10^4 <= xi, yi <= 3 * 10^4`
- The robot's initial position is not an obstacle.

Example:
Input: commands = [4, -1, 3], obstacles = []
Output: 25
Explanation: The robot moves north 4 units, turns right, and moves east 3 units. The farthest point is (3, 4), and the distance squared is 3^2 + 4^2 = 25.
"""

# Python Solution
def robotSim(commands, obstacles):
    # Directions: North, East, South, West
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0  # Starting position
    direction_idx = 0  # Start facing north
    max_distance_squared = 0

    # Convert obstacles to a set for O(1) lookup
    obstacle_set = set(map(tuple, obstacles))

    for command in commands:
        if command == -2:  # Turn left
            direction_idx = (direction_idx - 1) % 4
        elif command == -1:  # Turn right
            direction_idx = (direction_idx + 1) % 4
        else:  # Move forward
            dx, dy = directions[direction_idx]
            for _ in range(command):
                if (x + dx, y + dy) not in obstacle_set:
                    x += dx
                    y += dy
                    max_distance_squared = max(max_distance_squared, x**2 + y**2)
                else:
                    break

    return max_distance_squared

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    commands = [4, -1, 3]
    obstacles = []
    print(robotSim(commands, obstacles))  # Output: 25

    # Test Case 2
    commands = [4, -1, 4, -2, 4]
    obstacles = [[2, 4]]
    print(robotSim(commands, obstacles))  # Output: 65

    # Test Case 3
    commands = [6, -1, -1, 6]
    obstacles = []
    print(robotSim(commands, obstacles))  # Output: 36

"""
Time Complexity:
- Processing commands: O(n), where n is the length of the commands array.
- Checking obstacles: Each obstacle lookup is O(1) due to the set, so the total cost is O(n) for all commands.
- Overall: O(n).

Space Complexity:
- Storing obstacles in a set: O(k), where k is the number of obstacles.
- Overall: O(k).

Topic: Simulation
"""