"""
LeetCode Problem #527: Word Abbreviation

Problem Statement:
Given an array of n words, where each word contains only lowercase English letters, 
you need to abbreviate each word following these rules:

1. A word can be abbreviated by replacing all but the first and last character with the number of characters in between them. 
   For example, "like" can be abbreviated as "l2e", "leetcode" as "l6e", etc.
2. However, if two words have the same abbreviation, then the abbreviation is not unique. 
   In that case, the original word should be used instead of the abbreviation.
3. You need to return an array of the resulting words after applying the abbreviation rules.

Example:
Input: ["like", "leetcode", "god", "good"]
Output: ["l2e", "leetcode", "god", "g2d"]

Constraints:
- 1 <= words.length <= 400
- 1 <= words[i].length <= 20
- All words[i] consist of lowercase English letters.
"""

from collections import defaultdict

def wordsAbbreviation(words):
    """
    Function to abbreviate words according to the rules described in the problem statement.

    :param words: List[str] - List of words to abbreviate
    :return: List[str] - List of abbreviated words
    """
    def abbreviate(word, prefix_len):
        """
        Helper function to generate abbreviation for a word given a prefix length.
        """
        if len(word) - prefix_len - 1 <= 1:
            return word
        return word[:prefix_len] + str(len(word) - prefix_len - 1) + word[-1]

    n = len(words)
    result = [""] * n
    prefix_len = [1] * n  # Start with prefix length of 1 for all words
    groups = defaultdict(list)

    for i, word in enumerate(words):
        abbr = abbreviate(word, prefix_len[i])
        groups[abbr].append(i)

    while groups:
        new_groups = defaultdict(list)
        for abbr, indices in groups.items():
            if len(indices) == 1:
                # Unique abbreviation
                result[indices[0]] = abbr
            else:
                # Conflict, increase prefix length
                for i in indices:
                    prefix_len[i] += 1
                    new_abbr = abbreviate(words[i], prefix_len[i])
                    new_groups[new_abbr].append(i)
        groups = new_groups

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["like", "leetcode", "god", "good"]
    print(wordsAbbreviation(words1))  # Output: ["l2e", "leetcode", "god", "g2d"]

    # Test Case 2
    words2 = ["apple", "apricot", "banana", "bandana"]
    print(wordsAbbreviation(words2))  # Output: ["a3e", "apricot", "b4a", "bandana"]

    # Test Case 3
    words3 = ["internal", "interval", "intension", "intrusion"]
    print(wordsAbbreviation(words3))  # Output: ["internal", "interval", "intension", "intrusion"]

    # Test Case 4
    words4 = ["a", "b", "c"]
    print(wordsAbbreviation(words4))  # Output: ["a", "b", "c"]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iteratively resolves conflicts by increasing prefix lengths.
- In the worst case, each word may require up to its full length to resolve conflicts.
- Let n = number of words and m = average length of words.
- The complexity is approximately O(n * m), where m is the average word length.

Space Complexity:
- The space complexity is O(n + m), where n is the number of words and m is the average length of words.
- This includes the space for storing the result array and intermediate groups.

Topic: Strings
"""