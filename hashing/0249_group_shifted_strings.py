"""
LeetCode Question #249: Group Shifted Strings

Problem Statement:
We can shift a string by shifting each of its characters to its successive character.
For example, "abc" can be shifted to "bcd". We can keep shifting the string to form a sequence:
"abc" -> "bcd" -> ... -> "xyz".

Given a list of strings, group all strings that belong to the same shifting sequence.

Example:
Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
Output: [["abc", "bcd", "xyz"], ["acef"], ["az", "ba"], ["a", "z"]]

Note:
- Strings consist of lowercase English letters only.
- The order of groups in the output does not matter.

"""

from collections import defaultdict

def groupStrings(strings):
    """
    Groups strings that belong to the same shifting sequence.

    :param strings: List[str] - List of input strings
    :return: List[List[str]] - Grouped strings based on shifting sequence
    """
    def get_shift_key(s):
        # Generate a unique key for the shifting sequence
        key = []
        for i in range(1, len(s)):
            # Calculate the circular difference between consecutive characters
            diff = (ord(s[i]) - ord(s[i - 1])) % 26
            key.append(diff)
        return tuple(key)

    groups = defaultdict(list)
    for s in strings:
        key = get_shift_key(s)
        groups[key].append(s)

    return list(groups.values())

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    print(groupStrings(strings))
    # Expected Output: [["abc", "bcd", "xyz"], ["acef"], ["az", "ba"], ["a", "z"]]

    # Test Case 2
    strings = ["aaa", "bbb", "ccc"]
    print(groupStrings(strings))
    # Expected Output: [["aaa", "bbb", "ccc"]]

    # Test Case 3
    strings = ["abc", "def", "ghi"]
    print(groupStrings(strings))
    # Expected Output: [["abc"], ["def"], ["ghi"]]

    # Test Case 4
    strings = ["a", "b", "c"]
    print(groupStrings(strings))
    # Expected Output: [["a", "b", "c"]]

"""
Time and Space Complexity Analysis:

Time Complexity:
- For each string in the input list, we compute a key based on the differences between consecutive characters.
- Computing the key for a string of length `m` takes O(m) time.
- If there are `n` strings in the input list, the total time complexity is O(n * m), where `m` is the average length of the strings.

Space Complexity:
- We use a defaultdict to store groups of strings. In the worst case, all strings have unique keys, so the space complexity is O(n * m), where `m` is the average length of the strings (for storing keys and strings).

Topic: Hashing
"""