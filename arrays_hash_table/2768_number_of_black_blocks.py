"""
LeetCode Problem 2768: Number of Black Blocks

You are given two integers m and n representing the dimensions of a 0-indexed m x n grid.

You are also given a 0-indexed 2D integer array coordinates, where coordinates[i] = [x, y] indicates that the cell (x, y) is colored black. All other cells are colored white.

A block in this grid is a 2 x 2 subgrid. More formally, a block with top-left corner (r, c) is the set of 4 cells (r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1).

Return a 0-indexed integer array result of size 5 such that result[i] is the number of blocks that contains exactly i black cells.

Constraints:
- 2 <= m, n <= 10^5
- 0 <= coordinates.length <= 10^4
- coordinates[i].length == 2
- 0 <= coordinates[i][0] < m
- 0 <= coordinates[i][1] < n
- It is guaranteed that coordinates contains pairwise distinct coordinates.

Example 1:
Input: m = 3, n = 3, coordinates = [[0,0],[1,1],[2,2]]
Output: [3,1,1,1,0]

Example 2:
Input: m = 3, n = 3, coordinates = [[0,0]]
Output: [3,1,0,0,0]

Topics: Arrays, Hash Table, Counting
"""

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: list[list[int]]) -> list[int]:
        """
        Approach 1: Count affected blocks efficiently
        
        For each black cell, it can affect at most 4 different 2x2 blocks.
        Count the number of black cells in each potentially affected block.
        
        Time: O(k) where k = len(coordinates) 
        Space: O(k) for storing block counts
        """
        from collections import defaultdict
        
        # Convert coordinates to set for O(1) lookup
        black_cells = set(map(tuple, coordinates))
        
        # Count black cells in each 2x2 block
        block_count = defaultdict(int)
        
        # For each black cell, check which 2x2 blocks it belongs to
        for x, y in coordinates:
            # A cell (x, y) can be part of blocks with top-left corners:
            # (x-1, y-1), (x-1, y), (x, y-1), (x, y)
            for dx in [-1, 0]:
                for dy in [-1, 0]:
                    # Top-left corner of potential block
                    top_left_x = x + dx
                    top_left_y = y + dy
                    
                    # Check if this forms a valid 2x2 block within grid
                    if (0 <= top_left_x < m - 1 and 
                        0 <= top_left_y < n - 1):
                        block_count[(top_left_x, top_left_y)] += 1
        
        # Initialize result array
        result = [0] * 5
        
        # Count total possible 2x2 blocks
        total_blocks = (m - 1) * (n - 1)
        
        # Count blocks with 0 black cells
        result[0] = total_blocks - len(block_count)
        
        # Count blocks with 1, 2, 3, 4 black cells
        for count in block_count.values():
            result[count] += 1
        
        return result
    
    def countBlackBlocks_alternative(self, m: int, n: int, coordinates: list[list[int]]) -> list[int]:
        """
        Approach 2: Direct counting with coordinate checking
        
        Similar approach but with explicit coordinate validation.
        
        Time: O(k)
        Space: O(k)
        """
        from collections import Counter
        
        black_set = set(map(tuple, coordinates))
        block_black_count = Counter()
        
        # For each black cell, increment count for all blocks it's in
        for x, y in coordinates:
            # Check all possible 2x2 blocks containing this cell
            for r in range(max(0, x - 1), min(m - 1, x + 1)):
                for c in range(max(0, y - 1), min(n - 1, y + 1)):
                    if r + 1 < m and c + 1 < n:  # Valid 2x2 block
                        block_black_count[(r, c)] += 1
        
        # Count distribution
        result = [0] * 5
        total_blocks = (m - 1) * (n - 1)
        
        # All blocks not in block_black_count have 0 black cells
        result[0] = total_blocks - len(block_black_count)
        
        # Count blocks by number of black cells
        for count in block_black_count.values():
            result[count] += 1
        
        return result
    
    def countBlackBlocks_bruteforce(self, m: int, n: int, coordinates: list[list[int]]) -> list[int]:
        """
        Approach 3: Brute force (for verification on small inputs)
        
        Check every possible 2x2 block and count black cells.
        
        Time: O(m * n * k) where k = len(coordinates)
        Space: O(k)
        """
        black_set = set(map(tuple, coordinates))
        result = [0] * 5
        
        # Check every possible 2x2 block
        for r in range(m - 1):
            for c in range(n - 1):
                # Count black cells in this 2x2 block
                black_count = 0
                for dr in range(2):
                    for dc in range(2):
                        if (r + dr, c + dc) in black_set:
                            black_count += 1
                
                result[black_count] += 1
        
        return result

def test_count_black_blocks():
    """Test the count black blocks solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    result1 = solution.countBlackBlocks(3, 3, [[0,0],[1,1],[2,2]])
    assert result1 == [3, 1, 1, 1, 0]
    
    # Test case 2: Single black cell
    result2 = solution.countBlackBlocks(3, 3, [[0,0]])
    assert result2 == [3, 1, 0, 0, 0]
    
    # Test case 3: No black cells
    result3 = solution.countBlackBlocks(3, 3, [])
    assert result3 == [4, 0, 0, 0, 0]
    
    # Test case 4: Minimum grid size
    result4 = solution.countBlackBlocks(2, 2, [[0,0]])
    assert result4 == [0, 1, 0, 0, 0]
    
    # Test case 5: Full 2x2 block
    result5 = solution.countBlackBlocks(2, 2, [[0,0],[0,1],[1,0],[1,1]])
    assert result5 == [0, 0, 0, 0, 1]
    
    # Test case 6: Larger grid
    result6 = solution.countBlackBlocks(4, 4, [[1,1],[2,2]])
    assert result6 == [7, 2, 0, 0, 0]
    
    # Test case 7: Adjacent black cells
    result7 = solution.countBlackBlocks(3, 3, [[0,0],[0,1]])
    assert result7 == [2, 2, 0, 0, 0]
    
    # Compare with brute force on smaller inputs
    test_cases = [
        (3, 3, [[0,0],[1,1],[2,2]]),
        (3, 3, [[0,0]]),
        (3, 3, []),
        (2, 2, [[0,0]]),
        (2, 2, [[0,0],[0,1],[1,0],[1,1]]),
        (3, 3, [[0,0],[0,1]])
    ]
    
    for m, n, coords in test_cases:
        result1 = solution.countBlackBlocks(m, n, coords)
        result2 = solution.countBlackBlocks_alternative(m, n, coords)
        result3 = solution.countBlackBlocks_bruteforce(m, n, coords)
        assert result1 == result2 == result3, f"Mismatch for {m}, {n}, {coords}: {result1}, {result2}, {result3}"
    
    print("All count black blocks tests passed!")

if __name__ == "__main__":
    test_count_black_blocks()
