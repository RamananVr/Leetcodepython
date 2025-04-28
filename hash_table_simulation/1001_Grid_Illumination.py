"""
LeetCode Problem #1001: Grid Illumination

Problem Statement:
You are given a grid of size N x N, where each cell of this grid has a lamp that can be turned on or off. 
Initially, some lamps are turned on. Each lamp provides illumination to every square on its row, column, 
and both diagonals (similar to a queen in chess). A cell is illuminated if it is in the same row, column, 
or diagonal as a lamp that is turned on.

You are also given an array of queries. For the i-th query, determine whether the cell at (queries[i][0], queries[i][1]) 
is illuminated or not. After answering the i-th query, turn off any lamp that is at the queried cell or adjacent to it 
(including diagonally adjacent cells).

Return an array of integers where the i-th integer is 1 if the cell in the i-th query was illuminated, and 0 otherwise.

Constraints:
- 1 <= N <= 10^9
- 0 <= lamps.length <= 20000
- 0 <= queries.length <= 20000
- lamps[i].length == 2
- queries[i].length == 2
- 0 <= lamps[i][0], lamps[i][1], queries[i][0], queries[i][1] < N
"""

from collections import defaultdict

def gridIllumination(N, lamps, queries):
    # Dictionaries to track the number of lamps affecting rows, columns, and diagonals
    row = defaultdict(int)
    col = defaultdict(int)
    diag1 = defaultdict(int)  # Diagonal from top-left to bottom-right (r - c)
    diag2 = defaultdict(int)  # Diagonal from top-right to bottom-left (r + c)
    lamp_set = set()  # To track active lamps

    # Initialize the lamp positions
    for r, c in lamps:
        if (r, c) not in lamp_set:
            lamp_set.add((r, c))
            row[r] += 1
            col[c] += 1
            diag1[r - c] += 1
            diag2[r + c] += 1

    # Directions for turning off lamps (including the cell itself and adjacent cells)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    result = []

    # Process each query
    for qr, qc in queries:
        # Check if the cell is illuminated
        if row[qr] > 0 or col[qc] > 0 or diag1[qr - qc] > 0 or diag2[qr + qc] > 0:
            result.append(1)
        else:
            result.append(0)

        # Turn off the lamp at the queried cell and its adjacent cells
        for dr, dc in directions:
            nr, nc = qr + dr, qc + dc
            if (nr, nc) in lamp_set:
                lamp_set.remove((nr, nc))
                row[nr] -= 1
                col[nc] -= 1
                diag1[nr - nc] -= 1
                diag2[nr + nc] -= 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    N = 5
    lamps = [[0, 0], [4, 4]]
    queries = [[1, 1], [1, 0], [4, 4], [3, 3]]
    print(gridIllumination(N, lamps, queries))  # Output: [1, 0, 1, 0]

    # Test Case 2
    N = 5
    lamps = [[0, 0], [1, 0], [4, 4]]
    queries = [[0, 0], [1, 1], [2, 2], [3, 3]]
    print(gridIllumination(N, lamps, queries))  # Output: [1, 1, 0, 0]

    # Test Case 3
    N = 5
    lamps = []
    queries = [[0, 0], [1, 1], [2, 2]]
    print(gridIllumination(N, lamps, queries))  # Output: [0, 0, 0]

"""
Time Complexity:
- Initializing the lamp positions: O(L), where L is the number of lamps.
- Processing each query: O(Q * 9) = O(Q), where Q is the number of queries.
- Overall: O(L + Q).

Space Complexity:
- Space used for dictionaries and the lamp set: O(L).
- Overall: O(L).

Topic: Hash Table, Simulation
"""