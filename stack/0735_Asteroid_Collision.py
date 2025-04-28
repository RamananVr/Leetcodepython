"""
LeetCode Problem #735: Asteroid Collision

Problem Statement:
We are given an array `asteroids` of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction 
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Return an array of the asteroids after all collisions.

Constraints:
- 2 <= asteroids.length <= 10^4
- -1000 <= asteroids[i] <= 1000
- asteroids[i] != 0
"""

def asteroidCollision(asteroids):
    """
    Simulates the asteroid collision process and returns the final state of the asteroids.

    :param asteroids: List[int] - List of integers representing the asteroids.
    :return: List[int] - Final state of the asteroids after all collisions.
    """
    stack = []
    
    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            # Compare the top of the stack with the current asteroid
            if stack[-1] < -asteroid:  # Stack asteroid explodes
                stack.pop()
                continue
            elif stack[-1] == -asteroid:  # Both explode
                stack.pop()
            break
        else:
            # No collision or asteroid moves to the right
            stack.append(asteroid)
    
    return stack

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    asteroids = [5, 10, -5]
    print(asteroidCollision(asteroids))  # Output: [5, 10]

    # Test Case 2
    asteroids = [8, -8]
    print(asteroidCollision(asteroids))  # Output: []

    # Test Case 3
    asteroids = [10, 2, -5]
    print(asteroidCollision(asteroids))  # Output: [10]

    # Test Case 4
    asteroids = [-2, -1, 1, 2]
    print(asteroidCollision(asteroids))  # Output: [-2, -1, 1, 2]

    # Test Case 5
    asteroids = [1, -1, -2, 2]
    print(asteroidCollision(asteroids))  # Output: [-2, 2]

"""
Time Complexity Analysis:
- Each asteroid is pushed and popped from the stack at most once.
- Therefore, the time complexity is O(n), where n is the length of the `asteroids` array.

Space Complexity Analysis:
- The stack can hold at most n elements in the worst case.
- Therefore, the space complexity is O(n).

Topic: Stack
"""