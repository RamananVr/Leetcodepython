"""
LeetCode Problem #520: Detect Capital

Problem Statement:
We define the usage of capitals in a word to be correct when one of the following cases holds:
1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital, like "Google".

Given a string `word`, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false

Example 3:
Input: word = "Google"
Output: true

Constraints:
- 1 <= word.length <= 100
- word consists of lowercase and uppercase English letters.
"""

def detectCapitalUse(word: str) -> bool:
    """
    Function to determine if the usage of capitals in a word is correct.
    """
    # Check if all letters are uppercase
    if word.isupper():
        return True
    # Check if all letters are lowercase
    if word.islower():
        return True
    # Check if only the first letter is uppercase and the rest are lowercase
    if word[0].isupper() and word[1:].islower():
        return True
    # If none of the above conditions are met, return False
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: All letters are uppercase
    print(detectCapitalUse("USA"))  # Expected output: True

    # Test Case 2: Mixed case, incorrect usage
    print(detectCapitalUse("FlaG"))  # Expected output: False

    # Test Case 3: First letter uppercase, rest lowercase
    print(detectCapitalUse("Google"))  # Expected output: True

    # Test Case 4: All letters are lowercase
    print(detectCapitalUse("leetcode"))  # Expected output: True

    # Test Case 5: Single uppercase letter
    print(detectCapitalUse("A"))  # Expected output: True

    # Test Case 6: Single lowercase letter
    print(detectCapitalUse("a"))  # Expected output: True

    # Test Case 7: Empty string (not valid per constraints, but for robustness)
    # print(detectCapitalUse(""))  # Uncommenting this would raise an error due to constraints.

"""
Time Complexity Analysis:
- Checking if a string is all uppercase (`isupper`) or all lowercase (`islower`) takes O(n) time,
  where n is the length of the string.
- Slicing the string (`word[1:]`) and checking if it's lowercase also takes O(n) time.
- Since we perform these checks sequentially, the overall time complexity is O(n).

Space Complexity Analysis:
- The function uses a constant amount of extra space, so the space complexity is O(1).

Topic: Strings
"""