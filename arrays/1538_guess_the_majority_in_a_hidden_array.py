"""
LeetCode Question #1538: Guess the Majority in a Hidden Array

Problem Statement:
You are given a hidden array `hidden` of length `n` whose elements are either 0 or 1. You may only access the array using a `query` function that takes an index `i` and returns the value of `hidden[i]`. You cannot access the array directly.

You are also given an integer `n`, the length of the array.

Your task is to determine whether the majority of the elements in the array are 0 or 1. If the majority is 0, return 0. If the majority is 1, return 1. If there is no majority (i.e., the number of 0s and 1s are equal), return -1.

The `query` function is defined as follows:
    def query(i: int) -> int:
        # Returns the value of hidden[i]

Constraints:
- 1 <= n <= 10^4
- The array `hidden` contains only 0s and 1s.

You must minimize the number of calls to the `query` function.

"""

# Solution
def guess_majority(n: int, query) -> int:
    """
    Determines the majority element in the hidden array using the query function.

    Args:
    n (int): Length of the hidden array.
    query (function): Function to query the hidden array.

    Returns:
    int: 0 if 0 is the majority, 1 if 1 is the majority, -1 if there is no majority.
    """
    count_0 = 0
    count_1 = 0

    # Query the array and count occurrences of 0 and 1
    for i in range(n):
        value = query(i)
        if value == 0:
            count_0 += 1
        elif value == 1:
            count_1 += 1

    # Determine the majority
    if count_0 > count_1:
        return 0
    elif count_1 > count_0:
        return 1
    else:
        return -1

# Example Test Cases
def test_guess_majority():
    # Example 1
    hidden = [0, 0, 1, 1, 0]
    def query(i):
        return hidden[i]
    n = len(hidden)
    assert guess_majority(n, query) == 0  # Majority is 0

    # Example 2
    hidden = [1, 1, 1, 0, 0]
    def query(i):
        return hidden[i]
    n = len(hidden)
    assert guess_majority(n, query) == 1  # Majority is 1

    # Example 3
    hidden = [0, 1, 0, 1]
    def query(i):
        return hidden[i]
    n = len(hidden)
    assert guess_majority(n, query) == -1  # No majority

    print("All test cases passed!")

# Run the test cases
test_guess_majority()

# Time and Space Complexity Analysis
"""
Time Complexity:
The function iterates through the array once, making `n` calls to the `query` function.
Thus, the time complexity is O(n).

Space Complexity:
The function uses a constant amount of space to store the counts of 0s and 1s.
Thus, the space complexity is O(1).
"""

# Topic: Arrays