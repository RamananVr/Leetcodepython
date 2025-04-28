"""
LeetCode Problem #2199: Finding the Topic of a LeetCode Problem

Problem Statement:
You are given a LeetCode problem number, and your task is to write the full problem statement, 
provide a clean and correct Python solution, add example test cases, analyze the time and space complexity, 
and identify the primary topic of the problem.

Note: This is a meta-problem designed to demonstrate how to structure a solution for a LeetCode problem.

Solution:
Below is the structured solution for LeetCode Problem #2199.
"""

# Problem Statement for LeetCode Question #2199
"""
2199. Find All People With Secret

You are given an integer n indicating the total number of people labeled from 0 to n - 1. 
You are also given a 2D integer array meetings where meetings[i] = [x, y, time] indicates that person x and person y 
have a meeting at time time. Additionally, you are given an integer firstPerson.

Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. 
This secret is then shared every time a meeting takes place with someone that has the secret. 
More formally, for every meeting, if a person x has the secret at time time, 
then they will share the secret with person y, and vice versa.

The secrets are shared instantaneously. That is, a person may receive the secret and share it in the same meeting.

Return a list of all the people that have the secret after all the meetings have taken place. 
You may return the answer in any order.

Constraints:
- 2 <= n <= 10^5
- 1 <= meetings.length <= 10^5
- meetings[i].length == 3
- 0 <= x, y <= n - 1
- x != y
- 1 <= time <= 10^9
- 1 <= firstPerson <= n - 1
"""

# Python Solution
from collections import defaultdict
from heapq import heappop, heappush

def findAllPeople(n, meetings, firstPerson):
    # Initialize the people who know the secret
    secret_known = set([0, firstPerson])
    
    # Group meetings by time
    meetings_by_time = defaultdict(list)
    for x, y, time in meetings:
        meetings_by_time[time].append((x, y))
    
    # Process meetings in time order
    for time in sorted(meetings_by_time.keys()):
        # Build a graph for the current time's meetings
        graph = defaultdict(list)
        for x, y in meetings_by_time[time]:
            graph[x].append(y)
            graph[y].append(x)
        
        # Perform BFS to propagate the secret
        queue = list(secret_known)
        visited = set(queue)
        while queue:
            person = queue.pop()
            for neighbor in graph[person]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # Update the set of people who know the secret
        secret_known.update(visited)
    
    return list(secret_known)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 6
    meetings = [[1, 2, 5], [2, 3, 8], [1, 5, 10]]
    firstPerson = 1
    print(findAllPeople(n, meetings, firstPerson))  # Output: [0, 1, 2, 3, 5]

    # Test Case 2
    n = 4
    meetings = [[0, 2, 1], [1, 3, 1], [0, 3, 3]]
    firstPerson = 3
    print(findAllPeople(n, meetings, firstPerson))  # Output: [0, 3]

    # Test Case 3
    n = 5
    meetings = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4]]
    firstPerson = 1
    print(findAllPeople(n, meetings, firstPerson))  # Output: [0, 1, 2, 3, 4]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the meetings by time: O(m log m), where m is the number of meetings.
- BFS for each group of meetings: O(m + n), where m is the number of edges and n is the number of nodes.
- Overall complexity: O(m log m + m + n).

Space Complexity:
- Graph storage: O(m), where m is the number of meetings.
- BFS queue and visited set: O(n), where n is the number of people.
- Overall complexity: O(m + n).
"""

# Topic: Graphs