"""
LeetCode Problem #1705: Maximum Number of Eaten Apples

Problem Statement:
There is a special kind of apple tree that grows apples every day for some time. On the i-th day, the tree grows `apples[i]` apples that will rot after `days[i]` days, meaning that these apples must be eaten on or before the (i + days[i] - 1)-th day. You can only eat one apple per day (provided that there are any left to eat). You want to maximize the number of apples you can eat.

Given two integer arrays `apples` and `days` of length `n`, return the maximum number of apples you can eat.

Constraints:
- `n == apples.length == days.length`
- `1 <= n <= 2 * 10^4`
- `0 <= apples[i], days[i] <= 2 * 10^4`

Example:
Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
Output: 7

Input: apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
Output: 5
"""

import heapq

def eatenApples(apples, days):
    """
    Function to calculate the maximum number of apples that can be eaten.

    :param apples: List[int], number of apples grown each day
    :param days: List[int], number of days before apples rot
    :return: int, maximum number of apples that can be eaten
    """
    n = len(apples)
    heap = []  # Min-heap to store (rot_day, count_of_apples)
    max_apples = 0
    day = 0

    while day < n or heap:
        # Add new apples to the heap if available
        if day < n and apples[day] > 0:
            heapq.heappush(heap, (day + days[day], apples[day]))

        # Remove rotten apples from the heap
        while heap and heap[0][0] <= day:
            heapq.heappop(heap)

        # Eat one apple if available
        if heap:
            rot_day, count = heapq.heappop(heap)
            max_apples += 1
            if count > 1:
                heapq.heappush(heap, (rot_day, count - 1))

        day += 1

    return max_apples


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    apples = [1, 2, 3, 5, 2]
    days = [3, 2, 1, 4, 2]
    print(eatenApples(apples, days))  # Output: 7

    # Test Case 2
    apples = [3, 0, 0, 0, 0, 2]
    days = [3, 0, 0, 0, 0, 2]
    print(eatenApples(apples, days))  # Output: 5

    # Test Case 3
    apples = [0, 0, 0]
    days = [0, 0, 0]
    print(eatenApples(apples, days))  # Output: 0

    # Test Case 4
    apples = [2, 1, 10]
    days = [2, 10, 1]
    print(eatenApples(apples, days))  # Output: 3


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the `apples` and `days` arrays, which takes O(n).
- For each day, we may perform heap operations (push and pop), which take O(log k), where k is the size of the heap.
- In the worst case, the heap size can grow to O(n), so the overall time complexity is O(n log n).

Space Complexity:
- The heap can store up to O(n) elements in the worst case, so the space complexity is O(n).

Topic: Greedy, Heap (Priority Queue)
"""