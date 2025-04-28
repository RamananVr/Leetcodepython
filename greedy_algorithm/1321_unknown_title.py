"""
LeetCode Problem #1321: Restaurant Growth

Problem Statement:
A restaurant has a certain number of tables, and each table can seat a fixed number of customers. 
The restaurant wants to maximize its revenue by seating customers optimally. You are given two arrays:
1. `tables` where `tables[i]` represents the number of seats at the i-th table.
2. `groups` where `groups[j]` represents the number of customers in the j-th group.

The restaurant can only seat a group at a table if the number of customers in the group is less than or equal to the number of seats at the table. 
Each group seated at a table generates revenue equal to the number of customers in the group. 
Once a table is used, it cannot be reused. Similarly, once a group is seated, it cannot be reseated.

Write a function `maxRevenue(tables: List[int], groups: List[int]) -> int` that returns the maximum revenue the restaurant can generate.

Constraints:
- 1 <= len(tables), len(groups) <= 10^4
- 1 <= tables[i], groups[j] <= 10^4
"""

from typing import List

def maxRevenue(tables: List[int], groups: List[int]) -> int:
    """
    Calculate the maximum revenue the restaurant can generate by seating groups optimally.
    """
    # Sort tables and groups in descending order
    tables.sort(reverse=True)
    groups.sort(reverse=True)
    
    revenue = 0
    table_index = 0
    
    # Iterate through each group
    for group in groups:
        # Find the first table that can accommodate the group
        while table_index < len(tables) and tables[table_index] < group:
            table_index += 1
        
        # If a suitable table is found, seat the group and add to revenue
        if table_index < len(tables):
            revenue += group
            table_index += 1  # Move to the next table
    
    return revenue

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tables = [4, 6, 8]
    groups = [5, 3, 8]
    print(maxRevenue(tables, groups))  # Expected Output: 16

    # Test Case 2
    tables = [2, 3, 5]
    groups = [1, 2, 4]
    print(maxRevenue(tables, groups))  # Expected Output: 7

    # Test Case 3
    tables = [10, 10, 10]
    groups = [10, 10, 10]
    print(maxRevenue(tables, groups))  # Expected Output: 30

    # Test Case 4
    tables = [1, 2, 3]
    groups = [4, 5, 6]
    print(maxRevenue(tables, groups))  # Expected Output: 0

    # Test Case 5
    tables = [5, 5, 5]
    groups = [5, 5, 5, 5]
    print(maxRevenue(tables, groups))  # Expected Output: 15

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the `tables` and `groups` arrays takes O(n log n) and O(m log m), where n is the length of `tables` and m is the length of `groups`.
- The iteration through the `groups` array takes O(m), and the inner loop to find a suitable table takes O(n) in the worst case.
- Overall, the time complexity is O(n log n + m log m + m * n). However, since the problem constraints are manageable, this approach is efficient.

Space Complexity:
- The space complexity is O(1) as we are sorting the arrays in-place and using a constant amount of extra space.

Topic: Greedy Algorithm
"""