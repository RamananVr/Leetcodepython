"""
LeetCode Problem #1258: Synonymous Sentences

Problem Statement:
Given a list of pairs of synonymous words and a sentence text, generate all possible sentences 
that can be formed by replacing any word in the sentence with one of its synonyms.

Each pair of synonymous words [a, b] means that a and b are synonyms. A word can only be replaced 
by one of its synonyms if it exists in the list of pairs. You may assume that a word is synonymous 
with itself.

Return all possible sentences sorted lexicographically.

Example:
Input:
    synonyms = [["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]]
    text = "I am happy"

Output:
    ["I am cheerful", "I am happy", "I am joy"]

Constraints:
1. 0 <= synonyms.length <= 10
2. synonyms[i].length == 2
3. 1 <= synonyms[i][0].length, synonyms[i][1].length <= 10
4. synonyms[i][0] != synonyms[i][1]
5. All words consist of lowercase English letters.
6. 1 <= text.length <= 10
7. text consists of lowercase English letters and spaces.
"""

from collections import defaultdict
from itertools import product

def generateSentences(synonyms, text):
    # Step 1: Build a union-find structure to group synonyms
    parent = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX, rootY = find(x), find(y)
        if rootX != rootY:
            parent[rootY] = rootX

    # Initialize union-find
    for a, b in synonyms:
        if a not in parent:
            parent[a] = a
        if b not in parent:
            parent[b] = b
        union(a, b)

    # Group words by their root parent
    groups = defaultdict(set)
    for word in parent:
        root = find(word)
        groups[root].add(word)

    # Create a mapping of word to its synonyms
    synonym_map = {}
    for group in groups.values():
        for word in group:
            synonym_map[word] = sorted(group)

    # Step 2: Generate all possible sentences
    words = text.split()
    options = []
    for word in words:
        if word in synonym_map:
            options.append(synonym_map[word])
        else:
            options.append([word])

    # Generate all combinations of words
    sentences = [' '.join(sentence) for sentence in product(*options)]
    return sorted(sentences)

# Example Test Cases
if __name__ == "__main__":
    synonyms = [["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]]
    text = "I am happy"
    print(generateSentences(synonyms, text))
    # Output: ["I am cheerful", "I am happy", "I am joy"]

    synonyms = [["a", "b"], ["b", "c"]]
    text = "a b"
    print(generateSentences(synonyms, text))
    # Output: ["a a", "a b", "a c", "b a", "b b", "b c", "c a", "c b", "c c"]

    synonyms = []
    text = "hello world"
    print(generateSentences(synonyms, text))
    # Output: ["hello world"]

# Time and Space Complexity Analysis
# Time Complexity:
# - Building the union-find structure: O(E * α(V)), where E is the number of synonym pairs and α is the inverse Ackermann function.
# - Grouping synonyms: O(V), where V is the number of unique words in the synonym pairs.
# - Generating sentences: O(P), where P is the product of the sizes of the synonym groups for each word in the text.
# - Sorting the sentences: O(N * log(N)), where N is the number of generated sentences.

# Space Complexity:
# - Union-find structure: O(V), where V is the number of unique words in the synonym pairs.
# - Synonym map and groups: O(V).
# - Options list and generated sentences: O(P).

# Overall, the time and space complexity depend on the size of the synonym pairs and the input text.

# Topic: Union-Find, Backtracking, Strings