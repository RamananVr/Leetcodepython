"""
LeetCode Question #779: K-th Symbol in Grammar

Problem Statement:
We build a table of n rows (1-indexed). On the first row, we write a 0. 
Each subsequent row is formed as follows: For each symbol in the previous row, 
if the symbol is 0, we write 01; if the symbol is 1, we write 10.

Given two integers n and k, return the k-th (1-indexed) symbol in the n-th row of the table.

Constraints:
- 1 <= n <= 30
- 1 <= k <= 2^(n-1)
"""

def kthGrammar(n: int, k: int) -> int:
    """
    Recursive solution to find the k-th symbol in the n-th row of the grammar table.
    """
    # Base case: The first row always starts with 0
    if n == 1:
        return 0
    
    # Determine the parent symbol's position in the previous row
    parent = kthGrammar(n - 1, (k + 1) // 2)
    
    # If k is odd, the symbol is the same as the parent; if k is even, it's flipped
    if k % 2 == 1:
        return parent
    else:
        return 1 - parent

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n, k = 1, 1
    print(kthGrammar(n, k))  # Output: 0

    # Test Case 2
    n, k = 2, 1
    print(kthGrammar(n, k))  # Output: 0

    # Test Case 3
    n, k = 2, 2
    print(kthGrammar(n, k))  # Output: 1

    # Test Case 4
    n, k = 4, 5
    print(kthGrammar(n, k))  # Output: 1

    # Test Case 5
    n, k = 30, 1
    print(kthGrammar(n, k))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function makes recursive calls, reducing n by 1 in each step. 
  Since n can go up to 30, the recursion depth is O(n), which is at most 30.
- Each recursive call performs constant work, so the overall time complexity is O(n).

Space Complexity:
- The recursion stack can go up to a depth of n, so the space complexity is O(n).

Topic: Recursion
"""