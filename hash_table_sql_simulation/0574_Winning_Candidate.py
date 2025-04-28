"""
LeetCode Problem #574: Winning Candidate

Problem Statement:
Table: Candidate
+-----+---------+
| id  | name    |
+-----+---------+
| 1   | A       |
| 2   | B       |
| 3   | C       |
| 4   | D       |
+-----+---------+
id is the primary key for this table.

Table: Vote
+-----+---------+
| id  | candidateId |
+-----+---------+
| 1   | 2           |
| 2   | 4           |
| 3   | 3           |
| 4   | 2           |
| 5   | 2           |
+-----+---------+
id is the primary key for this table.

Each row of this table indicates that the voter with id voted for the candidate with candidateId.

Write an SQL query to find the name of the winning candidate (i.e., the candidate with the highest number of votes). If there is a tie, return the candidate with the smallest id.

The query result format is in the following example.

Example:
Candidate table:
+-----+---------+
| id  | name    |
+-----+---------+
| 1   | A       |
| 2   | B       |
| 3   | C       |
| 4   | D       |
+-----+---------+

Vote table:
+-----+---------+
| id  | candidateId |
+-----+---------+
| 1   | 2           |
| 2   | 4           |
| 3   | 3           |
| 4   | 2           |
| 5   | 2           |
+-----+---------+

Result table:
+---------+
| name    |
+---------+
| B       |
+---------+
"""

# Python Solution
def winning_candidate(candidate_table, vote_table):
    """
    Function to find the name of the winning candidate based on the highest number of votes.
    If there is a tie, the candidate with the smallest id is returned.

    Args:
    candidate_table (list of dict): List of dictionaries representing the Candidate table.
    vote_table (list of dict): List of dictionaries representing the Vote table.

    Returns:
    str: Name of the winning candidate.
    """
    from collections import Counter

    # Count votes for each candidateId
    vote_counts = Counter(vote['candidateId'] for vote in vote_table)

    # Find the candidateId with the highest votes, breaking ties by smallest id
    max_votes = max(vote_counts.values())
    winning_candidate_id = min(
        candidate_id for candidate_id, count in vote_counts.items() if count == max_votes
    )

    # Find the name of the winning candidate
    for candidate in candidate_table:
        if candidate['id'] == winning_candidate_id:
            return candidate['name']

# Example Test Cases
if __name__ == "__main__":
    candidate_table = [
        {"id": 1, "name": "A"},
        {"id": 2, "name": "B"},
        {"id": 3, "name": "C"},
        {"id": 4, "name": "D"},
    ]

    vote_table = [
        {"id": 1, "candidateId": 2},
        {"id": 2, "candidateId": 4},
        {"id": 3, "candidateId": 3},
        {"id": 4, "candidateId": 2},
        {"id": 5, "candidateId": 2},
    ]

    # Test Case 1
    print(winning_candidate(candidate_table, vote_table))  # Output: "B"

    # Test Case 2 (Tie scenario)
    candidate_table_2 = [
        {"id": 1, "name": "A"},
        {"id": 2, "name": "B"},
        {"id": 3, "name": "C"},
    ]

    vote_table_2 = [
        {"id": 1, "candidateId": 1},
        {"id": 2, "candidateId": 2},
        {"id": 3, "candidateId": 1},
        {"id": 4, "candidateId": 2},
    ]

    print(winning_candidate(candidate_table_2, vote_table_2))  # Output: "A"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting votes: O(V), where V is the number of rows in the vote_table.
- Finding the maximum votes and resolving ties: O(C), where C is the number of unique candidateIds.
- Searching for the winning candidate's name: O(C), where C is the number of rows in the candidate_table.
Overall: O(V + C).

Space Complexity:
- Space used by the Counter object: O(C), where C is the number of unique candidateIds.
Overall: O(C).
"""

# Topic: Hash Table, SQL Simulation