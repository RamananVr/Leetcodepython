"""
LeetCode Problem #753: Cracking the Safe

Problem Statement:
There is a safe with a circular dial. The safe has `n` dials, each of which can be set to one of `k` different digits (0, 1, ..., k-1). 
The safe can only be opened if you enter the correct combination of `n` digits. 

A combination is valid if:
- It is of length `n`.
- Each digit is in the range [0, k-1].

You need to find the shortest string that contains every possible combination of the safe's digits as a substring. 
If there are multiple valid strings, return any of them.

Example:
Input: n = 2, k = 2
Output: "00110"
Explanation: The string "00110" contains all possible combinations of length 2: "00", "01", "10", "11". 
Note that "01100", "10011", "11001" are also valid outputs.

Constraints:
- 1 <= n <= 4
- 1 <= k <= 10
- The answer is guaranteed to exist.
"""

# Solution
def crackSafe(n: int, k: int) -> str:
    """
    Finds the shortest string that contains every possible combination of n digits from 0 to k-1 as a substring.
    """
    # Helper function to generate all possible combinations of length n
    def dfs(node):
        for x in range(k):
            edge = node + str(x)
            if edge not in visited:
                visited.add(edge)
                dfs(edge[1:])
                result.append(str(x))

    # Initialize variables
    start = "0" * (n - 1)
    visited = set()
    result = []

    # Perform DFS to construct the De Bruijn sequence
    dfs(start)

    # Return the result as a string
    return "".join(result) + start

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1 = 2, 2
    print(crackSafe(n1, k1))  # Output: "00110" or any valid sequence

    # Test Case 2
    n2, k2 = 1, 2
    print(crackSafe(n2, k2))  # Output: "01" or "10"

    # Test Case 3
    n3, k3 = 2, 3
    print(crackSafe(n3, k3))  # Output: "002112010" or any valid sequence

    # Test Case 4
    n4, k4 = 3, 2
    print(crackSafe(n4, k4))  # Output: "0001011100" or any valid sequence

# Time and Space Complexity Analysis
"""
Time Complexity:
- The number of possible combinations of length n with k digits is k^n.
- The DFS traversal visits each combination exactly once, and appending to the result takes O(1) time.
- Therefore, the time complexity is O(k^n).

Space Complexity:
- The space complexity is dominated by the `visited` set, which stores all k^n combinations.
- Additionally, the recursion stack can go as deep as k^n in the worst case.
- Therefore, the space complexity is O(k^n).
"""

# Topic: Graphs (Eulerian Path/De Bruijn Sequence)