"""
LeetCode Problem #388: Longest Absolute File Path

Problem Statement:
Suppose we have a file system represented in a string where:
- Each file or directory is separated by a newline character '\n'.
- Each level of the directory structure is indicated by a tab character '\t'.
- A file is identified by the presence of a '.' in its name (e.g., "file.txt").
- A directory does not contain a '.' in its name.

Given a string `input` representing the file system, return the length of the longest absolute path to a file in the system. If there is no file in the system, return 0.

Example:
Input: "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
Output: 20
Explanation: The longest path is "dir/subdir2/file.ext", and its length is 20.

Constraints:
- 1 <= input.length <= 10^4
- input may contain lowercase or uppercase English letters, digits, '.', '\n', and '\t'.
- The file system is guaranteed to be valid.
"""

def lengthLongestPath(input: str) -> int:
    """
    Finds the length of the longest absolute path to a file in the given file system string.

    :param input: A string representing the file system.
    :return: The length of the longest absolute path to a file.
    """
    max_length = 0
    path_lengths = {0: 0}  # Dictionary to store the cumulative length at each depth.

    for line in input.split('\n'):
        depth = line.count('\t')  # Count the number of '\t' to determine the depth.
        name = line.lstrip('\t')  # Remove leading '\t' to get the actual name.

        if '.' in name:  # It's a file.
            max_length = max(max_length, path_lengths[depth] + len(name))
        else:  # It's a directory.
            path_lengths[depth + 1] = path_lengths[depth] + len(name) + 1  # Add 1 for the '/'.

    return max_length


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    input1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    print(lengthLongestPath(input1))  # Output: 20

    # Test Case 2
    input2 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext\n\t\tfile2.ext"
    print(lengthLongestPath(input2))  # Output: 20

    # Test Case 3
    input3 = "a"
    print(lengthLongestPath(input3))  # Output: 0 (no file present)

    # Test Case 4
    input4 = "file.txt"
    print(lengthLongestPath(input4))  # Output: 8

    # Test Case 5
    input5 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(lengthLongestPath(input5))  # Output: 32


"""
Time and Space Complexity Analysis:

Time Complexity:
- Splitting the input string by '\n' takes O(n), where n is the length of the input string.
- Iterating through each line and processing it (counting '\t', stripping '\t', and updating the dictionary) also takes O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(d), where d is the maximum depth of the directory structure. This is because we store the cumulative lengths for each depth in the `path_lengths` dictionary.

Topic: String Manipulation
"""