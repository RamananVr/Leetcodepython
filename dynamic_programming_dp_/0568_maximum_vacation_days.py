"""
LeetCode Question #568: Maximum Vacation Days

Problem Statement:
You are given an m x n matrix `flights` representing the airline flights available. 
`flights[i][j]` is 1 if there is a direct flight from city i to city j, and 0 otherwise. 
The cities are numbered from 0 to n-1.

You are also given an n x k matrix `days`, where `days[i][j]` is the number of vacation days 
you can spend in city i during week j.

You start your vacation in city 0 on week 0. You can only fly from the city you are in to another city 
at the end of each week. You cannot fly on the last week.

Return the maximum number of vacation days you can spend.

Constraints:
- `flights` is an m x n matrix where `m == n`.
- `days` is an n x k matrix.
- `1 <= n, k <= 100`.
- `flights[i][j]` is either 0 or 1.
- `0 <= days[i][j] <= 7`.

"""

def maxVacationDays(flights, days):
    """
    Calculate the maximum number of vacation days you can spend.

    :param flights: List[List[int]] - Matrix representing direct flights between cities.
    :param days: List[List[int]] - Matrix representing vacation days in each city per week.
    :return: int - Maximum number of vacation days.
    """
    n = len(flights)  # Number of cities
    k = len(days[0])  # Number of weeks

    # dp[i][j] represents the maximum vacation days you can have in city i at week j
    dp = [[-float('inf')] * k for _ in range(n)]
    dp[0][0] = days[0][0]  # Start in city 0 at week 0

    # Initialize the first week
    for city in range(n):
        if flights[0][city] == 1 or city == 0:  # Can travel to city or stay in city 0
            dp[city][0] = days[city][0]

    # Fill the DP table for subsequent weeks
    for week in range(1, k):
        for city in range(n):
            for prev_city in range(n):
                if flights[prev_city][city] == 1 or prev_city == city:  # Can travel or stay
                    dp[city][week] = max(dp[city][week], dp[prev_city][week - 1] + days[city][week])

    # Find the maximum vacation days across all cities in the last week
    return max(dp[city][k - 1] for city in range(n))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    flights1 = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    days1 = [[1, 3, 1], [6, 0, 3], [3, 3, 3]]
    print(maxVacationDays(flights1, days1))  # Expected Output: 12

    # Test Case 2
    flights2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    days2 = [[1, 1, 1], [7, 7, 7], [7, 7, 7]]
    print(maxVacationDays(flights2, days2))  # Expected Output: 3

    # Test Case 3
    flights3 = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
    days3 = [[1, 2, 3], [3, 2, 1], [1, 1, 1]]
    print(maxVacationDays(flights3, days3))  # Expected Output: 6


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates over all weeks (k), all cities (n), and all previous cities (n).
- Therefore, the time complexity is O(n^2 * k).

Space Complexity:
- The DP table requires O(n * k) space.
- Thus, the space complexity is O(n * k).

Topic: Dynamic Programming (DP)
"""