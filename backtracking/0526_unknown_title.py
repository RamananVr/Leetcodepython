"""
LeetCode Problem #526: Beautiful Arrangement

Problem Statement:
Suppose you have n integers labeled 1 through n. A permutation of those integers is considered a beautiful arrangement if:
- For every integer i in the range [1, n], either:
  - The ith position (1-based) is divisible by i, or
  - i is divisible by the ith position.

Given an integer n, return the number of the beautiful arrangements that you can construct.

Constraints:
- 1 <= n <= 15
"""

# Solution
def countArrangement(n: int) -> int:
    def backtrack(pos, visited):
        # Base case: if we have placed all numbers, count this arrangement
        if pos > n:
            return 1
        
        count = 0
        for num in range(1, n + 1):
            if not visited[num] and (num % pos == 0 or pos % num == 0):
                visited[num] = True
                count += backtrack(pos + 1, visited)
                visited[num] = False
        return count
    
    visited = [False] * (n + 1)
    return backtrack(1, visited)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 2
    print(f"Number of beautiful arrangements for n={n}: {countArrangement(n)}")  # Expected Output: 2

    # Test Case 2
    n = 3
    print(f"Number of beautiful arrangements for n={n}: {countArrangement(n)}")  # Expected Output: 3

    # Test Case 3
    n = 4
    print(f"Number of beautiful arrangements for n={n}: {countArrangement(n)}")  # Expected Output: 8

    # Test Case 4
    n = 1
    print(f"Number of beautiful arrangements for n={n}: {countArrangement(n)}")  # Expected Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution uses backtracking to explore all possible permutations of numbers from 1 to n.
- In the worst case, there are n! permutations to check, and for each permutation, we perform O(n) checks.
- Therefore, the time complexity is O(n * n!).

Space Complexity:
- The space complexity is O(n) due to the `visited` array and the recursion stack.
- The recursion stack can go as deep as n levels.

Overall:
Time Complexity: O(n * n!)
Space Complexity: O(n)
"""

# Topic: Backtracking