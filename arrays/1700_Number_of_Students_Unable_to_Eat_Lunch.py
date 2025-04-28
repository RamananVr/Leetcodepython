"""
LeetCode Problem #1700: Number of Students Unable to Eat Lunch

Problem Statement:
The school cafeteria offers lunch to students in a queue. Each student can be satisfied with either a square or a circular sandwich. 
The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. 
At each step:
- If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
- Otherwise, they will move to the end of the queue.

This continues until none of the students want the sandwich on the top of the stack, at which point the students who are unable to eat are counted.

You are given two integer arrays `students` and `sandwiches` where:
- `students[i]` is `0` if the i-th student prefers square sandwiches and `1` if they prefer circular sandwiches.
- `sandwiches[j]` is `0` if the j-th sandwich is square and `1` if it is circular.

Return the number of students that are unable to eat.

Constraints:
- 1 <= students.length, sandwiches.length <= 100
- students.length == sandwiches.length
- sandwiches[j] is 0 or 1.
- students[i] is 0 or 1.
"""

def countStudents(students, sandwiches):
    """
    Function to calculate the number of students unable to eat lunch.

    :param students: List[int] - List of students' preferences (0 for square, 1 for circular).
    :param sandwiches: List[int] - List of sandwiches in the stack (0 for square, 1 for circular).
    :return: int - Number of students unable to eat.
    """
    from collections import Counter

    # Count the number of students preferring each type of sandwich
    student_count = Counter(students)

    for sandwich in sandwiches:
        # If no student prefers the current sandwich, return the remaining students
        if student_count[sandwich] == 0:
            return student_count[0] + student_count[1]
        # Otherwise, serve the sandwich and reduce the count
        student_count[sandwich] -= 1

    # If all sandwiches are served, return 0
    return 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    students1 = [1, 1, 0, 0]
    sandwiches1 = [0, 1, 0, 1]
    print(countStudents(students1, sandwiches1))  # Output: 0

    # Test Case 2
    students2 = [1, 1, 1, 0, 0, 1]
    sandwiches2 = [1, 0, 0, 0, 1, 1]
    print(countStudents(students2, sandwiches2))  # Output: 3

    # Test Case 3
    students3 = [0, 0, 0, 1, 1]
    sandwiches3 = [1, 0, 0, 0, 1]
    print(countStudents(students3, sandwiches3))  # Output: 0

"""
Time Complexity Analysis:
- Counting the students' preferences using `Counter` takes O(n), where n is the length of the `students` list.
- Iterating through the `sandwiches` list takes O(n).
- Overall, the time complexity is O(n).

Space Complexity Analysis:
- The `Counter` object uses O(1) space since there are only two possible keys (0 and 1).
- The space complexity is O(1).

Topic: Arrays
"""