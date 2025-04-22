"""
LeetCode Problem #596: Classes More Than 5 Students

Problem Statement:
Table: `Courses`
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key column for this table.

Write an SQL query to find all classes that have at least 5 students.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+

Output:
+----------+
| class    |
+----------+
| Math     |
+----------+

Explanation:
- Math has 6 students, so it is included in the output.
- English, Biology, and Computer have less than 5 students, so they are not included.
"""

# Python Solution:
# Since this is an SQL problem, we will simulate the solution using Python for demonstration purposes.

from collections import defaultdict

def classes_with_more_than_5_students(courses):
    """
    Function to find all classes that have at least 5 students.

    :param courses: List of tuples where each tuple represents (student, class)
    :return: List of classes with at least 5 students
    """
    # Dictionary to count the number of students in each class
    class_count = defaultdict(int)
    
    # Count the number of students in each class
    for student, class_name in courses:
        class_count[class_name] += 1
    
    # Filter classes with at least 5 students
    result = [class_name for class_name, count in class_count.items() if count >= 5]
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    courses = [
        ("A", "Math"),
        ("B", "English"),
        ("C", "Math"),
        ("D", "Biology"),
        ("E", "Math"),
        ("F", "Computer"),
        ("G", "Math"),
        ("H", "Math"),
        ("I", "Math")
    ]
    print(classes_with_more_than_5_students(courses))  # Output: ['Math']

    # Test Case 2
    courses = [
        ("A", "Physics"),
        ("B", "Physics"),
        ("C", "Physics"),
        ("D", "Physics"),
        ("E", "Physics"),
        ("F", "Chemistry"),
        ("G", "Chemistry"),
        ("H", "Chemistry"),
        ("I", "Chemistry"),
        ("J", "Chemistry")
    ]
    print(classes_with_more_than_5_students(courses))  # Output: ['Physics', 'Chemistry']

    # Test Case 3
    courses = [
        ("A", "History"),
        ("B", "History"),
        ("C", "History"),
        ("D", "History")
    ]
    print(classes_with_more_than_5_students(courses))  # Output: []

# Time and Space Complexity Analysis:
# Time Complexity:
# - Counting the number of students in each class takes O(n), where n is the number of entries in the `courses` list.
# - Filtering the classes with at least 5 students takes O(k), where k is the number of unique classes.
# - Overall time complexity: O(n + k).

# Space Complexity:
# - The `class_count` dictionary stores counts for each unique class, which requires O(k) space, where k is the number of unique classes.
# - The result list stores the classes with at least 5 students, which requires O(m) space, where m is the number of such classes.
# - Overall space complexity: O(k + m).

# Topic: Hash Table