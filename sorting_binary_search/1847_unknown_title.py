"""
LeetCode Problem #1847: Closest Room

Problem Statement:
You are given n rooms represented by a 2D integer array rooms where rooms[i] = [roomId_i, size_i] denotes the ID and size of the ith room. All room IDs are distinct.

You are also given m queries represented by a 2D integer array queries where queries[j] = [preferred_j, minSize_j]. The answer to the jth query is the room ID of a room such that:
- The room has a size of at least minSize_j, and
- abs(roomId - preferred_j) is minimized, where abs(x) is the absolute value of x.

If there is a tie in the absolute difference, then use the room with the smallest room ID. If there is no such room, the answer is -1.

Return an array answer of length m where answer[j] is the answer to the jth query.

Constraints:
- 1 <= rooms.length <= 10^5
- 1 <= queries.length <= 10^4
- rooms[i].length == 2
- queries[j].length == 2
- 1 <= roomId_i, preferred_j <= 10^7
- 1 <= size_i, minSize_j <= 10^7
"""

# Python Solution
from sortedcontainers import SortedList

def closestRoom(rooms, queries):
    # Sort rooms by size in descending order
    rooms.sort(key=lambda x: x[1], reverse=True)
    
    # Add index to queries for sorting and result placement
    queries = [(preferred, minSize, idx) for idx, (preferred, minSize) in enumerate(queries)]
    queries.sort(key=lambda x: x[1], reverse=True)  # Sort queries by minSize in descending order
    
    result = [-1] * len(queries)
    valid_rooms = SortedList()  # Sorted list to maintain room IDs
    
    room_idx = 0
    for preferred, minSize, query_idx in queries:
        # Add rooms that satisfy the size constraint to valid_rooms
        while room_idx < len(rooms) and rooms[room_idx][1] >= minSize:
            valid_rooms.add(rooms[room_idx][0])
            room_idx += 1
        
        # If no valid rooms, answer is -1
        if not valid_rooms:
            result[query_idx] = -1
            continue
        
        # Find the closest room ID using binary search
        pos = valid_rooms.bisect(preferred)
        closest = float('inf')
        
        # Check the room at position pos (if exists)
        if pos < len(valid_rooms):
            closest = valid_rooms[pos]
        
        # Check the room at position pos - 1 (if exists)
        if pos > 0:
            if abs(valid_rooms[pos - 1] - preferred) < abs(closest - preferred) or (
                abs(valid_rooms[pos - 1] - preferred) == abs(closest - preferred) and valid_rooms[pos - 1] < closest):
                closest = valid_rooms[pos - 1]
        
        result[query_idx] = closest
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rooms = [[2, 3], [1, 4], [3, 5]]
    queries = [[2, 3], [2, 4], [2, 5]]
    print(closestRoom(rooms, queries))  # Output: [2, 1, 3]

    # Test Case 2
    rooms = [[1, 2], [2, 3], [3, 4]]
    queries = [[2, 3], [3, 4], [1, 2]]
    print(closestRoom(rooms, queries))  # Output: [2, 3, 1]

    # Test Case 3
    rooms = [[1, 5], [2, 6], [3, 7]]
    queries = [[4, 5], [1, 6], [2, 7]]
    print(closestRoom(rooms, queries))  # Output: [1, 2, 3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting rooms: O(n log n), where n is the number of rooms.
- Sorting queries: O(m log m), where m is the number of queries.
- Processing each query: O(log k), where k is the number of valid rooms at that point (using SortedList).
  In the worst case, k = n, so processing all queries takes O(m log n).
Overall: O(n log n + m log m + m log n).

Space Complexity:
- SortedList for valid rooms: O(n) in the worst case.
- Result array: O(m).
Overall: O(n + m).
"""

# Topic: Sorting, Binary Search