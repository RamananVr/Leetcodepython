"""
LeetCode Problem #1024: Video Stitching

Problem Statement:
You are given a list of video clips, where `clips[i] = [start_i, end_i]` indicates that the clip starts at `start_i` and ends at `end_i`. We can cut these clips into segments freely.

Given an integer `time`, return the minimum number of clips needed to cover the entire range `[0, time]`. If it is impossible to cover the range, return `-1`.

Example 1:
Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
Output: 3
Explanation: We take the clips [0,2], [1,9], and [8,10].

Example 2:
Input: clips = [[0,1],[1,2]], time = 5
Output: -1
Explanation: We cannot cover [0,5] with the given clips.

Example 3:
Input: clips = [[0,4],[2,8]], time = 5
Output: 2
Explanation: We take the clips [0,4] and [2,8].

Constraints:
- 1 <= clips.length <= 100
- 0 <= start_i <= end_i <= 100
- 0 <= time <= 100
"""

# Python Solution
def videoStitching(clips, time):
    # Sort clips by their start time, and if equal, by their end time
    clips.sort(key=lambda x: (x[0], x[1]))
    
    max_end = 0
    count = 0
    i = 0
    n = len(clips)
    
    while max_end < time:
        # Find the clip that extends the coverage the furthest within the current range
        furthest = max_end
        while i < n and clips[i][0] <= max_end:
            furthest = max(furthest, clips[i][1])
            i += 1
        
        # If no clip can extend the coverage, return -1
        if furthest == max_end:
            return -1
        
        # Update the maximum coverage and increment the count
        max_end = furthest
        count += 1
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    clips1 = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
    time1 = 10
    print(videoStitching(clips1, time1))  # Output: 3

    # Test Case 2
    clips2 = [[0,1],[1,2]]
    time2 = 5
    print(videoStitching(clips2, time2))  # Output: -1

    # Test Case 3
    clips3 = [[0,4],[2,8]]
    time3 = 5
    print(videoStitching(clips3, time3))  # Output: 2

    # Additional Test Case
    clips4 = [[0,1],[1,3],[2,5],[4,6]]
    time4 = 6
    print(videoStitching(clips4, time4))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the clips takes O(n log n), where n is the number of clips.
- The while loop iterates through the clips, and each clip is processed once, resulting in O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation uses O(n) space for the sorted array.
- No additional data structures are used, so the space complexity is O(1) (excluding input storage).

Overall space complexity: O(n).
"""

# Topic: Greedy Algorithm