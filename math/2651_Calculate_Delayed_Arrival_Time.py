"""
LeetCode Problem #2651: Calculate Delayed Arrival Time

Problem Statement:
You are given a positive integer `arrivalTime` denoting the arrival time of a train in hours, and another positive integer `delayedTime` denoting the delay in hours.

Return the time in hours when the train will arrive at the station after the delay. Note that the time in hours is represented in the 24-hour format.

Constraints:
- 1 <= arrivalTime < 24
- 1 <= delayedTime <= 24
"""

def findDelayedArrivalTime(arrivalTime: int, delayedTime: int) -> int:
    """
    Calculate the delayed arrival time in 24-hour format.

    Args:
    arrivalTime (int): The original arrival time in hours (1 <= arrivalTime < 24).
    delayedTime (int): The delay in hours (1 <= delayedTime <= 24).

    Returns:
    int: The delayed arrival time in 24-hour format.
    """
    return (arrivalTime + delayedTime) % 24

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arrivalTime = 15
    delayedTime = 5
    print(findDelayedArrivalTime(arrivalTime, delayedTime))  # Expected Output: 20

    # Test Case 2
    arrivalTime = 23
    delayedTime = 2
    print(findDelayedArrivalTime(arrivalTime, delayedTime))  # Expected Output: 1

    # Test Case 3
    arrivalTime = 1
    delayedTime = 24
    print(findDelayedArrivalTime(arrivalTime, delayedTime))  # Expected Output: 1

    # Test Case 4
    arrivalTime = 10
    delayedTime = 14
    print(findDelayedArrivalTime(arrivalTime, delayedTime))  # Expected Output: 0

"""
Time Complexity Analysis:
- The function performs a single addition and a modulo operation, both of which are O(1).
- Therefore, the time complexity is O(1).

Space Complexity Analysis:
- The function uses a constant amount of space for its computation.
- Therefore, the space complexity is O(1).

Topic: Math
"""