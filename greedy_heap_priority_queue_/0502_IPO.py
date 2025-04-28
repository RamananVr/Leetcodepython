"""
LeetCode Problem #502: IPO

Problem Statement:
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to venture capitalists, 
LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, 
it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the i-th project has a pure profit `profits[i]` and a minimum capital of `capital[i]` is needed to start it.

Initially, you have `w` capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

To maximize your total capital, you can finish at most k distinct projects.

You are given `k`, `w`, and the two integer arrays `profits` and `capital`. Return the maximum capital after finishing at most k distinct projects.

Constraints:
- 1 <= k <= 10^5
- 0 <= w <= 10^9
- n == profits.length == capital.length
- 1 <= n <= 10^5
- 0 <= profits[i] <= 10^4
- 0 <= capital[i] <= 10^9
"""

# Solution
import heapq

def findMaximizedCapital(k, w, profits, capital):
    """
    :type k: int
    :type w: int
    :type profits: List[int]
    :type capital: List[int]
    :rtype: int
    """
    # Pair projects with their capital and profit
    projects = list(zip(capital, profits))
    # Sort projects by their capital requirement
    projects.sort()
    
    # Max-heap to store profits of projects we can afford
    max_heap = []
    i = 0
    n = len(projects)
    
    for _ in range(k):
        # Add all projects we can afford to the max-heap
        while i < n and projects[i][0] <= w:
            heapq.heappush(max_heap, -projects[i][1])  # Use negative profit for max-heap
            i += 1
        
        # If no projects are affordable, break early
        if not max_heap:
            break
        
        # Select the project with the maximum profit
        w += -heapq.heappop(max_heap)
    
    return w

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    print(findMaximizedCapital(k, w, profits, capital))  # Expected Output: 4

    # Test Case 2
    k = 3
    w = 0
    profits = [1, 2, 3, 5]
    capital = [0, 1, 1, 2]
    print(findMaximizedCapital(k, w, profits, capital))  # Expected Output: 8

    # Test Case 3
    k = 1
    w = 10
    profits = [5, 10, 15]
    capital = [20, 30, 40]
    print(findMaximizedCapital(k, w, profits, capital))  # Expected Output: 10

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the projects by capital takes O(n log n), where n is the number of projects.
- Each project is pushed and popped from the max-heap at most once, and heap operations take O(log n).
- In the worst case, we iterate k times, and for each iteration, we may perform heap operations.
- Overall complexity: O(n log n + k log n).

Space Complexity:
- The max-heap can store up to n elements, so the space complexity is O(n).
- Additional space is used for storing the projects list, which is also O(n).
- Total space complexity: O(n).
"""

# Topic: Greedy, Heap (Priority Queue)