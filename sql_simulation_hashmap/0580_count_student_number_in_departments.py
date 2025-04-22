"""
LeetCode Question #580: Count Student Number in Departments

Problem Statement:
The `Student` table holds information about students including their ID and the ID of the department they belong to. 
The `Department` table holds information about departments including their ID and the name of the department.

Write an SQL query to find the number of students in each department. The result table should include the department name 
and the number of students in that department. If a department has no students, it should still be included in the result 
with a count of 0.

Return the result table in any order.

The query result format is in the following example:

Input:
Department table:
+------+------------------+
| id   | name             |
+------+------------------+
| 1    | Engineering      |
| 2    | Science          |
| 3    | Arts             |
+------+------------------+

Student table:
+------+------------------+
| id   | department_id    |
+------+------------------+
| 1    | 1                |
| 2    | 1                |
| 3    | 2                |
+------+------------------+

Output:
+------------------+------------------+
| department_name  | student_count    |
+------------------+------------------+
| Engineering      | 2                |
| Science          | 1                |
| Arts             | 0                |
+------------------+------------------+
"""

# Python Solution (Simulating SQL Query Execution)

# Since this is an SQL problem, we will simulate the solution using Python for demonstration purposes.

def count_students_in_departments(departments, students):
    """
    Function to count the number of students in each department.

    Args:
    departments (list of dict): List of department records, each containing 'id' and 'name'.
    students (list of dict): List of student records, each containing 'id' and 'department_id'.

    Returns:
    list of dict: List of department names and their respective student counts.
    """
    # Create a dictionary to store department counts
    department_counts = {dept['id']: 0 for dept in departments}
    
    # Count students for each department
    for student in students:
        department_id = student['department_id']
        if department_id in department_counts:
            department_counts[department_id] += 1
    
    # Prepare the result
    result = []
    for dept in departments:
        result.append({
            'department_name': dept['name'],
            'student_count': department_counts[dept['id']]
        })
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Input data
    departments = [
        {'id': 1, 'name': 'Engineering'},
        {'id': 2, 'name': 'Science'},
        {'id': 3, 'name': 'Arts'}
    ]
    
    students = [
        {'id': 1, 'department_id': 1},
        {'id': 2, 'department_id': 1},
        {'id': 3, 'department_id': 2}
    ]
    
    # Expected Output:
    # [
    #     {'department_name': 'Engineering', 'student_count': 2},
    #     {'department_name': 'Science', 'student_count': 1},
    #     {'department_name': 'Arts', 'student_count': 0}
    # ]
    print(count_students_in_departments(departments, students))

"""
Time and Space Complexity Analysis:

Time Complexity:
- Creating the `department_counts` dictionary: O(D), where D is the number of departments.
- Iterating through the `students` list to count students: O(S), where S is the number of students.
- Iterating through the `departments` list to prepare the result: O(D).
- Total time complexity: O(D + S).

Space Complexity:
- The `department_counts` dictionary requires O(D) space.
- The `result` list requires O(D) space.
- Total space complexity: O(D).

Topic: SQL Simulation / HashMap
"""