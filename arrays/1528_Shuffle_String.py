"""
LeetCode Problem #1528: Shuffle String

Problem Statement:
You are given a string `s` and an integer array `indices` of the same length. 
The string `s` will be shuffled such that the character at the `i`th position 
moves to `indices[i]` in the shuffled string.

Return the shuffled string.

Example 1:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

Example 2:
Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.

Constraints:
- `s.length == indices.length`
- `1 <= s.length <= 100`
- `s` consists of only lowercase English letters.
- `0 <= indices[i] < s.length`
- All values of `indices` are unique.
"""

# Python Solution
def restoreString(s: str, indices: list[int]) -> str:
    # Create a list of the same length as `s` to store the shuffled characters
    shuffled = [''] * len(s)
    
    # Place each character in its correct position
    for i, char in enumerate(s):
        shuffled[indices[i]] = char
    
    # Join the list into a string and return
    return ''.join(shuffled)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "codeleet"
    indices1 = [4, 5, 6, 7, 0, 2, 1, 3]
    print(restoreString(s1, indices1))  # Output: "leetcode"

    # Test Case 2
    s2 = "abc"
    indices2 = [0, 1, 2]
    print(restoreString(s2, indices2))  # Output: "abc"

    # Test Case 3
    s3 = "aiohn"
    indices3 = [3, 1, 4, 2, 0]
    print(restoreString(s3, indices3))  # Output: "nihao"

    # Test Case 4
    s4 = "a"
    indices4 = [0]
    print(restoreString(s4, indices4))  # Output: "a"

    # Test Case 5
    s5 = "art"
    indices5 = [1, 0, 2]
    print(restoreString(s5, indices5))  # Output: "rat"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the string `s` once, which takes O(n) time, 
  where `n` is the length of the string.
- Placing each character in the `shuffled` list is an O(1) operation.
- Joining the list into a string at the end also takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- The function uses an additional list `shuffled` of size `n` to store the shuffled characters.
- The space complexity is therefore O(n).
"""

# Topic: Arrays