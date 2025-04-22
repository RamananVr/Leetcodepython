"""
LeetCode Question #207: Course Schedule

Problem Statement:
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. 
You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` 
before course `ai`.

- For example, the pair `[0, 1]` indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

Constraints:
- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- All the pairs `[ai, bi]` are unique.

"""

from collections import defaultdict, deque

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    Determines if all courses can be finished given the prerequisites.

    Args:
    - numCourses (int): The total number of courses.
    - prerequisites (list[list[int]]): List of prerequisite pairs.

    Returns:
    - bool: True if all courses can be finished, False otherwise.
    """
    # Build the adjacency list and in-degree array
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Initialize a queue with all courses that have no prerequisites
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

    # Count of courses that can be taken
    taken_courses = 0

    while queue:
        current = queue.popleft()
        taken_courses += 1

        # Reduce the in-degree of neighboring courses
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we were able to take all courses, return True
    return taken_courses == numCourses


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple case with no cycles
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    print(canFinish(numCourses1, prerequisites1))  # Expected: True

    # Test Case 2: Cycle exists
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print(canFinish(numCourses2, prerequisites2))  # Expected: False

    # Test Case 3: Multiple courses with no cycles
    numCourses3 = 4
    prerequisites3 = [[1, 0], [2, 1], [3, 2]]
    print(canFinish(numCourses3, prerequisites3))  # Expected: True

    # Test Case 4: Multiple courses with a cycle
    numCourses4 = 4
    prerequisites4 = [[1, 0], [2, 1], [3, 2], [1, 3]]
    print(canFinish(numCourses4, prerequisites4))  # Expected: False

    # Test Case 5: No prerequisites
    numCourses5 = 3
    prerequisites5 = []
    print(canFinish(numCourses5, prerequisites5))  # Expected: True


"""
Time Complexity:
- Building the graph and in-degree array takes O(E), where E is the number of prerequisites.
- Processing the courses in the queue takes O(V + E), where V is the number of courses and E is the number of edges.
- Overall time complexity: O(V + E).

Space Complexity:
- The adjacency list (graph) takes O(E) space.
- The in-degree array takes O(V) space.
- The queue can hold up to O(V) elements in the worst case.
- Overall space complexity: O(V + E).

Topic: Graphs, Topological Sort
"""