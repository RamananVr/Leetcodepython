"""
LeetCode Problem #2262: Total Appeal of A String

Problem Statement:
The appeal of a string is the number of distinct characters found in the string. 
For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.

Given a string s, return the total appeal of all of its substrings.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "abbca"
Output: 28
Explanation: The following are the substrings of "abbca":
- "a" has an appeal of 1.
- "ab" has an appeal of 2.
- "abb" has an appeal of 2.
- "abbc" has an appeal of 3.
- "abbca" has an appeal of 3.
- "b" has an appeal of 1.
- "bb" has an appeal of 1.
- "bbc" has an appeal of 2.
- "bbca" has an appeal of 3.
- "b" has an appeal of 1.
- "bc" has an appeal of 2.
- "bca" has an appeal of 3.
- "c" has an appeal of 1.
- "ca" has an appeal of 2.
- "a" has an appeal of 1.
The total sum of appeals is 28.

Example 2:
Input: s = "code"
Output: 20
Explanation: The total sum of appeals of all substrings is 20.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
"""

# Clean and Correct Python Solution
def appealSum(s: str) -> int:
    """
    Calculate the total appeal of all substrings of the given string.

    :param s: A string consisting of lowercase English letters.
    :return: The total appeal of all substrings.
    """
    last_seen = {}
    total_appeal = 0
    current_appeal = 0

    for i, char in enumerate(s):
        # If the character was seen before, subtract its previous contribution
        if char in last_seen:
            current_appeal -= last_seen[char]
        
        # Update the character's contribution to the current index
        last_seen[char] = i + 1
        
        # Add the new contribution to the current appeal
        current_appeal += last_seen[char]
        
        # Add the current appeal to the total appeal
        total_appeal += current_appeal

    return total_appeal

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abbca"
    print(f"Total appeal of '{s1}': {appealSum(s1)}")  # Expected Output: 28

    # Test Case 2
    s2 = "code"
    print(f"Total appeal of '{s2}': {appealSum(s2)}")  # Expected Output: 20

    # Test Case 3
    s3 = "a"
    print(f"Total appeal of '{s3}': {appealSum(s3)}")  # Expected Output: 1

    # Test Case 4
    s4 = "abc"
    print(f"Total appeal of '{s4}': {appealSum(s4)}")  # Expected Output: 10

    # Test Case 5
    s5 = "aaaa"
    print(f"Total appeal of '{s5}': {appealSum(s5)}")  # Expected Output: 10

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the string once, performing O(1) operations for each character.
- Thus, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The algorithm uses a dictionary to store the last seen positions of characters.
- In the worst case, the dictionary can store up to 26 entries (one for each lowercase English letter).
- Thus, the space complexity is O(1) (constant space).

Overall Complexity: Time: O(n), Space: O(1)
"""

# Topic: Strings