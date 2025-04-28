"""
LeetCode Problem #2408: Design SQL-like Data Structure

Problem Statement:
You are tasked with designing a data structure that supports SQL-like operations. Specifically, you need to implement a class `DataStructure` that supports the following methods:

1. `insert(row: List[int]) -> None`: Inserts a row of integers into the data structure.
2. `delete(condition: Callable[[List[int]], bool]) -> None`: Deletes all rows that satisfy the given condition.
3. `query(condition: Callable[[List[int]], bool]) -> List[List[int]]`: Returns all rows that satisfy the given condition.

The `condition` parameter is a callable function that takes a row (a list of integers) as input and returns a boolean value indicating whether the row satisfies the condition.

Constraints:
- The number of rows inserted will not exceed 10^4.
- Each row will have a fixed number of integers (e.g., 2 ≤ len(row) ≤ 10).
- The integers in the rows will be in the range [-10^6, 10^6].

Your implementation should be efficient and handle the operations within reasonable time limits.

Example:
    ds = DataStructure()
    ds.insert([1, 2, 3])
    ds.insert([4, 5, 6])
    ds.insert([7, 8, 9])
    ds.delete(lambda row: row[0] == 4)
    result = ds.query(lambda row: row[2] > 5)
    print(result)  # Output: [[7, 8, 9]]
"""

from typing import List, Callable

class DataStructure:
    def __init__(self):
        # Initialize an empty list to store rows
        self.rows = []

    def insert(self, row: List[int]) -> None:
        """
        Inserts a row of integers into the data structure.
        """
        self.rows.append(row)

    def delete(self, condition: Callable[[List[int]], bool]) -> None:
        """
        Deletes all rows that satisfy the given condition.
        """
        self.rows = [row for row in self.rows if not condition(row)]

    def query(self, condition: Callable[[List[int]], bool]) -> List[List[int]]:
        """
        Returns all rows that satisfy the given condition.
        """
        return [row for row in self.rows if condition(row)]


# Example Test Cases
if __name__ == "__main__":
    ds = DataStructure()
    
    # Insert rows
    ds.insert([1, 2, 3])
    ds.insert([4, 5, 6])
    ds.insert([7, 8, 9])
    
    # Delete rows where the first element is 4
    ds.delete(lambda row: row[0] == 4)
    
    # Query rows where the third element is greater than 5
    result = ds.query(lambda row: row[2] > 5)
    print(result)  # Output: [[7, 8, 9]]
    
    # Query rows where the second element is less than or equal to 2
    result = ds.query(lambda row: row[1] <= 2)
    print(result)  # Output: [[1, 2, 3]]

    # Insert more rows and query again
    ds.insert([10, 11, 12])
    result = ds.query(lambda row: row[0] > 5)
    print(result)  # Output: [[7, 8, 9], [10, 11, 12]]


# Time and Space Complexity Analysis

# 1. `insert(row)`:
#    - Time Complexity: O(1), as appending to a list is an O(1) operation.
#    - Space Complexity: O(1), excluding the space required to store the row.

# 2. `delete(condition)`:
#    - Time Complexity: O(n * m), where `n` is the number of rows and `m` is the length of each row.
#      This is because we iterate through all rows and apply the condition to each row.
#    - Space Complexity: O(n * m), as a new list is created to store the rows that do not satisfy the condition.

# 3. `query(condition)`:
#    - Time Complexity: O(n * m), where `n` is the number of rows and `m` is the length of each row.
#      This is because we iterate through all rows and apply the condition to each row.
#    - Space Complexity: O(k * m), where `k` is the number of rows that satisfy the condition.
#      This is because a new list is created to store the rows that satisfy the condition.

# Overall Space Complexity:
# The space complexity is dominated by the storage of rows, which is O(n * m), where `n` is the number of rows and `m` is the length of each row.

# Topic: Arrays