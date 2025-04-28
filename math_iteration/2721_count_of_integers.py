"""
LeetCode Question #2721: Count of Integers

Problem Statement:
You are given two integers `low` and `high`. Return the count of integers between `low` and `high` (inclusive) that satisfy the following condition:
The sum of the digits of the integer is divisible by the number of digits in the integer.

Constraints:
- 1 <= low <= high <= 10^9

Write a function `count_integers(low: int, high: int) -> int` to solve the problem.
"""

def count_integers(low: int, high: int) -> int:
    """
    Counts integers between low and high (inclusive) where the sum of the digits
    is divisible by the number of digits in the integer.

    :param low: Lower bound of the range (inclusive).
    :param high: Upper bound of the range (inclusive).
    :return: Count of integers satisfying the condition.
    """
    def is_valid(num: int) -> bool:
        """
        Checks if the sum of the digits of num is divisible by the number of digits in num.

        :param num: The integer to check.
        :return: True if the condition is satisfied, False otherwise.
        """
        digits = list(map(int, str(num)))
        digit_sum = sum(digits)
        num_digits = len(digits)
        return digit_sum % num_digits == 0

    count = 0
    for num in range(low, high + 1):
        if is_valid(num):
            count += 1
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    low = 1
    high = 20
    print(count_integers(low, high))  # Expected Output: 5

    # Test Case 2
    low = 10
    high = 15
    print(count_integers(low, high))  # Expected Output: 2

    # Test Case 3
    low = 100
    high = 200
    print(count_integers(low, high))  # Expected Output: 15

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through all integers between `low` and `high` (inclusive), which takes O(high - low + 1).
- For each integer, we calculate the sum of its digits and the number of digits, which takes O(d) time, where d is the number of digits in the integer.
- In the worst case, d = log10(high), so the overall time complexity is O((high - low + 1) * log10(high)).

Space Complexity:
- The space complexity is O(d) for storing the digits of the current number, where d is the number of digits in the integer.
- Therefore, the space complexity is O(log10(high)).

Topic: Math, Iteration
"""