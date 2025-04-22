"""
LeetCode Problem #77: Combinations

Problem Statement:
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Example 2:
Input: n = 1, k = 1
Output: [[1]]

Constraints:
- 1 <= n <= 20
- 1 <= k <= n
"""

# Solution
def combine(n: int, k: int) -> list[list[int]]:
    """
    Generate all combinations of k numbers chosen from the range [1, n].

    Args:
    n (int): The upper limit of the range.
    k (int): The number of elements in each combination.

    Returns:
    list[list[int]]: A list of all possible combinations.
    """
    def backtrack(start, path):
        # If the current combination is complete, add it to the result
        if len(path) == k:
            result.append(path[:])
            return
        
        # Iterate through the range and build combinations
        for i in range(start, n + 1):
            path.append(i)  # Add the current number to the combination
            backtrack(i + 1, path)  # Recurse with the next number
            path.pop()  # Remove the last number to backtrack

    result = []
    backtrack(1, [])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1 = 4, 2
    print(f"Input: n = {n1}, k = {k1}")
    print(f"Output: {combine(n1, k1)}\n")

    # Test Case 2
    n2, k2 = 1, 1
    print(f"Input: n = {n2}, k = {k2}")
    print(f"Output: {combine(n2, k2)}\n")

    # Test Case 3
    n3, k3 = 5, 3
    print(f"Input: n = {n3}, k = {k3}")
    print(f"Output: {combine(n3, k3)}\n")

# Time and Space Complexity Analysis
"""
Time Complexity:
The number of combinations is given by C(n, k) = n! / (k! * (n-k)!), which is the number of ways to choose k elements from n elements.
The backtracking algorithm generates each combination exactly once, and each combination takes O(k) time to construct.
Thus, the overall time complexity is O(C(n, k) * k).

Space Complexity:
The space complexity is determined by the recursion stack and the space used to store the combinations.
- The recursion stack can go as deep as k, so it uses O(k) space.
- The result list stores C(n, k) combinations, each of size k, so it uses O(C(n, k) * k) space.
Overall space complexity: O(C(n, k) * k).
"""

# Topic: Backtracking