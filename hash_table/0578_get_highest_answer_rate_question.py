"""
LeetCode Question #578: Get Highest Answer Rate Question

Problem Statement:
You are given a table `survey_log` with the following schema:

+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| respondent_id       | int     |
| question_id         | int     |
| answer_time         | datetime|
+---------------------+---------+
There is no primary key for this table. It may contain duplicate rows.

Write an SQL query to find the question that has the highest answer rate. 
The answer rate of a question is defined as the number of respondents who answered the question divided by the total number of respondents who answered any question.

The query result format is in the following example:

survey_log table:
+---------------+-------------+---------------------+
| respondent_id | question_id | answer_time         |
+---------------+-------------+---------------------+
| 1             | 1           | 2020-01-01 00:00:00|
| 1             | 2           | 2020-01-01 00:00:00|
| 2             | 1           | 2020-01-01 00:00:00|
| 3             | 1           | 2020-01-01 00:00:00|
| 3             | 2           | 2020-01-01 00:00:00|
| 3             | 3           | 2020-01-01 00:00:00|
+---------------+-------------+---------------------+

Result table:
+-------------+
| question_id |
+-------------+
| 1           |
+-------------+

Explanation:
Question 1 has 3 respondents, which is the highest among all questions.
"""

# Note: Since this is an SQL problem, we cannot directly write a Python solution for it.
# However, we can simulate the logic in Python for educational purposes.

# Python Solution
from collections import defaultdict

def get_highest_answer_rate_question(survey_log):
    """
    Simulates the SQL query to find the question with the highest answer rate.
    
    :param survey_log: List of tuples representing the survey_log table.
                       Each tuple is (respondent_id, question_id, answer_time).
    :return: The question_id with the highest answer rate.
    """
    # Step 1: Count unique respondents for each question
    question_respondents = defaultdict(set)
    for respondent_id, question_id, _ in survey_log:
        question_respondents[question_id].add(respondent_id)
    
    # Step 2: Calculate the number of respondents for each question
    question_counts = {q: len(respondents) for q, respondents in question_respondents.items()}
    
    # Step 3: Find the question with the maximum respondents
    max_question = max(question_counts, key=question_counts.get)
    
    return max_question

# Example Test Cases
if __name__ == "__main__":
    survey_log = [
        (1, 1, "2020-01-01 00:00:00"),
        (1, 2, "2020-01-01 00:00:00"),
        (2, 1, "2020-01-01 00:00:00"),
        (3, 1, "2020-01-01 00:00:00"),
        (3, 2, "2020-01-01 00:00:00"),
        (3, 3, "2020-01-01 00:00:00"),
    ]
    
    # Expected Output: 1
    print(get_highest_answer_rate_question(survey_log))

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting unique respondents for each question: O(n), where n is the number of rows in the survey_log.
- Calculating the number of respondents for each question: O(k), where k is the number of unique questions.
- Finding the question with the maximum respondents: O(k).
Overall: O(n + k).

Space Complexity:
- Storing unique respondents for each question: O(n) in the worst case (if all respondents answer all questions).
- Storing the count of respondents for each question: O(k).
Overall: O(n + k).
"""

# Topic: Hash Table