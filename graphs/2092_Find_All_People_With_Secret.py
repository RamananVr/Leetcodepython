"""
LeetCode Problem #2092: Find All People With Secret

Problem Statement:
You are given an integer `n` indicating the number of people labeled from `0` to `n - 1`. 
You are also given a 2D integer array `meetings`, where `meetings[i] = [x_i, y_i, time_i]` indicates that person `x_i` and person `y_i` met at time `time_i`, and a person may share a secret with the other person at the meeting if either of them knows the secret. 
Initially, only person `0` knows the secret. You are also given an integer `firstPerson` that indicates that person `firstPerson` is the first person that person `0` shares the secret with.

Return a list of all the people that know the secret after all the meetings have taken place. You may return the answer in any order.

Constraints:
1. `2 <= n <= 10^5`
2. `1 <= meetings.length <= 10^5`
3. `meetings[i].length == 3`
4. `0 <= x_i, y_i <= n - 1`
5. `x_i != y_i`
6. `1 <= time_i <= 10^9`
7. `1 <= firstPerson <= n - 1`

The meetings are not necessarily sorted in increasing order of time.

"""

from collections import defaultdict, deque

def findAllPeople(n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
    # Step 1: Group meetings by time
    meetings_by_time = defaultdict(list)
    for x, y, time in meetings:
        meetings_by_time[time].append((x, y))
    
    # Step 2: Initialize the set of people who know the secret
    knows_secret = set([0, firstPerson])
    
    # Step 3: Process meetings in time order
    for time in sorted(meetings_by_time.keys()):
        graph = defaultdict(list)
        for x, y in meetings_by_time[time]:
            graph[x].append(y)
            graph[y].append(x)
        
        # BFS to find all people who can learn the secret at this time
        visited = set()
        queue = deque()
        for person in graph:
            if person in knows_secret:
                queue.append(person)
                visited.add(person)
        
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # Add all visited people to the set of people who know the secret
        knows_secret.update(visited)
    
    return list(knows_secret)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 6
    meetings = [[1, 2, 5], [2, 3, 8], [1, 5, 10]]
    firstPerson = 1
    print(findAllPeople(n, meetings, firstPerson))  # Output: [0, 1, 2, 3, 5]

    # Test Case 2
    n = 4
    meetings = [[3, 1, 3], [1, 2, 2], [0, 3, 3]]
    firstPerson = 3
    print(findAllPeople(n, meetings, firstPerson))  # Output: [0, 1, 3]

    # Test Case 3
    n = 5
    meetings = [[3, 4, 2], [1, 2, 1], [2, 3, 1]]
    firstPerson = 1
    print(findAllPeople(n, meetings, firstPerson))  # Output: [0, 1, 2, 3, 4]

"""
Time Complexity:
- Sorting the meetings by time: O(m log m), where m is the number of meetings.
- BFS for each time group: O(m + n), where m is the number of edges (meetings) and n is the number of nodes (people).
- Overall: O(m log m + m + n) ≈ O(m log m), since m dominates n in most cases.

Space Complexity:
- Storing the graph for each time group: O(m).
- BFS queue and visited set: O(n).
- Overall: O(m + n).

Topic: Graphs
"""