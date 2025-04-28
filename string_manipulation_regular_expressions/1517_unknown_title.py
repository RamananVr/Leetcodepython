"""
LeetCode Problem #1517: Find Users With Valid E-Mails

Problem Statement:
Given a table `Users` with the following structure:

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| name        | varchar |
| email       | varchar |
+-------------+---------+
user_id is the primary key for this table.
Each row of this table contains the name and email of a user. 

Write an SQL query to find the users who have valid emails. A valid email has all the following properties:
1. The email contains exactly one '@' character.
2. The local part (the part before '@') and the domain part (the part after '@') are both non-empty.
3. The domain part contains at least one '.' character.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Users table:
+---------+----------+-------------------------+
| user_id | name     | email                   |
+---------+----------+-------------------------+
| 1       | Alice    | alice@example.com       |
| 2       | Bob      | bob@leetcode            |
| 3       | Charlie  | @charlie.com            |
| 4       | David    | david@david@david.com   |
| 5       | Eve      | eve@leetcode.com        |
+---------+----------+-------------------------+

Output:
+---------+----------+-------------------------+
| user_id | name     | email                   |
+---------+----------+-------------------------+
| 1       | Alice    | alice@example.com       |
| 5       | Eve      | eve@leetcode.com        |
+---------+----------+-------------------------+

Explanation:
- Alice's email is valid because it contains one '@' character, and the domain part contains a '.'.
- Bob's email is invalid because the domain part does not contain a '.'.
- Charlie's email is invalid because the local part is empty.
- David's email is invalid because it contains two '@' characters.
- Eve's email is valid because it contains one '@' character, and the domain part contains a '.'.
"""

# Python Solution (Simulating SQL Query in Python)
import re

def find_valid_emails(users):
    """
    Function to filter users with valid emails based on the given criteria.
    
    Args:
    users (list of dict): A list of dictionaries where each dictionary represents a user with keys 'user_id', 'name', and 'email'.
    
    Returns:
    list of dict: A list of dictionaries containing users with valid emails.
    """
    valid_users = []
    for user in users:
        email = user['email']
        # Check if the email matches the criteria using regex
        if re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            valid_users.append(user)
    return valid_users

# Example Test Cases
if __name__ == "__main__":
    users = [
        {"user_id": 1, "name": "Alice", "email": "alice@example.com"},
        {"user_id": 2, "name": "Bob", "email": "bob@leetcode"},
        {"user_id": 3, "name": "Charlie", "email": "@charlie.com"},
        {"user_id": 4, "name": "David", "email": "david@david@david.com"},
        {"user_id": 5, "name": "Eve", "email": "eve@leetcode.com"}
    ]
    
    valid_users = find_valid_emails(users)
    print("Valid Users:")
    for user in valid_users:
        print(user)

"""
Output:
Valid Users:
{'user_id': 1, 'name': 'Alice', 'email': 'alice@example.com'}
{'user_id': 5, 'name': 'Eve', 'email': 'eve@leetcode.com'}
"""

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the list of users, so the time complexity is O(n), where n is the number of users.
- The regex match operation is O(m), where m is the length of the email string. In the worst case, this is O(n * m).

Space Complexity:
- The space complexity is O(k), where k is the number of valid users stored in the `valid_users` list.
- The regex pattern itself uses constant space.

Overall, the space complexity is O(k), and the time complexity is O(n * m).
"""

# Topic: String Manipulation, Regular Expressions