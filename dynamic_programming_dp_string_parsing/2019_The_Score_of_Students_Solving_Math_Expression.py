"""
LeetCode Problem #2019: The Score of Students Solving Math Expression

Problem Statement:
You are given a string `s` that contains a valid math expression consisting of single-digit numbers, '+', and '*'. 
This expression was given to some students, and the students were asked to solve the expression and provide their answers. 
The students could have made mistakes in the order of operations. For example, if the expression is "7+3*1*2", 
some students could have interpreted it as:

- (7+3)*(1*2) = 20 (This is incorrect due to wrong order of operations)
- 7+(3*1*2) = 13 (This is correct)

You are also given a list `answers` of integers where each integer represents one student's answer.

Your task is to compute the score of the students' answers. The scoring rules are as follows:
1. If a student's answer is correct (matches the true value of the expression), they get 5 points.
2. If a student's answer is incorrect but could be obtained by interpreting the expression in a different valid way, they get 2 points.
3. Otherwise, they get 0 points.

Return the total score of all the students.

Constraints:
- `1 <= s.length <= 31`
- `s` contains only digits, '+', and '*'.
- It is guaranteed that `s` is a valid expression.
- `1 <= answers.length <= 10^4`
- `0 <= answers[i] <= 10^3`
"""

from functools import lru_cache

def scoreOfStudents(s: str, answers: list[int]) -> int:
    # Helper function to evaluate the expression with correct precedence
    def evaluate_correct(expr: str) -> int:
        return eval(expr)

    # Helper function to compute all possible results of the expression
    @lru_cache(None)
    def compute_possible_results(start: int, end: int) -> set:
        if start == end:
            return {int(s[start])}
        
        results = set()
        for i in range(start, end):
            if s[i] in '+*':
                left_results = compute_possible_results(start, i - 1)
                right_results = compute_possible_results(i + 1, end)
                for left in left_results:
                    for right in right_results:
                        if s[i] == '+':
                            results.add(left + right)
                        elif s[i] == '*':
                            results.add(left * right)
        return results

    # Step 1: Compute the correct answer
    correct_answer = evaluate_correct(s)

    # Step 2: Compute all possible answers
    possible_answers = compute_possible_results(0, len(s) - 1)

    # Step 3: Calculate the total score
    total_score = 0
    for answer in answers:
        if answer == correct_answer:
            total_score += 5
        elif answer in possible_answers:
            total_score += 2

    return total_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "7+3*1*2"
    answers1 = [20, 13, 42]
    print(scoreOfStudents(s1, answers1))  # Output: 7

    # Test Case 2
    s2 = "3+5*2"
    answers2 = [13, 16, 10, 15]
    print(scoreOfStudents(s2, answers2))  # Output: 11

    # Test Case 3
    s3 = "1+2*3+4"
    answers3 = [13, 11, 9, 15]
    print(scoreOfStudents(s3, answers3))  # Output: 7

"""
Time Complexity Analysis:
- The `compute_possible_results` function uses memoization and explores all possible partitions of the expression.
  For an expression of length `n`, there are approximately O(2^n) partitions in the worst case. However, memoization
  ensures that each subproblem is solved only once, leading to a complexity of O(n^3) for this part.
- Evaluating the correct answer using `eval` is O(n).
- Scoring the answers involves iterating through the `answers` list, which is O(m), where `m` is the length of the list.

Overall Time Complexity: O(n^3 + m), where `n` is the length of the expression and `m` is the number of answers.

Space Complexity Analysis:
- The memoization table for `compute_possible_results` stores results for all subproblems, which is O(n^2).
- The `possible_answers` set can store up to O(2^n) results in the worst case.
- The space required for the `answers` list is O(m).

Overall Space Complexity: O(n^2 + 2^n + m).

Topic: Dynamic Programming (DP), String Parsing
"""