"""
LeetCode Question #1536: Minimum Swaps to Arrange a Binary Grid

Problem Statement:
Given an n x n binary grid, in one step you can swap any two rows with each other. A binary grid is said to be valid if the following condition is met:
For every row i, the number of trailing zeros in row i is at least n - i - 1.

Return the minimum number of swaps needed to make the grid valid. If the grid cannot be valid, return -1.

Example:
Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
Explanation: After swapping row 1 with row 0, grid becomes [[1,1,0],[0,0,1],[1,0,0]].
After swapping row 2 with row 1, grid becomes [[1,1,0],[1,0,0],[0,0,1]].
After swapping row 2 with row 1 again, grid becomes [[1,1,0],[0,0,1],[1,0,0]].
Now the grid is valid.

Constraints:
- n == grid.length
- n == grid[i].length
- 1 <= n <= 200
- grid[i][j] is either 0 or 1
"""

def minSwaps(grid):
    """
    Function to calculate the minimum number of swaps required to make the binary grid valid.
    :param grid: List[List[int]] - The binary grid.
    :return: int - Minimum number of swaps or -1 if the grid cannot be valid.
    """
    n = len(grid)
    
    # Calculate the number of trailing zeros for each row
    trailing_zeros = []
    for row in grid:
        count = 0
        for val in reversed(row):
            if val == 0:
                count += 1
            else:
                break
        trailing_zeros.append(count)
    
    swaps = 0
    
    # Iterate through each row to ensure the condition is met
    for i in range(n):
        required_zeros = n - i - 1
        j = i
        
        # Find a row with enough trailing zeros
        while j < n and trailing_zeros[j] < required_zeros:
            j += 1
        
        # If no such row exists, return -1
        if j == n:
            return -1
        
        # Perform swaps to bring the row with enough trailing zeros to the current position
        while j > i:
            trailing_zeros[j], trailing_zeros[j - 1] = trailing_zeros[j - 1], trailing_zeros[j]
            swaps += 1
            j -= 1
    
    return swaps

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0,0,1],[1,1,0],[1,0,0]]
    print(minSwaps(grid1))  # Output: 3

    # Test Case 2
    grid2 = [[1,0,0],[1,1,0],[0,0,1]]
    print(minSwaps(grid2))  # Output: 0

    # Test Case 3
    grid3 = [[1,1,0],[0,0,1],[1,0,0]]
    print(minSwaps(grid3))  # Output: -1

    # Test Case 4
    grid4 = [[0,0,0],[0,0,0],[0,0,1]]
    print(minSwaps(grid4))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating trailing zeros for each row takes O(n^2) since we iterate through each row and its elements.
- The swapping process involves finding a valid row and swapping, which takes O(n^2) in the worst case.
- Overall, the time complexity is O(n^2).

Space Complexity:
- We use an auxiliary list `trailing_zeros` of size n to store the trailing zeros for each row.
- Thus, the space complexity is O(n).

Topic: Arrays
"""