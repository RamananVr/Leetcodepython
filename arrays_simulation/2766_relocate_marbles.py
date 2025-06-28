"""
LeetCode Problem 2766: Relocate Marbles

You are given a 0-indexed integer array nums representing the initial positions of some marbles. You are also given two 0-indexed integer arrays moveFrom and moveTo of equal length.

Throughout moveFrom.length steps, you will change the positions of the marbles. On the ith step, you will move all marbles at position moveFrom[i] to position moveTo[i].

After completing all the steps, return a sorted array of the occupied positions.

Notes:
- We call a position occupied if there is at least one marble in that position.
- There may be multiple marbles in a single position.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= moveFrom.length <= 10^5
- moveFrom.length == moveTo.length
- 1 <= nums[i], moveFrom[i], moveTo[i] <= 10^9

Example 1:
Input: nums = [1,6,7,8], moveFrom = [1,7,2], moveTo = [2,9,5]
Output: [5,6,8,9]

Example 2:
Input: nums = [1,1,3,3], moveFrom = [1,3], moveTo = [2,2]
Output: [2]

Topics: Arrays, Hash Set, Simulation, Sorting
"""

class Solution:
    def relocateMarbles(self, nums: list[int], moveFrom: list[int], moveTo: list[int]) -> list[int]:
        """
        Approach 1: Set-based simulation
        
        Use a set to track occupied positions. For each move operation,
        remove the source position and add the destination position.
        
        Time: O(n + m + k log k) where n=len(nums), m=len(moveFrom), k=unique positions
        Space: O(k) where k is number of unique positions
        """
        # Initialize set with starting positions
        occupied = set(nums)
        
        # Process each move
        for from_pos, to_pos in zip(moveFrom, moveTo):
            if from_pos in occupied:
                occupied.remove(from_pos)
                occupied.add(to_pos)
        
        # Return sorted list of occupied positions
        return sorted(occupied)
    
    def relocateMarbles_simulation(self, nums: list[int], moveFrom: list[int], moveTo: list[int]) -> list[int]:
        """
        Approach 2: Hash map simulation with counts
        
        Track count of marbles at each position, though the problem
        only asks for occupied positions.
        
        Time: O(n + m + k log k)
        Space: O(k)
        """
        from collections import defaultdict
        
        # Count marbles at each position
        marble_count = defaultdict(int)
        for pos in nums:
            marble_count[pos] += 1
        
        # Process moves
        for from_pos, to_pos in zip(moveFrom, moveTo):
            if from_pos in marble_count and marble_count[from_pos] > 0:
                count = marble_count[from_pos]
                marble_count[from_pos] = 0
                marble_count[to_pos] += count
        
        # Get all occupied positions
        occupied = [pos for pos, count in marble_count.items() if count > 0]
        return sorted(occupied)
    
    def relocateMarbles_step_by_step(self, nums: list[int], moveFrom: list[int], moveTo: list[int]) -> list[int]:
        """
        Approach 3: Step by step tracking (for understanding)
        
        More explicit simulation that shows the process clearly.
        
        Time: O(n + m + k log k)
        Space: O(k)
        """
        # Start with initial positions
        positions = set(nums)
        
        # Apply each move operation
        for i in range(len(moveFrom)):
            source = moveFrom[i]
            target = moveTo[i]
            
            # Only move if there are marbles at source position
            if source in positions:
                positions.remove(source)
                positions.add(target)
        
        # Return sorted result
        return sorted(list(positions))

def test_relocate_marbles():
    """Test the relocate marbles solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    result1 = solution.relocateMarbles([1, 6, 7, 8], [1, 7, 2], [2, 9, 5])
    assert result1 == [5, 6, 8, 9]
    
    # Test case 2: Multiple marbles converge
    result2 = solution.relocateMarbles([1, 1, 3, 3], [1, 3], [2, 2])
    assert result2 == [2]
    
    # Test case 3: No moves
    result3 = solution.relocateMarbles([1, 2, 3], [], [])
    assert result3 == [1, 2, 3]
    
    # Test case 4: Single marble
    result4 = solution.relocateMarbles([5], [5], [10])
    assert result4 == [10]
    
    # Test case 5: Move to same position
    result5 = solution.relocateMarbles([1, 2], [1], [1])
    assert result5 == [1, 2]
    
    # Test case 6: Chain of moves
    result6 = solution.relocateMarbles([1], [1, 2, 3], [2, 3, 4])
    assert result6 == [4]
    
    # Test case 7: Multiple starting positions, some moves
    result7 = solution.relocateMarbles([3, 4, 5], [4, 5], [1, 2])
    assert result7 == [1, 2, 3]
    
    # Test case 8: Move non-existent position (should be ignored)
    result8 = solution.relocateMarbles([1, 2], [3], [4])
    assert result8 == [1, 2]
    
    # Compare different approaches
    test_cases = [
        ([1, 6, 7, 8], [1, 7, 2], [2, 9, 5]),
        ([1, 1, 3, 3], [1, 3], [2, 2]),
        ([1, 2, 3], [], []),
        ([5], [5], [10]),
        ([1, 2], [1], [1]),
        ([1], [1, 2, 3], [2, 3, 4]),
        ([3, 4, 5], [4, 5], [1, 2]),
        ([1, 2], [3], [4])
    ]
    
    for nums, moveFrom, moveTo in test_cases:
        result1 = solution.relocateMarbles(nums, moveFrom, moveTo)
        result2 = solution.relocateMarbles_simulation(nums, moveFrom, moveTo)
        result3 = solution.relocateMarbles_step_by_step(nums, moveFrom, moveTo)
        assert result1 == result2 == result3, f"Mismatch for {nums}, {moveFrom}, {moveTo}"
    
    print("All relocate marbles tests passed!")

if __name__ == "__main__":
    test_relocate_marbles()
