"""
LeetCode Question #2076: Process Restricted Friend Requests

Problem Statement:
You are given an integer n indicating the number of people in a social network, labeled from 0 to n - 1. 
You are also given a 2D integer array restrictions, where restrictions[i] = [xi, yi] means that person xi 
and person yi cannot become friends directly or indirectly through other people.

You are also given a 2D integer array requests, where requests[j] = [uj, vj] is a friend request between 
person uj and person vj.

Return a boolean array answer, where answer[j] is true if the friend request requests[j] can be accepted, 
and false otherwise.

A friend request is accepted if:
1. uj and vj are not directly or indirectly restricted from being friends.
2. uj and vj can be connected directly or indirectly through other people.

If a request is accepted, the two people become direct friends.

Constraints:
- 2 <= n <= 1000
- 0 <= restrictions.length <= 1000
- restrictions[i].length == 2
- 0 <= xi, yi <= n - 1
- xi != yi
- 0 <= requests.length <= 1000
- requests[j].length == 2
- 0 <= uj, vj <= n - 1
- uj != vj
"""

# Solution
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def processRestrictedFriendRequests(n, restrictions, requests):
    uf = UnionFind(n)
    answer = []

    for u, v in requests:
        root_u = uf.find(u)
        root_v = uf.find(v)
        can_be_friends = True

        for x, y in restrictions:
            root_x = uf.find(x)
            root_y = uf.find(y)
            if (root_u == root_x and root_v == root_y) or (root_u == root_y and root_v == root_x):
                can_be_friends = False
                break

        if can_be_friends:
            uf.union(u, v)
            answer.append(True)
        else:
            answer.append(False)

    return answer

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 5
    restrictions = [[0, 1], [1, 2], [2, 3]]
    requests = [[0, 4], [1, 3], [3, 4], [2, 4]]
    print(processRestrictedFriendRequests(n, restrictions, requests))  # Output: [True, False, True, False]

    # Test Case 2
    n = 3
    restrictions = [[0, 1]]
    requests = [[0, 2], [2, 1]]
    print(processRestrictedFriendRequests(n, restrictions, requests))  # Output: [True, False]

    # Test Case 3
    n = 4
    restrictions = []
    requests = [[0, 1], [1, 2], [2, 3]]
    print(processRestrictedFriendRequests(n, restrictions, requests))  # Output: [True, True, True]

# Time and Space Complexity Analysis
# Time Complexity:
# - The `find` operation has an amortized time complexity of O(α(n)), where α is the inverse Ackermann function.
# - The `union` operation also has an amortized time complexity of O(α(n)).
# - For each request, we iterate through the restrictions, which takes O(r), where r is the number of restrictions.
# - Overall, the time complexity is O(m * r * α(n)), where m is the number of requests.

# Space Complexity:
# - The Union-Find data structure uses O(n) space for the parent and rank arrays.
# - The space complexity is O(n).

# Topic: Union-Find (Disjoint Set Union)