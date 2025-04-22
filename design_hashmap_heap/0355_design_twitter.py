"""
LeetCode Question #355: Design Twitter

Problem Statement:
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and see the 10 most recent tweets in the user's news feed. Implement the Twitter class:

1. `Twitter()` Initializes your Twitter object.
2. `postTweet(userId: int, tweetId: int) -> None` Composes a new tweet with ID `tweetId` by the user `userId`. Each call to this method will assign a unique timestamp to the tweet.
3. `getNewsFeed(userId: int) -> List[int]` Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user follows or by the user themself. Tweets must be ordered from most recent to least recent.
4. `follow(followerId: int, followeeId: int) -> None` The user with ID `followerId` starts following the user with ID `followeeId`.
5. `unfollow(followerId: int, followeeId: int) -> None` The user with ID `followerId` stops following the user with ID `followeeId`.

Constraints:
- `1 <= userId, followerId, followeeId, tweetId <= 500`
- All the tweets have unique IDs.
- At most 10^4 calls will be made to `postTweet`, `getNewsFeed`, `follow`, and `unfollow`.

"""

from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        # Initialize data structures
        self.timestamp = 0  # Global timestamp to track tweet order
        self.tweets = defaultdict(list)  # Maps userId -> list of (timestamp, tweetId)
        self.following = defaultdict(set)  # Maps userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add the tweet to the user's tweet list with the current timestamp
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        # Get the user's own tweets and the tweets of the users they follow
        min_heap = []
        users_to_check = self.following[userId] | {userId}  # Include the user themself
        for user in users_to_check:
            for tweet in self.tweets[user]:
                heapq.heappush(min_heap, tweet)
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)

        # Extract the 10 most recent tweets in reverse order
        return [tweetId for _, tweetId in sorted(min_heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add followeeId to the followerId's following set
        if followerId != followeeId:  # Prevent self-following
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove followeeId from the followerId's following set
        self.following[followerId].discard(followeeId)


# Example Test Cases
if __name__ == "__main__":
    twitter = Twitter()

    # User 1 posts a tweet
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))  # Output: [5]

    # User 1 follows user 2
    twitter.follow(1, 2)

    # User 2 posts a tweet
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))  # Output: [6, 5]

    # User 1 unfollows user 2
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))  # Output: [5]

    # User 2 posts another tweet
    twitter.postTweet(2, 7)
    print(twitter.getNewsFeed(2))  # Output: [7, 6]

"""
Time and Space Complexity Analysis:

1. `postTweet`:
   - Time Complexity: O(1) (Appending a tweet to the user's list is constant time.)
   - Space Complexity: O(1) (Each tweet takes constant space.)

2. `getNewsFeed`:
   - Time Complexity: O(U + T * log(10)), where U is the number of users the user follows, and T is the total number of tweets from those users. The heap is limited to size 10, so operations on it are O(log(10)).
   - Space Complexity: O(10) = O(1) (The heap is limited to size 10.)

3. `follow`:
   - Time Complexity: O(1) (Adding a user to a set is constant time.)
   - Space Complexity: O(1) (Each follow relationship takes constant space.)

4. `unfollow`:
   - Time Complexity: O(1) (Removing a user from a set is constant time.)
   - Space Complexity: O(1) (No additional space is used.)

Overall:
- Time Complexity: Efficient for the given constraints, with `getNewsFeed` being the most expensive operation.
- Space Complexity: Scales with the number of tweets and follow relationships.

Topic: Design, HashMap, Heap