"""
LeetCode Question #630: Course Schedule III

Problem Statement:
There are n different online courses numbered from 1 to n. You are given an array courses where 
courses[i] = [duration_i, lastDay_i] indicates that the i-th course will take duration_i days to complete 
and must be finished before or on lastDay_i.

You can start a course on any day and you can take only one course at a time. Return the maximum number 
of courses that you can take.

Constraints:
- 1 <= courses.length <= 10^4
- 1 <= duration_i, lastDay_i <= 10^4
"""

import heapq

def scheduleCourse(courses):
    """
    Function to determine the maximum number of courses that can be taken.

    Args:
    courses (List[List[int]]): List of courses where each course is represented as [duration, lastDay].

    Returns:
    int: Maximum number of courses that can be taken.
    """
    # Sort courses by their lastDay
    courses.sort(key=lambda x: x[1])
    
    # Max heap to store the durations of courses taken
    max_heap = []
    total_time = 0
    
    for duration, last_day in courses:
        # Add the course duration to total_time
        total_time += duration
        # Push the duration into the max heap (negative for max heap behavior)
        heapq.heappush(max_heap, -duration)
        
        # If total_time exceeds the last_day, remove the longest duration course
        if total_time > last_day:
            total_time += heapq.heappop(max_heap)  # Remove the largest duration (negative value)
    
    # The number of courses in the heap is the maximum number of courses that can be taken
    return len(max_heap)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    courses1 = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    print(scheduleCourse(courses1))  # Expected Output: 3

    # Test Case 2
    courses2 = [[1, 2], [2, 3], [3, 4]]
    print(scheduleCourse(courses2))  # Expected Output: 3

    # Test Case 3
    courses3 = [[5, 5], [4, 6], [2, 6]]
    print(scheduleCourse(courses3))  # Expected Output: 2

    # Test Case 4
    courses4 = [[3, 2], [4, 3]]
    print(scheduleCourse(courses4))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the courses by their lastDay takes O(n log n), where n is the number of courses.
- Iterating through the courses takes O(n).
- Each heap operation (push and pop) takes O(log k), where k is the size of the heap. In the worst case, k = n.
- Therefore, the overall time complexity is O(n log n).

Space Complexity:
- The max heap can store up to n elements, so the space complexity is O(n).

Topic: Greedy, Heap (Priority Queue)
"""