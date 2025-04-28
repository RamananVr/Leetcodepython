"""
LeetCode Question #2512: Reward Top K Students

Problem Statement:
You are given two string arrays `positive_feedback` and `negative_feedback`, containing words denoting positive and negative feedback, respectively. You are also given a 2D integer array `report` and an integer `k`.

- `report[i]` contains two elements: [student_id, feedback], where `student_id` is the ID of the student and `feedback` is a string containing words separated by spaces.
- A student's score is calculated as follows:
  - For each word in the feedback:
    - If the word is in `positive_feedback`, add 3 points to the score.
    - If the word is in `negative_feedback`, subtract 1 point from the score.
- Return the IDs of the top `k` students with the highest scores. If there is a tie, return the IDs in ascending order.

Constraints:
- `1 <= positive_feedback.length, negative_feedback.length <= 100`
- `1 <= positive_feedback[i].length, negative_feedback[i].length <= 20`
- `1 <= report.length <= 100`
- `report[i].length == 2`
- `1 <= report[i][0] <= 10^5`
- `1 <= report[i][1].length <= 1000`
- `1 <= k <= report.length`
- The words in feedback are separated by a single space.

"""

# Solution
from collections import defaultdict

def topStudents(positive_feedback, negative_feedback, report, k):
    # Convert positive and negative feedback lists into sets for O(1) lookup
    positive_set = set(positive_feedback)
    negative_set = set(negative_feedback)
    
    # Dictionary to store scores for each student
    scores = defaultdict(int)
    
    # Calculate scores for each student
    for student_id, feedback in report:
        words = feedback.split()
        score = 0
        for word in words:
            if word in positive_set:
                score += 3
            elif word in negative_set:
                score -= 1
        scores[student_id] += score
    
    # Sort students by score (descending), then by ID (ascending) in case of ties
    sorted_students = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
    
    # Extract the top k student IDs
    return [student_id for student_id, _ in sorted_students[:k]]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    positive_feedback = ["good", "excellent", "great"]
    negative_feedback = ["bad", "poor", "terrible"]
    report = [
        [1, "good excellent great"],
        [2, "bad poor terrible"],
        [3, "good bad good excellent"],
        [4, "great great great"]
    ]
    k = 2
    print(topStudents(positive_feedback, negative_feedback, report, k))  # Output: [4, 1]

    # Test Case 2
    positive_feedback = ["amazing", "awesome", "fantastic"]
    negative_feedback = ["awful", "horrible", "disgusting"]
    report = [
        [101, "amazing awesome fantastic"],
        [102, "awful horrible disgusting"],
        [103, "amazing awful amazing awesome"],
        [104, "fantastic fantastic fantastic"]
    ]
    k = 3
    print(topStudents(positive_feedback, negative_feedback, report, k))  # Output: [104, 101, 103]

    # Test Case 3
    positive_feedback = ["nice", "kind", "helpful"]
    negative_feedback = ["rude", "mean", "selfish"]
    report = [
        [201, "nice kind helpful"],
        [202, "rude mean selfish"],
        [203, "nice rude nice kind"],
        [204, "helpful helpful helpful"]
    ]
    k = 1
    print(topStudents(positive_feedback, negative_feedback, report, k))  # Output: [204]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Converting `positive_feedback` and `negative_feedback` to sets: O(P + N), where P and N are the lengths of the respective lists.
- Iterating through `report` and calculating scores: O(R * F), where R is the number of reports and F is the average number of words in feedback.
- Sorting the scores: O(R log R), where R is the number of students.

Overall: O(P + N + R * F + R log R)

Space Complexity:
- Storage for `positive_set` and `negative_set`: O(P + N)
- Storage for `scores` dictionary: O(R)
- Sorting requires additional space for intermediate results: O(R)

Overall: O(P + N + R)

Topic: Arrays, Hashing, Sorting
"""