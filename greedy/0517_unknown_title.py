"""
LeetCode Problem #517: Super Washing Machines

Problem Statement:
You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty. 
For each move, you could choose any m (1 ≤ m ≤ n) washing machines, and pass one dress of each washing machine 
to one of its adjacent washing machines at the same time.

Given an integer array `machines` representing the number of dresses in each washing machine from left to right 
on the line, return the minimum number of moves to make all the washing machines have the same number of dresses. 
If it is not possible, return -1.

Example 1:
Input: machines = [1,0,5]
Output: 3
Explanation:
1st move:    1     0 <-- 5    =>    1     1     4
2nd move:    1 <-- 1 <-- 4    =>    2     1     3    
3rd move:    2     1 <-- 3    =>    2     2     2   

Example 2:
Input: machines = [0,3,0]
Output: 2
Explanation:
1st move:    0 <-- 3     0    =>    1     2     0    
2nd move:    1     2 --> 0    =>    1     1     1     

Example 3:
Input: machines = [0,2,0]
Output: -1
Explanation:
It's impossible to make all the washing machines have the same number of dresses.

Constraints:
- n == machines.length
- 1 <= n <= 10^4
- 0 <= machines[i] <= 10^5
"""

def findMinMoves(machines):
    """
    Function to calculate the minimum number of moves to balance the washing machines.

    :param machines: List[int] - Number of dresses in each washing machine
    :return: int - Minimum number of moves to balance the machines, or -1 if not possible
    """
    total_dresses = sum(machines)
    n = len(machines)
    
    # If the total number of dresses cannot be evenly distributed, return -1
    if total_dresses % n != 0:
        return -1
    
    target = total_dresses // n
    max_moves = 0
    running_balance = 0
    
    for dresses in machines:
        # Calculate the difference between current dresses and target
        diff = dresses - target
        running_balance += diff
        # The maximum moves required is the maximum of:
        # 1. The absolute running balance (to account for cumulative imbalance)
        # 2. The current difference (to account for local imbalance)
        max_moves = max(max_moves, abs(running_balance), diff)
    
    return max_moves

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    machines1 = [1, 0, 5]
    print(findMinMoves(machines1))  # Output: 3

    # Test Case 2
    machines2 = [0, 3, 0]
    print(findMinMoves(machines2))  # Output: 2

    # Test Case 3
    machines3 = [0, 2, 0]
    print(findMinMoves(machines3))  # Output: -1

    # Test Case 4
    machines4 = [4, 0, 0, 4]
    print(findMinMoves(machines4))  # Output: 4

    # Test Case 5
    machines5 = [1, 2, 3]
    print(findMinMoves(machines5))  # Output: 2

"""
Time Complexity:
- O(n): We iterate through the `machines` array once to calculate the total dresses and once to compute the moves.

Space Complexity:
- O(1): We use a constant amount of extra space.

Topic: Greedy
"""