"""
LeetCode Problem #1948: Delete Duplicate Folders in System

Problem Statement:
Due to a bug, duplicate folders are appearing in the file system. Two folders are considered 
duplicates if they contain the same collection of subfolders and subfolder structures. 
The root folder itself is not a duplicate.

Given the root of a file system represented as a list of paths, where each path is a list of 
strings representing folder names from the root to the folder, return the file system after 
removing all the duplicate folders in the same format.

Example:
Input: paths = [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]
Output: [["d"], ["d", "a"]]

Constraints:
1. 1 <= paths.length <= 2 * 10^4
2. 1 <= paths[i].length <= 500
3. 1 <= paths[i][j].length <= 10
4. paths[i] is unique.
5. paths[i][j] consists of only lowercase English letters.

"""

from collections import defaultdict

def deleteDuplicateFolder(paths):
    # Step 1: Build the folder tree
    def build_tree():
        root = {}
        for path in paths:
            node = root
            for folder in path:
                if folder not in node:
                    node[folder] = {}
                node = node[folder]
        return root

    # Step 2: Serialize the tree and identify duplicates
    def serialize(node):
        if not node:
            return ""
        serialized = []
        for folder in sorted(node.keys()):
            serialized.append(folder + "(" + serialize(node[folder]) + ")")
        serialized_str = "".join(serialized)
        count[serialized_str] += 1
        return serialized_str

    # Step 3: Remove duplicates
    def remove_duplicates(node):
        keys_to_remove = []
        for folder, child in node.items():
            if count[serialize(child)] > 1:
                keys_to_remove.append(folder)
        for key in keys_to_remove:
            del node[key]
        for child in node.values():
            remove_duplicates(child)

    # Step 4: Convert the tree back to paths
    def tree_to_paths(node, path):
        if not node:
            return
        for folder, child in node.items():
            result.append(path + [folder])
            tree_to_paths(child, path + [folder])

    # Main logic
    root = build_tree()
    count = defaultdict(int)
    serialize(root)
    remove_duplicates(root)
    result = []
    tree_to_paths(root, [])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    paths = [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]
    print(deleteDuplicateFolder(paths))  # Output: [["d"], ["d", "a"]]

    # Test Case 2
    paths = [["a"], ["a", "x"], ["a", "x", "y"], ["a", "z"], ["b"], ["b", "x"], ["b", "x", "y"], ["b", "z"]]
    print(deleteDuplicateFolder(paths))  # Output: []

    # Test Case 3
    paths = [["a"], ["a", "b"], ["a", "b", "c"], ["a", "d"], ["a", "d", "c"], ["e"], ["e", "b"], ["e", "b", "c"], ["e", "d"], ["e", "d", "c"]]
    print(deleteDuplicateFolder(paths))  # Output: [["a"], ["a", "b"], ["a", "b", "c"], ["a", "d"], ["a", "d", "c"], ["e"], ["e", "b"], ["e", "b", "c"], ["e", "d"], ["e", "d", "c"]]

# Time Complexity Analysis:
# 1. Building the tree: O(N * L), where N is the number of paths and L is the average length of a path.
# 2. Serialization: O(T), where T is the total number of nodes in the tree.
# 3. Removing duplicates: O(T).
# 4. Converting the tree back to paths: O(T).
# Overall: O(N * L + T), where T is proportional to the total number of nodes in the tree.

# Space Complexity Analysis:
# 1. Tree storage: O(T).
# 2. Serialization map: O(T).
# 3. Recursive stack: O(H), where H is the height of the tree.
# Overall: O(T + H).

# Topic: Tree, Hashing, Recursion