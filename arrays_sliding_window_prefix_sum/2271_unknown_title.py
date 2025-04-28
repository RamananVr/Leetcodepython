"""
LeetCode Problem #2271: Maximum White Tiles Covered by a Carpet

Problem Statement:
You are given a 2D integer array `tiles` where `tiles[i] = [li, ri]` represents that every tile 
in the range [li, ri] (inclusive) is white. You are also given an integer `carpetLen`, the length 
of a single carpet that can be placed anywhere.

Return the maximum number of white tiles that can be covered by the carpet.

Notes:
- The tiles may overlap.
- Tiles are not guaranteed to be sorted.
- A carpet can only cover contiguous tiles.

Constraints:
- 1 <= tiles.length <= 5 * 10^4
- tiles[i].length == 2
- 1 <= li <= ri <= 10^9
- 1 <= carpetLen <= 10^9
"""

from typing import List

def maximumWhiteTiles(tiles: List[List[int]], carpetLen: int) -> int:
    # Step 1: Sort the tiles by their starting position
    tiles.sort()
    
    # Step 2: Create a prefix sum array for the total number of white tiles
    prefix_sum = []
    total = 0
    for start, end in tiles:
        total += (end - start + 1)
        prefix_sum.append(total)
    
    # Step 3: Use a sliding window approach to find the maximum coverage
    max_covered = 0
    n = len(tiles)
    j = 0  # Right pointer of the sliding window
    
    for i in range(n):
        start_i, end_i = tiles[i]
        # Calculate the farthest point the carpet can reach starting from tiles[i][0]
        carpet_end = start_i + carpetLen - 1
        
        # Move the right pointer to the farthest tile that the carpet can partially or fully cover
        while j < n and tiles[j][1] < carpet_end:
            j += 1
        
        # Calculate the number of tiles covered
        if j < n and tiles[j][0] <= carpet_end:
            # Carpet partially covers tiles[j]
            covered = prefix_sum[j - 1] - (prefix_sum[i - 1] if i > 0 else 0)
            covered += (carpet_end - tiles[j][0] + 1)
        else:
            # Carpet fully covers up to tiles[j-1]
            covered = prefix_sum[j - 1] - (prefix_sum[i - 1] if i > 0 else 0)
        
        # Update the maximum coverage
        max_covered = max(max_covered, covered)
    
    return max_covered

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tiles = [[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]]
    carpetLen = 10
    print(maximumWhiteTiles(tiles, carpetLen))  # Expected Output: 9

    # Test Case 2
    tiles = [[10, 11], [1, 1]]
    carpetLen = 2
    print(maximumWhiteTiles(tiles, carpetLen))  # Expected Output: 2

    # Test Case 3
    tiles = [[1, 2], [3, 5], [6, 8]]
    carpetLen = 4
    print(maximumWhiteTiles(tiles, carpetLen))  # Expected Output: 4

"""
Time Complexity Analysis:
- Sorting the tiles takes O(n log n), where n is the number of tiles.
- The sliding window approach iterates through the tiles, and for each tile, the inner loop 
  moves the right pointer. In total, the two pointers traverse the list at most 2n times, 
  resulting in O(n) for the sliding window.
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- The prefix sum array requires O(n) space.
- Overall space complexity: O(n).

Topic: Arrays, Sliding Window, Prefix Sum
"""