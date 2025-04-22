"""
LeetCode Problem #699: Falling Squares

Problem Statement:
You are given an array `positions` where `positions[i] = [left, side_length]` represents the ith square dropped with its left edge aligned at `left` and having a side length of `side_length`. Each square is dropped one at a time from a height sufficient to ensure it lands on top of either another square or the ground.

Return a list `ans` where `ans[i]` represents the height of the tallest stack of squares after the ith square is dropped.

Constraints:
1. 1 <= positions.length <= 1000
2. 1 <= positions[i][0] <= 10^8
3. 1 <= positions[i][1] <= 10^6

Example:
Input: positions = [[1, 2], [2, 3], [6, 1]]
Output: [2, 5, 5]

Explanation:
- After the first square is dropped, the height of the stack is 2.
- After the second square is dropped, the height of the stack is 5.
- After the third square is dropped, the height of the stack remains 5.

Topic: Arrays, Simulation, Segment Tree
"""

def fallingSquares(positions):
    """
    Simulates the falling of squares and calculates the height of the tallest stack after each drop.

    :param positions: List[List[int]] - List of positions where each position is [left, side_length].
    :return: List[int] - List of heights of the tallest stack after each square is dropped.
    """
    intervals = []  # To store the intervals and their heights
    result = []     # To store the maximum height after each square drop
    max_height = 0  # Tracks the global maximum height

    for left, side_length in positions:
        right = left + side_length  # Calculate the right edge of the square
        current_height = 0

        # Check for overlap with existing intervals
        for l, r, h in intervals:
            if not (right <= l or left >= r):  # Overlap condition
                current_height = max(current_height, h)

        # Add the height of the current square
        current_height += side_length
        max_height = max(max_height, current_height)

        # Add the current interval to the list
        intervals.append((left, right, current_height))
        result.append(max_height)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    positions = [[1, 2], [2, 3], [6, 1]]
    print(fallingSquares(positions))  # Output: [2, 5, 5]

    # Test Case 2
    positions = [[100, 100], [200, 100]]
    print(fallingSquares(positions))  # Output: [100, 100]

    # Test Case 3
    positions = [[1, 5], [2, 2], [7, 3]]
    print(fallingSquares(positions))  # Output: [5, 7, 7]

"""
Time Complexity:
- For each square, we iterate through the list of intervals to check for overlaps.
- In the worst case, there are O(n) intervals, and we process O(n) squares.
- Thus, the time complexity is O(n^2), where n is the number of squares.

Space Complexity:
- We store the intervals in a list, which can grow up to O(n) in size.
- The space complexity is O(n).

Topic: Arrays, Simulation
"""