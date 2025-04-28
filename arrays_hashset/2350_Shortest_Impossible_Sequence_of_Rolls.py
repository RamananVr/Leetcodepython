"""
LeetCode Problem #2350: Shortest Impossible Sequence of Rolls

Problem Statement:
You are given an integer array `rolls` of length `n` and an integer `k`. You roll a k-sided die n times, where the result of the ith roll is `rolls[i]`.

Return the length of the shortest sequence of rolls that cannot be obtained as a subsequence of `rolls`.

A subsequence is a sequence derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example:
Input: rolls = [4, 2, 1, 2], k = 4
Output: 3
Explanation: The shortest impossible sequence is [1, 2, 3]. It cannot be formed as a subsequence of rolls.

Constraints:
- `n == rolls.length`
- `1 <= n <= 10^5`
- `1 <= rolls[i] <= k`
- `1 <= k <= 10^5`
"""

# Python Solution
def shortestSequence(rolls, k):
    """
    Finds the length of the shortest sequence of rolls that cannot be obtained as a subsequence of rolls.

    :param rolls: List[int] - The results of rolling a k-sided die n times.
    :param k: int - The number of sides on the die.
    :return: int - The length of the shortest impossible sequence.
    """
    seen = set()
    impossible_length = 1

    for roll in rolls:
        seen.add(roll)
        if len(seen) == k:
            impossible_length += 1
            seen.clear()

    return impossible_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rolls = [4, 2, 1, 2]
    k = 4
    print(shortestSequence(rolls, k))  # Output: 3

    # Test Case 2
    rolls = [1, 1, 2, 2, 2, 2]
    k = 2
    print(shortestSequence(rolls, k))  # Output: 2

    # Test Case 3
    rolls = [1, 2, 3, 4, 5, 6]
    k = 6
    print(shortestSequence(rolls, k))  # Output: 2

    # Test Case 4
    rolls = [1, 1, 1, 1]
    k = 1
    print(shortestSequence(rolls, k))  # Output: 5

    # Test Case 5
    rolls = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
    k = 6
    print(shortestSequence(rolls, k))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the `rolls` array once, making it O(n), where n is the length of the `rolls` array.
- Operations on the `seen` set (add and clear) are O(1) on average.

Space Complexity:
- The space complexity is O(k), where k is the number of sides on the die, because the `seen` set can store up to k elements.

Overall:
- Time Complexity: O(n)
- Space Complexity: O(k)
"""

# Topic: Arrays, HashSet