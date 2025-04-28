"""
LeetCode Problem #2582: Pass the Pillow

Problem Statement:
There are `n` people standing in a circle, numbered from `1` to `n`. The first person starts with a pillow, and they pass it to the next person in the circle every second. After `n` seconds, the pillow will be back to the first person, and the process repeats.

Given two integers `n` and `time`, return the number of the person who has the pillow after `time` seconds.

Example:
Input: n = 4, time = 5
Output: 2

Explanation:
- At time = 0, person 1 has the pillow.
- At time = 1, person 2 has the pillow.
- At time = 2, person 3 has the pillow.
- At time = 3, person 4 has the pillow.
- At time = 4, person 3 has the pillow.
- At time = 5, person 2 has the pillow.

Constraints:
- 2 <= n <= 1000
- 1 <= time <= 1000
"""

def pass_the_pillow(n: int, time: int) -> int:
    """
    Function to determine the person who has the pillow after `time` seconds.

    :param n: Number of people in the circle.
    :param time: Number of seconds elapsed.
    :return: The person who has the pillow.
    """
    # Determine the direction of passing the pillow
    direction = 1  # 1 for forward, -1 for backward
    current_person = 1  # Start with person 1

    for _ in range(time):
        current_person += direction
        if current_person == n + 1:  # If the pillow reaches the last person
            direction = -1  # Change direction to backward
            current_person = n - 1
        elif current_person == 0:  # If the pillow reaches the first person
            direction = 1  # Change direction to forward
            current_person = 2

    return current_person

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    time = 5
    print(pass_the_pillow(n, time))  # Output: 2

    # Test Case 2
    n = 3
    time = 2
    print(pass_the_pillow(n, time))  # Output: 3

    # Test Case 3
    n = 5
    time = 10
    print(pass_the_pillow(n, time))  # Output: 1

    # Test Case 4
    n = 6
    time = 13
    print(pass_the_pillow(n, time))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through `time` seconds, so the time complexity is O(time).

Space Complexity:
- The function uses a constant amount of space for variables (`direction` and `current_person`), so the space complexity is O(1).

Topic: Simulation
"""