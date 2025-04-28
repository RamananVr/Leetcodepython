"""
LeetCode Problem #2356: Number of Unique Subjects Taught by Each Teacher

Problem Statement:
You are given a list of tuples where each tuple represents a teacher and the subjects they teach. 
Each tuple is of the form (teacher_name, subject_name). Your task is to determine the number of 
unique subjects taught by each teacher.

Write a function `count_unique_subjects` that takes a list of tuples as input and returns a dictionary 
where the keys are teacher names and the values are the number of unique subjects they teach.

Example:
Input: [("Alice", "Math"), ("Bob", "Science"), ("Alice", "Physics"), ("Alice", "Math"), ("Bob", "Math")]
Output: {"Alice": 2, "Bob": 2}

Constraints:
- The input list can have up to 10^5 tuples.
- Each teacher_name and subject_name is a string of length between 1 and 100.
- The input list may contain duplicate entries.
"""

# Solution
def count_unique_subjects(teacher_subject_pairs):
    """
    Counts the number of unique subjects taught by each teacher.

    Args:
    teacher_subject_pairs (List[Tuple[str, str]]): A list of tuples where each tuple contains a teacher's name
                                                   and a subject they teach.

    Returns:
    Dict[str, int]: A dictionary where the keys are teacher names and the values are the number of unique
                    subjects they teach.
    """
    from collections import defaultdict

    # Dictionary to store the set of subjects for each teacher
    teacher_subjects = defaultdict(set)

    # Populate the dictionary with unique subjects for each teacher
    for teacher, subject in teacher_subject_pairs:
        teacher_subjects[teacher].add(subject)

    # Convert the sets to counts of unique subjects
    result = {teacher: len(subjects) for teacher, subjects in teacher_subjects.items()}

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    input_data = [("Alice", "Math"), ("Bob", "Science"), ("Alice", "Physics"), ("Alice", "Math"), ("Bob", "Math")]
    expected_output = {"Alice": 2, "Bob": 2}
    assert count_unique_subjects(input_data) == expected_output

    # Test Case 2
    input_data = [("Alice", "Math"), ("Alice", "Math"), ("Alice", "Math")]
    expected_output = {"Alice": 1}
    assert count_unique_subjects(input_data) == expected_output

    # Test Case 3
    input_data = [("Alice", "Math"), ("Bob", "Math"), ("Charlie", "Math"), ("Alice", "Physics")]
    expected_output = {"Alice": 2, "Bob": 1, "Charlie": 1}
    assert count_unique_subjects(input_data) == expected_output

    # Test Case 4
    input_data = []
    expected_output = {}
    assert count_unique_subjects(input_data) == expected_output

    # Test Case 5
    input_data = [("Alice", "Math"), ("Alice", "Physics"), ("Alice", "Chemistry"), ("Alice", "Biology")]
    expected_output = {"Alice": 4}
    assert count_unique_subjects(input_data) == expected_output

    print("All test cases passed!")

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n be the number of tuples in the input list.
- Iterating through the list of tuples takes O(n).
- Adding a subject to a set is an O(1) operation on average.
- Constructing the final dictionary from the sets takes O(k), where k is the number of unique teachers.
- Overall time complexity: O(n).

Space Complexity:
- The space required to store the dictionary of sets is proportional to the number of unique teachers and subjects.
- Let t be the number of unique teachers and s be the number of unique subjects.
- Space complexity: O(t + s).
"""

# Topic: Hash Table, String Manipulation