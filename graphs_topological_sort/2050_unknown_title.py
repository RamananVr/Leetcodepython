"""
LeetCode Problem #2050: Parallel Courses III

Problem Statement:
You are given an integer n, which indicates that there are n courses labeled from 1 to n. 
You are also given a 2D integer array relations where relations[j] = [prevCourse, nextCourse], 
representing a prerequisite relationship between course prevCourse and course nextCourse: 
course prevCourse has to be completed before course nextCourse can be started. 
You are also given a 0-indexed integer array time where time[i] indicates how many months it takes to complete the (i+1)th course.

You must find the minimum number of months needed to complete all the courses following these rules:
1. You may start multiple courses at the same time if the prerequisites for each course are met.
2. The time needed to complete a course is independent of the time needed to complete other courses.

Return the minimum number of months needed to complete all the courses.

Constraints:
- 1 <= n <= 5 * 10^4
- 0 <= relations.length <= min(n * (n - 1) / 2, 5 * 10^4)
- relations[j].length == 2
- 1 <= prevCourse, nextCourse <= n
- prevCourse != nextCourse
- All the pairs [prevCourse, nextCourse] are unique.
- time.length == n
- 1 <= time[i] <= 10^4
"""

from collections import defaultdict, deque

def minimumTime(n: int, relations: list[list[int]], time: list[int]) -> int:
    # Step 1: Build the graph and in-degree array
    graph = defaultdict(list)
    in_degree = [0] * n
    for prev, next in relations:
        graph[prev - 1].append(next - 1)
        in_degree[next - 1] += 1

    # Step 2: Initialize the queue with courses having no prerequisites
    queue = deque()
    course_time = [0] * n  # To store the time to complete each course
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
            course_time[i] = time[i]

    # Step 3: Process the courses in topological order
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            course_time[neighbor] = max(course_time[neighbor], course_time[current] + time[neighbor])
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Return the maximum time among all courses
    return max(course_time)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 3
    relations1 = [[1, 3], [2, 3]]
    time1 = [3, 2, 5]
    print(minimumTime(n1, relations1, time1))  # Output: 8

    # Test Case 2
    n2 = 5
    relations2 = [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]]
    time2 = [1, 2, 3, 4, 5]
    print(minimumTime(n2, relations2, time2))  # Output: 12

    # Test Case 3
    n3 = 4
    relations3 = []
    time3 = [1, 2, 3, 4]
    print(minimumTime(n3, relations3, time3))  # Output: 4

"""
Time Complexity:
- Building the graph and in-degree array takes O(E), where E is the number of relations.
- Processing the courses in topological order takes O(V + E), where V is the number of courses.
- Overall, the time complexity is O(V + E), which is O(n + relations.length).

Space Complexity:
- The graph uses O(E) space.
- The in-degree array and course_time array use O(V) space.
- The queue can hold up to O(V) elements in the worst case.
- Overall, the space complexity is O(V + E), which is O(n + relations.length).

Topic: Graphs, Topological Sort
"""