"""
LeetCode Question #71: Simplify Path

Problem Statement:
Given a string `path`, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system:
- A period '.' refers to the current directory.
- A double period '..' moves the directory up a level.
- Multiple consecutive slashes '//' are treated as a single slash '/'.
- The canonical path should have the following format:
  - The path starts with a single slash '/'.
  - Any two directories are separated by a single slash '/'.
  - The path does not end with a trailing '/'.
  - The path only contains the directories on the path from the root directory to the target file or directory (i.e., no '.' or '..' components).

Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"

Example 2:
Input: path = "/../"
Output: "/"

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"

Constraints:
- 1 <= path.length <= 3000
- path consists of English letters, digits, period '.', slash '/' or '_'.
- path is a valid absolute Unix path.
"""

# Python Solution
def simplifyPath(path: str) -> str:
    stack = []
    components = path.split('/')
    
    for component in components:
        if component == '' or component == '.':
            # Skip empty or current directory components
            continue
        elif component == '..':
            # Pop the last directory if possible
            if stack:
                stack.pop()
        else:
            # Add valid directory names to the stack
            stack.append(component)
    
    # Join the stack with '/' to form the canonical path
    return '/' + '/'.join(stack)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    path1 = "/home/"
    print(simplifyPath(path1))  # Output: "/home"

    # Test Case 2
    path2 = "/../"
    print(simplifyPath(path2))  # Output: "/"

    # Test Case 3
    path3 = "/home//foo/"
    print(simplifyPath(path3))  # Output: "/home/foo"

    # Test Case 4
    path4 = "/a/./b/../../c/"
    print(simplifyPath(path4))  # Output: "/c"

    # Test Case 5
    path5 = "/a/../../b/../c//.//"
    print(simplifyPath(path5))  # Output: "/c"

    # Test Case 6
    path6 = "/a//b////c/d//././/.."
    print(simplifyPath(path6))  # Output: "/a/b/c"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting the input string `path` into components using `split('/')` takes O(n), where n is the length of the string.
- Iterating through the components and performing stack operations (push/pop) takes O(m), where m is the number of components.
- Joining the stack into the canonical path takes O(k), where k is the number of valid components in the stack.
- Overall, the time complexity is O(n), as splitting dominates the operations.

Space Complexity:
- The space complexity is O(m), where m is the number of components stored in the stack. In the worst case, all components are valid directories, and the stack size equals the number of components.
- The space used for the output string is negligible compared to the stack size.
- Overall, the space complexity is O(m).
"""

# Topic: Strings, Stack