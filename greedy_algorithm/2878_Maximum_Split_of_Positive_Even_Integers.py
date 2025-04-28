"""
LeetCode Problem #2878: Maximum Split of Positive Even Integers

Problem Statement:
You are given a positive integer `finalSum`. You want to split it into a sum of a maximum number of unique positive even integers.

- For example, given `finalSum = 12`, you could split it into `[2, 4, 6]` or `[2, 10]`. The first choice maximizes the number of integers.

Return a list of the integers in any order. If it is not possible to split `finalSum` into a sum of unique positive even integers, return an empty list.

Constraints:
- `1 <= finalSum <= 10^10`
"""

def maximumEvenSplit(finalSum: int) -> list[int]:
    """
    Function to split the given finalSum into the maximum number of unique positive even integers.
    """
    # If finalSum is odd, it's impossible to split into even integers
    if finalSum % 2 != 0:
        return []

    result = []
    current_even = 2

    # Greedily add the smallest even integers
    while finalSum >= current_even:
        result.append(current_even)
        finalSum -= current_even
        current_even += 2

    # Add the remaining sum to the last element to ensure the total matches finalSum
    if finalSum > 0:
        result[-1] += finalSum

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    finalSum = 12
    print(maximumEvenSplit(finalSum))  # Output: [2, 4, 6]

    # Test Case 2
    finalSum = 28
    print(maximumEvenSplit(finalSum))  # Output: [2, 4, 6, 16]

    # Test Case 3
    finalSum = 7
    print(maximumEvenSplit(finalSum))  # Output: []

    # Test Case 4
    finalSum = 2
    print(maximumEvenSplit(finalSum))  # Output: [2]

    # Test Case 5
    finalSum = 20
    print(maximumEvenSplit(finalSum))  # Output: [2, 4, 6, 8]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The loop iterates over even numbers starting from 2 until the sum is exhausted.
- In the worst case, the number of iterations is proportional to the square root of `finalSum` because the sum of the first `n` even numbers is proportional to `n^2`.
- Thus, the time complexity is O(sqrt(finalSum)).

Space Complexity:
- The space complexity is O(k), where `k` is the number of even integers in the result list.
- In the worst case, `k` is proportional to sqrt(finalSum), so the space complexity is O(sqrt(finalSum)).

Topic: Greedy Algorithm
"""