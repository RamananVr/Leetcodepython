"""
LeetCode Question #667: Beautiful Arrangement II

Problem Statement:
Given two integers `n` and `k`, construct a list `nums` of size `n` such that:
1. `nums` contains all integers from 1 to `n`.
2. The absolute difference between consecutive elements in `nums` has exactly `k` distinct values.

Return any such list `nums`. It is guaranteed that one exists.

Example:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The absolute differences are [2, 1], which has 2 distinct values.

Input: n = 5, k = 2
Output: [1, 5, 2, 3, 4]
Explanation: The absolute differences are [4, 3, 1, 1], which has 2 distinct values.

Constraints:
- 1 <= k < n <= 10^4
"""

# Solution
def constructArray(n: int, k: int) -> list[int]:
    """
    Constructs a list of size n with exactly k distinct absolute differences
    between consecutive elements.
    """
    result = []
    # First, create the first k+1 elements to ensure k distinct differences
    for i in range(1, k + 2):
        if i % 2 == 1:
            result.append((i + 1) // 2)  # Odd index: ascending order
        else:
            result.append(k + 2 - i // 2)  # Even index: descending order
    
    # Append the remaining elements in ascending order
    result.extend(range(k + 2, n + 1))
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1 = 3, 2
    print(f"Input: n = {n1}, k = {k1}")
    print(f"Output: {constructArray(n1, k1)}\n")

    # Test Case 2
    n2, k2 = 5, 2
    print(f"Input: n = {n2}, k = {k2}")
    print(f"Output: {constructArray(n2, k2)}\n")

    # Test Case 3
    n3, k3 = 7, 3
    print(f"Input: n = {n3}, k = {k3}")
    print(f"Output: {constructArray(n3, k3)}\n")

    # Test Case 4
    n4, k4 = 10, 4
    print(f"Input: n = {n4}, k = {k4}")
    print(f"Output: {constructArray(n4, k4)}\n")

"""
Time and Space Complexity Analysis:
- Time Complexity: O(n)
  The algorithm constructs the array in linear time by iterating over the range of numbers.
- Space Complexity: O(n)
  The result array requires space proportional to the size of `n`.

Topic: Arrays
"""