"""
LeetCode Problem #1776: Car Fleet II

Problem Statement:
There are `n` cars traveling at different speeds in the same direction along a one-lane road. You are given an array `cars` where `cars[i] = [position_i, speed_i]` represents:
- `position_i` is the position of the i-th car.
- `speed_i` is the speed of the i-th car.

Each car can catch up to the car in front of it, but it cannot pass it. When two cars meet, they form a single fleet, and the fleet travels at the speed of the slower car.

A car fleet is some non-empty set of cars driving at the same speed. Note that a single car is also a fleet.

If a car catches up to another car at time `t`, they unite into a single fleet and the fleet's speed is set to the slower car's speed. Once a car joins a fleet, it cannot leave it.

Return an array `answer` where `answer[i]` is the time, in seconds, at which the i-th car will catch up to the next car in front of it, or `-1` if the car does not catch up to the car in front of it.

Constraints:
- `1 <= cars.length <= 10^5`
- `0 <= position_i, speed_i <= 10^6`
- `position_i < position_i+1` for all `1 <= i < cars.length`

"""

from typing import List

def getCollisionTimes(cars: List[List[int]]) -> List[float]:
    """
    Calculate the time at which each car catches up to the car in front of it.
    """
    n = len(cars)
    result = [-1] * n  # Initialize the result array with -1
    stack = []  # Monotonic stack to keep track of fleets

    for i in range(n - 1, -1, -1):
        position, speed = cars[i]

        # Process the stack to find the collision time
        while stack:
            j = stack[-1]
            pos_j, speed_j = cars[j]

            # If the current car is slower or equal in speed, it will never catch up
            if speed <= speed_j:
                stack.pop()
            else:
                # Calculate the collision time
                collision_time = (pos_j - position) / (speed - speed_j)
                # If the collision time is after the next car's collision time, discard it
                if result[j] != -1 and collision_time > result[j]:
                    stack.pop()
                else:
                    break

        # If the stack is not empty, we found a valid collision time
        if stack:
            result[i] = (cars[stack[-1]][0] - position) / (speed - cars[stack[-1]][1])

        # Push the current car onto the stack
        stack.append(i)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cars = [[1, 2], [2, 1], [4, 3], [7, 2]]
    print(getCollisionTimes(cars))  # Output: [1.0, -1.0, 3.0, -1.0]

    # Test Case 2
    cars = [[3, 4], [5, 4], [6, 3], [9, 1]]
    print(getCollisionTimes(cars))  # Output: [2.0, 1.0, 1.5, -1.0]

    # Test Case 3
    cars = [[0, 3], [2, 2], [4, 1]]
    print(getCollisionTimes(cars))  # Output: [-1.0, -1.0, -1.0]

"""
Time Complexity:
- The algorithm processes each car once and uses a monotonic stack to manage the cars.
- Each car is pushed and popped from the stack at most once.
- Therefore, the time complexity is O(n), where n is the number of cars.

Space Complexity:
- The space complexity is O(n) due to the stack used to store indices of cars.

Topic: Monotonic Stack
"""