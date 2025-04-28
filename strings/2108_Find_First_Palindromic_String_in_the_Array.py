"""
LeetCode Problem #2108: Find First Palindromic String in the Array

Problem Statement:
Given an array of strings `words`, return the first palindromic string in the array. 
If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

Example 1:
Input: words = ["abc", "car", "ada", "racecar", "cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".

Example 2:
Input: words = ["notapalindrome", "racecar"]
Output: "racecar"
Explanation: The first string that is palindromic is "racecar".

Example 3:
Input: words = ["def", "ghi"]
Output: ""
Explanation: There is no palindromic string in the array.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists only of lowercase English letters.
"""

# Python Solution
def firstPalindrome(words):
    """
    Finds the first palindromic string in the array.

    :param words: List[str] - List of strings
    :return: str - The first palindromic string or an empty string if none exists
    """
    for word in words:
        if word == word[::-1]:  # Check if the word is a palindrome
            return word
    return ""  # Return empty string if no palindrome is found

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["abc", "car", "ada", "racecar", "cool"]
    print(firstPalindrome(words1))  # Output: "ada"

    # Test Case 2
    words2 = ["notapalindrome", "racecar"]
    print(firstPalindrome(words2))  # Output: "racecar"

    # Test Case 3
    words3 = ["def", "ghi"]
    print(firstPalindrome(words3))  # Output: ""

    # Test Case 4
    words4 = ["level", "rotor", "civic"]
    print(firstPalindrome(words4))  # Output: "level"

    # Test Case 5
    words5 = ["hello", "world"]
    print(firstPalindrome(words5))  # Output: ""

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n = len(words) (number of strings in the array)
- Let m = average length of a string in the array
- For each string, we check if it is a palindrome, which takes O(m) time.
- In the worst case, we iterate through all n strings, resulting in a time complexity of O(n * m).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures that scale with the input size.
"""

# Topic: Strings