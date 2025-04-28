"""
LeetCode Problem #648: Replace Words

Problem Statement:
In English, we have a concept called "root," which can be followed by some other words to form another word - let's call this word "successor." For example, the root "an" can be followed by "other," which forms "another."

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

Example 1:
Input: dictionary = ["cat", "bat", "rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:
Input: dictionary = ["a", "b", "c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"

Example 3:
Input: dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa aaaa aaa aaa aaa aaa"
Output: "a aa a aaa aaa aaa aaa"

Example 4:
Input: dictionary = ["catt", "cat", "bat", "rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 5:
Input: dictionary = ["ac", "ab"], sentence = "it is abnormal that this took so long"
Output: "it is ab that this took so long"

Constraints:
- 1 <= dictionary.length <= 1000
- 1 <= dictionary[i].length <= 100
- dictionary[i] consists of only lower-case letters.
- 1 <= sentence.length <= 10^6
- sentence consists of only lower-case letters and spaces.
- The words in sentence are separated by a single space.
- There are no leading or trailing spaces in the sentence.

"""

# Python Solution
def replaceWords(dictionary, sentence):
    """
    Replace successors in the sentence with their shortest root from the dictionary.

    :param dictionary: List[str] - List of root words.
    :param sentence: str - Sentence to process.
    :return: str - Sentence after replacement.
    """
    # Create a set for faster lookup of roots
    root_set = set(dictionary)
    
    def replace_word(word):
        # Try to find the shortest root for the word
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            if prefix in root_set:
                return prefix
        return word

    # Split the sentence into words, replace each word, and join back
    return " ".join(replace_word(word) for word in sentence.split())

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(replaceWords(dictionary, sentence))  # Output: "the cat was rat by the bat"

    # Test Case 2
    dictionary = ["a", "b", "c"]
    sentence = "aadsfasf absbs bbab cadsfafs"
    print(replaceWords(dictionary, sentence))  # Output: "a a b c"

    # Test Case 3
    dictionary = ["a", "aa", "aaa", "aaaa"]
    sentence = "a aa aaaa aaa aaa aaa aaa"
    print(replaceWords(dictionary, sentence))  # Output: "a aa a aaa aaa aaa aaa"

    # Test Case 4
    dictionary = ["catt", "cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(replaceWords(dictionary, sentence))  # Output: "the cat was rat by the bat"

    # Test Case 5
    dictionary = ["ac", "ab"]
    sentence = "it is abnormal that this took so long"
    print(replaceWords(dictionary, sentence))  # Output: "it is ab that this took so long"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let `n` be the number of words in the sentence and `m` be the average length of a word.
- Let `k` be the number of roots in the dictionary and `l` be the average length of a root.
- For each word in the sentence, we check prefixes up to its length (O(m)).
- Checking if a prefix exists in the set is O(1) on average.
- Total complexity: O(n * m).

Space Complexity:
- The space required for the dictionary set is O(k * l), where `k` is the number of roots and `l` is the average length of a root.
- The space required for the sentence split and join operations is O(n * m).
- Total space complexity: O(k * l + n * m).
"""

# Topic: Strings, Hash Table