"""
LeetCode Question #519: Random Flip Matrix

Problem Statement:
You are given the number of rows `m` and number of columns `n` of a 2D binary matrix where all values are initially 0. 
Write a class `Solution` to perform the following operations:

1. `flip()`: Randomly flip a 0 to a 1 and return the position `[row, col]` of that flipped cell. 
   Each cell with a value of 0 must be equally likely to be flipped.
2. `reset()`: Reset all values of the matrix to 0.

Implement the `Solution` class:
- `Solution(int m, int n)` Initializes the object with the size of the binary matrix `m x n`.
- `List[int] flip()` Flips one of the 0s randomly and returns the position `[row, col]`.
- `void reset()` Resets all the values of the matrix to be 0.

Constraints:
- 1 <= m, n <= 10^4
- There will be at least one 0 in the matrix when `flip` is called.
- At most 1000 calls will be made to `flip` and `reset`.

"""

import random

class Solution:
    def __init__(self, m: int, n: int):
        """
        Initialize the Solution object with a matrix of size m x n.
        """
        self.m = m
        self.n = n
        self.total = m * n
        self.flipped = {}
        self.available = self.total

    def flip(self) -> list[int]:
        """
        Randomly flip a 0 to a 1 and return the position [row, col].
        """
        # Generate a random index in the range of available cells
        rand_index = random.randint(0, self.available - 1)
        
        # Find the actual index to flip
        actual_index = self.flipped.get(rand_index, rand_index)
        
        # Update the mapping for the current index
        self.flipped[rand_index] = self.flipped.get(self.available - 1, self.available - 1)
        
        # Decrease the number of available cells
        self.available -= 1
        
        # Convert the 1D index to 2D coordinates
        row, col = divmod(actual_index, self.n)
        return [row, col]

    def reset(self) -> None:
        """
        Reset all values of the matrix to 0.
        """
        self.flipped.clear()
        self.available = self.total


# Example Test Cases
if __name__ == "__main__":
    # Initialize the matrix with 3 rows and 1 column
    solution = Solution(3, 1)
    
    # Flip a cell and print the result
    print(solution.flip())  # Example output: [1, 0]
    print(solution.flip())  # Example output: [0, 0]
    print(solution.flip())  # Example output: [2, 0]
    
    # Reset the matrix
    solution.reset()
    
    # Flip again after reset
    print(solution.flip())  # Example output: [1, 0]

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - `flip()`: O(1) on average. The random index generation and dictionary lookups are O(1).
   - `reset()`: O(1) since clearing the dictionary is O(1).

2. Space Complexity:
   - The space complexity is O(k), where k is the number of flipped cells. 
     This is because we store the mapping of flipped indices in the `flipped` dictionary.

Topic: Arrays, Randomization
"""