"""
LeetCode Problem #2515: Shortest Distance to Target String in a Circular Array

Problem Statement:
You are given a 0-indexed circular string array `words` and a string `target`. A circular array means that the end of the array is connected to the beginning of the array.

Formally, the next element of `words[i]` is `words[(i + 1) % n]` and the previous element of `words[i]` is `words[(i - 1 + n) % n]`, where `n` is the length of `words`.

You are also given an integer `startIndex`, which represents your current position in the array.

Return the shortest distance required to reach any occurrence of `target` in `words`. If the target does not exist in `words`, return -1.

The distance between two indices `i` and `j` in a circular array is defined as the minimum number of steps required to move from `i` to `j`. The movement can be either clockwise or counterclockwise.

Example 1:
Input: words = ["hello", "world", "leetcode"], target = "hello", startIndex = 1
Output: 1
Explanation: The target "hello" is at index 0. The shortest distance from index 1 to index 0 is 1 step.

Example 2:
Input: words = ["a", "b", "c", "d"], target = "b", startIndex = 0
Output: 1
Explanation: The target "b" is at index 1. The shortest distance from index 0 to index 1 is 1 step.

Example 3:
Input: words = ["a", "b", "c", "d"], target = "e", startIndex = 0
Output: -1
Explanation: The target "e" does not exist in `words`.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- `words[i]` and `target` consist of only lowercase English letters.
- 0 <= startIndex < words.length
"""

# Python Solution
def shortestDistance(words, target, startIndex):
    """
    Finds the shortest distance to the target string in a circular array.

    :param words: List[str] - Circular array of strings
    :param target: str - Target string to find
    :param startIndex: int - Starting index in the array
    :return: int - Shortest distance to the target, or -1 if target is not found
    """
    n = len(words)
    min_distance = float('inf')
    found = False

    for i in range(n):
        if words[i] == target:
            found = True
            clockwise_distance = (i - startIndex) % n
            counterclockwise_distance = (startIndex - i + n) % n
            min_distance = min(min_distance, clockwise_distance, counterclockwise_distance)

    return min_distance if found else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["hello", "world", "leetcode"]
    target1 = "hello"
    startIndex1 = 1
    print(shortestDistance(words1, target1, startIndex1))  # Output: 1

    # Test Case 2
    words2 = ["a", "b", "c", "d"]
    target2 = "b"
    startIndex2 = 0
    print(shortestDistance(words2, target2, startIndex2))  # Output: 1

    # Test Case 3
    words3 = ["a", "b", "c", "d"]
    target3 = "e"
    startIndex3 = 0
    print(shortestDistance(words3, target3, startIndex3))  # Output: -1

    # Test Case 4
    words4 = ["a", "b", "c", "a", "b"]
    target4 = "b"
    startIndex4 = 3
    print(shortestDistance(words4, target4, startIndex4))  # Output: 1

    # Test Case 5
    words5 = ["x", "y", "z", "x", "y", "z"]
    target5 = "z"
    startIndex5 = 0
    print(shortestDistance(words5, target5, startIndex5))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `words` array once, which has a length of `n`.
- For each element, it performs constant-time calculations to determine the clockwise and counterclockwise distances.
- Therefore, the time complexity is O(n).

Space Complexity:
- The function uses a constant amount of extra space for variables like `min_distance` and `found`.
- No additional data structures are used, so the space complexity is O(1).
"""

# Topic: Arrays