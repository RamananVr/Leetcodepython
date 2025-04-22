"""
LeetCode Question #14: Longest Common Prefix

Problem Statement:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.
"""

def longestCommonPrefix(strs):
    """
    Finds the longest common prefix among an array of strings.

    :param strs: List[str] - List of strings
    :return: str - Longest common prefix
    """
    if not strs:
        return ""

    # Start with the first string as the prefix
    prefix = strs[0]

    # Compare the prefix with each string in the list
    for string in strs[1:]:
        # Reduce the prefix until it matches the start of the current string
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    strs1 = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strs1))  # Output: "fl"

    # Test Case 2
    strs2 = ["dog", "racecar", "car"]
    print(longestCommonPrefix(strs2))  # Output: ""

    # Test Case 3
    strs3 = ["interspecies", "interstellar", "interstate"]
    print(longestCommonPrefix(strs3))  # Output: "inters"

    # Test Case 4
    strs4 = ["a"]
    print(longestCommonPrefix(strs4))  # Output: "a"

    # Test Case 5
    strs5 = ["", "b"]
    print(longestCommonPrefix(strs5))  # Output: ""

    # Test Case 6
    strs6 = ["prefix", "prefixes", "prefixation"]
    print(longestCommonPrefix(strs6))  # Output: "prefix"

"""
Time Complexity Analysis:
- Let n be the number of strings in the input list `strs`.
- Let m be the length of the shortest string in the list.
- In the worst case, we compare each character of the prefix with all n strings.
- Therefore, the time complexity is O(n * m), where m is the length of the shortest string.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Strings
"""