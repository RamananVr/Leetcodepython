"""
LeetCode Question #210: Course Schedule II

Problem Statement:
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. 
You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

- Return the ordering of courses you should take to finish all courses.
- If there are many valid answers, return any of them.
- If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3, you should have finished courses 1 and 2. 
Both courses 1 and 2 should be taken after course 0. So a valid course order is [0,2,1,3].

Example 2:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: To take course 1, you should have finished course 0. So the correct course order is [0,1].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs `[ai, bi]` are unique.
"""

from collections import defaultdict, deque

def findOrder(numCourses, prerequisites):
    """
    Finds the order of courses to take to finish all courses.

    :param numCourses: int - Total number of courses
    :param prerequisites: List[List[int]] - List of prerequisite pairs
    :return: List[int] - Order of courses to take, or an empty list if impossible
    """
    # Step 1: Build the graph and calculate in-degrees
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Step 2: Initialize the queue with courses having zero in-degree
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    order = []
    
    # Step 3: Perform topological sort
    while queue:
        current = queue.popleft()
        order.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Step 4: Check if all courses are included in the order
    if len(order) == numCourses:
        return order
    else:
        return []

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(findOrder(numCourses, prerequisites))  # Output: [0,2,1,3] or any valid order
    
    # Test Case 2
    numCourses = 2
    prerequisites = [[1,0]]
    print(findOrder(numCourses, prerequisites))  # Output: [0,1]
    
    # Test Case 3
    numCourses = 1
    prerequisites = []
    print(findOrder(numCourses, prerequisites))  # Output: [0]
    
    # Test Case 4 (Impossible case)
    numCourses = 2
    prerequisites = [[0,1],[1,0]]
    print(findOrder(numCourses, prerequisites))  # Output: []

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(P), where P is the length of prerequisites.
- Initializing the queue takes O(N), where N is the number of courses.
- Topological sort involves visiting each node and its edges, which takes O(N + P).
Overall: O(N + P)

Space Complexity:
- The graph uses O(P) space to store edges.
- The in-degree array uses O(N) space.
- The queue and order list use O(N) space.
Overall: O(N + P)

Topic: Graphs (Topological Sort)
"""