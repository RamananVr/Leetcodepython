"""
LeetCode Problem #1990: Count the Number of Experiments

Problem Statement:
You are given an integer `n` and an array `experiments` where `experiments[i] = [start_i, end_i]` indicates that the i-th experiment was conducted from time `start_i` to time `end_i` (inclusive). 

Return the number of integers between 1 and `n` (inclusive) that are covered by at least one experiment.

An integer `x` is covered by an experiment if `start_i <= x <= end_i` for some `i`.

Example 1:
Input: n = 5, experiments = [[1, 2], [2, 4], [3, 5]]
Output: 5
Explanation: All integers from 1 to 5 are covered:
- 1 is covered by the first experiment.
- 2 is covered by the first and second experiments.
- 3 is covered by the second and third experiments.
- 4 is covered by the second experiment.
- 5 is covered by the third experiment.

Example 2:
Input: n = 10, experiments = [[1, 3], [5, 7], [9, 10]]
Output: 6
Explanation: The integers covered are 1, 2, 3, 5, 6, 7, 9, and 10.

Constraints:
- 1 <= n <= 10^4
- 1 <= experiments.length <= 10^4
- experiments[i].length == 2
- 1 <= start_i <= end_i <= n
"""

# Solution
def countCoveredIntegers(n, experiments):
    covered = set()
    for start, end in experiments:
        for i in range(start, end + 1):
            covered.add(i)
    return len(covered)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    experiments1 = [[1, 2], [2, 4], [3, 5]]
    print(countCoveredIntegers(n1, experiments1))  # Output: 5

    # Test Case 2
    n2 = 10
    experiments2 = [[1, 3], [5, 7], [9, 10]]
    print(countCoveredIntegers(n2, experiments2))  # Output: 6

    # Test Case 3
    n3 = 7
    experiments3 = [[1, 2], [4, 6]]
    print(countCoveredIntegers(n3, experiments3))  # Output: 5

    # Test Case 4
    n4 = 15
    experiments4 = [[1, 5], [10, 15], [5, 10]]
    print(countCoveredIntegers(n4, experiments4))  # Output: 15

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop iterates over the `experiments` array, which has a length of at most 10^4.
- The inner loop iterates over the range from `start` to `end` for each experiment. In the worst case, this range can be up to `n` (10^4).
- Therefore, the total time complexity is O(m * k), where `m` is the number of experiments and `k` is the average range size. In the worst case, this is O(n * m), which is O(10^8).

Space Complexity:
- The `covered` set stores integers between 1 and `n`. In the worst case, all integers from 1 to `n` are covered, so the space complexity is O(n).
"""

# Topic: Arrays