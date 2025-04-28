"""
LeetCode Problem #1500: Design a File Sharing System

Problem Statement:
We want to design a file-sharing system that allows users to upload, download, and delete files. The system should also allow users to share files with other users. Specifically, the system should support the following operations:

1. `join(int userID)`: A new user joins the system with the given `userID`. If the user already exists, do nothing.
2. `leave(int userID)`: A user with the given `userID` leaves the system. All files shared by this user are removed.
3. `upload(int userID, int fileID)`: A user uploads a file with the given `fileID`. The file is shared with all users in the system.
4. `download(int userID, int fileID)`: A user downloads a file with the given `fileID`. If the file does not exist, return `-1`.
5. `delete(int fileID)`: A file with the given `fileID` is deleted from the system.

Implement a class `FileSharing` that supports the above operations.

Constraints:
- `1 <= userID, fileID <= 10^5`
- At most `10^4` operations will be performed.

Your implementation should be efficient and handle the constraints effectively.
"""

class FileSharing:
    def __init__(self):
        # Dictionary to store files and the set of users who have access to them
        self.files = {}
        # Set to store active users
        self.users = set()

    def join(self, userID: int) -> None:
        # Add the user to the system
        self.users.add(userID)

    def leave(self, userID: int) -> None:
        # Remove the user from the system
        if userID in self.users:
            self.users.remove(userID)
            # Remove the user from all files they have access to
            for fileID in self.files:
                self.files[fileID].discard(userID)

    def upload(self, userID: int, fileID: int) -> None:
        # Ensure the user is in the system
        if userID not in self.users:
            return
        # Share the file with all users
        self.files[fileID] = set(self.users)

    def download(self, userID: int, fileID: int) -> int:
        # Ensure the user is in the system and the file exists
        if userID in self.users and fileID in self.files:
            return fileID
        return -1

    def delete(self, fileID: int) -> None:
        # Remove the file from the system
        if fileID in self.files:
            del self.files[fileID]


# Example Test Cases
if __name__ == "__main__":
    fs = FileSharing()

    # Test Case 1: User joins the system
    fs.join(1)
    fs.join(2)
    print(fs.users)  # Expected: {1, 2}

    # Test Case 2: User uploads a file
    fs.upload(1, 100)
    print(fs.files)  # Expected: {100: {1, 2}}

    # Test Case 3: User downloads a file
    print(fs.download(2, 100))  # Expected: 100
    print(fs.download(3, 100))  # Expected: -1 (user 3 is not in the system)

    # Test Case 4: User leaves the system
    fs.leave(2)
    print(fs.users)  # Expected: {1}
    print(fs.files)  # Expected: {100: {1}}

    # Test Case 5: File is deleted
    fs.delete(100)
    print(fs.files)  # Expected: {}

# Time and Space Complexity Analysis:
# Time Complexity:
# - `join`: O(1) to add a user to the set.
# - `leave`: O(F) where F is the number of files, as we need to remove the user from all files.
# - `upload`: O(U) where U is the number of users, as we share the file with all users.
# - `download`: O(1) to check if the file exists and return it.
# - `delete`: O(1) to remove the file from the dictionary.

# Space Complexity:
# - The space complexity is O(F * U) where F is the number of files and U is the number of users, as we store a set of users for each file.

# Topic: HashMap, Set, Design