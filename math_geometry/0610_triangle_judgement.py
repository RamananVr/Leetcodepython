"""
LeetCode Question #610: Triangle Judgement

Problem Statement:
Table: Triangle

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
(x, y, z) is the primary key column for this table.
Each row of this table contains three integers x, y, and z representing the lengths of three line segments.

Write an SQL query to report for every row in the table whether the three line segments can form a triangle. 
Return the result table in any order.

A triangle is valid if the sum of any two sides is greater than the third side.

The result format is in the following example:

Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+

Result table:
+----+----+----+-------+
| x  | y  | z  | valid |
+----+----+----+-------+
| 13 | 15 | 30 | No    |
| 10 | 20 | 15 | Yes   |
+----+----+----+-------+
"""

# Clean, Correct Python Solution
# Since this is an SQL problem, we will simulate the solution in Python.

def is_triangle_valid(x, y, z):
    """
    Function to determine if three sides can form a valid triangle.
    A triangle is valid if the sum of any two sides is greater than the third side.
    """
    if x + y > z and x + z > y and y + z > x:
        return "Yes"
    else:
        return "No"

# Example Test Cases
if __name__ == "__main__":
    # Test case 1
    x1, y1, z1 = 13, 15, 30
    print(f"Triangle sides ({x1}, {y1}, {z1}) -> Valid: {is_triangle_valid(x1, y1, z1)}")  # Expected: No

    # Test case 2
    x2, y2, z2 = 10, 20, 15
    print(f"Triangle sides ({x2}, {y2}, {z2}) -> Valid: {is_triangle_valid(x2, y2, z2)}")  # Expected: Yes

    # Test case 3
    x3, y3, z3 = 7, 10, 5
    print(f"Triangle sides ({x3}, {y3}, {z3}) -> Valid: {is_triangle_valid(x3, y3, z3)}")  # Expected: Yes

    # Test case 4
    x4, y4, z4 = 1, 2, 3
    print(f"Triangle sides ({x4}, {y4}, {z4}) -> Valid: {is_triangle_valid(x4, y4, z4)}")  # Expected: No

    # Test case 5
    x5, y5, z5 = 6, 8, 10
    print(f"Triangle sides ({x5}, {y5}, {z5}) -> Valid: {is_triangle_valid(x5, y5, z5)}")  # Expected: Yes

# Time and Space Complexity Analysis
# Time Complexity: O(1) for each triangle check, as it involves a constant number of comparisons and additions.
# Space Complexity: O(1), as no additional data structures are used.

# Topic: Math / Geometry