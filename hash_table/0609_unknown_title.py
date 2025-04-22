"""
LeetCode Problem #609: Find Duplicate File in System

Problem Statement:
Given a list `paths` where `paths[i]` is a string representing a directory path that contains all the files in that directory, 
including their names and content, return all the groups of duplicate files in the file system in terms of their paths. 
You may return the answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single directory path in the input is represented as follows:
- "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
  - It means there are `n` files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) respectively in the directory "root/d1/d2/.../dm".

Note:
- A file content is in parentheses.
- You may assume no files or directories share the same name in a single directory.
- You may assume each given directory path is valid and no files or directories are empty.

The output should be a list of groups of duplicate file paths. For each group, it should contain all the file paths that have the same content.

Example:
Input:
paths = [
    "root/a 1.txt(abcd) 2.txt(efgh)",
    "root/c 3.txt(abcd)",
    "root/c/d 4.txt(efgh)",
    "root/e 5.txt(efgh)"
]
Output:
[
    ["root/a/1.txt", "root/c/3.txt"],
    ["root/a/2.txt", "root/c/d/4.txt", "root/e/5.txt"]
]

Constraints:
- 1 <= paths.length <= 2 * 10^4
- 1 <= paths[i].length <= 3000
- 1 <= sum(paths[i].length) <= 5 * 10^5
- The directory path and file names have at most 300 characters.
- The file content is unique per file except for the duplicate files.
"""

# Solution
from collections import defaultdict

def findDuplicate(paths):
    """
    Finds groups of duplicate files based on their content.

    :param paths: List[str] - List of directory paths with file names and content.
    :return: List[List[str]] - Groups of duplicate file paths.
    """
    content_to_paths = defaultdict(list)
    
    for path in paths:
        parts = path.split(" ")
        directory = parts[0]
        for file_info in parts[1:]:
            file_name, content = file_info.split("(")
            content = content[:-1]  # Remove the closing parenthesis
            full_path = f"{directory}/{file_name}"
            content_to_paths[content].append(full_path)
    
    # Filter out groups with only one file (not duplicates)
    return [group for group in content_to_paths.values() if len(group) > 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    paths1 = [
        "root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)",
        "root/c/d 4.txt(efgh)",
        "root/e 5.txt(efgh)"
    ]
    print(findDuplicate(paths1))  # Expected: [["root/a/1.txt", "root/c/3.txt"], ["root/a/2.txt", "root/c/d/4.txt", "root/e/5.txt"]]

    # Test Case 2
    paths2 = [
        "root/a 1.txt(abc) 2.txt(def)",
        "root/b 3.txt(abc)",
        "root/c 4.txt(def)",
        "root/d 5.txt(ghi)"
    ]
    print(findDuplicate(paths2))  # Expected: [["root/a/1.txt", "root/b/3.txt"], ["root/a/2.txt", "root/c/4.txt"]]

    # Test Case 3
    paths3 = [
        "root/a 1.txt(xyz)",
        "root/b 2.txt(xyz)",
        "root/c 3.txt(xyz)"
    ]
    print(findDuplicate(paths3))  # Expected: [["root/a/1.txt", "root/b/2.txt", "root/c/3.txt"]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting each path string and processing its files takes O(L), where L is the total length of all strings in `paths`.
- Adding file paths to the dictionary is O(L) in total.
- Filtering the dictionary values to find duplicates is O(L) in the worst case.
Overall: O(L)

Space Complexity:
- The `content_to_paths` dictionary stores file paths grouped by content. In the worst case, all files have unique content, so the space used is proportional to the total number of files and their paths.
Overall: O(L)
"""

# Topic: Hash Table