"""
LeetCode Question #953: Verifying an Alien Dictionary

Problem Statement:
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. 
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only 
if the given words are sorted lexicographically in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then the sequence is not sorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in lexicographical order, 
"apple" should come after "app").

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 20
- order.length == 26
- All characters in `words[i]` and `order` are English lowercase letters.
"""

# Python Solution
def isAlienSorted(words, order):
    """
    Determines if the given list of words is sorted lexicographically according to the alien dictionary order.

    :param words: List[str] - List of words written in the alien language.
    :param order: str - String representing the order of the alien alphabet.
    :return: bool - True if the words are sorted, False otherwise.
    """
    # Create a mapping of each character to its rank in the alien dictionary
    order_map = {char: index for index, char in enumerate(order)}

    # Helper function to compare two words
    def is_sorted(word1, word2):
        for c1, c2 in zip(word1, word2):
            if order_map[c1] < order_map[c2]:
                return True
            elif order_map[c1] > order_map[c2]:
                return False
        # If all characters are the same, the shorter word should come first
        return len(word1) <= len(word2)

    # Compare each pair of adjacent words
    for i in range(len(words) - 1):
        if not is_sorted(words[i], words[i + 1]):
            return False

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["hello", "leetcode"]
    order1 = "hlabcdefgijkmnopqrstuvwxyz"
    print(isAlienSorted(words1, order1))  # Output: True

    # Test Case 2
    words2 = ["word", "world", "row"]
    order2 = "worldabcefghijkmnpqstuvxyz"
    print(isAlienSorted(words2, order2))  # Output: False

    # Test Case 3
    words3 = ["apple", "app"]
    order3 = "abcdefghijklmnopqrstuvwxyz"
    print(isAlienSorted(words3, order3))  # Output: False

    # Test Case 4
    words4 = ["abc", "ab"]
    order4 = "abcdefghijklmnopqrstuvwxyz"
    print(isAlienSorted(words4, order4))  # Output: False

    # Test Case 5
    words5 = ["a", "b", "c"]
    order5 = "abcdefghijklmnopqrstuvwxyz"
    print(isAlienSorted(words5, order5))  # Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the `order_map` takes O(26) = O(1) since the alien alphabet has a fixed size of 26 characters.
- Comparing adjacent words involves iterating through their characters. In the worst case, we compare all characters 
  of all words, which takes O(S), where S is the total number of characters across all words.
- Overall time complexity: O(S).

Space Complexity:
- The `order_map` dictionary requires O(26) = O(1) space.
- The function uses a constant amount of additional space for variables.
- Overall space complexity: O(1).
"""

# Topic: Arrays