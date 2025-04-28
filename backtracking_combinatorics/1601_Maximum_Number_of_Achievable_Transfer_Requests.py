"""
LeetCode Problem #1601: Maximum Number of Achievable Transfer Requests

Problem Statement:
We have n buildings numbered from 0 to n - 1. Each building has a number of employees. 
It's guaranteed that no two buildings have the same number of employees in the beginning. 
You are given an array requests where requests[i] = [from_i, to_i] represents an employee's 
request to transfer from building from_i to building to_i.

All buildings are connected by an employee transfer system, and you can grant or deny any number of requests. 
If you grant a request, the number of employees in both buildings involved in the request changes by one. 
In particular, "from_i" loses an employee, and "to_i" gains an employee.

Your task is to find the maximum number of requests that can be granted such that the number of employees 
in all the buildings is the same after processing all the granted requests.

Example 1:
Input: n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
Output: 5

Example 2:
Input: n = 3, requests = [[0,0],[1,2],[2,1]]
Output: 3

Example 3:
Input: n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
Output: 4

Constraints:
- 1 <= n <= 20
- 1 <= requests.length <= 16
- requests[i].length == 2
- 0 <= from_i, to_i < n
"""

# Solution
from itertools import combinations

def maximumRequests(n, requests):
    def is_valid(balance):
        return all(b == 0 for b in balance)

    max_requests = 0
    for k in range(len(requests) + 1):
        for subset in combinations(requests, k):
            balance = [0] * n
            for from_i, to_i in subset:
                balance[from_i] -= 1
                balance[to_i] += 1
            if is_valid(balance):
                max_requests = max(max_requests, k)
    return max_requests

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    requests1 = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
    print(maximumRequests(n1, requests1))  # Output: 5

    # Test Case 2
    n2 = 3
    requests2 = [[0,0],[1,2],[2,1]]
    print(maximumRequests(n2, requests2))  # Output: 3

    # Test Case 3
    n3 = 4
    requests3 = [[0,3],[3,1],[1,2],[2,0]]
    print(maximumRequests(n3, requests3))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- The number of subsets of requests is 2^m, where m is the length of the requests array.
- For each subset, we calculate the balance array, which takes O(m) time.
- Therefore, the overall time complexity is O(m * 2^m), where m is the number of requests.

Space Complexity:
- The space complexity is O(n) for the balance array, where n is the number of buildings.
- Additionally, the combinations function may use extra space for generating subsets, but this is negligible compared to the exponential growth of subsets.

Overall Space Complexity: O(n)
"""

# Topic: Backtracking, Combinatorics