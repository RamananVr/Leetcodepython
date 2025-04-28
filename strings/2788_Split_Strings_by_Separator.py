"""
LeetCode Problem #2788: Split Strings by Separator

Problem Statement:
Given a list of strings `words` and a character `separator`, split each string in `words` by the `separator` 
and return all the resulting substrings in the order they were found. Note that you can return the substrings 
in any order, but they should not contain the `separator`.

Constraints:
- 1 <= len(words) <= 1000
- 1 <= len(words[i]) <= 1000
- `separator` is a single character.
- The input strings may contain letters, digits, and special characters.

Example:
Input: words = ["one.two.three", "four.five", "six"], separator = '.'
Output: ["one", "two", "three", "four", "five", "six"]

Input: words = ["$easy$", "$problem$"], separator = '$'
Output: ["easy", "problem"]

Input: words = ["|||"], separator = '|'
Output: []

"""

def split_words_by_separator(words, separator):
    """
    Splits each string in the list `words` by the given `separator` and returns a list of all resulting substrings.

    Args:
    words (List[str]): A list of strings to be split.
    separator (str): A single character used as the separator.

    Returns:
    List[str]: A list of substrings obtained by splitting the input strings.
    """
    result = []
    for word in words:
        # Split the word by the separator and filter out empty strings
        result.extend([substring for substring in word.split(separator) if substring])
    return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["one.two.three", "four.five", "six"]
    separator1 = '.'
    print(split_words_by_separator(words1, separator1))  # Output: ["one", "two", "three", "four", "five", "six"]

    # Test Case 2
    words2 = ["$easy$", "$problem$"]
    separator2 = '$'
    print(split_words_by_separator(words2, separator2))  # Output: ["easy", "problem"]

    # Test Case 3
    words3 = ["|||"]
    separator3 = '|'
    print(split_words_by_separator(words3, separator3))  # Output: []

    # Test Case 4
    words4 = ["hello-world", "leet-code", "python"]
    separator4 = '-'
    print(split_words_by_separator(words4, separator4))  # Output: ["hello", "world", "leet", "code", "python"]

    # Test Case 5
    words5 = ["a,b,c", "d,e", "f"]
    separator5 = ','
    print(split_words_by_separator(words5, separator5))  # Output: ["a", "b", "c", "d", "e", "f"]


"""
Time Complexity:
- Splitting a string of length `n` by a separator takes O(n) time.
- If there are `m` strings in the `words` list, and the total number of characters across all strings is `N`,
  the total time complexity is O(N), where N is the sum of the lengths of all strings in `words`.

Space Complexity:
- The space complexity is O(N) for storing the resulting substrings, where N is the total number of characters
  in the input strings (excluding separators).

Topic: Strings
"""