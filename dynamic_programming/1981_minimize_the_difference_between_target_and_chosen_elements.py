"""
LeetCode Question #1981: Minimize the Difference Between Target and Chosen Elements

Problem Statement:
You are given an m x n integer matrix mat and an integer target.

Choose one element from each row in the matrix such that the absolute difference 
between target and the sum of the chosen elements is minimized.

Return the minimum absolute difference.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
Output: 0
Explanation: Choose 1 from the first row, 5 from the second row, and 7 from the third row. 
The sum is 1 + 5 + 7 = 13, which is equal to the target, so the absolute difference is 0.

Example 2:
Input: mat = [[1],[2],[3]], target = 100
Output: 94
Explanation: The best possible sum is 1 + 2 + 3 = 6, and the absolute difference is |100 - 6| = 94.

Example 3:
Input: mat = [[1,2,9,8,7]], target = 6
Output: 1
Explanation: The best possible sum is 7, and the absolute difference is |6 - 7| = 1.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 70
- 1 <= mat[i][j] <= 70
- 1 <= target <= 800
"""

# Python Solution
def minimizeTheDifference(mat, target):
    # Use a set to store possible sums
    possible_sums = {0}
    
    for row in mat:
        # Update possible sums for the current row
        new_sums = set()
        for num in row:
            for s in possible_sums:
                new_sums.add(s + num)
        possible_sums = new_sums
    
    # Find the minimum absolute difference
    return min(abs(target - s) for s in possible_sums)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[1,2,3],[4,5,6],[7,8,9]]
    target1 = 13
    print(minimizeTheDifference(mat1, target1))  # Output: 0

    # Test Case 2
    mat2 = [[1],[2],[3]]
    target2 = 100
    print(minimizeTheDifference(mat2, target2))  # Output: 94

    # Test Case 3
    mat3 = [[1,2,9,8,7]]
    target3 = 6
    print(minimizeTheDifference(mat3, target3))  # Output: 1

    # Additional Test Case
    mat4 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    target4 = 30
    print(minimizeTheDifference(mat4, target4))  # Output: 0


# Time and Space Complexity Analysis
"""
Time Complexity:
- Let m be the number of rows and n be the number of columns in the matrix.
- For each row, we iterate over all possible sums from the previous rows and add each element in the current row.
- In the worst case, the number of possible sums grows exponentially with m and n.
- Therefore, the time complexity is approximately O(m * n * |possible_sums|), where |possible_sums| depends on the range of values.

Space Complexity:
- We use a set to store possible sums, which can grow significantly depending on the range of values in the matrix.
- In the worst case, the space complexity is O(|possible_sums|), where |possible_sums| depends on the range of values.

Overall, this solution is efficient for the given constraints but may struggle with very large matrices or targets.
"""

# Topic: Dynamic Programming