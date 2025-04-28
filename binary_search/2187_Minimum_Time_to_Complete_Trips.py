"""
LeetCode Problem #2187: Minimum Time to Complete Trips

Problem Statement:
You are given an array `time` where `time[i]` denotes the time taken by the i-th bus to complete one trip. 
Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. 
Also, you are given an integer `totalTrips`, which denotes the number of trips all buses should make in total. 

Return the minimum time required for all buses to complete at least `totalTrips` trips.

Constraints:
- 1 <= time.length <= 10^5
- 1 <= time[i], totalTrips <= 10^7
"""

# Solution
def minimumTime(time, totalTrips):
    def canCompleteTrips(mid):
        # Check if we can complete at least `totalTrips` in `mid` time
        trips = 0
        for t in time:
            trips += mid // t
            if trips >= totalTrips:
                return True
        return trips >= totalTrips

    # Binary search for the minimum time
    left, right = 1, min(time) * totalTrips
    while left < right:
        mid = (left + right) // 2
        if canCompleteTrips(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    time = [1, 2, 3]
    totalTrips = 5
    print(minimumTime(time, totalTrips))  # Output: 3

    # Test Case 2
    time = [2]
    totalTrips = 1
    print(minimumTime(time, totalTrips))  # Output: 2

    # Test Case 3
    time = [5, 10, 10]
    totalTrips = 9
    print(minimumTime(time, totalTrips))  # Output: 25

    # Test Case 4
    time = [1, 1, 1]
    totalTrips = 1000000
    print(minimumTime(time, totalTrips))  # Output: 1000000

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search runs in O(log(min(time) * totalTrips)) iterations.
- For each iteration, we calculate the total trips in O(n), where n is the length of the `time` array.
- Therefore, the overall time complexity is O(n * log(min(time) * totalTrips)).

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Binary Search
"""