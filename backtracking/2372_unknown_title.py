"""
LeetCode Problem #2372: Calculate the Maximum Number of Transfer Requests

Problem Statement:
We have n buildings numbered from 0 to n - 1. Each building has a certain number of employees in it (possibly zero). 
However, there are m transfer requests, and each request consists of two integers [from_i, to_i], where:
- from_i is the building the employee is leaving.
- to_i is the building the employee is moving to.

We can approve some of these requests. The goal is to maximize the number of requests that can be approved such that 
the net change in the number of employees in each building is zero. This means the number of employees leaving a building 
is equal to the number of employees entering it for all buildings.

Return the maximum number of requests that can be approved.

Constraints:
- 1 <= n <= 20
- 1 <= requests.length <= 16
- 0 <= from_i, to_i < n

Example:
Input: n = 3, requests = [[0,1],[1,2],[2,0],[1,0],[2,1]]
Output: 5
Explanation: All requests can be approved because the net change in the number of employees for each building is zero.
"""

from typing import List

def maximumRequests(n: int, requests: List[List[int]]) -> int:
    def is_valid(balance):
        # Check if all buildings have a net balance of 0
        return all(b == 0 for b in balance)

    def backtrack(index, count, balance):
        nonlocal max_requests
        if index == len(requests):
            if is_valid(balance):
                max_requests = max(max_requests, count)
            return
        
        # Option 1: Approve the current request
        from_i, to_i = requests[index]
        balance[from_i] -= 1
        balance[to_i] += 1
        backtrack(index + 1, count + 1, balance)
        # Backtrack the changes
        balance[from_i] += 1
        balance[to_i] -= 1

        # Option 2: Skip the current request
        backtrack(index + 1, count, balance)

    max_requests = 0
    balance = [0] * n
    backtrack(0, 0, balance)
    return max_requests

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 3
    requests1 = [[0, 1], [1, 2], [2, 0], [1, 0], [2, 1]]
    print(maximumRequests(n1, requests1))  # Output: 5

    # Test Case 2
    n2 = 4
    requests2 = [[0, 3], [3, 1], [1, 2], [2, 0], [0, 1], [1, 0]]
    print(maximumRequests(n2, requests2))  # Output: 4

    # Test Case 3
    n3 = 2
    requests3 = [[0, 1], [1, 0], [0, 1], [1, 0]]
    print(maximumRequests(n3, requests3))  # Output: 4

"""
Time Complexity:
- The solution uses backtracking to explore all subsets of the requests array.
- For each request, we have two choices: approve or skip. This results in 2^m subsets, where m is the number of requests.
- For each subset, we check the balance array, which takes O(n) time.
- Overall time complexity: O(n * 2^m), where n is the number of buildings and m is the number of requests.

Space Complexity:
- The space complexity is O(n) due to the balance array used to track the net change in employees for each building.

Topic: Backtracking
"""