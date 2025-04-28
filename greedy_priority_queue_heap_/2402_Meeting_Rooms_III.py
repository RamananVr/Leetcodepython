"""
LeetCode Problem #2402: Meeting Rooms III

Problem Statement:
You are given an integer n representing the number of meeting rooms, and an array meetings where 
meetings[i] = [start_i, end_i] represents the start and end times of the ith meeting. All the start 
and end times are given as integers.

All the meeting rooms are initially empty. When a meeting starts, you can either:
- Assign an empty meeting room to the meeting.
- If there are no empty meeting rooms, the meeting waits for the earliest available meeting room to become free. 
  If multiple rooms are free at the same time, assign the meeting to the room with the smallest index.

Return the index of the meeting room that held the most meetings. If there are multiple meeting rooms 
that held the same number of meetings, return the smallest index.

Constraints:
- 1 <= n <= 100
- 1 <= meetings.length <= 10^4
- meetings[i].length == 2
- 0 <= start_i < end_i <= 5 * 10^5
"""

import heapq
from collections import Counter

def mostBooked(n, meetings):
    # Sort meetings by their start time
    meetings.sort(key=lambda x: x[0])
    
    # Priority queue for available rooms (sorted by room index)
    available_rooms = list(range(n))
    heapq.heapify(available_rooms)
    
    # Priority queue for ongoing meetings (sorted by end time)
    ongoing_meetings = []
    
    # Counter to track the number of meetings held by each room
    room_meeting_count = Counter()
    
    for start, end in meetings:
        # Free up rooms that have completed their meetings
        while ongoing_meetings and ongoing_meetings[0][0] <= start:
            _, room = heapq.heappop(ongoing_meetings)
            heapq.heappush(available_rooms, room)
        
        if available_rooms:
            # Assign the meeting to the smallest available room
            room = heapq.heappop(available_rooms)
        else:
            # Wait for the earliest available room
            end_time, room = heapq.heappop(ongoing_meetings)
            start = end_time  # Update start time to when the room becomes available
        
        # Schedule the meeting in the room
        heapq.heappush(ongoing_meetings, (start + (end - start), room))
        room_meeting_count[room] += 1
    
    # Find the room with the maximum number of meetings
    max_meetings = max(room_meeting_count.values())
    return min(room for room, count in room_meeting_count.items() if count == max_meetings)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 2
    meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
    print(mostBooked(n, meetings))  # Output: 0

    # Test Case 2
    n = 3
    meetings = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
    print(mostBooked(n, meetings))  # Output: 1

    # Test Case 3
    n = 1
    meetings = [[0, 5], [5, 10], [10, 15]]
    print(mostBooked(n, meetings))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the meetings array takes O(m log m), where m is the number of meetings.
- Each meeting is processed once, and operations on the priority queues (available_rooms and ongoing_meetings) 
  take O(log n), where n is the number of rooms. Thus, processing all meetings takes O(m log n).
- Overall time complexity: O(m log m + m log n).

Space Complexity:
- The available_rooms priority queue stores up to n elements, and the ongoing_meetings priority queue 
  stores up to m elements. Thus, the space complexity is O(n + m).
- The room_meeting_count dictionary uses O(n) space.
- Overall space complexity: O(n + m).

Topic: Greedy, Priority Queue (Heap)
"""