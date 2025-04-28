"""
LeetCode Problem #1324: Print Words Vertically

Problem Statement:
Given a string `s`. Return all the words vertically in the same order in which they appear in `s`.
Words are returned as a list of strings, complete with spaces when necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

Example 1:
Input: s = "HOW ARE YOU"
Output: ["HAY", "ORO", "WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"

Example 2:
Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB", "OEROOE", "   T"]

Example 3:
Input: s = "CONTEST IS COMING"
Output: ["CIC", "OSO", "N M", "T I", "E N", "S G", "T"]

Constraints:
- `1 <= s.length <= 200`
- `s` contains only upper case English letters and spaces.
- It's guaranteed that there is at least one word in `s`.
"""

def printVertically(s: str) -> list[str]:
    # Split the input string into words
    words = s.split()
    
    # Find the maximum length of the words
    max_length = max(len(word) for word in words)
    
    # Create the vertical representation
    result = []
    for i in range(max_length):
        vertical_word = ""
        for word in words:
            # Append the character at the current index or a space if the index is out of bounds
            vertical_word += word[i] if i < len(word) else " "
        # Strip trailing spaces and add to the result
        result.append(vertical_word.rstrip())
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "HOW ARE YOU"
    print(printVertically(s1))  # Output: ["HAY", "ORO", "WEU"]

    # Test Case 2
    s2 = "TO BE OR NOT TO BE"
    print(printVertically(s2))  # Output: ["TBONTB", "OEROOE", "   T"]

    # Test Case 3
    s3 = "CONTEST IS COMING"
    print(printVertically(s3))  # Output: ["CIC", "OSO", "N M", "T I", "E N", "S G", "T"]

# Time Complexity Analysis:
# - Splitting the string into words takes O(n), where n is the length of the string.
# - Finding the maximum word length takes O(k), where k is the number of words.
# - Constructing the vertical words involves iterating over the maximum word length (m) and the number of words (k),
#   resulting in O(m * k).
# Overall time complexity: O(n + m * k).

# Space Complexity Analysis:
# - The space required for the result list is proportional to the number of vertical words and their lengths, O(m * k).
# - Additional space is used for the `words` list, which is O(k).
# Overall space complexity: O(m * k).

# Topic: Strings