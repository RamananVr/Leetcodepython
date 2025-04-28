"""
LeetCode Problem #588: Design In-Memory File System

Problem Statement:
Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:
- FileSystem() Initializes the object of the file system.
- List[str] ls(String path) Returns a list of all files and directories in the directory specified by path in lexicographical order. If path is a file, returns a list containing only this file's name.
- void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
- void addContentToFile(String filePath, String content) Adds content to the file at filePath. If filePath does not exist, a new file is created containing the given content.
- String readContentFromFile(String filePath) Returns the content in the file at filePath.

Constraints:
- The input path is always valid, and it follows the format of Unix-style file system paths.
- The path starts with a '/' and is a valid absolute path.
- The operations will be called in order, meaning that you can assume mkdir will be called before any addContentToFile or ls calls.
- The number of calls to any function is at most 300.
- The length of any path is at most 100.
- The length of content in addContentToFile is at most 50.
- The path contains only alphanumeric characters, '/' and '.'.

"""

class FileSystem:
    def __init__(self):
        self.fs = {"": {}}  # Root directory represented as a nested dictionary

    def ls(self, path: str) -> list:
        parts = path.split("/")
        node = self.fs[""]
        for part in parts[1:]:
            if part in node:
                node = node[part]
            else:
                return [parts[-1]]  # If it's a file, return its name
        if isinstance(node, dict):
            return sorted(node.keys())  # List directory contents
        return [parts[-1]]  # If it's a file, return its name

    def mkdir(self, path: str) -> None:
        parts = path.split("/")
        node = self.fs[""]
        for part in parts[1:]:
            if part not in node:
                node[part] = {}
            node = node[part]

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = filePath.split("/")
        node = self.fs[""]
        for part in parts[1:-1]:
            if part not in node:
                node[part] = {}
            node = node[part]
        if parts[-1] not in node:
            node[parts[-1]] = ""
        node[parts[-1]] += content

    def readContentFromFile(self, filePath: str) -> str:
        parts = filePath.split("/")
        node = self.fs[""]
        for part in parts[1:-1]:
            node = node[part]
        return node[parts[-1]]


# Example Test Cases
if __name__ == "__main__":
    fs = FileSystem()

    # Test mkdir and ls
    fs.mkdir("/a/b/c")
    print(fs.ls("/"))  # Output: ['a']
    print(fs.ls("/a/b"))  # Output: ['c']

    # Test addContentToFile and readContentFromFile
    fs.addContentToFile("/a/b/c/d", "hello")
    print(fs.readContentFromFile("/a/b/c/d"))  # Output: "hello"

    # Test ls for a file
    print(fs.ls("/a/b/c/d"))  # Output: ['d']

    # Test appending content to a file
    fs.addContentToFile("/a/b/c/d", " world")
    print(fs.readContentFromFile("/a/b/c/d"))  # Output: "hello world"

# Time and Space Complexity Analysis
# ls:
#   - Time Complexity: O(n), where n is the depth of the path.
#   - Space Complexity: O(1).
# mkdir:
#   - Time Complexity: O(n), where n is the depth of the path.
#   - Space Complexity: O(1).
# addContentToFile:
#   - Time Complexity: O(n), where n is the depth of the path.
#   - Space Complexity: O(1).
# readContentFromFile:
#   - Time Complexity: O(n), where n is the depth of the path.
#   - Space Complexity: O(1).

# Topic: Design, HashMap, Trie