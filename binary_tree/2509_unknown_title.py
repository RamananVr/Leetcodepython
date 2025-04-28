"""
LeetCode Problem #2509: Cycle Length Queries in a Tree

Problem Statement:
You are given an integer `n` representing the number of nodes in a binary tree rooted at node 1. 
The nodes are numbered from 1 to n. Each node i has two children: 2 * i and 2 * i + 1 if they are 
less than or equal to n.

You are also given a 2D integer array `queries` of size m where `queries[j] = [u, v]`. For each query, 
find the cycle length between nodes u and v. The cycle length is defined as the number of edges 
in the cycle formed by the path from u to v and back to u.

Return an array of integers `answer` where `answer[j]` is the answer to the j-th query.

Constraints:
- 1 <= n <= 10^5
- 1 <= queries.length <= 10^4
- queries[j].length == 2
- 1 <= u, v <= n

"""

# Solution
def cycleLengthQueries(n, queries):
    def find_depth(node):
        depth = 0
        while node > 1:
            node //= 2
            depth += 1
        return depth

    def find_lca(u, v):
        while u != v:
            if u > v:
                u //= 2
            else:
                v //= 2
        return u

    result = []
    for u, v in queries:
        depth_u = find_depth(u)
        depth_v = find_depth(v)
        lca = find_lca(u, v)
        depth_lca = find_depth(lca)
        cycle_length = (depth_u - depth_lca) + (depth_v - depth_lca) + 1
        result.append(cycle_length)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 8
    queries = [[4, 7], [2, 6], [1, 8]]
    print(cycleLengthQueries(n, queries))  # Output: [5, 4, 6]

    # Test Case 2
    n = 15
    queries = [[9, 14], [5, 11], [1, 15]]
    print(cycleLengthQueries(n, queries))  # Output: [5, 6, 8]

    # Test Case 3
    n = 3
    queries = [[1, 2], [2, 3], [1, 3]]
    print(cycleLengthQueries(n, queries))  # Output: [2, 3, 3]

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The `find_depth` function takes O(log(n)) time because it repeatedly divides the node by 2.
   - The `find_lca` function also takes O(log(n)) time because it moves up the tree until the nodes converge.
   - For each query, we perform these operations, so the total time complexity is O(m * log(n)), 
     where m is the number of queries.

2. Space Complexity:
   - The solution uses O(1) additional space since no extra data structures are used apart from variables.

Topic: Binary Tree
"""