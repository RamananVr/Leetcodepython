"""
LeetCode Problem #1942: The Number of the Smallest Unoccupied Chair

Problem Statement:
There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

- When a friend leaves the party, their chair becomes unoccupied.
- If a friend arrives at the same time another friend leaves, the arriving friend can take the chair that is becoming vacant.

You are given a 0-indexed 2D integer array `times` where `times[i] = [arrival[i], leaving[i]]`, indicating the arrival and leaving times of the ith friend. All arrival times are distinct.

Return the chair number that the friend numbered `targetFriend` will sit on.

Example:
Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
Output: 1
Explanation:
- Friend 0 arrives at time 1 and sits on chair 0.
- Friend 1 arrives at time 2 and sits on chair 1.
- Friend 1 leaves at time 3 and chair 1 becomes free.
- Friend 2 arrives at time 4 and sits on chair 1.
Thus, friend 1 sits on chair 1.

Constraints:
- n == times.length
- 2 <= n <= 10^4
- times[i].length == 2
- 1 <= arrival[i] < leaving[i] <= 10^5
- 0 <= targetFriend < n
- All arrival times are distinct.
"""

from heapq import heappush, heappop

def smallestChair(times, targetFriend):
    # Add index to times and sort by arrival time
    times = sorted((arrival, leaving, i) for i, (arrival, leaving) in enumerate(times))
    
    # Min-heaps for available chairs and occupied chairs
    available_chairs = []
    occupied_chairs = []
    
    # Initialize available chairs
    for i in range(len(times)):
        heappush(available_chairs, i)
    
    for arrival, leaving, friend in times:
        # Free up chairs that are now unoccupied
        while occupied_chairs and occupied_chairs[0][0] <= arrival:
            _, chair = heappop(occupied_chairs)
            heappush(available_chairs, chair)
        
        # Assign the smallest available chair
        chair = heappop(available_chairs)
        heappush(occupied_chairs, (leaving, chair))
        
        # If this is the target friend, return the chair number
        if friend == targetFriend:
            return chair

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    times = [[1, 4], [2, 3], [4, 6]]
    targetFriend = 1
    print(smallestChair(times, targetFriend))  # Output: 1

    # Test Case 2
    times = [[3, 10], [1, 5], [2, 6]]
    targetFriend = 0
    print(smallestChair(times, targetFriend))  # Output: 2

    # Test Case 3
    times = [[1, 2], [2, 3], [3, 4]]
    targetFriend = 2
    print(smallestChair(times, targetFriend))  # Output: 0

"""
Time Complexity:
- Sorting the `times` array takes O(n log n), where n is the number of friends.
- Processing each friend's arrival and departure involves heap operations, which are O(log n) each. Since there are n friends, this part takes O(n log n).
- Overall time complexity: O(n log n).

Space Complexity:
- The `available_chairs` and `occupied_chairs` heaps each store at most n elements, so the space complexity is O(n).

Topic: Heap (Priority Queue)
"""