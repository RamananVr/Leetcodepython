"""
LeetCode Problem #1962: Remove Stones to Minimize the Total

Problem Statement:
You are given a 0-indexed integer array `piles`, where `piles[i]` represents the number of stones in the ith pile, 
and an integer `k`. You should apply the following operation exactly `k` times:

1. Choose any pile of stones.
2. Remove half of the stones from that pile (floor division).

Return the minimum possible total number of stones remaining after applying the `k` operations.

Example:
Input: piles = [5, 4, 9], k = 2
Output: 12
Explanation:
- Choose the pile with 9 stones. Remove half of the stones: 9 // 2 = 4 stones removed. Remaining stones = [5, 4, 5].
- Choose the pile with 5 stones. Remove half of the stones: 5 // 2 = 2 stones removed. Remaining stones = [3, 4, 5].
The total number of stones left is 3 + 4 + 5 = 12.

Constraints:
- 1 <= piles.length <= 10^5
- 1 <= piles[i] <= 10^4
- 1 <= k <= 10^5
"""

import heapq

def minStoneSum(piles, k):
    """
    Minimize the total number of stones after k operations.

    :param piles: List[int] - List of integers representing the number of stones in each pile.
    :param k: int - Number of operations to perform.
    :return: int - Minimum possible total number of stones remaining.
    """
    # Convert piles into a max-heap by negating the values
    max_heap = [-pile for pile in piles]
    heapq.heapify(max_heap)
    
    # Perform k operations
    for _ in range(k):
        # Extract the largest pile (negated back to positive)
        largest = -heapq.heappop(max_heap)
        # Remove half of the stones (floor division)
        reduced = largest - (largest // 2)
        # Push the reduced pile back into the heap
        heapq.heappush(max_heap, -reduced)
    
    # Calculate the total number of stones remaining
    return -sum(max_heap)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    piles = [5, 4, 9]
    k = 2
    print(minStoneSum(piles, k))  # Output: 12

    # Test Case 2
    piles = [4, 3, 6, 7]
    k = 3
    print(minStoneSum(piles, k))  # Output: 12

    # Test Case 3
    piles = [10, 10, 10]
    k = 5
    print(minStoneSum(piles, k))  # Output: 17

    # Test Case 4
    piles = [1]
    k = 1
    print(minStoneSum(piles, k))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Converting the list into a heap takes O(n), where n is the length of `piles`.
- Each of the `k` operations involves extracting the maximum element (O(log n)) and reinserting the reduced value (O(log n)).
- Thus, the total time complexity is O(n + k * log n).

Space Complexity:
- The space complexity is O(n) due to the heap storage.

Topic: Heap (Priority Queue)
"""