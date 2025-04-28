"""
LeetCode Problem #2657: Find the Prefix Common Array of Two Arrays

Problem Statement:
You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers 
that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

Example:
Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]

Explanation:
- For i = 0: No common numbers at or before index 0 in A and B. So, C[0] = 0.
- For i = 1: The numbers 1 and 3 are common at or before index 1 in A and B. So, C[1] = 2.
- For i = 2: The numbers 1, 2, and 3 are common at or before index 2 in A and B. So, C[2] = 3.
- For i = 3: All the numbers 1, 2, 3, and 4 are common at or before index 3 in A and B. So, C[3] = 4.

Constraints:
- n == A.length == B.length
- 1 <= n <= 1000
- 1 <= A[i], B[i] <= n
- A and B are permutations of integers from 1 to n.
"""

def findThePrefixCommonArray(A, B):
    """
    Function to compute the prefix common array of two permutations A and B.

    Args:
    A (List[int]): The first permutation array.
    B (List[int]): The second permutation array.

    Returns:
    List[int]: The prefix common array.
    """
    n = len(A)
    seen = set()
    common_count = 0
    result = []

    for i in range(n):
        # Add current elements of A and B to the seen set
        if A[i] in seen:
            common_count += 1
        else:
            seen.add(A[i])
        
        if B[i] in seen:
            common_count += 1
        else:
            seen.add(B[i])
        
        # Append the current common count to the result
        result.append(common_count)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    A = [1, 3, 2, 4]
    B = [3, 1, 2, 4]
    print(findThePrefixCommonArray(A, B))  # Output: [0, 2, 3, 4]

    # Test Case 2
    A = [2, 1, 4, 3]
    B = [1, 2, 3, 4]
    print(findThePrefixCommonArray(A, B))  # Output: [0, 2, 3, 4]

    # Test Case 3
    A = [1, 2, 3, 4]
    B = [1, 2, 3, 4]
    print(findThePrefixCommonArray(A, B))  # Output: [1, 2, 3, 4]

    # Test Case 4
    A = [4, 3, 2, 1]
    B = [1, 2, 3, 4]
    print(findThePrefixCommonArray(A, B))  # Output: [0, 0, 0, 4]

# Time Complexity Analysis:
# The function iterates through the arrays A and B once, performing O(1) operations for each index.
# Therefore, the time complexity is O(n), where n is the length of the arrays.

# Space Complexity Analysis:
# The function uses a set to store seen elements, which can grow up to size n in the worst case.
# Therefore, the space complexity is O(n).

# Topic: Arrays, Hashing