"""
LeetCode Question #1166: Design File System

Problem Statement:
You are asked to design a file system that allows you to create new paths and associate them with values. The system should support the following functions:

1. `createPath(path, value)`:
   - Creates a new path and associates a value to it.
   - Returns `True` if the path was successfully created, `False` otherwise.
   - A path can only be created if all the parent directories exist. For example, `/a/b/c` can only be created if `/a/b` exists.
   - The path should be a valid absolute path starting with a single forward slash `/` and must not end with a forward slash `/`.
   - The value associated with the path must be an integer.

2. `get(path)`:
   - Returns the value associated with the path.
   - Returns `-1` if the path does not exist.

Constraints:
- The number of calls to `createPath` and `get` will not exceed `3000`.
- The length of the path will not exceed `100`.
- The value associated with a path will be between `1` and `10^9`.

"""

class FileSystem:
    def __init__(self):
        # Initialize a dictionary to store paths and their associated values
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        # Check if the path is valid and does not already exist
        if path in self.paths or path == "/" or value <= 0:
            return False
        
        # Find the parent directory of the path
        parent = path.rsplit('/', 1)[0]
        # Ensure the parent directory exists (except for root "/")
        if parent and parent not in self.paths:
            return False
        
        # Create the path and associate the value
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        # Return the value associated with the path, or -1 if it does not exist
        return self.paths.get(path, -1)


# Example Test Cases
if __name__ == "__main__":
    fs = FileSystem()

    # Test case 1: Create a valid path
    assert fs.createPath("/a", 1) == True  # Path "/a" created successfully
    assert fs.get("/a") == 1              # Value associated with "/a" is 1

    # Test case 2: Create a path with a missing parent
    assert fs.createPath("/a/b", 2) == True  # Path "/a/b" created successfully
    assert fs.get("/a/b") == 2               # Value associated with "/a/b" is 2

    # Test case 3: Attempt to create a path that already exists
    assert fs.createPath("/a", 3) == False  # Path "/a" already exists

    # Test case 4: Attempt to create a path with an invalid parent
    assert fs.createPath("/c/d", 4) == False  # Parent "/c" does not exist

    # Test case 5: Get value of a non-existent path
    assert fs.get("/c") == -1  # Path "/c" does not exist

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. `createPath(path, value)`:
   - Time Complexity: O(n), where n is the length of the path string. This is due to the `rsplit` operation to find the parent directory.
   - Space Complexity: O(1), as we are only adding a single entry to the dictionary.

2. `get(path)`:
   - Time Complexity: O(1), as dictionary lookups are O(1) on average.
   - Space Complexity: O(1), as no additional space is used.

Overall:
- Time Complexity: O(n) for `createPath` and O(1) for `get`.
- Space Complexity: O(m), where m is the number of paths stored in the dictionary.

Topic: Hash Table
"""