"""
LeetCode Question #60: Permutation Sequence

Problem Statement:
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

Given n and k, return the k-th permutation sequence.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"

Constraints:
- 1 <= n <= 9
- 1 <= k <= n!
"""

# Solution
def getPermutation(n: int, k: int) -> str:
    """
    Returns the k-th permutation sequence of numbers from 1 to n.
    """
    from math import factorial

    # Create a list of numbers from 1 to n
    numbers = list(range(1, n + 1))
    # Convert k to zero-based index
    k -= 1
    # Initialize the result
    result = []

    # Generate the k-th permutation
    for i in range(n):
        # Determine the index of the current number
        index = k // factorial(n - 1 - i)
        # Append the number at the index to the result
        result.append(str(numbers[index]))
        # Remove the used number from the list
        numbers.pop(index)
        # Update k for the next iteration
        k %= factorial(n - 1 - i)

    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1 = 3, 3
    print(getPermutation(n1, k1))  # Output: "213"

    # Test Case 2
    n2, k2 = 4, 9
    print(getPermutation(n2, k2))  # Output: "2314"

    # Test Case 3
    n3, k3 = 3, 6
    print(getPermutation(n3, k3))  # Output: "321"

    # Test Case 4
    n4, k4 = 1, 1
    print(getPermutation(n4, k4))  # Output: "1"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through n numbers, and for each number, it performs a constant number of operations (factorial calculation, list indexing, and list removal).
- Factorial calculations are O(1) for small n (since n <= 9), so the overall complexity is O(n).

Space Complexity:
- The algorithm uses a list of size n to store the numbers and a result list of size n.
- The space complexity is O(n).
"""

# Topic: Math, Permutations