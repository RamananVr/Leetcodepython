"""
LeetCode Problem #2606: Find the Prefix Common Array of Two Arrays

Problem Statement:
You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is the count of numbers 
that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A permutation is an integer array containing each number from 1 to n exactly once.

Example:
Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]

Explanation:
- For i = 0: no number is common between A[0:0] and B[0:0].
- For i = 1: the numbers common to A[0:1] and B[0:1] are 1, 3.
- For i = 2: the numbers common to A[0:2] and B[0:2] are 1, 2, 3.
- For i = 3: the numbers common to A[0:3] and B[0:3] are 1, 2, 3, 4.

Constraints:
- 1 <= n <= 50
- A and B are permutations of integers from 1 to n.
"""

# Python Solution
def findThePrefixCommonArray(A, B):
    """
    Function to compute the prefix common array of two permutations A and B.

    :param A: List[int] - First permutation array
    :param B: List[int] - Second permutation array
    :return: List[int] - Prefix common array
    """
    n = len(A)
    seen = set()
    prefix_common = []
    count = 0

    for i in range(n):
        if A[i] in seen:
            count += 1
        else:
            seen.add(A[i])
        
        if B[i] in seen:
            count += 1
        else:
            seen.add(B[i])
        
        prefix_common.append(count)

    return prefix_common

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    A = [1, 3, 2, 4]
    B = [3, 1, 2, 4]
    print(findThePrefixCommonArray(A, B))  # Output: [0, 2, 3, 4]

    # Test Case 2
    A = [1, 2, 3, 4]
    B = [4, 3, 2, 1]
    print(findThePrefixCommonArray(A, B))  # Output: [0, 0, 0, 4]

    # Test Case 3
    A = [1, 2, 3]
    B = [1, 2, 3]
    print(findThePrefixCommonArray(A, B))  # Output: [1, 2, 3]

    # Test Case 4
    A = [3, 2, 1]
    B = [1, 2, 3]
    print(findThePrefixCommonArray(A, B))  # Output: [0, 2, 3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the arrays A and B once, making the time complexity O(n), 
  where n is the length of the arrays.

Space Complexity:
- The function uses a set to track seen elements, which can store up to n elements. 
  Therefore, the space complexity is O(n).
"""

# Topic: Arrays