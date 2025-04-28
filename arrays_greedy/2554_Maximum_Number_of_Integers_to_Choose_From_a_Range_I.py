"""
LeetCode Problem #2554: Maximum Number of Integers to Choose From a Range I

Problem Statement:
You are given an integer array `banned` and two integers `n` and `maxSum`. You are tasked with choosing some integers from the range `[1, n]` such that:

1. The chosen integers are not in the `banned` array.
2. The sum of the chosen integers does not exceed `maxSum`.
3. You maximize the number of chosen integers.

Return the maximum number of integers you can choose.

Constraints:
- 1 <= banned.length <= 10^4
- 1 <= banned[i] <= n
- 1 <= n <= 10^4
- 1 <= maxSum <= 10^9
- The elements in `banned` are distinct.

"""

def maxCount(banned, n, maxSum):
    """
    Function to calculate the maximum number of integers that can be chosen
    from the range [1, n] while satisfying the given constraints.

    :param banned: List[int] - List of integers that cannot be chosen.
    :param n: int - The upper bound of the range [1, n].
    :param maxSum: int - The maximum allowed sum of chosen integers.
    :return: int - The maximum number of integers that can be chosen.
    """
    banned_set = set(banned)  # Convert banned list to a set for O(1) lookups
    current_sum = 0
    count = 0

    for i in range(1, n + 1):
        if i in banned_set:
            continue
        if current_sum + i > maxSum:
            break
        current_sum += i
        count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    banned = [1, 4, 6]
    n = 10
    maxSum = 20
    print(maxCount(banned, n, maxSum))  # Expected Output: 4

    # Test Case 2
    banned = [2, 3, 5]
    n = 7
    maxSum = 10
    print(maxCount(banned, n, maxSum))  # Expected Output: 3

    # Test Case 3
    banned = []
    n = 5
    maxSum = 15
    print(maxCount(banned, n, maxSum))  # Expected Output: 5

    # Test Case 4
    banned = [1, 2, 3]
    n = 5
    maxSum = 6
    print(maxCount(banned, n, maxSum))  # Expected Output: 2

    # Test Case 5
    banned = [1, 2, 3, 4, 5]
    n = 10
    maxSum = 15
    print(maxCount(banned, n, maxSum))  # Expected Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The loop iterates over the range [1, n], which takes O(n) time.
- Checking if an element is in the `banned_set` takes O(1) on average.
- Thus, the overall time complexity is O(n).

Space Complexity:
- The `banned_set` requires O(banned.length) space.
- Other variables use O(1) space.
- Therefore, the overall space complexity is O(banned.length).

Topic: Arrays, Greedy
"""