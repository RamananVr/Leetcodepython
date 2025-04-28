"""
LeetCode Question #1136: Parallel Courses

Problem Statement:
You are given an integer n, which indicates that there are n courses labeled from 1 to n. 
You are also given an array relations where relations[i] = [a, b], representing a prerequisite relationship, 
that course a must be taken before course b.

In one semester, you can take any number of courses as long as you have satisfied all the prerequisites for the courses you are taking.

Return the minimum number of semesters needed to complete all courses. If there is no way to complete all the courses, return -1.

Constraints:
- 1 <= n <= 5000
- 1 <= relations.length <= 5000
- relations[i].length == 2
- 1 <= a, b <= n
- a != b
- All the pairs [a, b] are unique.

"""

from collections import deque, defaultdict

def minimumSemesters(n: int, relations: list[list[int]]) -> int:
    # Step 1: Build the graph and calculate in-degrees
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for a, b in relations:
        graph[a].append(b)
        in_degree[b] += 1
    
    # Step 2: Initialize the queue with courses having no prerequisites
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    # Step 3: Perform topological sort
    semesters = 0
    courses_taken = 0
    
    while queue:
        semesters += 1
        for _ in range(len(queue)):
            course = queue.popleft()
            courses_taken += 1
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    
    # Step 4: Check if all courses are taken
    return semesters if courses_taken == n else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 3
    relations1 = [[1, 3], [2, 3]]
    print(minimumSemesters(n1, relations1))  # Output: 2

    # Test Case 2
    n2 = 3
    relations2 = [[1, 2], [2, 3], [3, 1]]
    print(minimumSemesters(n2, relations2))  # Output: -1

    # Test Case 3
    n3 = 4
    relations3 = [[1, 2], [2, 3], [3, 4]]
    print(minimumSemesters(n3, relations3))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph and calculating in-degrees takes O(relations.length).
- Topological sort involves visiting each node and edge once, which takes O(n + relations.length).
- Overall time complexity: O(n + relations.length).

Space Complexity:
- The graph uses O(relations.length) space.
- The in-degree array uses O(n) space.
- The queue can hold up to O(n) elements in the worst case.
- Overall space complexity: O(n + relations.length).

Topic: Graphs, Topological Sort
"""