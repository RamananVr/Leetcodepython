"""
LeetCode Problem #2456: Most Popular Video Creator

Problem Statement:
You are given two lists `creators` and `ids`, and a list `views` where:
- `creators[i]` is the name of the creator of the i-th video.
- `ids[i]` is the unique ID of the i-th video.
- `views[i]` is the number of views on the i-th video.

The popularity of a creator is the sum of the number of views on all of their videos. Return a list of the most popular creators and their most viewed video. If there are multiple creators with the same popularity, return all of them.

For each creator in the result, return their name and the ID of their most viewed video. If there is a tie for the most viewed video, return the lexicographically smallest ID.

Input:
- `creators`, `ids`, and `views` are lists of the same length.
- `1 <= len(creators) == len(ids) == len(views) <= 10^5`
- `1 <= len(creators[i]), len(ids[i]) <= 10`
- `0 <= views[i] <= 10^7`

Output:
- A list of tuples where each tuple contains the name of a creator and the ID of their most viewed video.

Example:
Input:
creators = ["alice", "bob", "alice", "chris"]
ids = ["one", "two", "three", "four"]
views = [5, 10, 5, 4]

Output:
[("alice", "one"), ("bob", "two")]

Explanation:
- "alice" has 10 views (5 + 5) and her most viewed video is "one" (5 views).
- "bob" has 10 views and his most viewed video is "two" (10 views).
- "chris" has 4 views, but he is not among the most popular creators.

Constraints:
- The input data is guaranteed to be valid.

"""

# Python Solution
from collections import defaultdict

def mostPopularCreator(creators, ids, views):
    # Step 1: Initialize dictionaries to store popularity and most viewed video info
    popularity = defaultdict(int)
    most_viewed = defaultdict(lambda: (0, ""))  # (views, id)

    # Step 2: Populate the dictionaries
    for creator, video_id, view_count in zip(creators, ids, views):
        popularity[creator] += view_count
        # Update most viewed video for the creator
        if view_count > most_viewed[creator][0] or (view_count == most_viewed[creator][0] and video_id < most_viewed[creator][1]):
            most_viewed[creator] = (view_count, video_id)

    # Step 3: Find the maximum popularity
    max_popularity = max(popularity.values())

    # Step 4: Collect the result for creators with maximum popularity
    result = []
    for creator, total_views in popularity.items():
        if total_views == max_popularity:
            result.append((creator, most_viewed[creator][1]))

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    creators = ["alice", "bob", "alice", "chris"]
    ids = ["one", "two", "three", "four"]
    views = [5, 10, 5, 4]
    print(mostPopularCreator(creators, ids, views))  # Output: [("alice", "one"), ("bob", "two")]

    # Test Case 2
    creators = ["alice", "alice", "bob", "bob", "chris"]
    ids = ["a", "b", "c", "d", "e"]
    views = [10, 20, 15, 15, 5]
    print(mostPopularCreator(creators, ids, views))  # Output: [("alice", "b"), ("bob", "c")]

    # Test Case 3
    creators = ["x", "y", "z"]
    ids = ["id1", "id2", "id3"]
    views = [100, 200, 300]
    print(mostPopularCreator(creators, ids, views))  # Output: [("z", "id3")]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the input lists once, which takes O(n) time, where n is the length of the input lists.
- Finding the maximum popularity takes O(m) time, where m is the number of unique creators.
- Overall, the time complexity is O(n + m).

Space Complexity:
- The `popularity` and `most_viewed` dictionaries store data for each unique creator, which takes O(m) space.
- The result list takes O(k) space, where k is the number of most popular creators.
- Overall, the space complexity is O(m + k).

In the worst case, m = n (all creators are unique), so the space complexity becomes O(n).
"""

# Topic: Hash Table, Arrays