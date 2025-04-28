"""
LeetCode Problem #1348: Tweet Counts Per Frequency

Problem Statement:
Design a system that receives tweets and returns the number of tweets in a particular time frame.

Implement the `TweetCounts` class:
- `TweetCounts()` Initializes the object.
- `void recordTweet(String tweetName, int time)` Stores the tweetName at the recorded time (in seconds).
- `List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime)` 
  Returns the number of tweets per frequency interval for the given tweetName in the time range [startTime, endTime] inclusive.

The frequency intervals are:
- "minute" -> 60 seconds
- "hour" -> 3600 seconds
- "day" -> 86400 seconds

The first interval always starts at `startTime`, so the intervals are:
[startTime, startTime + interval - 1], [startTime + interval, startTime + 2 * interval - 1], and so on.
The last interval may end before `endTime`.

Constraints:
- There will be at most 10000 calls in total to `recordTweet` and `getTweetCountsPerFrequency`.
- Each `time` is in the range [0, 10^9].
- `startTime` and `endTime` are in the range [0, 10^9].
- `startTime` <= `endTime`.
- `freq` is one of "minute", "hour", or "day".
- At most 10 different tweet names will be used.

"""

from collections import defaultdict
import bisect

class TweetCounts:
    def __init__(self):
        # Dictionary to store tweetName as key and a sorted list of times as value
        self.tweet_records = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        # Append the time to the list for the given tweetName and keep it sorted
        bisect.insort(self.tweet_records[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> list:
        # Determine the interval size based on the frequency
        interval = {"minute": 60, "hour": 3600, "day": 86400}[freq]
        result = []
        
        # Get the list of times for the given tweetName
        times = self.tweet_records[tweetName]
        
        # Iterate over intervals
        for start in range(startTime, endTime + 1, interval):
            end = min(start + interval - 1, endTime)
            # Count the number of tweets in the current interval using binary search
            left = bisect.bisect_left(times, start)
            right = bisect.bisect_right(times, end)
            result.append(right - left)
        
        return result

# Example Test Cases
if __name__ == "__main__":
    tweetCounts = TweetCounts()
    
    # Record tweets
    tweetCounts.recordTweet("tweet1", 0)
    tweetCounts.recordTweet("tweet1", 60)
    tweetCounts.recordTweet("tweet1", 10)
    
    # Test case 1: Get tweet counts per minute
    print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet1", 0, 59))  # Output: [2]
    
    # Test case 2: Get tweet counts per minute
    print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet1", 0, 60))  # Output: [2, 1]
    
    # Test case 3: Get tweet counts per hour
    print(tweetCounts.getTweetCountsPerFrequency("hour", "tweet1", 0, 210))  # Output: [3]

"""
Time Complexity:
- `recordTweet`: O(n) for inserting into a sorted list using `bisect.insort`, where n is the number of tweets for the given tweetName.
- `getTweetCountsPerFrequency`: O(k * log(n)), where k is the number of intervals and n is the number of tweets for the given tweetName. Binary search is used to count tweets in each interval.

Space Complexity:
- O(n), where n is the total number of tweets recorded. This is the space required to store all tweet times.

Topic: HashMap, Binary Search
"""