"""
LeetCode Problem #134: Gas Station

Problem Statement:
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank, and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. 
If there exists a solution, it is guaranteed to be unique.

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 units of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. Your tank = 5 - 5 + 4 = 4
The car can travel around the circuit once.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at any station to make the circuit.

Constraints:
- n == gas.length == cost.length
- 1 <= n <= 10^5
- 0 <= gas[i], cost[i] <= 10^4
"""

def canCompleteCircuit(gas, cost):
    """
    Determines the starting gas station index if the car can complete the circuit, otherwise returns -1.

    :param gas: List[int] - Amount of gas at each station
    :param cost: List[int] - Cost of gas to travel to the next station
    :return: int - Starting gas station index or -1 if not possible
    """
    total_tank = 0
    current_tank = 0
    start_index = 0

    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        current_tank += gas[i] - cost[i]

        # If the current tank is negative, reset the start index and current tank
        if current_tank < 0:
            start_index = i + 1
            current_tank = 0

    # If the total tank is negative, it's impossible to complete the circuit
    return start_index if total_tank >= 0 else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(canCompleteCircuit(gas, cost))  # Output: 3

    # Test Case 2
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    print(canCompleteCircuit(gas, cost))  # Output: -1

    # Test Case 3
    gas = [5, 1, 2, 3, 4]
    cost = [4, 4, 1, 5, 1]
    print(canCompleteCircuit(gas, cost))  # Output: 4

    # Test Case 4
    gas = [1, 2, 3, 4]
    cost = [4, 4, 4, 4]
    print(canCompleteCircuit(gas, cost))  # Output: -1

# Time Complexity Analysis:
# The algorithm iterates through the gas and cost arrays once, making it O(n), where n is the number of gas stations.

# Space Complexity Analysis:
# The algorithm uses a constant amount of extra space, making it O(1).

# Topic: Arrays