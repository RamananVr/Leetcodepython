"""
LeetCode Problem #2205: Optimal Way to Partition a String

Problem Statement:
You are given a string `s` consisting of lowercase English letters. You want to partition the string into one or more substrings such that the number of distinct characters in each substring is the same.

Return the minimum number of substrings required to achieve this.

Constraints:
- 1 <= s.length <= 10^5
- `s` consists of only lowercase English letters.

Example:
Input: s = "abac"
Output: 2
Explanation: You can partition the string into "ab" and "ac". Both substrings have 2 distinct characters.

Input: s = "aaaa"
Output: 1
Explanation: The entire string has only 1 distinct character, so no partitioning is needed.

Input: s = "abcde"
Output: 5
Explanation: Each character is distinct, so each character must be its own substring.
"""

def optimal_partition(s: str) -> int:
    """
    Function to find the minimum number of substrings required to partition the string
    such that each substring has the same number of distinct characters.
    """
    # Initialize a set to track distinct characters in the current substring
    distinct_chars = set()
    # Initialize the count of partitions
    partitions = 0

    for char in s:
        # If the character is already in the set, it means we need a new partition
        if char in distinct_chars:
            partitions += 1
            distinct_chars.clear()  # Start a new partition
        # Add the character to the current set
        distinct_chars.add(char)

    # Add one more partition for the last group of characters
    return partitions + 1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abac"
    print(optimal_partition(s1))  # Expected Output: 2

    # Test Case 2
    s2 = "aaaa"
    print(optimal_partition(s2))  # Expected Output: 1

    # Test Case 3
    s3 = "abcde"
    print(optimal_partition(s3))  # Expected Output: 5

    # Test Case 4
    s4 = "aabbcc"
    print(optimal_partition(s4))  # Expected Output: 3

    # Test Case 5
    s5 = "abacabadabacaba"
    print(optimal_partition(s5))  # Expected Output: 8


"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the string `s` once, performing O(1) operations for each character.
- Therefore, the time complexity is O(n), where `n` is the length of the string.

Space Complexity:
- The function uses a set to store distinct characters in the current substring.
- In the worst case, the set can contain all 26 lowercase English letters.
- Therefore, the space complexity is O(1) (constant space).

Topic: Strings, Hashing
"""