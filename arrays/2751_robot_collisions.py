"""
LeetCode Problem 2751: Robot Collisions

There are n robots, each having a position on a number line, initial health, and movement direction.

You are given three 0-indexed integer arrays positions, healths, and directions of length n. All integers in positions are unique.

All robots start moving on the number line simultaneously. A robot moves in its given direction until one of the following happens:
- It collides with another robot.
- It reaches the end of the line.

When two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction. If both robots have the same health, both robots are removed from the line.

Your task is to determine the health of the robots that survive after all collisions, in the same order that the robots were given in the input.

Note: The positions may be given in any order.

Example 1:
Input: positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = ["R","L","L","R","R"]
Output: [2,17,9,15,10]
Explanation: 
No robot collides with another robot. They either move forever or reach the end of the line.

Example 2:
Input: positions = [3,5,2,6], healths = [10,10,15,12], directions = ["L","R","R","R"]
Output: [14]
Explanation: 
Robot 1 and robot 2 will collide and since both have the same health, both are removed. Robot 3 and robot 4 will collide and robot 3 will survive with health 14.

Example 3:
Input: positions = [1,2,5,6], healths = [10,12,14,15], directions = ["R","L","L","R"]
Output: []
Explanation: 
Robot 1 and robot 2 collide. Robot 2 survives with health 11.
Robot 2 and robot 3 collide. Robot 3 survives with health 13.
Robot 3 and robot 4 collide. Robot 4 survives with health 14.
Robot 4 reaches the end.

Constraints:
- 1 <= n <= 10^5
- 1 <= positions[i], healths[i] <= 10^9
- directions[i] == 'L' or directions[i] == 'R'
- All values in positions are distinct
"""

from typing import List


def survivedRobotsHealths(positions: List[int], healths: List[int], directions: List[str]) -> List[int]:
    """
    Simulate robot collisions and return surviving robots' healths.
    
    Strategy:
    1. Sort robots by position to process collisions in order
    2. Use stack to track robots moving right
    3. When a left-moving robot is encountered, resolve collisions with right-moving robots
    4. Return surviving robots in original order
    
    Args:
        positions: Initial positions of robots
        healths: Initial healths of robots
        directions: Movement directions ('L' or 'R')
        
    Returns:
        List of surviving robots' healths in original order
        
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    n = len(positions)
    
    # Create robots with original indices
    robots = []
    for i in range(n):
        robots.append({
            'pos': positions[i],
            'health': healths[i],
            'dir': directions[i],
            'index': i
        })
    
    # Sort by position
    robots.sort(key=lambda x: x['pos'])
    
    # Stack to store robots moving right
    right_moving = []
    survivors = []
    
    for robot in robots:
        if robot['dir'] == 'R':
            right_moving.append(robot)
        else:  # robot['dir'] == 'L'
            current_health = robot['health']
            
            # Resolve collisions with right-moving robots
            while right_moving and current_health > 0:
                right_robot = right_moving[-1]
                
                if right_robot['health'] < current_health:
                    # Right robot destroyed, left robot loses 1 health
                    right_moving.pop()
                    current_health -= 1
                elif right_robot['health'] > current_health:
                    # Left robot destroyed, right robot loses 1 health
                    right_robot['health'] -= 1
                    current_health = 0
                else:
                    # Both robots destroyed
                    right_moving.pop()
                    current_health = 0
            
            # If left robot survives, add to survivors
            if current_health > 0:
                robot['health'] = current_health
                survivors.append(robot)
    
    # Add remaining right-moving robots to survivors
    survivors.extend(right_moving)
    
    # Sort survivors by original index and extract healths
    survivors.sort(key=lambda x: x['index'])
    return [robot['health'] for robot in survivors]


def survivedRobotsHealthsOptimized(positions: List[int], healths: List[int], directions: List[str]) -> List[int]:
    """
    Optimized version using indices array for cleaner implementation.
    
    Args:
        positions: Initial positions of robots
        healths: Initial healths of robots
        directions: Movement directions ('L' or 'R')
        
    Returns:
        List of surviving robots' healths in original order
        
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    n = len(positions)
    indices = list(range(n))
    
    # Sort indices by position
    indices.sort(key=lambda i: positions[i])
    
    stack = []  # Stack of indices of robots moving right
    
    for i in indices:
        if directions[i] == 'R':
            stack.append(i)
        else:  # directions[i] == 'L'
            # Process collisions with right-moving robots
            while stack and healths[i] > 0:
                j = stack[-1]  # Right-moving robot
                
                if healths[j] < healths[i]:
                    # Right robot destroyed
                    stack.pop()
                    healths[i] -= 1
                elif healths[j] > healths[i]:
                    # Left robot destroyed
                    healths[j] -= 1
                    healths[i] = 0
                else:
                    # Both destroyed
                    stack.pop()
                    healths[i] = 0
    
    # Return surviving robots' healths in original order
    return [healths[i] for i in range(n) if healths[i] > 0]


