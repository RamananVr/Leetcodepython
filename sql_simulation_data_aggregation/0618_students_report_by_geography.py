"""
LeetCode Question #618: Students Report By Geography

Problem Statement:
A university has a table `Student` with the following columns:
- `student_id` (int): The ID of the student.
- `student_name` (varchar): The name of the student.
- `gender` (varchar): The gender of the student ('male' or 'female').
- `geography` (varchar): The geographical region of the student.
- `marks` (int): The marks scored by the student.

Write an SQL query to report the following:
- The geographical region.
- The number of male students in that region.
- The number of female students in that region.
- The average marks of all students in that region rounded to 2 decimal places.

The result should be sorted by `geography` in ascending order.

Note: This is an SQL problem, but for the sake of this task, we will simulate the solution in Python using pandas.

"""

# Python Solution
import pandas as pd

def students_report_by_geography(student_data):
    """
    Function to generate a report of students by geography.

    Args:
    student_data (pd.DataFrame): A DataFrame containing student data with columns:
        - 'student_id' (int)
        - 'student_name' (str)
        - 'gender' (str)
        - 'geography' (str)
        - 'marks' (int)

    Returns:
    pd.DataFrame: A DataFrame containing the report with columns:
        - 'geography' (str)
        - 'male_count' (int)
        - 'female_count' (int)
        - 'average_marks' (float)
    """
    # Group by geography and calculate the required metrics
    report = student_data.groupby('geography').agg(
        male_count=('gender', lambda x: (x == 'male').sum()),
        female_count=('gender', lambda x: (x == 'female').sum()),
        average_marks=('marks', lambda x: round(x.mean(), 2))
    ).reset_index()

    return report


# Example Test Cases
if __name__ == "__main__":
    # Sample student data
    data = {
        'student_id': [1, 2, 3, 4, 5, 6],
        'student_name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
        'gender': ['female', 'male', 'male', 'male', 'female', 'male'],
        'geography': ['North', 'North', 'South', 'South', 'North', 'South'],
        'marks': [85, 90, 78, 88, 92, 76]
    }
    student_data = pd.DataFrame(data)

    # Generate the report
    report = students_report_by_geography(student_data)
    print(report)

"""
Expected Output:
  geography  male_count  female_count  average_marks
0     North           1             2          89.00
1     South           3             0          80.67
"""

# Time and Space Complexity Analysis
"""
Time Complexity:
- Grouping the data by geography: O(n), where n is the number of rows in the DataFrame.
- Calculating male_count, female_count, and average_marks: O(n) for each aggregation.
- Overall: O(n).

Space Complexity:
- The space required to store the grouped data and the resulting report: O(k), where k is the number of unique geographical regions.
- Overall: O(k).

"""

# Topic: SQL Simulation / Data Aggregation