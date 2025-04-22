"""
LeetCode Question #858: Mirror Reflection

Problem Statement:
There is a special square room with mirrors on each of the four walls. 
Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length `p`, and a laser ray from the southwest corner first meets the east wall at a distance `q` from the 0th receptor.

Given the two integers `p` and `q`, return the number of the receptor that the ray meets first. 
The laser ray keeps bouncing between the walls infinitely until it meets a receptor.

Constraints:
- 1 <= q <= p <= 1000
- The greatest common divisor (GCD) of `p` and `q` is used to determine the ray's behavior.

Example:
Input: p = 3, q = 1
Output: 1

Explanation:
The ray first meets the receptor 1.

"""

from math import gcd

def mirrorReflection(p: int, q: int) -> int:
    """
    Determines which receptor the laser ray meets first.

    Args:
    p (int): The length of the square room's walls.
    q (int): The distance from the 0th receptor where the ray first meets the east wall.

    Returns:
    int: The number of the receptor that the ray meets first.
    """
    # Find the least common multiple (LCM) of p and q
    lcm = (p * q) // gcd(p, q)
    
    # Determine the number of room heights (m) and widths (n) the ray travels
    m = lcm // p  # Number of room heights
    n = lcm // q  # Number of room widths

    # If m is odd and n is odd, the ray meets receptor 1
    if m % 2 == 1 and n % 2 == 1:
        return 1
    # If m is odd and n is even, the ray meets receptor 2
    elif m % 2 == 1 and n % 2 == 0:
        return 2
    # If m is even and n is odd, the ray meets receptor 0
    else:
        return 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    p = 3
    q = 1
    print(f"Input: p = {p}, q = {q} -> Output: {mirrorReflection(p, q)}")  # Expected: 1

    # Test Case 2
    p = 2
    q = 1
    print(f"Input: p = {p}, q = {q} -> Output: {mirrorReflection(p, q)}")  # Expected: 2

    # Test Case 3
    p = 4
    q = 3
    print(f"Input: p = {p}, q = {q} -> Output: {mirrorReflection(p, q)}")  # Expected: 0

    # Test Case 4
    p = 5
    q = 2
    print(f"Input: p = {p}, q = {q} -> Output: {mirrorReflection(p, q)}")  # Expected: 1

"""
Time Complexity:
- Calculating the GCD takes O(log(min(p, q))) time.
- Calculating the LCM and performing modulo operations are O(1).
- Overall, the time complexity is O(log(min(p, q))).

Space Complexity:
- The algorithm uses a constant amount of space, so the space complexity is O(1).

Topic: Math, Geometry
"""