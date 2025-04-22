"""
LeetCode Problem #165: Compare Version Numbers

Problem Statement:
Given two version numbers, `version1` and `version2`, compare them.

Version numbers are composed of one or more revisions joined by a dot `'.'`. Each revision consists of digits and may contain leading zeros. Every revision is interpreted as a decimal number.

- For example, `1.01` and `1.001` are considered equal because they both represent the same integer `1`.
- However, `1.0` is not equal to `1.0.0` because the first version has one revision while the second version has two revisions.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions `1` and `001` are considered equal. If a version number does not specify a revision at an index, treat the revision as `0`.

Return the following:
- If `version1 > version2`, return `1`.
- If `version1 < version2`, return `-1`.
- Otherwise, return `0`.

Example 1:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 2:
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".

Example 3:
Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's first revision is "0", while version2's first revision is "1". 0 < 1, so version1 < version2.

Constraints:
- `1 <= version1.length, version2.length <= 500`
- `version1` and `version2` only contain digits and `'.'`.
- `version1` and `version2` do not have leading or trailing dots.
- All revisions in `version1` and `version2` are integers that can be represented as a 32-bit integer.
"""

def compareVersion(version1: str, version2: str) -> int:
    # Split the version strings into lists of revisions
    v1_parts = list(map(int, version1.split('.')))
    v2_parts = list(map(int, version2.split('.')))
    
    # Determine the maximum length of the two version lists
    max_length = max(len(v1_parts), len(v2_parts))
    
    # Compare each revision, treating missing revisions as 0
    for i in range(max_length):
        rev1 = v1_parts[i] if i < len(v1_parts) else 0
        rev2 = v2_parts[i] if i < len(v2_parts) else 0
        if rev1 > rev2:
            return 1
        elif rev1 < rev2:
            return -1
    
    # If all revisions are equal, return 0
    return 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    version1 = "1.01"
    version2 = "1.001"
    print(compareVersion(version1, version2))  # Output: 0

    # Test Case 2
    version1 = "1.0"
    version2 = "1.0.0"
    print(compareVersion(version1, version2))  # Output: 0

    # Test Case 3
    version1 = "0.1"
    version2 = "1.1"
    print(compareVersion(version1, version2))  # Output: -1

    # Test Case 4
    version1 = "1.2"
    version2 = "1.10"
    print(compareVersion(version1, version2))  # Output: -1

    # Test Case 5
    version1 = "1.0.1"
    version2 = "1"
    print(compareVersion(version1, version2))  # Output: 1

"""
Time Complexity:
- Splitting the version strings into lists of revisions takes O(n + m), where n and m are the lengths of `version1` and `version2`, respectively.
- Comparing the revisions takes O(max(n, m)) since we iterate through the longer of the two lists.
- Overall time complexity: O(n + m).

Space Complexity:
- The space required to store the split lists of revisions is O(n + m).
- Overall space complexity: O(n + m).

Topic: Strings
"""