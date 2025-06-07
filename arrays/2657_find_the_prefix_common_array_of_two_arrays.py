"""
LeetCode Question #2657: Find the Prefix Common Array of Two Arrays

Problem Statement:
You are given two 0-indexed integer permutation arrays A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present in both the prefix A[0..i] and the prefix B[0..i].

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

Examples:
Example 1:
Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A[0..1] and B[0..1], so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A[0..2] and B[0..2], so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A[0..3] and B[0..3], so C[3] = 4.

Example 2:
Input: A = [2,3,1], B = [3,1,2]
Output: [0,1,3]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A[0..1] and B[0..1], so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A[0..2] and B[0..2], so C[2] = 3.

Constraints:
- 1 <= A.length == B.length == n <= 50
- 1 <= A[i], B[i] <= n
- It is guaranteed that A and B are both a permutation of the array [1, 2, ..., n].
"""

from typing import List

def findThePrefixCommonArray(A: List[int], B: List[int]) -> List[int]:
    """
    Find prefix common array using sets to track seen elements.
    """
    n = len(A)
    result = []
    seen_A = set()
    seen_B = set()
    
    for i in range(n):
        seen_A.add(A[i])
        seen_B.add(B[i])
        
        # Count common elements in current prefix
        common_count = len(seen_A & seen_B)
        result.append(common_count)
    
    return result

def findThePrefixCommonArrayOptimized(A: List[int], B: List[int]) -> List[int]:
    """
    Optimized approach using frequency counting.
    
    Since both arrays are permutations, we can track when elements
    appear in both prefixes by counting their frequency.
    """
    n = len(A)
    result = []
    freq = [0] * (n + 1)  # frequency array for numbers 1 to n
    common_count = 0
    
    for i in range(n):
        # Process A[i]
        freq[A[i]] += 1
        if freq[A[i]] == 2:  # appeared in both arrays
            common_count += 1
        
        # Process B[i]
        freq[B[i]] += 1
        if freq[B[i]] == 2:  # appeared in both arrays
            common_count += 1
        
        result.append(common_count)
    
    return result

def findThePrefixCommonArrayBruteForce(A: List[int], B: List[int]) -> List[int]:
    """
    Brute force approach - check each prefix separately.
    """
    n = len(A)
    result = []
    
    for i in range(n):
        # Get prefixes
        prefix_A = set(A[:i+1])
        prefix_B = set(B[:i+1])
        
        # Count common elements
        common_count = len(prefix_A & prefix_B)
        result.append(common_count)
    
    return result

def findThePrefixCommonArrayBitMask(A: List[int], B: List[int]) -> List[int]:
    """
    Bit manipulation approach for tracking seen elements.
    """
    n = len(A)
    result = []
    mask_A = 0
    mask_B = 0
    
    for i in range(n):
        # Set bit for A[i] and B[i]
        mask_A |= (1 << A[i])
        mask_B |= (1 << B[i])
        
        # Count common bits (common elements)
        common_mask = mask_A & mask_B
        common_count = bin(common_mask).count('1')
        result.append(common_count)
    
    return result

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([1, 3, 2, 4], [3, 1, 2, 4], [0, 2, 3, 4]),
        ([2, 3, 1], [3, 1, 2], [0, 1, 3]),
        ([1], [1], [1]),
        ([1, 2], [2, 1], [0, 2]),
        ([1, 2, 3], [1, 2, 3], [1, 2, 3])
    ]
    
    print("Testing main approach:")
    for A, B, expected in test_cases:
        result = findThePrefixCommonArray(A, B)
        print(f"findThePrefixCommonArray({A}, {B}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting optimized approach:")
    for A, B, expected in test_cases:
        result = findThePrefixCommonArrayOptimized(A, B)
        print(f"findThePrefixCommonArrayOptimized({A}, {B}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting brute force approach:")
    for A, B, expected in test_cases:
        result = findThePrefixCommonArrayBruteForce(A, B)
        print(f"findThePrefixCommonArrayBruteForce({A}, {B}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting bit mask approach:")
    for A, B, expected in test_cases:
        result = findThePrefixCommonArrayBitMask(A, B)
        print(f"findThePrefixCommonArrayBitMask({A}, {B}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")

"""
Time and Space Complexity Analysis:

Main Approach (Sets):
Time Complexity: O(n^2) - set intersection operation can be O(n) for each prefix
Space Complexity: O(n) - for storing sets

Optimized Approach (Frequency):
Time Complexity: O(n) - single pass through arrays
Space Complexity: O(n) - frequency array

Brute Force Approach:
Time Complexity: O(n^2) - creating sets for each prefix
Space Complexity: O(n) - temporary sets for each prefix

Bit Mask Approach:
Time Complexity: O(n * log n) - counting bits for each prefix
Space Complexity: O(1) - only using bit masks

Key Insights:
1. Since arrays are permutations, each number appears exactly once
2. An element is common in prefixes if it has appeared in both arrays so far
3. Frequency counting is most efficient: increment when seen, count when freq=2

Topic: Arrays, Prefix Sum, Set Operations, Bit Manipulation
"""
