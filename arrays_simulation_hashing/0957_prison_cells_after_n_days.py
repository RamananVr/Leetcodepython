"""
LeetCode Question #957: Prison Cells After N Days

Problem Statement:
There are 8 prison cells in a row, and each cell is either occupied or vacant, represented by an integer array `cells` where `cells[i] == 1` if the `i`th cell is occupied, and `cells[i] == 0` if it is vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:
1. If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
2. Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

You are given the integer `N`, the number of days, and the initial state of the prison cells. Return the state of the prison after `N` days. The answer will always be the same for a given `N` and `cells`.

Constraints:
- `cells.length == 8`
- `cells[i]` is either `0` or `1`.
- `1 <= N <= 10^9`
"""

def prisonAfterNDays(cells, N):
    """
    Simulates the state of prison cells after N days.
    
    :param cells: List[int] - Initial state of the prison cells (length 8, values 0 or 1)
    :param N: int - Number of days
    :return: List[int] - State of the prison cells after N days
    """
    def next_day(cells):
        # Compute the next day's state based on the current state
        return [0] + [1 if cells[i - 1] == cells[i + 1] else 0 for i in range(1, 7)] + [0]

    seen = {}
    is_fast_forwarded = False

    while N > 0:
        if not is_fast_forwarded:
            # Convert the current state to a tuple and check if we've seen it before
            state_tuple = tuple(cells)
            if state_tuple in seen:
                # Cycle detected, calculate the remaining days modulo the cycle length
                cycle_length = seen[state_tuple] - N
                N %= cycle_length
                is_fast_forwarded = True
            else:
                # Store the current state and the remaining days
                seen[state_tuple] = N

        # If there are still days left, simulate the next day
        if N > 0:
            N -= 1
            cells = next_day(cells)

    return cells

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cells = [0, 1, 0, 1, 1, 0, 0, 1]
    N = 7
    print(prisonAfterNDays(cells, N))  # Output: [0, 0, 1, 1, 0, 0, 0, 0]

    # Test Case 2
    cells = [1, 0, 0, 1, 0, 0, 1, 0]
    N = 1000000000
    print(prisonAfterNDays(cells, N))  # Output: [0, 0, 1, 1, 1, 1, 1, 0]

    # Test Case 3
    cells = [1, 1, 1, 0, 0, 0, 1, 1]
    N = 15
    print(prisonAfterNDays(cells, N))  # Output: [0, 0, 0, 0, 0, 1, 1, 0]

"""
Time and Space Complexity Analysis:

Time Complexity:
- In the worst case, we simulate up to 2^6 = 64 unique states (since there are 6 middle cells, each of which can be 0 or 1).
- If a cycle is detected, we fast-forward the simulation, reducing the number of iterations.
- Thus, the time complexity is O(64) = O(1) for detecting cycles and simulating states.

Space Complexity:
- We store up to 64 unique states in the `seen` dictionary.
- The space complexity is O(64) = O(1).

Overall, the solution is efficient due to the small number of possible states.

Topic: Arrays, Simulation, Hashing
"""