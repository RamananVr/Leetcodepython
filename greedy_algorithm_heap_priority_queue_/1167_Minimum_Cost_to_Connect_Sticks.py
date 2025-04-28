"""
LeetCode Problem #1167: Minimum Cost to Connect Sticks

Problem Statement:
You have some sticks with positive integer lengths. You can connect any two sticks of lengths `x` and `y` into one stick by paying a cost of `x + y`. You perform this action until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick.

Example 1:
Input: sticks = [2, 4, 3]
Output: 14
Explanation:
You start with sticks = [2, 4, 3].
1. Combine sticks 2 and 3 for a cost of 5. Now you have sticks = [5, 4].
2. Combine sticks 4 and 5 for a cost of 9. Now you have sticks = [9].
There is only one stick left, so the total cost is 5 + 9 = 14.

Example 2:
Input: sticks = [1, 8, 3, 5]
Output: 30
Explanation:
You start with sticks = [1, 8, 3, 5].
1. Combine sticks 1 and 3 for a cost of 4. Now you have sticks = [4, 8, 5].
2. Combine sticks 4 and 5 for a cost of 9. Now you have sticks = [9, 8].
3. Combine sticks 9 and 8 for a cost of 17. Now you have sticks = [17].
There is only one stick left, so the total cost is 4 + 9 + 17 = 30.

Constraints:
- 1 <= sticks.length <= 10^4
- 1 <= sticks[i] <= 10^4
"""

import heapq

def connectSticks(sticks):
    """
    Function to calculate the minimum cost to connect all sticks into one stick.

    :param sticks: List[int] - List of stick lengths
    :return: int - Minimum cost to connect all sticks
    """
    # Edge case: If there's only one stick, no cost is incurred
    if len(sticks) <= 1:
        return 0

    # Use a min-heap to efficiently get the smallest two sticks
    heapq.heapify(sticks)
    total_cost = 0

    # Combine sticks until only one stick remains
    while len(sticks) > 1:
        # Pop the two smallest sticks
        first = heapq.heappop(sticks)
        second = heapq.heappop(sticks)

        # Calculate the cost to combine them
        cost = first + second
        total_cost += cost

        # Push the combined stick back into the heap
        heapq.heappush(sticks, cost)

    return total_cost

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sticks1 = [2, 4, 3]
    print(connectSticks(sticks1))  # Output: 14

    # Test Case 2
    sticks2 = [1, 8, 3, 5]
    print(connectSticks(sticks2))  # Output: 30

    # Test Case 3
    sticks3 = [5]
    print(connectSticks(sticks3))  # Output: 0

    # Test Case 4
    sticks4 = [1, 2, 3, 4, 5]
    print(connectSticks(sticks4))  # Output: 33

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses a min-heap to efficiently retrieve the smallest two sticks.
- Heap operations (push and pop) take O(log n) time.
- Since we perform these operations for each stick (n-1 times), the total time complexity is O(n log n), where n is the number of sticks.

Space Complexity:
- The space complexity is O(n) due to the heap storage.

Topic: Greedy Algorithm, Heap (Priority Queue)
"""