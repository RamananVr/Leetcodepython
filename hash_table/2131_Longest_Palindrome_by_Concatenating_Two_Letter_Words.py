"""
LeetCode Problem #2131: Longest Palindrome by Concatenating Two Letter Words

Problem Statement:
You are given an array of strings `words` consisting of two lowercase English letters. 
You need to find the longest palindrome that can be formed by concatenating the words 
from the given array. You may use each word exactly once.

Return the length of the longest palindrome that can be formed.

Note:
- A palindrome is a string that reads the same forward and backward.
- Words can be used in any order.

Example 1:
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One way to form a palindrome is "lc" + "gg" + "cl", resulting in "lcggcl", 
which has a length of 6.

Example 2:
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One way to form a palindrome is "ab" + "ty" + "yt" + "ba", resulting in 
"abtyytba", which has a length of 8.

Example 3:
Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One way to form a palindrome is "cc", resulting in "cc", which has a length of 2.

Constraints:
- 1 <= words.length <= 10^5
- words[i].length == 2
- words[i] consists of lowercase English letters.
"""

# Python Solution
from collections import Counter

def longestPalindrome(words):
    # Count the frequency of each word
    word_count = Counter(words)
    palindrome_length = 0
    central_word_used = False

    for word, count in word_count.items():
        # If the word is a palindrome itself (e.g., "gg", "cc")
        if word[0] == word[1]:
            # Add pairs of this word to the palindrome
            palindrome_length += (count // 2) * 4
            # Check if we can use one as the central word
            if count % 2 == 1 and not central_word_used:
                palindrome_length += 2
                central_word_used = True
        else:
            # If the word is not a palindrome, check its reverse
            reverse_word = word[::-1]
            if reverse_word in word_count:
                # Add pairs of this word and its reverse to the palindrome
                pairs = min(count, word_count[reverse_word])
                palindrome_length += pairs * 4
                # Remove the used pairs from the counter to avoid double counting
                word_count[reverse_word] = 0

    return palindrome_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["lc", "cl", "gg"]
    print(longestPalindrome(words1))  # Output: 6

    # Test Case 2
    words2 = ["ab", "ty", "yt", "lc", "cl", "ab"]
    print(longestPalindrome(words2))  # Output: 8

    # Test Case 3
    words3 = ["cc", "ll", "xx"]
    print(longestPalindrome(words3))  # Output: 2

    # Test Case 4
    words4 = ["aa", "bb", "aa", "bb", "cc"]
    print(longestPalindrome(words4))  # Output: 10

    # Test Case 5
    words5 = ["ab", "ba", "cd", "dc", "ee"]
    print(longestPalindrome(words5))  # Output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of words takes O(n), where n is the length of the `words` array.
- Iterating through the word_count dictionary takes O(m), where m is the number of unique words.
- Overall, the time complexity is O(n + m). Since m <= n, the time complexity is effectively O(n).

Space Complexity:
- The space complexity is O(m), where m is the number of unique words stored in the Counter dictionary.
- In the worst case, m = n (all words are unique), so the space complexity is O(n).

Topic: Hash Table
"""