"""
LeetCode Problem #2167: Minimum Time to Remove All Cars Containing Illegal Goods

Problem Statement:
You are given a binary string `s` where `s[i] = '0'` indicates the `i-th` car does not contain illegal goods, 
and `s[i] = '1'` indicates the `i-th` car contains illegal goods.

The cars are parked in a single row. You cannot remove a car that is already removed. 
You can remove a car containing illegal goods by paying a cost of `1`. Additionally, 
you can remove all cars to the left or right of a car containing illegal goods by paying a cost equal to the number of cars removed.

Return the minimum cost to remove all cars containing illegal goods.

Constraints:
- `1 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.

"""

# Solution
def minimumTime(s: str) -> int:
    n = len(s)
    left_cost = [0] * n
    right_cost = [0] * n
    
    # Calculate minimum cost to remove cars from the left
    left_cost[0] = int(s[0])
    for i in range(1, n):
        if s[i] == '1':
            left_cost[i] = min(left_cost[i - 1] + 2, i + 1)
        else:
            left_cost[i] = left_cost[i - 1]
    
    # Calculate minimum cost to remove cars from the right
    right_cost[n - 1] = int(s[n - 1])
    for i in range(n - 2, -1, -1):
        if s[i] == '1':
            right_cost[i] = min(right_cost[i + 1] + 2, n - i)
        else:
            right_cost[i] = right_cost[i + 1]
    
    # Combine left and right costs to find the minimum total cost
    min_cost = float('inf')
    for i in range(n - 1):
        min_cost = min(min_cost, left_cost[i] + right_cost[i + 1])
    
    # Consider removing all cars from one side
    min_cost = min(min_cost, left_cost[n - 1], right_cost[0])
    
    return min_cost

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "1100101"
    print(minimumTime(s1))  # Expected Output: 5

    # Test Case 2
    s2 = "0010"
    print(minimumTime(s2))  # Expected Output: 2

    # Test Case 3
    s3 = "1111"
    print(minimumTime(s3))  # Expected Output: 4

    # Test Case 4
    s4 = "0000"
    print(minimumTime(s4))  # Expected Output: 0

    # Test Case 5
    s5 = "101010"
    print(minimumTime(s5))  # Expected Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating `left_cost` takes O(n) time as we iterate through the string once.
- Calculating `right_cost` takes O(n) time as we iterate through the string once in reverse.
- Combining the costs to find the minimum total cost takes O(n) time.
- Overall, the time complexity is O(n).

Space Complexity:
- We use two arrays `left_cost` and `right_cost` of size `n`, which takes O(n) space.
- The overall space complexity is O(n).

Topic: Greedy
"""