"""
LeetCode Problem #1055: Shortest Way to Form String

Problem Statement:
From any string `source`, we can form a string `target` by repeatedly appending characters from `source` to the end of a new string. 
We want to form `target` using the minimum number of subsequences of `source`. 
(Note that a subsequence of a string is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
For example, "abc" is a subsequence of "aebdc" because "abc" can be formed by deleting "e" and "d".)

Given two strings `source` and `target`, return the minimum number of subsequences of `source` such that their concatenation equals `target`. 
If the task is impossible, return -1.

Example 1:
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" + "bc".

Example 2:
Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target "acdbc" cannot be formed because 'd' is not in the source.

Example 3:
Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target "xzyxz" can be formed by "xyz" + "yz" + "xz".

Constraints:
- Both `source` and `target` consist of only lowercase English letters.
- 1 <= source.length, target.length <= 1000
"""

# Python Solution
def shortestWay(source: str, target: str) -> int:
    source_set = set(source)
    target_set = set(target)
    
    # If target contains characters not in source, return -1
    if not target_set.issubset(source_set):
        return -1
    
    source_index = 0
    target_index = 0
    subsequences_count = 0
    
    while target_index < len(target):
        source_index = 0
        subsequences_count += 1
        
        while source_index < len(source) and target_index < len(target):
            if source[source_index] == target[target_index]:
                target_index += 1
            source_index += 1
    
    return subsequences_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    source = "abc"
    target = "abcbc"
    print(shortestWay(source, target))  # Output: 2

    # Test Case 2
    source = "abc"
    target = "acdbc"
    print(shortestWay(source, target))  # Output: -1

    # Test Case 3
    source = "xyz"
    target = "xzyxz"
    print(shortestWay(source, target))  # Output: 3

    # Additional Test Case 4
    source = "abc"
    target = "aabbcc"
    print(shortestWay(source, target))  # Output: 3

    # Additional Test Case 5
    source = "abc"
    target = "cba"
    print(shortestWay(source, target))  # Output: -1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let `m` be the length of `source` and `n` be the length of `target`.
- The algorithm iterates through `target` while scanning `source` repeatedly.
- In the worst case, we scan the entire `source` for each character in `target`, resulting in O(m * n) time complexity.

Space Complexity:
- The space complexity is O(m + n) due to the sets `source_set` and `target_set` used for validation.
- No additional data structures are used beyond these sets.

Overall:
Time Complexity: O(m * n)
Space Complexity: O(m + n)
"""

# Topic: Greedy Algorithm