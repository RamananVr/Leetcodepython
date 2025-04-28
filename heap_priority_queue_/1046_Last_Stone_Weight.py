"""
LeetCode Problem #1046: Last Stone Weight

Problem Statement:
We have a collection of stones, each with a positive integer weight. Each turn, we choose the two heaviest stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

- If x == y, both stones are destroyed.
- If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left. Return the weight of this stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array becomes [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array becomes [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array becomes [1,1,1] then,
we combine 1 and 1 to get 0 so the array becomes [1] then that's the last stone.

Example 2:
Input: stones = [1]
Output: 1

Constraints:
- 1 <= stones.length <= 30
- 1 <= stones[i] <= 1000
"""

# Python Solution
import heapq

def lastStoneWeight(stones):
    """
    Function to calculate the weight of the last remaining stone.
    
    :param stones: List[int] - List of stone weights
    :return: int - Weight of the last remaining stone or 0 if no stones are left
    """
    # Convert stones list into a max-heap (using negative values for max-heap behavior)
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)
    
    while len(max_heap) > 1:
        # Extract the two heaviest stones
        stone1 = -heapq.heappop(max_heap)
        stone2 = -heapq.heappop(max_heap)
        
        # If they are not equal, push the difference back into the heap
        if stone1 != stone2:
            heapq.heappush(max_heap, -(stone1 - stone2))
    
    # Return the last stone weight or 0 if no stones are left
    return -max_heap[0] if max_heap else 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    stones1 = [2, 7, 4, 1, 8, 1]
    print(lastStoneWeight(stones1))  # Output: 1

    # Test Case 2
    stones2 = [1]
    print(lastStoneWeight(stones2))  # Output: 1

    # Test Case 3
    stones3 = [10, 10, 10]
    print(lastStoneWeight(stones3))  # Output: 10

    # Test Case 4
    stones4 = [5, 3, 1, 1, 1]
    print(lastStoneWeight(stones4))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The heap operations (heapify, heappop, heappush) take O(log n) time.
- In the worst case, we perform these operations for all stones, resulting in O(n log n) time complexity.

Space Complexity:
- The space complexity is O(n) due to the storage of the heap.

Topic: Heap (Priority Queue)
"""