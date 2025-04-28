"""
LeetCode Problem #841: Keys and Rooms

Problem Statement:
There are `n` rooms labeled from `0` to `n - 1`, and all the rooms are locked except for room `0`. 
Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, 
denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array `rooms` where `rooms[i]` is the set of keys that you can obtain if you visit room `i`, 
return `true` if you can visit all the rooms, or `false` otherwise.

Constraints:
- `n == rooms.length`
- `2 <= n <= 1000`
- `0 <= rooms[i].length <= 1000`
- `1 <= sum(rooms[i].length) <= 3000`
- `0 <= rooms[i][j] < n`
- All the values of `rooms[i]` are unique.
"""

from collections import deque

def canVisitAllRooms(rooms):
    """
    Determines if all rooms can be visited starting from room 0.

    :param rooms: List[List[int]] - A list of rooms where each room contains a list of keys.
    :return: bool - True if all rooms can be visited, False otherwise.
    """
    n = len(rooms)
    visited = set()
    queue = deque([0])  # Start with room 0

    while queue:
        current_room = queue.popleft()
        if current_room not in visited:
            visited.add(current_room)
            for key in rooms[current_room]:
                if key not in visited:
                    queue.append(key)

    return len(visited) == n


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rooms1 = [[1], [2], [3], []]
    print(canVisitAllRooms(rooms1))  # Expected Output: True

    # Test Case 2
    rooms2 = [[1, 3], [3, 0, 1], [2], [0]]
    print(canVisitAllRooms(rooms2))  # Expected Output: False

    # Test Case 3
    rooms3 = [[1, 2, 3], [], [], []]
    print(canVisitAllRooms(rooms3))  # Expected Output: True

    # Test Case 4
    rooms4 = [[1], [2], [], [0]]
    print(canVisitAllRooms(rooms4))  # Expected Output: False


"""
Time Complexity Analysis:
- Let `n` be the number of rooms and `k` be the total number of keys across all rooms.
- In the worst case, we visit each room once and process all keys once.
- Visiting each room and processing its keys takes O(k) time in total.
- Therefore, the time complexity is O(k).

Space Complexity Analysis:
- The `visited` set stores up to `n` rooms, and the `queue` can also hold up to `n` rooms in the worst case.
- Therefore, the space complexity is O(n).

Topic: Graph Traversal (BFS)
"""