"""
LeetCode Problem #2558: Take Gifts From the Richest Pile

Problem Statement:
You are given an integer array `gifts` denoting the number of gifts in several piles. Every second, you do the following:
1. Choose the pile with the maximum number of gifts.
2. Take the square root of the number of gifts in that pile (rounded down to the nearest integer) and put that many gifts back into the pile.

Return the number of gifts remaining after `k` seconds.

Example:
Input: gifts = [25, 64, 9, 4, 100], k = 4
Output: 29
Explanation:
- In the first second, take sqrt(100) = 10 gifts from the pile with 100 gifts. Remaining gifts: [25, 64, 9, 4, 10].
- In the second second, take sqrt(64) = 8 gifts from the pile with 64 gifts. Remaining gifts: [25, 8, 9, 4, 10].
- In the third second, take sqrt(25) = 5 gifts from the pile with 25 gifts. Remaining gifts: [5, 8, 9, 4, 10].
- In the fourth second, take sqrt(10) = 3 gifts from the pile with 10 gifts. Remaining gifts: [5, 8, 9, 4, 3].
The total number of gifts remaining is 5 + 8 + 9 + 4 + 3 = 29.

Constraints:
- 1 <= gifts.length <= 10^3
- 1 <= gifts[i] <= 10^9
- 1 <= k <= 10^3
"""

import heapq
import math

def pickGifts(gifts, k):
    """
    Function to calculate the number of gifts remaining after k seconds.
    
    Args:
    gifts (List[int]): List of integers representing the number of gifts in each pile.
    k (int): Number of seconds to perform the operation.
    
    Returns:
    int: Total number of gifts remaining after k seconds.
    """
    # Convert the gifts array into a max-heap by negating the values
    max_heap = [-gift for gift in gifts]
    heapq.heapify(max_heap)
    
    # Perform the operation k times
    for _ in range(k):
        # Extract the largest pile (negate to get the original value)
        largest = -heapq.heappop(max_heap)
        # Take the square root of the largest pile and round down
        reduced_gifts = math.isqrt(largest)
        # Push the reduced pile back into the heap (negated)
        heapq.heappush(max_heap, -reduced_gifts)
    
    # Calculate the total number of gifts remaining
    return -sum(max_heap)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    gifts = [25, 64, 9, 4, 100]
    k = 4
    print(pickGifts(gifts, k))  # Output: 29

    # Test Case 2
    gifts = [1, 1, 1, 1]
    k = 2
    print(pickGifts(gifts, k))  # Output: 4

    # Test Case 3
    gifts = [81, 49, 36]
    k = 3
    print(pickGifts(gifts, k))  # Output: 14

"""
Time and Space Complexity Analysis:

Time Complexity:
- Converting the list into a heap takes O(n), where n is the length of the `gifts` array.
- Each heap operation (pop and push) takes O(log n).
- Since we perform k operations, the total time complexity is O(n + k * log n).

Space Complexity:
- The space complexity is O(n) due to the heap storage.

Topic: Heap (Priority Queue)
"""