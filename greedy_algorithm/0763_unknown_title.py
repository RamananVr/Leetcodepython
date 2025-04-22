"""
LeetCode Problem #763: Partition Labels

Problem Statement:
You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part. 
Return a list of integers representing the size of these parts.

Example:
Input: s = "ababcbacadefegdehijhklij"
Output: [9, 7, 8]

Explanation:
The partition is "ababcbaca", "defegde", "hijhklij". This is a valid partition because each letter appears in at most one part.

Constraints:
- 1 <= s.length <= 500
- `s` consists of lowercase English letters.
"""

# Solution
def partitionLabels(s: str) -> list[int]:
    # Step 1: Record the last occurrence of each character
    last_occurrence = {char: idx for idx, char in enumerate(s)}
    
    # Step 2: Initialize variables for partitioning
    partitions = []
    start, end = 0, 0
    
    # Step 3: Iterate through the string
    for idx, char in enumerate(s):
        # Update the end of the current partition
        end = max(end, last_occurrence[char])
        
        # If the current index matches the end of the partition
        if idx == end:
            # Add the size of the partition to the result
            partitions.append(end - start + 1)
            # Update the start for the next partition
            start = idx + 1
    
    return partitions

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "ababcbacadefegdehijhklij"
    print(partitionLabels(s1))  # Output: [9, 7, 8]

    # Test Case 2
    s2 = "eccbbbbdec"
    print(partitionLabels(s2))  # Output: [10]

    # Test Case 3
    s3 = "a"
    print(partitionLabels(s3))  # Output: [1]

    # Test Case 4
    s4 = "abcde"
    print(partitionLabels(s4))  # Output: [1, 1, 1, 1, 1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the last occurrence of each character takes O(n), where n is the length of the string.
- Iterating through the string to determine partitions also takes O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(1) for the result list and O(26) for the dictionary storing the last occurrences of characters (since there are at most 26 lowercase English letters).
- Thus, the space complexity is O(1) (constant space usage).
"""

# Topic: Greedy Algorithm