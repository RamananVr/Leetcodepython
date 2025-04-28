"""
LeetCode Problem #1189: Maximum Number of Balloons

Problem Statement:
Given a string `text`, you want to use the characters of `text` to form as many instances of the word "balloon" as possible.

Each character in `text` can be used in at most one instance of "balloon". Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0

Constraints:
- 1 <= text.length <= 10^4
- text consists of lowercase English letters only.
"""

def maxNumberOfBalloons(text: str) -> int:
    """
    Function to calculate the maximum number of instances of the word "balloon"
    that can be formed using the characters in the input string `text`.
    """
    from collections import Counter

    # Count the frequency of each character in the input text
    char_count = Counter(text)

    # Define the frequency requirements for each character in "balloon"
    balloon_count = {
        'b': 1,
        'a': 1,
        'l': 2,
        'o': 2,
        'n': 1
    }

    # Calculate the maximum number of "balloon" instances that can be formed
    max_balloons = float('inf')
    for char, required_count in balloon_count.items():
        max_balloons = min(max_balloons, char_count[char] // required_count)

    return max_balloons


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    text1 = "nlaebolko"
    print(maxNumberOfBalloons(text1))  # Output: 1

    # Test Case 2
    text2 = "loonbalxballpoon"
    print(maxNumberOfBalloons(text2))  # Output: 2

    # Test Case 3
    text3 = "leetcode"
    print(maxNumberOfBalloons(text3))  # Output: 0

    # Additional Test Case
    text4 = "balloonballoonballoon"
    print(maxNumberOfBalloons(text4))  # Output: 3


"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of characters in `text` using `Counter` takes O(n), where n is the length of the input string.
- Iterating through the characters in "balloon" (a fixed-length word) takes O(1).
- Overall, the time complexity is O(n).

Space Complexity:
- The `Counter` object stores the frequency of each character in `text`, which requires O(26) space (since there are at most 26 lowercase English letters).
- The space complexity is O(1) in terms of additional space usage.

Topic: Strings
"""