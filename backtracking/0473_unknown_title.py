"""
LeetCode Problem #473: Matchsticks to Square

Problem Statement:
You are given an integer array `matchsticks` where `matchsticks[i]` is the length of the ith matchstick. 
You want to use all the matchsticks to form a square. You should not break any stick, but you can link them 
up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Example 1:
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with side length 2, using the matchsticks.

Example 2:
Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot form a square with these matchsticks.

Constraints:
- 1 <= matchsticks.length <= 15
- 1 <= matchsticks[i] <= 10^8
"""

# Python Solution
from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Calculate the total length of all matchsticks
        total_length = sum(matchsticks)
        
        # If the total length is not divisible by 4, we cannot form a square
        if total_length % 4 != 0:
            return False
        
        # The target side length of the square
        side_length = total_length // 4
        
        # Sort matchsticks in descending order to optimize backtracking
        matchsticks.sort(reverse=True)
        
        # Initialize the four sides of the square
        sides = [0] * 4
        
        # Helper function for backtracking
        def backtrack(index: int) -> bool:
            # If we've placed all matchsticks, check if all sides are equal to the target side length
            if index == len(matchsticks):
                return all(side == side_length for side in sides)
            
            # Try placing the current matchstick in each side
            for i in range(4):
                # If placing the matchstick exceeds the target side length, skip
                if sides[i] + matchsticks[index] > side_length:
                    continue
                
                # Place the matchstick in the current side
                sides[i] += matchsticks[index]
                
                # Recursively try to place the next matchstick
                if backtrack(index + 1):
                    return True
                
                # Backtrack: remove the matchstick from the current side
                sides[i] -= matchsticks[index]
                
                # Optimization: if the current side is still 0 after trying, no need to try other sides
                if sides[i] == 0:
                    break
            
            return False
        
        # Start backtracking from the first matchstick
        return backtrack(0)

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    matchsticks1 = [1, 1, 2, 2, 2]
    print(solution.makesquare(matchsticks1))  # Output: True
    
    # Test Case 2
    matchsticks2 = [3, 3, 3, 3, 4]
    print(solution.makesquare(matchsticks2))  # Output: False
    
    # Test Case 3
    matchsticks3 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    print(solution.makesquare(matchsticks3))  # Output: True
    
    # Test Case 4
    matchsticks4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(solution.makesquare(matchsticks4))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the matchsticks takes O(n log n), where n is the number of matchsticks.
- The backtracking function explores all possible combinations of matchstick placements. 
  In the worst case, there are 4^n combinations (each matchstick can be placed in one of 4 sides).
- However, due to pruning and optimization (e.g., sorting and skipping invalid placements), the actual 
  number of combinations explored is much smaller. The exact complexity depends on the input.

Space Complexity:
- The space complexity is O(n) due to the recursion stack in the backtracking function.

Topic: Backtracking
"""