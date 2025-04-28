"""
LeetCode Problem #2178: Maximum Split of Positive Even Integers

Problem Statement:
You are given an integer `finalSum`. Split it into a sum of a maximum number of unique positive even integers.

- For example, given `finalSum = 12`, the output could be `[2, 4, 6]`. These integers are unique and their sum is equal to 12.
- Return the list of integers. If there are multiple solutions, return any of them. If it is not possible to split `finalSum` into such a sum, return an empty list.

Constraints:
1. `1 <= finalSum <= 10^10`
"""

def maximumEvenSplit(finalSum: int) -> list[int]:
    """
    Function to split the given finalSum into a maximum number of unique positive even integers.
    If it's not possible, return an empty list.
    """
    # If finalSum is odd, it's impossible to split into even integers
    if finalSum % 2 != 0:
        return []

    result = []
    current_even = 2

    # Greedily add the smallest even numbers until we can't add more
    while finalSum >= current_even:
        result.append(current_even)
        finalSum -= current_even
        current_even += 2

    # If there's any remaining sum, add it to the last number in the result
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
- In the worst case, the number of iterations is proportional to the square root of `finalSum` because the sum of the first `k` even numbers is proportional to `k^2`.
- Therefore, the time complexity is O(sqrt(finalSum)).

Space Complexity:
- The space complexity is O(k), where `k` is the number of even integers in the result. This is because we store the result in a list.

Topic: Greedy Algorithm
"""