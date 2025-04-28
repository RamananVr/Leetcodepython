"""
LeetCode Problem #849: Maximize Distance to Closest Person

Problem Statement:
You are given an array representing a row of seats where `seats[i] = 1` represents a person sitting in the `i-th` seat, and `seats[i] = 0` represents that the `i-th` seat is empty (0-indexed).

There is at least one empty seat and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person is maximized. Return that maximum distance to the closest person.

Example 1:
Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second empty seat (seats[2]), the closest person is 2 seats away. 
This is the maximum distance possible, so the answer is 2.

Example 2:
Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last empty seat (seats[3]), the closest person is 3 seats away. 
This is the maximum distance possible, so the answer is 3.

Example 3:
Input: seats = [0,1]
Output: 1
Explanation: 
If Alex sits in the first empty seat (seats[0]), the closest person is 1 seat away. 
This is the maximum distance possible, so the answer is 1.

Constraints:
- 2 <= seats.length <= 2 * 10^4
- seats[i] is 0 or 1.
- At least one seat is empty (0).
- At least one seat is occupied (1).
"""

# Python Solution
def maxDistToClosest(seats):
    """
    Function to calculate the maximum distance to the closest person.
    
    :param seats: List[int] - A list of integers representing the seating arrangement.
    :return: int - The maximum distance to the closest person.
    """
    n = len(seats)
    prev_person = -1
    max_distance = 0

    # Iterate through the seats
    for i in range(n):
        if seats[i] == 1:
            # If this is the first person encountered, calculate distance from the start
            if prev_person == -1:
                max_distance = i
            else:
                # Calculate the distance to the closest person in the middle
                max_distance = max(max_distance, (i - prev_person) // 2)
            prev_person = i

    # Handle the case where the last segment is empty
    max_distance = max(max_distance, n - 1 - prev_person)

    return max_distance

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    seats1 = [1, 0, 0, 0, 1, 0, 1]
    print(maxDistToClosest(seats1))  # Output: 2

    # Test Case 2
    seats2 = [1, 0, 0, 0]
    print(maxDistToClosest(seats2))  # Output: 3

    # Test Case 3
    seats3 = [0, 1]
    print(maxDistToClosest(seats3))  # Output: 1

    # Additional Test Case
    seats4 = [0, 0, 1, 0, 0, 0, 1, 0, 0]
    print(maxDistToClosest(seats4))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the `seats` array once, making it O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space (variables `prev_person` and `max_distance`), making it O(1).

Topic: Arrays
"""