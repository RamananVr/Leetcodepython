"""
LeetCode Question #1109: Corporate Flight Bookings

Problem Statement:
There are n flights, and they are labeled from 1 to n.

You are given an array of flight bookings `bookings`, where `bookings[i] = [first_i, last_i, seats_i]` represents a booking for flights `first_i` through `last_i` (inclusive) with `seats_i` seats reserved for each flight in that range.

Return an array `answer` of length `n`, where `answer[i]` is the total number of seats reserved for flight `i`.

Constraints:
- 1 <= n <= 2 * 10^4
- 1 <= bookings.length <= 2 * 10^4
- bookings[i].length == 3
- 1 <= first_i <= last_i <= n
- 1 <= seats_i <= 10^4
"""

# Solution
def corpFlightBookings(bookings, n):
    """
    Calculate the total number of seats reserved for each flight.

    :param bookings: List[List[int]] - List of bookings where each booking is [first, last, seats].
    :param n: int - Total number of flights.
    :return: List[int] - Total seats reserved for each flight.
    """
    # Initialize an array to store the difference values
    seats = [0] * (n + 1)
    
    # Apply the difference array technique
    for first, last, seats_i in bookings:
        seats[first - 1] += seats_i
        seats[last] -= seats_i
    
    # Compute the prefix sum to get the final seat counts
    answer = [0] * n
    running_sum = 0
    for i in range(n):
        running_sum += seats[i]
        answer[i] = running_sum
    
    return answer

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    print(corpFlightBookings(bookings, n))  # Output: [10, 55, 45, 25, 25]

    # Test Case 2
    bookings = [[1, 1, 5], [2, 2, 10], [3, 3, 15]]
    n = 3
    print(corpFlightBookings(bookings, n))  # Output: [5, 10, 15]

    # Test Case 3
    bookings = [[1, 3, 10], [2, 4, 20], [3, 5, 30]]
    n = 5
    print(corpFlightBookings(bookings, n))  # Output: [10, 30, 60, 50, 30]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the `bookings` list once, which takes O(m) time, where m is the number of bookings.
- It then iterates through the `seats` array to compute the prefix sum, which takes O(n) time, where n is the number of flights.
- Overall time complexity: O(m + n).

Space Complexity:
- The algorithm uses an auxiliary array `seats` of size n + 1 to store the difference values.
- The final result array `answer` is of size n.
- Overall space complexity: O(n).

Topic: Arrays
"""