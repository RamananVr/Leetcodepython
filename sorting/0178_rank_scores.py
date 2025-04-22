"""
LeetCode Question #178: Rank Scores

Problem Statement:
Write an SQL query to rank the scores. If there is a tie between two scores, both should have the same ranking. 
Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, 
there should be no "holes" between ranks.

The `Scores` table is defined as follows:
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
id is the primary key for this table.
Each row of this table contains the score of a game. Score is a floating-point number with at most two decimal places.

Write a query to output the following table:
+-------+------+
| score | rank |
+-------+------+
| 3.50  | 1    |
| 3.65  | 2    |
| 4.00  | 3    |
| 5.00  | 4    |
+-------+------+
The output should be sorted by the score in descending order.

Note: Since this is an SQL problem, we will provide a Python solution to simulate the ranking logic in Python.
"""

# Python Solution
def rank_scores(scores):
    """
    Function to rank scores in descending order with no gaps in ranks for ties.

    :param scores: List of scores (floating-point numbers)
    :return: List of tuples where each tuple contains (score, rank)
    """
    # Sort scores in descending order
    sorted_scores = sorted(scores, reverse=True)
    
    # Create a dictionary to store the rank of each unique score
    rank_dict = {}
    rank = 1
    for i, score in enumerate(sorted_scores):
        if score not in rank_dict:
            rank_dict[score] = rank
        rank += 1

    # Generate the result as a list of tuples (score, rank)
    result = [(score, rank_dict[score]) for score in sorted_scores]
    return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    scores = [3.50, 3.65, 4.00, 5.00]
    print("Input Scores:", scores)
    print("Ranked Scores:", rank_scores(scores))
    # Expected Output: [(5.00, 1), (4.00, 2), (3.65, 3), (3.50, 4)]

    # Test Case 2
    scores = [3.50, 3.50, 4.00, 5.00]
    print("Input Scores:", scores)
    print("Ranked Scores:", rank_scores(scores))
    # Expected Output: [(5.00, 1), (4.00, 2), (3.50, 3), (3.50, 3)]

    # Test Case 3
    scores = [1.00, 2.00, 2.00, 3.00]
    print("Input Scores:", scores)
    print("Ranked Scores:", rank_scores(scores))
    # Expected Output: [(3.00, 1), (2.00, 2), (2.00, 2), (1.00, 3)]

    # Test Case 4
    scores = [10.00, 10.00, 10.00]
    print("Input Scores:", scores)
    print("Ranked Scores:", rank_scores(scores))
    # Expected Output: [(10.00, 1), (10.00, 1), (10.00, 1)]


# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the scores takes O(n log n), where n is the number of scores.
- Iterating through the sorted scores to assign ranks takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The `rank_dict` dictionary stores unique scores and their ranks, which takes O(u) space, where u is the number of unique scores.
- The sorted list and result list also take O(n) space.
- Overall space complexity: O(n).

Primary Topic: Sorting
"""