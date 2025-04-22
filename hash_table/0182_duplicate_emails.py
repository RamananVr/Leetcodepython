"""
LeetCode Question #182: Duplicate Emails

Problem Statement:
Write a SQL query to find all duplicate emails in a table named `Person`.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+

For the above table, your query should return the following result:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+

Note:
- The `Id` column is the primary key for this table.
- Your output should not contain duplicate emails.

Since this is a SQL problem, we will simulate the solution in Python for educational purposes.
"""

# Python Solution
from collections import Counter

def find_duplicate_emails(person):
    """
    Function to find duplicate emails from a list of dictionaries representing the Person table.

    :param person: List[Dict[str, str]] - A list of dictionaries where each dictionary represents a row in the Person table.
    :return: List[str] - A list of duplicate emails.
    """
    # Extract all emails from the input
    emails = [row['Email'] for row in person]
    
    # Count the occurrences of each email
    email_counts = Counter(emails)
    
    # Filter emails that appear more than once
    duplicates = [email for email, count in email_counts.items() if count > 1]
    
    return duplicates

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    person_table = [
        {"Id": 1, "Email": "a@b.com"},
        {"Id": 2, "Email": "c@d.com"},
        {"Id": 3, "Email": "a@b.com"}
    ]
    print(find_duplicate_emails(person_table))  # Output: ['a@b.com']

    # Test Case 2
    person_table = [
        {"Id": 1, "Email": "x@y.com"},
        {"Id": 2, "Email": "z@w.com"},
        {"Id": 3, "Email": "x@y.com"},
        {"Id": 4, "Email": "x@y.com"}
    ]
    print(find_duplicate_emails(person_table))  # Output: ['x@y.com']

    # Test Case 3
    person_table = [
        {"Id": 1, "Email": "unique@domain.com"},
        {"Id": 2, "Email": "another@domain.com"}
    ]
    print(find_duplicate_emails(person_table))  # Output: []

"""
Time and Space Complexity Analysis:

Time Complexity:
- Extracting emails from the input list takes O(n), where n is the number of rows in the `person` table.
- Counting the occurrences of each email using `Counter` also takes O(n).
- Filtering the duplicates from the `Counter` dictionary takes O(m), where m is the number of unique emails.
- Overall, the time complexity is O(n + m). In the worst case, m ≈ n, so the complexity simplifies to O(n).

Space Complexity:
- The `emails` list requires O(n) space to store all email addresses.
- The `Counter` dictionary requires O(m) space to store the counts of unique emails.
- The `duplicates` list requires O(k) space, where k is the number of duplicate emails.
- Overall, the space complexity is O(n + m + k). In the worst case, this simplifies to O(n).

Topic: Hash Table
"""