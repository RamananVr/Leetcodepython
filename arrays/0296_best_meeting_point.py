"""
LeetCode Question #296: Best Meeting Point

Problem Statement:
A group of two or more people wants to meet and minimize the total travel distance. 
You are given a 2D grid of values 0 or 1, where each 1 marks a home of someone in the group. 
The distance is calculated using Manhattan Distance, where distance between (x1, y1) and (x2, y2) is 
|x1 - x2| + |y1 - y2|.

Return the minimum total travel distance.

Example:
Input: 
grid = [
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]
Output: 6

Explanation:
The point (0, 2) is the best meeting point, with a total travel distance of 6.

Constraints:
- The number of rows and columns in the grid is at most 200.
- The number of people in the group is at least 2.
"""

# Solution
def minTotalDistance(grid):
    """
    Finds the minimum total travel distance for a group of people in a 2D grid.

    :param grid: List[List[int]] - 2D grid where 1 represents a home and 0 represents an empty space.
    :return: int - Minimum total travel distance.
    """
    def collect_coordinates(grid, axis):
        """
        Collects all coordinates along a given axis (rows or columns).
        """
        coordinates = []
        if axis == "row":
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        coordinates.append(i)
        elif axis == "col":
            for j in range(len(grid[0])):
                for i in range(len(grid)):
                    if grid[i][j] == 1:
                        coordinates.append(j)
        return coordinates

    # Collect all row and column coordinates of homes
    rows = collect_coordinates(grid, "row")
    cols = collect_coordinates(grid, "col")

    # Find the median of rows and columns
    def find_median(coordinates):
        coordinates.sort()
        mid = len(coordinates) // 2
        return coordinates[mid]

    row_median = find_median(rows)
    col_median = find_median(cols)

    # Calculate total travel distance
    total_distance = sum(abs(row - row_median) for row in rows) + sum(abs(col - col_median) for col in cols)
    return total_distance

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]
    print(minTotalDistance(grid1))  # Output: 6

    # Test Case 2
    grid2 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print(minTotalDistance(grid2))  # Output: 4

    # Test Case 3
    grid3 = [
        [1, 1],
        [1, 1]
    ]
    print(minTotalDistance(grid3))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- Collecting coordinates: O(m * n), where m is the number of rows and n is the number of columns in the grid.
- Sorting coordinates: O(k * log(k)), where k is the number of homes (1s in the grid).
- Calculating total distance: O(k).
Overall: O(m * n + k * log(k)).

Space Complexity:
- Storing coordinates: O(k), where k is the number of homes.
Overall: O(k).

Topic: Arrays
"""