"""
LeetCode Problem #196: Delete Duplicate Emails

Problem Statement:
Write a SQL query to delete all duplicate email entries in a table named `Person`, keeping only the smallest `Id`.

For example, after running your query, the `Person` table should look like this:

Input:
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+

Output:
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+

Explanation:
john@example.com is repeated twice. We keep the row with the smallest Id = 1.

Note:
- The `Id` column is the primary key for this table.
- You are only required to write the SQL query for this problem.

Since this is a SQL problem, we will simulate the solution in Python for educational purposes.
"""

# Python Solution (Simulating SQL Behavior)
def delete_duplicate_emails(person_table):
    """
    Simulates the deletion of duplicate emails from a table, keeping only the smallest Id.

    Args:
    person_table (list of dict): A list of dictionaries representing the Person table.
                                 Each dictionary has keys 'Id' and 'Email'.

    Returns:
    list of dict: The updated table with duplicates removed.
    """
    # Create a dictionary to store the smallest Id for each email
    email_to_id = {}

    # Iterate through the table to find the smallest Id for each email
    for row in person_table:
        email = row['Email']
        id_ = row['Id']
        if email not in email_to_id or id_ < email_to_id[email]:
            email_to_id[email] = id_

    # Filter the table to include only rows with the smallest Id for each email
    result_table = [row for row in person_table if row['Id'] == email_to_id[row['Email']]]

    # Sort the result by Id to maintain order
    result_table.sort(key=lambda x: x['Id'])

    return result_table


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    person_table = [
        {"Id": 1, "Email": "john@example.com"},
        {"Id": 2, "Email": "bob@example.com"},
        {"Id": 3, "Email": "john@example.com"}
    ]
    print(delete_duplicate_emails(person_table))
    # Expected Output:
    # [{'Id': 1, 'Email': 'john@example.com'}, {'Id': 2, 'Email': 'bob@example.com'}]

    # Test Case 2
    person_table = [
        {"Id": 4, "Email": "alice@example.com"},
        {"Id": 5, "Email": "alice@example.com"},
        {"Id": 6, "Email": "charlie@example.com"}
    ]
    print(delete_duplicate_emails(person_table))
    # Expected Output:
    # [{'Id': 4, 'Email': 'alice@example.com'}, {'Id': 6, 'Email': 'charlie@example.com'}]

    # Test Case 3
    person_table = [
        {"Id": 7, "Email": "dave@example.com"},
        {"Id": 8, "Email": "eve@example.com"},
        {"Id": 9, "Email": "dave@example.com"},
        {"Id": 10, "Email": "eve@example.com"}
    ]
    print(delete_duplicate_emails(person_table))
    # Expected Output:
    # [{'Id': 7, 'Email': 'dave@example.com'}, {'Id': 8, 'Email': 'eve@example.com'}]


# Time and Space Complexity Analysis

# Time Complexity:
# - Iterating through the table to populate the `email_to_id` dictionary takes O(n), where n is the number of rows.
# - Filtering the table to create the result takes O(n).
# - Sorting the result table takes O(n log n).
# Overall time complexity: O(n log n).

# Space Complexity:
# - The `email_to_id` dictionary requires O(k) space, where k is the number of unique emails.
# - The result table requires O(n) space.
# Overall space complexity: O(n).

# Topic: Hash Table