"""
LeetCode Problem #1851: Minimum Interval to Include Each Query

Problem Statement:
You are given an array `intervals`, where `intervals[i] = [start_i, end_i]` represents the start and end of the ith interval, and an array `queries` where `queries[j]` is the jth query.

For the jth query, find the minimum size of an interval `intervals[i]` such that `start_i <= queries[j] <= end_i`. If no such interval exists, return -1.

Return an array containing the answers to all queries.

Example:
Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]

Constraints:
- 1 <= intervals.length <= 10^5
- 1 <= queries.length <= 10^5
- queries[j] and start_i, end_i are integers in the range [1, 10^7].
"""

# Solution
import heapq

def minInterval(intervals, queries):
    # Sort intervals by their start time
    intervals.sort(key=lambda x: x[0])
    # Sort queries and keep track of their original indices
    sorted_queries = sorted((q, i) for i, q in enumerate(queries))
    
    # Min-heap to store intervals based on their size
    min_heap = []
    result = [-1] * len(queries)
    i = 0
    
    for query, original_index in sorted_queries:
        # Add intervals that start before or at the current query
        while i < len(intervals) and intervals[i][0] <= query:
            start, end = intervals[i]
            heapq.heappush(min_heap, (end - start + 1, end, start))
            i += 1
        
        # Remove intervals that end before the current query
        while min_heap and min_heap[0][1] < query:
            heapq.heappop(min_heap)
        
        # If the heap is not empty, the smallest interval is at the top
        if min_heap:
            result[original_index] = min_heap[0][0]
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
    queries = [2, 3, 4, 5]
    print(minInterval(intervals, queries))  # Output: [3, 3, 1, 4]

    # Test Case 2
    intervals = [[1, 2], [2, 3], [3, 4]]
    queries = [1, 2, 3, 4, 5]
    print(minInterval(intervals, queries))  # Output: [2, 2, 2, 2, -1]

    # Test Case 3
    intervals = [[1, 10], [2, 9], [3, 8]]
    queries = [5, 6, 7]
    print(minInterval(intervals, queries))  # Output: [8, 8, 8]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the intervals takes O(n log n), where n is the number of intervals.
- Sorting the queries takes O(m log m), where m is the number of queries.
- For each query, we may add/remove intervals from the heap, which takes O(log n) per operation.
- In the worst case, we process all intervals for all queries, resulting in O(n + m log n).

Overall time complexity: O(n log n + m log m).

Space Complexity:
- The heap can store up to n intervals, so the space complexity for the heap is O(n).
- The result array and sorted queries array take O(m) space.

Overall space complexity: O(n + m).

Topic: Heap (Priority Queue)
"""