"""
LeetCode Question #2120: Execution of All Suffix Instructions Staying in a Grid

Problem Statement:
You are given an n x n grid, a starting position (startPos) in the grid, and a string s of instructions. Each instruction in s moves the position in the grid according to the following rules:
- 'L' moves left (decrease the column index by 1),
- 'R' moves right (increase the column index by 1),
- 'U' moves up (decrease the row index by 1),
- 'D' moves down (increase the row index by 1).

The position stays within the grid boundaries; if an instruction causes the position to go outside the grid, it is ignored.

Return an array answer of length s.length where answer[i] is the number of instructions that can be executed starting from the ith instruction in s and moving forward without going outside the grid.

Example:
Input: n = 3, startPos = [0, 1], s = "RRDDLU"
Output: [1, 5, 4, 3, 1, 0]

Constraints:
- 1 <= n <= 500
- startPos.length == 2
- 0 <= startPos[0], startPos[1] < n
- 1 <= s.length <= 500
- s consists of 'L', 'R', 'U', 'D'.

"""

# Python Solution
def executeInstructions(n, startPos, s):
    def canExecute(start_row, start_col, instructions):
        row, col = start_row, start_col
        count = 0
        for instruction in instructions:
            if instruction == 'L':
                col -= 1
            elif instruction == 'R':
                col += 1
            elif instruction == 'U':
                row -= 1
            elif instruction == 'D':
                row += 1
            
            if 0 <= row < n and 0 <= col < n:
                count += 1
            else:
                break
        return count
    
    result = []
    for i in range(len(s)):
        result.append(canExecute(startPos[0], startPos[1], s[i:]))
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    startPos = [0, 1]
    s = "RRDDLU"
    print(executeInstructions(n, startPos, s))  # Output: [1, 5, 4, 3, 1, 0]

    # Test Case 2
    n = 2
    startPos = [1, 1]
    s = "LURD"
    print(executeInstructions(n, startPos, s))  # Output: [4, 1, 0, 0]

    # Test Case 3
    n = 1
    startPos = [0, 0]
    s = "LRUD"
    print(executeInstructions(n, startPos, s))  # Output: [0, 0, 0, 0]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop iterates over each instruction in the string `s`, which has a length of `m`.
- For each instruction, the inner loop simulates the movement, which can take up to `m` steps in the worst case.
- Therefore, the overall time complexity is O(m^2), where `m` is the length of the string `s`.

Space Complexity:
- The space complexity is O(1) since we are only using a few variables to track the current position and count.

Topic: Arrays, Simulation
"""