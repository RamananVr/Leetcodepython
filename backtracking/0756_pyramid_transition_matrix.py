"""
LeetCode Question #756: Pyramid Transition Matrix

Problem Statement:
We are stacking blocks to form a pyramid. Each block has a color represented by a single character. 
We are given a bottom row of blocks as a string `bottom`, and a list of allowed triples as a list of strings `allowed`. 
Each allowed triple is represented as a string of length 3, where the first two characters represent the colors of the 
blocks in the current level, and the third character is the color of the block in the next level.

You can place a block on top of two adjacent blocks if and only if the triple of the two blocks and the block above 
is in the allowed list.

Return True if it is possible to build the pyramid from the bottom up using the allowed triples, otherwise return False.

Constraints:
- `bottom` will be a string with length in the range [2, 8].
- `allowed` will have length in the range [0, 200].
- Each string in `allowed` will be of length 3.
- The letters in `bottom` and `allowed` are all uppercase English letters.

Example:
Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
Output: True
Explanation: We can stack the pyramid as follows:
    A
   G E
  B C D
We can build the pyramid from the bottom up using the allowed triples.

Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
Output: False
"""

from collections import defaultdict

def pyramidTransition(bottom: str, allowed: list[str]) -> bool:
    # Create a mapping from pairs of blocks to possible top blocks
    allowed_map = defaultdict(list)
    for triple in allowed:
        allowed_map[triple[:2]].append(triple[2])

    def can_build(current: str, next_row: str) -> bool:
        # If we have built the top of the pyramid, return True
        if len(current) == 1:
            return True
        # If we have completed a row, move to the next row
        if len(next_row) + 1 == len(current):
            return can_build(next_row, "")
        # Try all possible blocks for the next position
        for block in allowed_map[current[len(next_row):len(next_row)+2]]:
            if can_build(current, next_row + block):
                return True
        return False

    return can_build(bottom, "")

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    bottom1 = "BCD"
    allowed1 = ["BCG", "CDE", "GEA", "FFF"]
    print(pyramidTransition(bottom1, allowed1))  # Output: True

    # Test Case 2
    bottom2 = "AABA"
    allowed2 = ["AAA", "AAB", "ABA", "ABB", "BAC"]
    print(pyramidTransition(bottom2, allowed2))  # Output: False

    # Test Case 3
    bottom3 = "ABCD"
    allowed3 = ["ABE", "BCF", "CDE", "DEF", "EFG", "FGH", "GHI"]
    print(pyramidTransition(bottom3, allowed3))  # Output: False

    # Test Case 4
    bottom4 = "XYZ"
    allowed4 = ["XYA", "YZA", "XYY", "YZZ", "ZZZ"]
    print(pyramidTransition(bottom4, allowed4))  # Output: False

    # Test Case 5
    bottom5 = "AA"
    allowed5 = ["AAA", "AAB", "ABA", "ABB"]
    print(pyramidTransition(bottom5, allowed5))  # Output: True

"""
Time Complexity:
- Let `n` be the length of the bottom string and `m` be the number of allowed triples.
- In the worst case, for each pair of blocks in the current row, we may have to try all possible blocks from the allowed triples.
- The recursion depth is at most `n`, and at each level, we may try multiple combinations of blocks.
- The time complexity is approximately O(k^(n-1)), where `k` is the average number of possible blocks for a pair.

Space Complexity:
- The space complexity is O(n) for the recursion stack, where `n` is the length of the bottom string.
- Additionally, the `allowed_map` dictionary takes O(m) space, where `m` is the number of allowed triples.

Topic: Backtracking
"""