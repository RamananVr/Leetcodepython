"""
LeetCode Problem #966: Vowel Spellchecker

Problem Statement:
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word from the wordlist.

The spellchecker should follow these rules:
1. If the query matches a word in the wordlist (case-sensitive), return the matched word.
2. If the query matches a word in the wordlist (case-insensitive), return the matched word with the same case as the wordlist.
3. If the query matches a word in the wordlist ignoring vowels ('a', 'e', 'i', 'o', 'u'), return the matched word with the same case as the wordlist.
4. If none of the above rules match, return an empty string.

The spellchecker should process a list of queries and return a list of results for each query.

Example:
Input:
wordlist = ["KiTe", "kite", "hare", "Hare"]
queries = ["kite", "Kite", "KiTe", "Hare", "hare", "Hear", "hear", "keti", "keet", "keto"]

Output:
["kite", "KiTe", "KiTe", "Hare", "hare", "hare", "", "KiTe", "", "KiTe"]

Constraints:
- 1 <= wordlist.length, queries.length <= 5000
- 1 <= wordlist[i].length, queries[i].length <= 7
- wordlist[i] and queries[i] consist only of English letters.
"""

# Python Solution
def spellchecker(wordlist, queries):
    def devowel(word):
        return ''.join('*' if c in 'aeiou' else c for c in word.lower())
    
    # Create dictionaries for exact match, case-insensitive match, and vowel-insensitive match
    exact_match = set(wordlist)
    case_insensitive_match = {}
    vowel_insensitive_match = {}
    
    for word in wordlist:
        lower_word = word.lower()
        devoweled_word = devowel(word)
        if lower_word not in case_insensitive_match:
            case_insensitive_match[lower_word] = word
        if devoweled_word not in vowel_insensitive_match:
            vowel_insensitive_match[devoweled_word] = word
    
    result = []
    for query in queries:
        if query in exact_match:
            result.append(query)
        elif query.lower() in case_insensitive_match:
            result.append(case_insensitive_match[query.lower()])
        elif devowel(query) in vowel_insensitive_match:
            result.append(vowel_insensitive_match[devowel(query)])
        else:
            result.append("")
    
    return result

# Example Test Cases
if __name__ == "__main__":
    wordlist = ["KiTe", "kite", "hare", "Hare"]
    queries = ["kite", "Kite", "KiTe", "Hare", "hare", "Hear", "hear", "keti", "keet", "keto"]
    print(spellchecker(wordlist, queries))  # Expected Output: ["kite", "KiTe", "KiTe", "Hare", "hare", "hare", "", "KiTe", "", "KiTe"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Building the dictionaries takes O(n * m), where n is the length of the wordlist and m is the average length of the words.
- Processing the queries takes O(q * m), where q is the length of the queries and m is the average length of the words.
- Overall time complexity: O((n + q) * m).

Space Complexity:
- The space required for the dictionaries is proportional to the size of the wordlist, so O(n * m).
- The result list takes O(q).
- Overall space complexity: O(n * m + q).
"""

# Topic: Hash Table