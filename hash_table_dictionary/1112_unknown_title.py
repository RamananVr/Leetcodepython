"""
LeetCode Problem #1112: Highest Grade For Each Student

Problem Statement:
You are given a list of student records, where each record is represented as a tuple (student_id, grade). 
Each student may have multiple grades. Your task is to return a dictionary where the keys are the student IDs 
and the values are the highest grade for each student.

Example:
Input: records = [(1, 91), (2, 85), (1, 92), (2, 88), (3, 100)]
Output: {1: 92, 2: 88, 3: 100}

Constraints:
- The input list `records` contains tuples of integers.
- Each tuple consists of two integers: student_id (1 <= student_id <= 10^5) and grade (0 <= grade <= 100).
- The list may contain up to 10^5 records.
- Each student_id is unique in the output dictionary.
"""

def highest_grades(records):
    """
    Function to compute the highest grade for each student.

    Args:
    records (List[Tuple[int, int]]): A list of tuples where each tuple contains a student ID and a grade.

    Returns:
    Dict[int, int]: A dictionary where the keys are student IDs and the values are their highest grades.
    """
    highest_grade = {}
    
    for student_id, grade in records:
        if student_id not in highest_grade:
            highest_grade[student_id] = grade
        else:
            highest_grade[student_id] = max(highest_grade[student_id], grade)
    
    return highest_grade

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    records = [(1, 91), (2, 85), (1, 92), (2, 88), (3, 100)]
    print(highest_grades(records))  # Expected Output: {1: 92, 2: 88, 3: 100}

    # Test Case 2
    records = [(4, 75), (4, 80), (5, 60), (5, 95), (6, 90)]
    print(highest_grades(records))  # Expected Output: {4: 80, 5: 95, 6: 90}

    # Test Case 3
    records = [(7, 50), (7, 50), (8, 100), (8, 99), (9, 70)]
    print(highest_grades(records))  # Expected Output: {7: 50, 8: 100, 9: 70}

    # Test Case 4
    records = []
    print(highest_grades(records))  # Expected Output: {}

    # Test Case 5
    records = [(10, 100)]
    print(highest_grades(records))  # Expected Output: {10: 100}

"""
Time Complexity Analysis:
- The function iterates through the list of records once, performing constant-time operations for each record.
- Let n be the number of records in the input list.
- Time Complexity: O(n)

Space Complexity Analysis:
- The function uses a dictionary to store the highest grade for each student. In the worst case, the dictionary will 
  contain one entry for each unique student ID.
- Let m be the number of unique student IDs.
- Space Complexity: O(m)

Topic: Hash Table / Dictionary
"""