def survivedRobotsHealthsSimulation(positions: List[int], healths: List[int], directions: List[str]) -> List[int]:
    """
    Direct simulation approach for better understanding.
    
    Args:
        positions: Initial positions of robots
        healths: Initial healths of robots
        directions: Movement directions ('L' or 'R')
        
    Returns:
        List of surviving robots' healths in original order
        
    Time Complexity: O(n^2) worst case
    Space Complexity: O(n)
    """
    n = len(positions)
    robots = list(range(n))
    robot_healths = healths[:]
    
    # Continue until no more collisions
    changed = True
    while changed:
        changed = False
        
        # Sort active robots by position
        robots.sort(key=lambda i: positions[i])
        
        # Check for collisions
        i = 0
        while i < len(robots) - 1:
            left_idx = robots[i]
            right_idx = robots[i + 1]
            
            # Check if collision will happen
            if (directions[left_idx] == 'R' and directions[right_idx] == 'L'):
                # Collision occurs
                if robot_healths[left_idx] < robot_healths[right_idx]:
                    # Left robot destroyed
                    robots.remove(left_idx)
                    robot_healths[right_idx] -= 1
                    changed = True
                elif robot_healths[left_idx] > robot_healths[right_idx]:
                    # Right robot destroyed
                    robots.remove(right_idx)
                    robot_healths[left_idx] -= 1
                    changed = True
                else:
                    # Both destroyed
                    robots.remove(left_idx)
                    robots.remove(right_idx)
                    changed = True
                
                # Don't increment i, check same position again
            else:
                i += 1
    
    # Return surviving robots in original order
    result = [0] * n
    for i in robots:
        result[i] = robot_healths[i]
    
    return [h for h in result if h > 0]


# Test cases
def test_survivedRobotsHealths():
    """Test the survivedRobotsHealths function with various inputs."""
    
    test_cases = [
        {
            "positions": [5,4,3,2,1],
            "healths": [2,17,9,15,10],
            "directions": ["R","L","L","R","R"],
            "expected": [2,17,9,15,10],
            "description": "Example 1: No collisions"
        },
        {
            "positions": [3,5,2,6],
            "healths": [10,10,15,12],
            "directions": ["L","R","R","R"],
            "expected": [14],
            "description": "Example 2: Multiple collisions with survivors"
        },
        {
            "positions": [1,2,5,6],
            "healths": [10,12,14,15],
            "directions": ["R","L","L","R"],
            "expected": [],
            "description": "Example 3: All robots destroyed"
        },
        {
            "positions": [1,2],
            "healths": [1,2],
            "directions": ["R","L"],
            "expected": [1],
            "description": "Simple collision: right robot survives"
        },
        {
            "positions": [1,2],
            "healths": [2,2],
            "directions": ["R","L"],
            "expected": [],
            "description": "Equal health collision: both destroyed"
        },
        {
            "positions": [1,2,3],
            "healths": [1,1,1],
            "directions": ["R","R","L"],
            "expected": [1],
            "description": "Chain reaction collision"
        },
        {
            "positions": [1],
            "healths": [5],
            "directions": ["R"],
            "expected": [5],
            "description": "Single robot"
        }
    ]
    
    for i, test in enumerate(test_cases):
        positions = test["positions"]
        healths = test["healths"]
        directions = test["directions"]
        expected = test["expected"]
        
        # Test main solution
        result1 = survivedRobotsHealths(positions, healths, directions)
        print(f"Test {i+1}: {test['description']}")
        print(f"  Input: positions = {positions}")
        print(f"  Input: healths = {healths}")
        print(f"  Input: directions = {directions}")
        print(f"  Expected: {expected}")
        print(f"  Stack approach: {result1}")
        
        # Test optimized solution
        result2 = survivedRobotsHealthsOptimized(positions[:], healths[:], directions[:])
        print(f"  Optimized: {result2}")
        
        # Verify results
        assert result1 == expected, f"Stack approach failed for test {i+1}"
        assert result2 == expected, f"Optimized failed for test {i+1}"
        
        print(f"  ✓ All solutions passed!")
        print()


if __name__ == "__main__":
    test_survivedRobotsHealths()

"""
Complexity Analysis:

1. Stack Approach (survivedRobotsHealths):
   - Time Complexity: O(n log n) - sorting robots + O(n) collision processing
   - Space Complexity: O(n) - robot data structures and stack

2. Optimized (survivedRobotsHealthsOptimized):
   - Time Complexity: O(n log n) - sorting by position + linear collision processing
   - Space Complexity: O(n) - indices array and stack

3. Simulation (survivedRobotsHealthsSimulation):
   - Time Complexity: O(n^2) - potentially multiple passes through robots
   - Space Complexity: O(n) - robot tracking arrays

Key Insights:
- Collisions only happen between adjacent robots moving in opposite directions (R meets L)
- Use stack to efficiently track right-moving robots
- Process robots left-to-right by position to handle collisions in order
- When left-moving robot encounters right-moving robots, resolve all collisions
- Maintain original indices to return results in input order

Edge Cases:
- No collisions (all same direction or no meetings)
- All robots destroyed
- Single robot
- Equal health collisions
- Chain reactions

Algorithm:
1. Sort robots by position
2. Use stack for right-moving robots
3. For each left-moving robot, resolve collisions with stack
4. Return survivors in original order

Topics: Arrays, Stack, Simulation, Sorting
"""
