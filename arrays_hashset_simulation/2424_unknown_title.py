"""
LeetCode Problem #2424: Longest Uploaded Prefix

Problem Statement:
You are given a stream of `n` videos, each identified by a unique integer from `1` to `n` that you need to upload to a server. You are also given a class `LUPrefix` which is used to manage the upload process. Implement the class `LUPrefix`:

1. `LUPrefix(int n)`: Initializes the object for managing `n` videos.
2. `void upload(int video)`: Uploads the video with the given ID.
3. `int longest()`: Returns the length of the longest prefix of uploaded videos (starting from `1`).

Constraints:
- `1 <= n <= 10^5`
- `1 <= video <= n`
- All calls to `upload` are made with distinct values of `video`.

Example:
Input:
    ["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"]
    [[4], [3], [], [1], [], [2], []]
Output:
    [null, null, 0, null, 1, null, 3]

Explanation:
    LUPrefix obj = new LUPrefix(4); // Initialize the object for 4 videos.
    obj.upload(3); // Upload video 3.
    obj.longest(); // The longest uploaded prefix is 0 because video 1 is not uploaded.
    obj.upload(1); // Upload video 1.
    obj.longest(); // The longest uploaded prefix is 1 because video 1 is uploaded.
    obj.upload(2); // Upload video 2.
    obj.longest(); // The longest uploaded prefix is 3 because videos 1, 2, and 3 are uploaded.
"""

# Python Solution
class LUPrefix:
    def __init__(self, n: int):
        """
        Initializes the LUPrefix object for managing n videos.
        """
        self.uploaded = set()  # To track uploaded videos
        self.longest_prefix = 0  # Tracks the longest prefix of uploaded videos

    def upload(self, video: int) -> None:
        """
        Uploads the video with the given ID.
        """
        self.uploaded.add(video)
        # Update the longest prefix if possible
        while self.longest_prefix + 1 in self.uploaded:
            self.longest_prefix += 1

    def longest(self) -> int:
        """
        Returns the length of the longest prefix of uploaded videos.
        """
        return self.longest_prefix


# Example Test Cases
if __name__ == "__main__":
    # Initialize the object for 4 videos
    obj = LUPrefix(4)
    
    # Test Case 1
    obj.upload(3)  # Upload video 3
    assert obj.longest() == 0  # Longest prefix is 0 because video 1 is not uploaded
    
    # Test Case 2
    obj.upload(1)  # Upload video 1
    assert obj.longest() == 1  # Longest prefix is 1 because video 1 is uploaded
    
    # Test Case 3
    obj.upload(2)  # Upload video 2
    assert obj.longest() == 3  # Longest prefix is 3 because videos 1, 2, and 3 are uploaded
    
    print("All test cases passed!")

"""
Time Complexity Analysis:
1. `__init__`: O(1) - Initializing the object and variables takes constant time.
2. `upload`: O(1) on average - Adding a video to the set is O(1), and updating the longest prefix involves a single while loop that increments the prefix counter. Each video is processed at most once.
3. `longest`: O(1) - Simply returns the value of `self.longest_prefix`.

Overall, each operation is O(1) on average.

Space Complexity:
- O(n): The `uploaded` set can store up to `n` video IDs.

Topic: Arrays, HashSet, Simulation
"""