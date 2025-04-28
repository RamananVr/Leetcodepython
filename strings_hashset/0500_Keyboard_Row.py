"""
LeetCode Problem #500: Keyboard Row

Problem Statement:
Given an array of strings `words`, return the words that can be typed using letters of only one row of the American keyboard like the image below.

In the American keyboard:
- The first row consists of the characters: "qwertyuiop"
- The second row consists of the characters: "asdfghjkl"
- The third row consists of the characters: "zxcvbnm"

Example 1:
Input: words = ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf", "sfd"]
Output: ["adsdf", "sfd"]

Constraints:
- 1 <= words.length <= 20
- 1 <= words[i].length <= 100
- `words[i]` consists of English letters (both lowercase and uppercase).
"""

# Python Solution
def findWords(words):
    # Define the rows of the keyboard
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")
    
    result = []
    
    for word in words:
        # Convert the word to lowercase for case-insensitive comparison
        lower_word = set(word.lower())
        
        # Check if the word can be typed using one row
        if lower_word <= row1 or lower_word <= row2 or lower_word <= row3:
            result.append(word)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["Hello", "Alaska", "Dad", "Peace"]
    print(findWords(words1))  # Output: ["Alaska", "Dad"]

    # Test Case 2
    words2 = ["omk"]
    print(findWords(words2))  # Output: []

    # Test Case 3
    words3 = ["adsdf", "sfd"]
    print(findWords(words3))  # Output: ["adsdf", "sfd"]

    # Test Case 4
    words4 = ["row", "type", "zoo"]
    print(findWords(words4))  # Output: ["row", "zoo"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n be the number of words in the input list `words`, and let m be the average length of a word.
- For each word, we convert it to lowercase and check if its set of characters is a subset of one of the three rows.
- The subset check takes O(m) time, and we do this for all n words.
- Therefore, the overall time complexity is O(n * m).

Space Complexity:
- We use three sets to represent the keyboard rows, which take O(1) space since the size of each set is constant.
- Additionally, we create a set for each word during the iteration, which takes O(m) space for each word.
- The result list stores at most n words, so it takes O(n) space in the worst case.
- Overall, the space complexity is O(n + m).
"""

# Topic: Strings, HashSet