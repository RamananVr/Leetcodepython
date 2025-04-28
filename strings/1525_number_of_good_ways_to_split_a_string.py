"""
LeetCode Question #1525: Number of Good Ways to Split a String

Problem Statement:
You are given a string s. A split is called good if you can split s into two non-empty strings s1 and s2 
such that the number of distinct characters in s1 is equal to the number of distinct characters in s2.

Return the number of good splits you can make in s.

Example:
Input: s = "aacaba"
Output: 2
Explanation:
There are 5 ways to split "aacaba" and 2 of them are good:
- "a" and "acaba" -> distinct characters in both parts are 1 and 3 respectively.
- "aa" and "caba" -> distinct characters in both parts are 1 and 3 respectively.
- "aac" and "aba" -> distinct characters in both parts are 2 and 2 respectively (good split).
- "aaca" and "ba" -> distinct characters in both parts are 3 and 2 respectively.
- "aacab" and "a" -> distinct characters in both parts are 3 and 1 respectively.

Constraints:
- s contains only lowercase English letters.
- 1 <= s.length <= 10^5
"""

# Solution
def numSplits(s: str) -> int:
    # Initialize dictionaries to track distinct characters in left and right parts
    left_count = {}
    right_count = {}
    
    # Populate the right_count dictionary with the frequency of each character in the string
    for char in s:
        right_count[char] = right_count.get(char, 0) + 1
    
    # Initialize variables to track the number of distinct characters in left and right parts
    left_distinct = 0
    right_distinct = len(right_count)
    
    # Initialize the count of good splits
    good_splits = 0
    
    # Iterate through the string to calculate good splits
    for char in s:
        # Move the current character from right to left
        if char not in left_count:
            left_distinct += 1
        left_count[char] = left_count.get(char, 0) + 1
        
        right_count[char] -= 1
        if right_count[char] == 0:
            right_distinct -= 1
        
        # Check if the number of distinct characters in left and right parts are equal
        if left_distinct == right_distinct:
            good_splits += 1
    
    return good_splits

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aacaba"
    print(numSplits(s1))  # Output: 2

    # Test Case 2
    s2 = "abcd"
    print(numSplits(s2))  # Output: 1

    # Test Case 3
    s3 = "aaaa"
    print(numSplits(s3))  # Output: 3

    # Test Case 4
    s4 = "a"
    print(numSplits(s4))  # Output: 0

    # Test Case 5
    s5 = "ababab"
    print(numSplits(s5))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution iterates through the string once to populate the `right_count` dictionary (O(n)).
- Then, it iterates through the string again to calculate the good splits (O(n)).
- Overall time complexity: O(n).

Space Complexity:
- The solution uses two dictionaries (`left_count` and `right_count`) to track character frequencies.
- In the worst case, each dictionary can store up to 26 entries (for all lowercase English letters).
- Overall space complexity: O(1) (constant space for the dictionaries).

Topic: Strings
"""