"""
LeetCode Problem #1311: Get Watched Videos by Your Friends

Problem Statement:
You are given two things: a list of friends, and a list of watched videos by each friend. 
The friends list is represented as an adjacency list, where `friends[i]` is a list of all the friends of the person `i`.
The watched videos list is represented as a list of lists, where `watchedVideos[i]` is a list of all the videos watched by the person `i`.

You are also given two integers `id` and `level`. A person `j` is considered to be at the `level`-th level of person `id` if the shortest path in the friends list from `id` to `j` is exactly `level`.

Return a list of videos ordered by their frequency within the `level`-th level of friends of the given person `id`. If multiple videos have the same frequency, order them alphabetically.

Constraints:
- `2 <= n <= 100`
- `1 <= watchedVideos[i].length <= 100`
- `1 <= watchedVideos[i][j].length <= 8`
- `0 <= friends[i][j] < n`
- `0 <= id < n`
- `1 <= level < n`
- `friends[i]` does not contain `i`.
- All the values of `friends[i]` are unique.
- All the values of `watchedVideos[i]` are unique.

"""

from collections import deque, Counter

def watchedVideosByFriends(watchedVideos, friends, id, level):
    """
    Returns a list of videos ordered by their frequency within the `level`-th level of friends of the given person `id`.
    
    :param watchedVideos: List[List[str]] - List of videos watched by each person.
    :param friends: List[List[int]] - Adjacency list representing friendships.
    :param id: int - ID of the person.
    :param level: int - Level of friends to consider.
    :return: List[str] - List of videos ordered by frequency and alphabetically.
    """
    # Perform BFS to find friends at the given level
    queue = deque([id])
    visited = set([id])
    current_level = 0
    
    while queue and current_level < level:
        for _ in range(len(queue)):
            person = queue.popleft()
            for friend in friends[person]:
                if friend not in visited:
                    visited.add(friend)
                    queue.append(friend)
        current_level += 1
    
    # Collect videos watched by friends at the target level
    videos = []
    for friend in queue:
        videos.extend(watchedVideos[friend])
    
    # Count video frequencies and sort by frequency and lexicographical order
    video_count = Counter(videos)
    return sorted(video_count.keys(), key=lambda x: (video_count[x], x))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    watchedVideos = [["A", "B"], ["C"], ["B", "C"], ["D"]]
    friends = [[1, 2], [0, 3], [0, 3], [1, 2]]
    id = 0
    level = 1
    print(watchedVideosByFriends(watchedVideos, friends, id, level))  # Output: ["B", "C"]

    # Test Case 2
    watchedVideos = [["A", "B"], ["C"], ["B", "C"], ["D"]]
    friends = [[1, 2], [0, 3], [0, 3], [1, 2]]
    id = 0
    level = 2
    print(watchedVideosByFriends(watchedVideos, friends, id, level))  # Output: ["D"]

    # Test Case 3
    watchedVideos = [["X", "Y"], ["Z"], ["X", "Z"], ["Y", "Z"]]
    friends = [[1, 2], [0, 3], [0, 3], [1, 2]]
    id = 1
    level = 1
    print(watchedVideosByFriends(watchedVideos, friends, id, level))  # Output: ["X", "Y"]

"""
Time and Space Complexity Analysis:

Time Complexity:
- BFS traversal: O(n + e), where `n` is the number of people and `e` is the number of edges in the friends graph.
- Collecting videos: O(f), where `f` is the number of friends at the target level.
- Counting frequencies: O(v), where `v` is the total number of videos watched by friends at the target level.
- Sorting videos: O(v log v), where `v` is the number of unique videos.

Overall: O(n + e + v log v)

Space Complexity:
- BFS queue and visited set: O(n)
- Video list and frequency counter: O(v)

Overall: O(n + v)

Topic: Graphs
"""