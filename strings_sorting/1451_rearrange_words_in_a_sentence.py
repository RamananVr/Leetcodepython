"""
LeetCode Question #1451: Rearrange Words in a Sentence

Problem Statement:
Given a sentence `text` (a string of space-separated words), rearrange the words in the sentence such that:
1. Words are sorted by their lengths in ascending order.
2. If two words have the same length, they should remain in their original order relative to each other.
3. The first word in the resulting sentence should be capitalized, and the rest should be in lowercase.

Return the rearranged sentence as a string.

Constraints:
- `text` consists of only capital and lowercase English letters and spaces.
- `text` contains at least one word.
- All words in `text` are separated by a single space.
- `text` does not contain leading or trailing spaces.

Example:
Input: text = "LeetCode is a great platform"
Output: "A is great Leetcode platform"
"""

# Solution
def arrangeWords(text: str) -> str:
    # Split the text into words and store their original indices
    words = text.split()
    # Lowercase all words and pair them with their original indices
    words = [(word.lower(), i) for i, word in enumerate(words)]
    # Sort words by length, and by original index if lengths are equal
    words.sort(key=lambda x: (len(x[0]), x[1]))
    # Reconstruct the sentence with the first word capitalized
    result = " ".join(word[0] for word in words)
    return result.capitalize()

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    text1 = "LeetCode is a great platform"
    print(arrangeWords(text1))  # Output: "A is great Leetcode platform"

    # Test Case 2
    text2 = "Keep calm and code on"
    print(arrangeWords(text2))  # Output: "On and keep calm code"

    # Test Case 3
    text3 = "To be or not to be"
    print(arrangeWords(text3))  # Output: "To be or to not be"

    # Test Case 4
    text4 = "Hello world"
    print(arrangeWords(text4))  # Output: "Hello world"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting the sentence into words takes O(n), where n is the length of the input string.
- Sorting the words takes O(m log m), where m is the number of words in the sentence.
- Joining the words back into a sentence takes O(n).
Overall, the time complexity is O(n + m log m), where n is the length of the input string and m is the number of words.

Space Complexity:
- The space required for storing the list of words is O(m), where m is the number of words.
- Additional space is used for sorting, which is O(m).
Overall, the space complexity is O(m).
"""

# Topic: Strings, Sorting