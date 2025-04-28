"""
LeetCode Problem #1183: Maximum Number of Ones

Problem Statement:
Consider a binary matrix with dimensions `width x width`, where each cell contains either a 0 or a 1. 
You can select at most `numSelect` rows and at most `numSelect` columns to form a submatrix. 
The goal is to maximize the number of 1s in the submatrix.

Write a function `maximumNumberOfOnes(width: int, numSelect: int, rowSelect: int, colSelect: int) -> int` 
that returns the maximum number of 1s that can be obtained in the submatrix.

Constraints:
- 1 <= width <= 50
- 1 <= numSelect <= width
- 1 <= rowSelect, colSelect <= numSelect
"""

def maximumNumberOfOnes(width: int, numSelect: int, rowSelect: int, colSelect: int) -> int:
    """
    This function calculates the maximum number of 1s that can be obtained in a submatrix
    by selecting at most `numSelect` rows and `numSelect` columns.
    """
    # Frequency matrix to count how many times each cell contributes to the submatrix
    freq = [[0] * width for _ in range(width)]
    
    # Calculate the frequency of each cell
    for i in range(width):
        for j in range(width):
            freq[i][j] = ((i % rowSelect) + 1) * ((j % colSelect) + 1)
    
    # Flatten the frequency matrix and sort in descending order
    flat_freq = sorted([freq[i][j] for i in range(width) for j in range(width)], reverse=True)
    
    # Select the top `numSelect * numSelect` cells
    max_ones = sum(flat_freq[:numSelect * numSelect])
    
    return max_ones

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    width = 3
    numSelect = 2
    rowSelect = 2
    colSelect = 2
    print(maximumNumberOfOnes(width, numSelect, rowSelect, colSelect))  # Expected Output: 8

    # Test Case 2
    width = 4
    numSelect = 3
    rowSelect = 2
    colSelect = 2
    print(maximumNumberOfOnes(width, numSelect, rowSelect, colSelect))  # Expected Output: 18

    # Test Case 3
    width = 5
    numSelect = 3
    rowSelect = 3
    colSelect = 3
    print(maximumNumberOfOnes(width, numSelect, rowSelect, colSelect))  # Expected Output: 27

"""
Time Complexity Analysis:
- Calculating the frequency matrix takes O(width^2) time.
- Flattening and sorting the frequency matrix takes O(width^2 * log(width^2)) time.
- Summing the top `numSelect * numSelect` elements takes O(numSelect^2) time.
Overall time complexity: O(width^2 * log(width^2)).

Space Complexity Analysis:
- The frequency matrix requires O(width^2) space.
- The flattened frequency list also requires O(width^2) space.
Overall space complexity: O(width^2).

Topic: Greedy, Matrix
"""