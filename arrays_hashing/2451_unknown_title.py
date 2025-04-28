"""
LeetCode Problem #2451: Odd String Difference

Problem Statement:
You are given an array of strings `words`. Each string consists of lowercase English letters and has the same length.

A string `s` is called an "odd string" if the difference array of `s` is different from the difference arrays of all the other strings in `words`.

The difference array of a string `s` is the array `differences` where `differences[i] = ord(s[i+1]) - ord(s[i])` for all `0 <= i < len(s) - 1`.

For example, for the string "acb", the difference array is `[2, -1]` because:
- `ord('c') - ord('a') = 2`
- `ord('b') - ord('c') = -1`

You are tasked to return the "odd string" in the array `words`. It is guaranteed that there is exactly one odd string in the input.

Constraints:
- `3 <= words.length <= 100`
- `2 <= words[i].length <= 20`
- All strings in `words` have the same length.
- There is exactly one odd string in `words`.

"""

def oddString(words):
    """
    Function to find the odd string in the list of words.
    
    Args:
    words (List[str]): List of strings where one string has a unique difference array.
    
    Returns:
    str: The odd string.
    """
    def get_difference_array(word):
        return [ord(word[i+1]) - ord(word[i]) for i in range(len(word) - 1)]
    
    # Create a dictionary to store difference arrays and their corresponding words
    diff_map = {}
    for word in words:
        diff = tuple(get_difference_array(word))
        if diff not in diff_map:
            diff_map[diff] = []
        diff_map[diff].append(word)
    
    # Find the difference array with only one word associated with it
    for diff, word_list in diff_map.items():
        if len(word_list) == 1:
            return word_list[0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["adc", "wzy", "abc"]
    print(oddString(words1))  # Output: "abc"

    # Test Case 2
    words2 = ["aaa", "bob", "ccc", "ddd"]
    print(oddString(words2))  # Output: "bob"

    # Test Case 3
    words3 = ["xyz", "xzz", "xzy"]
    print(oddString(words3))  # Output: "xzy"

"""
Time Complexity Analysis:
- Calculating the difference array for a single word takes O(L), where L is the length of the word.
- For `n` words, this process takes O(n * L).
- Storing and iterating through the dictionary also takes O(n * L) in the worst case.
- Overall time complexity: O(n * L).

Space Complexity Analysis:
- The space required for the dictionary is proportional to the number of unique difference arrays, which is at most O(n * L) in the worst case.
- Overall space complexity: O(n * L).

Topic: Arrays, Hashing
"""