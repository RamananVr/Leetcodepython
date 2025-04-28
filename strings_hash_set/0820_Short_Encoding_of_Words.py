"""
LeetCode Problem #820: Short Encoding of Words

Problem Statement:
A valid encoding of an array of words is any reference string s and array of indices indices such that:
- words[i] can be obtained from s by taking the substring starting at indices[i] and up to the next '#' character.

Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

Example:
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].

Note:
- 1 <= words.length <= 2000
- 1 <= words[i].length <= 7
- words[i] consists of only lowercase letters.
"""

# Clean, Correct Python Solution
def minimumLengthEncoding(words):
    """
    Finds the length of the shortest reference string encoding for the given words.

    :param words: List[str] - List of words to encode
    :return: int - Length of the shortest encoding string
    """
    # Use a set to remove duplicates
    unique_words = set(words)
    
    # Remove words that are suffixes of other words
    for word in words:
        for k in range(1, len(word)):
            unique_words.discard(word[k:])
    
    # Calculate the total length of the encoding
    return sum(len(word) + 1 for word in unique_words)  # +1 for the '#' character

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["time", "me", "bell"]
    print(minimumLengthEncoding(words1))  # Expected Output: 10

    # Test Case 2
    words2 = ["t"]
    print(minimumLengthEncoding(words2))  # Expected Output: 2

    # Test Case 3
    words3 = ["time", "me", "bell", "ell"]
    print(minimumLengthEncoding(words3))  # Expected Output: 10

    # Test Case 4
    words4 = ["abc", "c", "bc"]
    print(minimumLengthEncoding(words4))  # Expected Output: 4

    # Test Case 5
    words5 = ["a", "b", "c"]
    print(minimumLengthEncoding(words5))  # Expected Output: 6

# Time and Space Complexity Analysis
"""
Time Complexity:
- Removing suffixes: For each word, we iterate through its suffixes. In the worst case, this is O(n * m^2), 
  where n is the number of words and m is the average length of a word.
- Calculating the encoding length: This is O(n), where n is the number of unique words.
- Overall: O(n * m^2).

Space Complexity:
- The set `unique_words` stores the unique words, which takes O(n * m) space in the worst case.
- Overall: O(n * m).
"""

# Topic: Strings, Hash Set