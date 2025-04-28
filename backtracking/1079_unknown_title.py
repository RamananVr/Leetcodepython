"""
LeetCode Problem #1079: Letter Tile Possibilities

Problem Statement:
You have a set of tiles, where each tile has one letter printed on it. You can use each tile 
exactly once. Return the number of possible non-empty sequences of letters you can make.

Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: tiles = "AAABBC"
Output: 188

Example 3:
Input: tiles = "V"
Output: 1

Constraints:
- 1 <= tiles.length <= 7
- tiles consists of uppercase English letters.
"""

from itertools import permutations

def numTilePossibilities(tiles: str) -> int:
    """
    Calculate the number of possible non-empty sequences of letters that can be formed
    using the given tiles.
    """
    # Use a set to store all unique permutations
    unique_sequences = set()
    
    # Generate permutations of all possible lengths
    for length in range(1, len(tiles) + 1):
        unique_sequences.update(permutations(tiles, length))
    
    # Return the count of unique sequences
    return len(unique_sequences)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tiles1 = "AAB"
    print(f"Input: {tiles1} -> Output: {numTilePossibilities(tiles1)}")  # Expected: 8

    # Test Case 2
    tiles2 = "AAABBC"
    print(f"Input: {tiles2} -> Output: {numTilePossibilities(tiles2)}")  # Expected: 188

    # Test Case 3
    tiles3 = "V"
    print(f"Input: {tiles3} -> Output: {numTilePossibilities(tiles3)}")  # Expected: 1

    # Test Case 4
    tiles4 = "XYZ"
    print(f"Input: {tiles4} -> Output: {numTilePossibilities(tiles4)}")  # Expected: 15

"""
Time Complexity Analysis:
- Generating all permutations for a string of length n has a time complexity of O(n!).
- Since we generate permutations for all lengths from 1 to n, the total time complexity is O(n * n!).
- Adding permutations to a set and calculating the length of the set are both O(1) operations.

Space Complexity Analysis:
- The space complexity is determined by the storage of all unique permutations in the set.
- In the worst case, the set can contain up to n! elements, where n is the length of the input string.
- Thus, the space complexity is O(n!).

Topic: Backtracking
"""