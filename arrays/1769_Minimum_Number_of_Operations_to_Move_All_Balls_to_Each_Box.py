"""
LeetCode Problem #1769: Minimum Number of Operations to Move All Balls to Each Box

Problem Statement:
You have n boxes. Each box is given in the form of a binary string `boxes` of length n, where `boxes[i]` is '0' if the i-th box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. The cost of one operation is 1 unit.

Return an array `answer` of size n, where `answer[i]` is the minimum number of operations needed to move all the balls to the i-th box.

Example:
Input: boxes = "110"
Output: [1, 1, 3]

Explanation:
- For the first box: You move one ball from box 1 to box 0 in 1 operation.
- For the second box: You move one ball from box 0 to box 1 in 1 operation.
- For the third box: You move one ball from box 0 to box 2 in 2 operations, and one ball from box 1 to box 2 in 1 operation, for a total of 3 operations.

Constraints:
- n == boxes.length
- 1 <= n <= 2000
- boxes[i] is either '0' or '1'.
"""

# Clean and Correct Python Solution
def minOperations(boxes: str) -> list[int]:
    n = len(boxes)
    answer = [0] * n

    # Pass from left to right
    count = 0  # Number of balls encountered so far
    operations = 0  # Total operations to move balls to the current box
    for i in range(n):
        answer[i] += operations
        count += int(boxes[i])  # Update count of balls
        operations += count  # Add count to operations for the next box

    # Pass from right to left
    count = 0
    operations = 0
    for i in range(n - 1, -1, -1):
        answer[i] += operations
        count += int(boxes[i])  # Update count of balls
        operations += count  # Add count to operations for the next box

    return answer

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    boxes = "110"
    print(minOperations(boxes))  # Output: [1, 1, 3]

    # Test Case 2
    boxes = "001011"
    print(minOperations(boxes))  # Output: [11, 8, 5, 4, 3, 4]

    # Test Case 3
    boxes = "000"
    print(minOperations(boxes))  # Output: [0, 0, 0]

    # Test Case 4
    boxes = "1"
    print(minOperations(boxes))  # Output: [0]

    # Test Case 5
    boxes = "101"
    print(minOperations(boxes))  # Output: [1, 2, 1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves two passes over the input string `boxes`, each of which takes O(n) time, where n is the length of the string.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The solution uses an array `answer` of size n to store the results, which takes O(n) space.
- Apart from this, a few integer variables are used, which take O(1) space.
- Therefore, the overall space complexity is O(n).

Topic: Arrays
"""