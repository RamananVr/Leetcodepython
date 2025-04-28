"""
LeetCode Problem #799: Champagne Tower

Problem Statement:
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the nth row. Each glass holds one cup of champagne.

- We pour `poured` cups of champagne into the top glass of the tower.
- When a glass overflows, the excess champagne is equally distributed to the two glasses below it.
- Once a glass reaches its capacity (1 cup), it cannot hold more champagne.

Given two integers `poured` (the number of cups of champagne poured into the top glass) and `query_row` (the row number, 0-indexed) and `query_glass` (the glass index in that row, 0-indexed), return how full the glass in `query_row` and `query_glass` is. If the glass is overfilled, return 1.

Constraints:
- 0 <= poured <= 10^9
- 0 <= query_row < 100
- 0 <= query_glass <= query_row
"""

def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    # Initialize a 2D list to store the amount of champagne in each glass
    tower = [[0] * (i + 1) for i in range(query_row + 1)]
    
    # Pour champagne into the top glass
    tower[0][0] = poured
    
    # Iterate through each row up to query_row
    for row in range(query_row):
        for glass in range(row + 1):
            # If the current glass overflows
            if tower[row][glass] > 1:
                excess = tower[row][glass] - 1
                tower[row][glass] = 1  # Cap the current glass at 1
                
                # Distribute the excess champagne equally to the two glasses below
                tower[row + 1][glass] += excess / 2
                tower[row + 1][glass + 1] += excess / 2
    
    # Return the amount of champagne in the target glass, capped at 1
    return min(1, tower[query_row][query_glass])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic case
    poured = 1
    query_row = 1
    query_glass = 1
    print(champagneTower(poured, query_row, query_glass))  # Output: 0.0

    # Test Case 2: Overflowing champagne
    poured = 2
    query_row = 1
    query_glass = 1
    print(champagneTower(poured, query_row, query_glass))  # Output: 0.5

    # Test Case 3: Large pour
    poured = 100
    query_row = 4
    query_glass = 2
    print(champagneTower(poured, query_row, query_glass))  # Output: 1.0

    # Test Case 4: Edge case with no champagne
    poured = 0
    query_row = 0
    query_glass = 0
    print(champagneTower(poured, query_row, query_glass))  # Output: 0.0

    # Test Case 5: Edge case with large row and glass indices
    poured = 10
    query_row = 3
    query_glass = 2
    print(champagneTower(poured, query_row, query_glass))  # Output: 0.25

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through each row up to `query_row` and each glass in that row.
- The total number of glasses processed is approximately (query_row * (query_row + 1)) / 2.
- Therefore, the time complexity is O(query_row^2).

Space Complexity:
- The algorithm uses a 2D list `tower` to store the champagne levels for all glasses up to `query_row`.
- The space required is proportional to the number of glasses, which is approximately (query_row * (query_row + 1)) / 2.
- Therefore, the space complexity is O(query_row^2).

Topic: Dynamic Programming
"""