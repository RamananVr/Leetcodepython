"""
LeetCode Problem #1233: Remove Sub-Folders from the Filesystem

Problem Statement:
Given a list of folders `folder`, you are asked to remove all sub-folders in those folders and return the folders in lexicographical order.

If a folder[i] is located within another folder[j], it is called a sub-folder of folder[j]. The format of a folder path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters. 
- For example, "/a" and "/a/b" are valid paths, but not "//a" or "/a//b".

Return the folders after removing all sub-folders. You may return the answer in any order.

Example 1:
Input: folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
Output: ["/a", "/c/d", "/c/f"]
Explanation: Folders "/a/b" is a sub-folder of "/a", and "/c/d/e" is inside "/c/d", so they are removed.

Example 2:
Input: folder = ["/a", "/a/b/c", "/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" are sub-folders of "/a", so they are removed.

Example 3:
Input: folder = ["/a/b/c", "/a/b/ca", "/a/b/d"]
Output: ["/a/b/c", "/a/b/ca", "/a/b/d"]

Constraints:
- 1 <= folder.length <= 4 * 10^4
- 2 <= folder[i].length <= 100
- folder[i] contains only lowercase letters and '/'
- folder[i] always starts with '/'
- Each folder name is unique
"""

# Python Solution
from typing import List

def removeSubfolders(folder: List[str]) -> List[str]:
    # Sort the folders lexicographically
    folder.sort()
    result = []
    
    for f in folder:
        # If the result is empty or the current folder is not a sub-folder of the last added folder
        if not result or not f.startswith(result[-1] + '/'):
            result.append(f)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    folder1 = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    print(removeSubfolders(folder1))  # Output: ["/a", "/c/d", "/c/f"]

    # Test Case 2
    folder2 = ["/a", "/a/b/c", "/a/b/d"]
    print(removeSubfolders(folder2))  # Output: ["/a"]

    # Test Case 3
    folder3 = ["/a/b/c", "/a/b/ca", "/a/b/d"]
    print(removeSubfolders(folder3))  # Output: ["/a/b/c", "/a/b/ca", "/a/b/d"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the folder list takes O(n log n), where n is the length of the folder list.
- Iterating through the sorted list takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The space used for sorting is O(n) (depending on the sorting algorithm).
- The result list takes O(k) space, where k is the number of folders in the final result.
- Overall space complexity: O(n).
"""

# Topic: Strings, Sorting