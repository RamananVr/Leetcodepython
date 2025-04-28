"""
LeetCode Problem #2000: Reverse Prefix of Word

Problem Statement:
Given a 0-indexed string `word` and a character `ch`, reverse the segment of `word` that starts at the beginning of the string and ends at the first occurrence of `ch` (inclusive). 
If the character `ch` does not exist in `word`, do nothing.

- For example, if `word = "abcdefd"` and `ch = "d"`, then you should reverse the segment that starts at 0 and ends at 3 (inclusive). 
  The resulting string will be `"dcbaefd"`.

Return the resulting string after reversing the segment.

Constraints:
1. `1 <= word.length <= 250`
2. `word` consists of lowercase English letters.
3. `ch` is a lowercase English letter.
"""

def reversePrefix(word: str, ch: str) -> str:
    """
    Reverses the prefix of the word up to and including the first occurrence of ch.
    
    :param word: The input string.
    :param ch: The character to reverse up to.
    :return: The modified string after reversing the prefix.
    """
    # Find the index of the first occurrence of ch
    index = word.find(ch)
    
    # If ch is not found, return the original word
    if index == -1:
        return word
    
    # Reverse the prefix up to index and concatenate with the rest of the string
    return word[:index + 1][::-1] + word[index + 1:]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "abcdefd"
    ch1 = "d"
    print(reversePrefix(word1, ch1))  # Expected Output: "dcbaefd"

    # Test Case 2
    word2 = "xyxzxe"
    ch2 = "z"
    print(reversePrefix(word2, ch2))  # Expected Output: "zxyxxe"

    # Test Case 3
    word3 = "abcd"
    ch3 = "z"
    print(reversePrefix(word3, ch3))  # Expected Output: "abcd"

    # Test Case 4
    word4 = "a"
    ch4 = "a"
    print(reversePrefix(word4, ch4))  # Expected Output: "a"

    # Test Case 5
    word5 = "hello"
    ch5 = "o"
    print(reversePrefix(word5, ch5))  # Expected Output: "olleh"

"""
Time Complexity Analysis:
- Finding the first occurrence of `ch` in `word` using `find()` takes O(n), where n is the length of the string.
- Reversing the prefix using slicing and concatenation also takes O(n) in the worst case.
- Therefore, the overall time complexity is O(n).

Space Complexity Analysis:
- The slicing and reversing operation creates a new string, which takes O(n) space.
- Thus, the space complexity is O(n).

Topic: Strings
"""