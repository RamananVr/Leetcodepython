"""
LeetCode Question #754: Reach a Number

Problem Statement:
You are standing at position 0 on an infinite number line. There is a target position target.
You can make a move of +1 or -1 at each step. Each move you make increases the length of the step by 1.

Return the minimum number of steps required to reach the target position.

Constraints:
- -10^9 <= target <= 10^9
- target is an integer.
"""

def reachNumber(target: int) -> int:
    """
    Function to calculate the minimum number of steps required to reach the target position.
    """
    target = abs(target)  # Since the number line is symmetric, we only need to consider positive targets.
    step = 0
    sum_steps = 0

    # Keep moving until the sum of steps is greater than or equal to the target
    while sum_steps < target or (sum_steps - target) % 2 != 0:
        step += 1
        sum_steps += step

    return step


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Target is 3
    print(reachNumber(3))  # Expected Output: 2

    # Test Case 2: Target is 2
    print(reachNumber(2))  # Expected Output: 3

    # Test Case 3: Target is -5
    print(reachNumber(-5))  # Expected Output: 5

    # Test Case 4: Target is 0
    print(reachNumber(0))  # Expected Output: 0

    # Test Case 5: Target is 10
    print(reachNumber(10))  # Expected Output: 4


"""
Time and Space Complexity Analysis:

Time Complexity:
- The while loop runs until the sum of steps is greater than or equal to the target and the difference (sum_steps - target) is even.
- In the worst case, the loop runs approximately O(sqrt(target)) iterations because the sum of the first n natural numbers is n * (n + 1) / 2, which grows quadratically.
- Therefore, the time complexity is O(sqrt(target)).

Space Complexity:
- The algorithm uses a constant amount of space for variables (step, sum_steps, target).
- No additional data structures are used.
- Therefore, the space complexity is O(1).

Topic: Math
"""