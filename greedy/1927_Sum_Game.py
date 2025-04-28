"""
LeetCode Problem #1927: Sum Game

Problem Statement:
Alice and Bob take turns playing a game, with Alice starting first.

You are given a string `num` of even length consisting of digits and '?' characters. On each turn, a player can replace a single '?' in the string with any digit from '0' to '9'. The game ends when there are no more '?' characters.

The winner is determined based on the following rules:
- Alice wins if the sum of the digits in the first half of the string is not equal to the sum of the digits in the second half.
- Bob wins if the sums are equal.

Assuming both players play optimally, return `true` if Alice will win and `false` if Bob will win.

Constraints:
- `2 <= num.length <= 10^5`
- `num.length` is even.
- `num` consists of digits and '?' characters.
"""

def sumGame(num: str) -> bool:
    n = len(num)
    half = n // 2

    # Calculate the sum of digits and count '?' for both halves
    left_sum, left_question_marks = 0, 0
    right_sum, right_question_marks = 0, 0

    for i in range(half):
        if num[i] == '?':
            left_question_marks += 1
        else:
            left_sum += int(num[i])

    for i in range(half, n):
        if num[i] == '?':
            right_question_marks += 1
        else:
            right_sum += int(num[i])

    # Calculate the difference in sums and question marks
    sum_diff = left_sum - right_sum
    question_diff = left_question_marks - right_question_marks

    # If the number of '?' is odd, Alice always wins
    if question_diff % 2 != 0:
        return True

    # Calculate the maximum possible difference Alice can create
    max_diff = (question_diff // 2) * 9

    # Alice wins if the absolute difference cannot be balanced
    return abs(sum_diff) != max_diff

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "5023"
    print(sumGame(num1))  # Output: False

    # Test Case 2
    num2 = "25??"
    print(sumGame(num2))  # Output: True

    # Test Case 3
    num3 = "?3295???"
    print(sumGame(num3))  # Output: False

    # Test Case 4
    num4 = "??"
    print(sumGame(num4))  # Output: True

"""
Time Complexity:
- O(n), where n is the length of the string `num`. We iterate through the string once to calculate the sums and count the '?' characters.

Space Complexity:
- O(1), as we use a constant amount of extra space.

Topic: Greedy
"""