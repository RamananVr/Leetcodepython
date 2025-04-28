"""
LeetCode Problem #1179: Reformat Department Table

Problem Statement:
Table: `Department`
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| revenue     | int     |
| month       | varchar |
+-------------+---------+
(id, month) is the primary key of this table.
The table contains information about the revenue of each department per month.

Write an SQL query to reformat the table such that there is a department id column and a revenue column for each month.

The result table should be in the following format:
+-------------+-------------+-------------+-------------+-------------+
| id          | Jan_Revenue | Feb_Revenue | Mar_Revenue | Apr_Revenue |
+-------------+-------------+-------------+-------------+-------------+
| 1           | 100         | 200         | 300         | 400         |
| 2           | 500         | 600         | 700         | 800         |
+-------------+-------------+-------------+-------------+-------------+

The SQL query should return the reformatted table. The order of the rows in the output does not matter.

Note:
The solution to this problem is an SQL query, not a Python function. However, for completeness, we will provide a Python solution to simulate the transformation of the data.

"""

# Python Solution to Simulate the Transformation of the Data

def reformat_department_table(department_data):
    """
    Reformats the department table to have a revenue column for each month.

    Args:
        department_data (list of dict): A list of dictionaries representing the department table.
                                        Each dictionary contains 'id', 'revenue', and 'month'.

    Returns:
        list of dict: Reformatted table with 'id' and revenue columns for each month.
    """
    # Create a dictionary to store the reformatted data
    reformatted_data = {}

    # Iterate through the department data
    for record in department_data:
        department_id = record['id']
        month = record['month']
        revenue = record['revenue']

        # Initialize the department entry if it doesn't exist
        if department_id not in reformatted_data:
            reformatted_data[department_id] = {'id': department_id}

        # Add the revenue for the corresponding month
        reformatted_data[department_id][f"{month}_Revenue"] = revenue

    # Convert the dictionary to a list of dictionaries
    return list(reformatted_data.values())


# Example Test Cases
if __name__ == "__main__":
    # Input data
    department_data = [
        {'id': 1, 'revenue': 100, 'month': 'Jan'},
        {'id': 1, 'revenue': 200, 'month': 'Feb'},
        {'id': 1, 'revenue': 300, 'month': 'Mar'},
        {'id': 1, 'revenue': 400, 'month': 'Apr'},
        {'id': 2, 'revenue': 500, 'month': 'Jan'},
        {'id': 2, 'revenue': 600, 'month': 'Feb'},
        {'id': 2, 'revenue': 700, 'month': 'Mar'},
        {'id': 2, 'revenue': 800, 'month': 'Apr'},
    ]

    # Expected output
    expected_output = [
        {'id': 1, 'Jan_Revenue': 100, 'Feb_Revenue': 200, 'Mar_Revenue': 300, 'Apr_Revenue': 400},
        {'id': 2, 'Jan_Revenue': 500, 'Feb_Revenue': 600, 'Mar_Revenue': 700, 'Apr_Revenue': 800},
    ]

    # Run the function
    output = reformat_department_table(department_data)

    # Print the output
    print("Output:")
    for row in output:
        print(row)

    # Verify the output
    assert output == expected_output, "Test case failed!"
    print("Test case passed!")


# Time and Space Complexity Analysis

"""
Time Complexity:
- The function iterates through the `department_data` list once, which takes O(n) time, where n is the number of records in the input data.
- The dictionary operations (insertion and lookup) are O(1) on average.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The function uses a dictionary to store the reformatted data. In the worst case, the dictionary will have as many entries as there are unique department IDs, and each entry will have a fixed number of keys (one for each month).
- The space complexity is O(m), where m is the number of unique department IDs.
"""

# Topic: SQL Transformation / Data Manipulation