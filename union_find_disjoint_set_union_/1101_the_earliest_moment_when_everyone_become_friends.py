"""
LeetCode Question #1101: The Earliest Moment When Everyone Become Friends

Problem Statement:
There are n people in a social group labeled from 0 to n - 1. You are given a list of logs, 
where logs[i] = [timestamp, person1, person2] indicates that person1 and person2 became friends 
at the time timestamp. Friendship is transitive, meaning if person1 is a friend of person2 and 
person2 is a friend of person3, then person1 is also a friend of person3. A person is considered 
to be friends with themselves.

Return the earliest time at which all n people become friends. If it is impossible for all n 
people to become friends, return -1.

Example 1:
Input: logs = [[20190101, 0, 1], [20190104, 1, 2], [20190107, 2, 3], [20190109, 3, 4]], n = 5
Output: 20190107
Explanation:
At timestamp = 20190101, person 0 and 1 become friends.
At timestamp = 20190104, person 1 and 2 become friends.
At timestamp = 20190107, person 2 and 3 become friends. All 5 people are now connected.

Example 2:
Input: logs = [[0, 1, 2], [1, 3, 4]], n = 5
Output: -1
Explanation:
There is no way to connect all 5 people.

Constraints:
- 2 <= n <= 100
- 1 <= logs.length <= 10^4
- logs[i].length == 3
- 0 <= timestamp <= 10^9
- 0 <= person1, person2 <= n - 1
- person1 != person2
- All the timestamps in logs are unique.
"""

# Python Solution
from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n  # Number of connected components

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.components -= 1  # Reduce the number of components

def earliestAcq(logs: List[List[int]], n: int) -> int:
    # Sort logs by timestamp
    logs.sort(key=lambda x: x[0])
    
    uf = UnionFind(n)
    
    for timestamp, person1, person2 in logs:
        uf.union(person1, person2)
        if uf.components == 1:  # All people are connected
            return timestamp
    
    return -1  # Not all people are connected

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    logs1 = [[20190101, 0, 1], [20190104, 1, 2], [20190107, 2, 3], [20190109, 3, 4]]
    n1 = 5
    print(earliestAcq(logs1, n1))  # Output: 20190107

    # Test Case 2
    logs2 = [[0, 1, 2], [1, 3, 4]]
    n2 = 5
    print(earliestAcq(logs2, n2))  # Output: -1

    # Test Case 3
    logs3 = [[1, 0, 1], [2, 1, 2], [3, 2, 3], [4, 3, 4], [5, 4, 0]]
    n3 = 5
    print(earliestAcq(logs3, n3))  # Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the logs takes O(m * log(m)), where m is the length of the logs.
- Union-Find operations (find and union) are nearly constant time, O(α(n)), where α is the inverse Ackermann function.
- Overall complexity: O(m * log(m) + m * α(n)) ≈ O(m * log(m)) for large m.

Space Complexity:
- The Union-Find data structure uses O(n) space for the parent and rank arrays.
- Overall space complexity: O(n).
"""

# Topic: Union-Find (Disjoint Set Union)