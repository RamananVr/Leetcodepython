"""
LeetCode Question #1007: Minimum Domino Rotations For Equal Row

Problem Statement:
In a row of dominoes, `tops[i]` and `bottoms[i]` represent the top and bottom halves of the i-th domino. 
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that `tops[i]` and `bottoms[i]` swap values.

Return the minimum number of rotations so that all the values in `tops` are the same, or all the values in `bottoms` are the same.

If it cannot be done, return -1.

Example 1:
Input: tops = [2, 1, 2, 4, 2, 2], bottoms = [5, 2, 6, 2, 3, 2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:
Input: tops = [3, 5, 1, 2, 3], bottoms = [3, 6, 3, 3, 4]
Output: -1
Explanation: 
In this case, it is not possible to make one row of values equal.

Constraints:
- 2 <= tops.length <= 2 * 10^4
- bottoms.length == tops.length
- 1 <= tops[i], bottoms[i] <= 6
"""

def minDominoRotations(tops, bottoms):
    """
    Function to calculate the minimum number of rotations required to make all values in tops or bottoms equal.
    
    :param tops: List[int] - The top row of dominoes.
    :param bottoms: List[int] - The bottom row of dominoes.
    :return: int - Minimum number of rotations required, or -1 if not possible.
    """
    def check(x):
        """
        Helper function to check the minimum rotations needed to make all values equal to x.
        """
        rotations_top = rotations_bottom = 0
        for i in range(len(tops)):
            if tops[i] != x and bottoms[i] != x:
                return float('inf')  # Impossible to make all values equal to x
            elif tops[i] != x:
                rotations_top += 1
            elif bottoms[i] != x:
                rotations_bottom += 1
        return min(rotations_top, rotations_bottom)
    
    # Check for both tops[0] and bottoms[0] as potential candidates
    rotations = min(check(tops[0]), check(bottoms[0]))
    return rotations if rotations != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tops = [2, 1, 2, 4, 2, 2]
    bottoms = [5, 2, 6, 2, 3, 2]
    print(minDominoRotations(tops, bottoms))  # Output: 2

    # Test Case 2
    tops = [3, 5, 1, 2, 3]
    bottoms = [3, 6, 3, 3, 4]
    print(minDominoRotations(tops, bottoms))  # Output: -1

    # Test Case 3
    tops = [1, 2, 1, 1, 1, 1]
    bottoms = [2, 1, 2, 2, 2, 2]
    print(minDominoRotations(tops, bottoms))  # Output: 1

    # Test Case 4
    tops = [1, 1, 1, 1, 1]
    bottoms = [1, 1, 1, 1, 1]
    print(minDominoRotations(tops, bottoms))  # Output: 0

"""
Time and Space Complexity Analysis:
- Time Complexity: O(n), where n is the length of the `tops` and `bottoms` arrays. 
  We iterate through the arrays twice (once for tops[0] and once for bottoms[0]).
- Space Complexity: O(1), as we use a constant amount of extra space.

Topic: Arrays
"""