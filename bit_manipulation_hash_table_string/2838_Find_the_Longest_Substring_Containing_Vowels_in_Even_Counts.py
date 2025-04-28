"""
LeetCode Problem #2838: Find the Longest Substring Containing Vowels in Even Counts

Problem Statement:
Given a string `s`, find the length of the longest substring that contains each of the vowels 
('a', 'e', 'i', 'o', 'u') an even number of times. You may assume that the input string 
only contains lowercase English letters.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.

Example:
Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains all vowels in even counts.

Approach:
The problem can be solved using a bitmasking technique. Each vowel is represented by a bit in a 
5-bit integer (e.g., 'a' = 1st bit, 'e' = 2nd bit, etc.). As we iterate through the string, we 
track the current state of vowel counts using this bitmask. If the same bitmask state is seen 
again, it means the substring between these two indices has all vowels in even counts.
"""

def findTheLongestSubstring(s: str) -> int:
    # Map to store the first occurrence of each bitmask
    state_to_index = {0: -1}
    # Initialize variables
    current_state = 0
    max_length = 0
    # Vowel to bitmask mapping
    vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
    
    for i, char in enumerate(s):
        # Update the current state if the character is a vowel
        if char in vowels:
            current_state ^= vowels[char]
        
        # Check if the current state has been seen before
        if current_state in state_to_index:
            # Calculate the length of the substring
            max_length = max(max_length, i - state_to_index[current_state])
        else:
            # Store the first occurrence of this state
            state_to_index[current_state] = i
    
    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "eleetminicoworoep"
    print(findTheLongestSubstring(s1))  # Output: 13

    # Test Case 2
    s2 = "leetcodeisgreat"
    print(findTheLongestSubstring(s2))  # Output: 5

    # Test Case 3
    s3 = "bcbcbc"
    print(findTheLongestSubstring(s3))  # Output: 6

"""
Time Complexity Analysis:
- The algorithm iterates through the string once, performing constant-time operations for each character.
- Thus, the time complexity is O(n), where n is the length of the string.

Space Complexity Analysis:
- The space complexity is O(1) for the bitmask and O(k) for the dictionary, where k is the number of unique states.
- Since there are at most 2^5 = 32 possible states (5 vowels), the space complexity is effectively O(1).

Topic: Bit Manipulation, Hash Table, String
"""