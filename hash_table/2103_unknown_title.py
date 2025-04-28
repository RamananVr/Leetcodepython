"""
LeetCode Problem #2103: Rings and Rods

Problem Statement:
There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0 to 9. 
You are given a string `rings` of length 2n that describes the n rings that are placed onto the rods. 
Every two characters in `rings` forms a description of a ring where:
- The first character of the pair represents the color of the ring ('R', 'G', 'B').
- The second character of the pair represents the rod on which the ring is placed ('0' to '9').

For example, "R3G2B1" describes three rings:
- A red ring on rod 3.
- A green ring on rod 2.
- A blue ring on rod 1.

Return the number of rods that have all three colors of rings on them.

Constraints:
- `rings.length == 2 * n`
- `1 <= n <= 100`
- `rings[i]` is either 'R', 'G', 'B', or a digit ('0' to '9').

"""

def countPoints(rings: str) -> int:
    # Dictionary to store the set of colors for each rod
    rod_colors = {i: set() for i in range(10)}
    
    # Iterate through the rings string in pairs
    for i in range(0, len(rings), 2):
        color = rings[i]
        rod = int(rings[i + 1])
        rod_colors[rod].add(color)
    
    # Count the number of rods that have all three colors
    return sum(1 for colors in rod_colors.values() if len(colors) == 3)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rings = "B0B6G0R6R0R6G9"
    print(countPoints(rings))  # Output: 1

    # Test Case 2
    rings = "B0R0G0R9R0B0G0"
    print(countPoints(rings))  # Output: 1

    # Test Case 3
    rings = "G4"
    print(countPoints(rings))  # Output: 0

    # Test Case 4
    rings = "R0G0B0R1G1B1R2G2B2"
    print(countPoints(rings))  # Output: 3

"""
Time Complexity Analysis:
- The loop iterates through the `rings` string, which has a length of 2n. Thus, the time complexity is O(n).
- The final summation iterates over a fixed number of rods (10), which is O(1).
- Overall time complexity: O(n).

Space Complexity Analysis:
- We use a dictionary `rod_colors` with 10 keys (one for each rod), and each key maps to a set of at most 3 colors. 
  This results in a constant space usage of O(1).
- Overall space complexity: O(1).

Topic: Hash Table
"""