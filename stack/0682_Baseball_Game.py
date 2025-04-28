"""
LeetCode Problem #682: Baseball Game

Problem Statement:
You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings `ops`, where `ops[i]` is the operation you must apply for the `i-th` round of the game. The operation can be one of the following:

1. An integer `x` - Record this round's score as `x`.
2. `"+"` - Record this round's score as the sum of the previous two scores. It is guaranteed there will always be at least two previous scores.
3. `"D"` - Record this round's score as double the previous round's score. It is guaranteed there will always be a previous score.
4. `"C"` - Invalidate the previous round's score, removing it from the record. It is guaranteed there will always be a previous score.

Return the sum of all the scores on the record after all operations are applied.

Example 1:
Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
- "5" -> Add 5 to the record, record is now [5].
- "2" -> Add 2 to the record, record is now [5, 2].
- "C" -> Invalidate and remove the previous score, record is now [5].
- "D" -> Add double the previous score (2 * 5 = 10), record is now [5, 10].
- "+" -> Add the sum of the previous two scores (5 + 10 = 15), record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.

Example 2:
Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
- "5" -> Add 5 to the record, record is now [5].
- "-2" -> Add -2 to the record, record is now [5, -2].
- "4" -> Add 4 to the record, record is now [5, -2, 4].
- "C" -> Invalidate and remove the previous score, record is now [5, -2].
- "D" -> Add double the previous score (-2 * 2 = -4), record is now [5, -2, -4].
- "9" -> Add 9 to the record, record is now [5, -2, -4, 9].
- "+" -> Add the sum of the previous two scores (-4 + 9 = 5), record is now [5, -2, -4, 9, 5].
- "+" -> Add the sum of the previous two scores (9 + 5 = 14), record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

Constraints:
- 1 <= ops.length <= 1000
- ops[i] is "C", "D", "+", or a string representing an integer.
- For operation "+", there will always be at least two previous scores on the record.
- For operation "D", there will always be at least one previous score on the record.
- For operation "C", there will always be at least one previous score on the record.
"""

# Python Solution
def calPoints(ops):
    """
    Calculate the total score based on the given operations.

    :param ops: List[str] - List of operations
    :return: int - Total score
    """
    record = []
    for op in ops:
        if op == "C":
            record.pop()
        elif op == "D":
            record.append(2 * record[-1])
        elif op == "+":
            record.append(record[-1] + record[-2])
        else:
            record.append(int(op))
    return sum(record)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    ops1 = ["5", "2", "C", "D", "+"]
    print(calPoints(ops1))  # Output: 30

    # Test Case 2
    ops2 = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(calPoints(ops2))  # Output: 27

    # Test Case 3
    ops3 = ["1", "C"]
    print(calPoints(ops3))  # Output: 0

    # Test Case 4
    ops4 = ["10", "20", "+", "D", "C"]
    print(calPoints(ops4))  # Output: 60

# Time Complexity Analysis:
# - Each operation in `ops` is processed once, and operations like "C", "D", and "+" involve constant-time operations on the `record` list.
# - Therefore, the time complexity is O(n), where n is the length of `ops`.

# Space Complexity Analysis:
# - The `record` list stores the scores, and in the worst case, it can grow to the size of `ops`.
# - Therefore, the space complexity is O(n).

# Topic: Stack