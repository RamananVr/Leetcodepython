"""
LeetCode Problem #2254: Design Video Sharing Platform

Problem Statement:
You are tasked with designing a video-sharing platform. The platform should support the following operations:

1. **Upload a video**: A user can upload a video. Each video is assigned a unique ID starting from 0 and incrementing by 1 for each new video.
2. **Remove a video**: A user can remove a video by its ID. Once a video is removed, its ID becomes available for reuse.
3. **Watch a video**: A user can watch a video by its ID. Watching a video increases its view count by 1.
4. **Like a video**: A user can like a video by its ID. Liking a video increases its like count by 1.
5. **Dislike a video**: A user can dislike a video by its ID. Disliking a video increases its dislike count by 1.
6. **Get video information**: A user can retrieve information about a video by its ID. The information includes the video ID, the number of views, likes, and dislikes.
7. **Get all videos**: A user can retrieve a list of all video IDs currently on the platform.

Implement the `VideoSharingPlatform` class:

- `__init__()`: Initializes the platform.
- `upload() -> int`: Uploads a video and returns its ID.
- `remove(videoId: int) -> None`: Removes the video with the given ID.
- `watch(videoId: int) -> None`: Increments the view count of the video with the given ID.
- `like(videoId: int) -> None`: Increments the like count of the video with the given ID.
- `dislike(videoId: int) -> None`: Increments the dislike count of the video with the given ID.
- `getInfo(videoId: int) -> List[int]`: Returns a list `[videoId, views, likes, dislikes]` for the video with the given ID.
- `getAllVideos() -> List[int]`: Returns a list of all video IDs currently on the platform.

Constraints:
- All operations should run efficiently.
- Video IDs are guaranteed to be non-negative integers.
"""

class VideoSharingPlatform:
    def __init__(self):
        self.videos = {}
        self.available_ids = []
        self.next_id = 0

    def upload(self) -> int:
        # Assign an ID to the new video
        if self.available_ids:
            video_id = self.available_ids.pop(0)
        else:
            video_id = self.next_id
            self.next_id += 1
        
        # Initialize video stats
        self.videos[video_id] = {"views": 0, "likes": 0, "dislikes": 0}
        return video_id

    def remove(self, videoId: int) -> None:
        if videoId in self.videos:
            del self.videos[videoId]
            self.available_ids.append(videoId)
            self.available_ids.sort()

    def watch(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId]["views"] += 1

    def like(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId]["likes"] += 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId]["dislikes"] += 1

    def getInfo(self, videoId: int) -> list:
        if videoId in self.videos:
            video = self.videos[videoId]
            return [videoId, video["views"], video["likes"], video["dislikes"]]
        return []

    def getAllVideos(self) -> list:
        return sorted(self.videos.keys())


# Example Test Cases
if __name__ == "__main__":
    platform = VideoSharingPlatform()

    # Test Case 1: Upload videos
    video1 = platform.upload()  # Should return 0
    video2 = platform.upload()  # Should return 1
    print(video1, video2)  # Output: 0, 1

    # Test Case 2: Watch, like, and dislike videos
    platform.watch(0)
    platform.like(0)
    platform.dislike(1)
    print(platform.getInfo(0))  # Output: [0, 1, 1, 0]
    print(platform.getInfo(1))  # Output: [1, 0, 0, 1]

    # Test Case 3: Remove a video and reuse its ID
    platform.remove(0)
    video3 = platform.upload()  # Should reuse ID 0
    print(video3)  # Output: 0
    print(platform.getAllVideos())  # Output: [0, 1]

    # Test Case 4: Get all videos
    print(platform.getAllVideos())  # Output: [0, 1]


# Time and Space Complexity Analysis
"""
Time Complexity:
- `upload`: O(1) if no IDs are available for reuse, O(log(n)) if IDs need to be sorted after reuse.
- `remove`: O(log(n)) due to sorting of available IDs.
- `watch`, `like`, `dislike`: O(1) as they involve direct dictionary access.
- `getInfo`: O(1) as it involves direct dictionary access.
- `getAllVideos`: O(n * log(n)) due to sorting of video IDs.

Space Complexity:
- O(n) where n is the number of videos currently on the platform.

Topic: Design, Hash Table
"""