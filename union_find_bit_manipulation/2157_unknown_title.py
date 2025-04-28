"""
LeetCode Problem #2157: Groups of Strings

Problem Statement:
You are given a list of strings `words`. Each string consists of lowercase English letters only. 
Two strings `s1` and `s2` are said to be connected if the set of characters of `s1` can be 
transformed into the set of characters of `s2` by adding or removing a single character.

For example:
- "abc" and "ab" are connected because you can remove 'c' from "abc" to get "ab".
- "abc" and "abd" are not connected because you need to change two characters.

A group of strings is a subset of strings in which any two strings are connected directly or indirectly. 
Two strings are indirectly connected if there is a string that is directly connected to both of them.

Return an array `answer` of size 2 where:
- `answer[0]` is the number of groups of strings in `words`.
- `answer[1]` is the size of the largest group.

Constraints:
- 1 <= words.length <= 2 * 10^4
- 1 <= words[i].length <= 26
- words[i] consists of lowercase English letters only.
"""

from collections import defaultdict

def groupStrings(words):
    def word_to_bitmask(word):
        """Convert a word to its bitmask representation."""
        bitmask = 0
        for char in word:
            bitmask |= 1 << (ord(char) - ord('a'))
        return bitmask

    def find(x):
        """Find the root of x in the union-find structure."""
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        """Union two sets in the union-find structure."""
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x
            size[root_x] += size[root_y]

    # Step 1: Convert words to bitmasks
    bitmask_to_words = defaultdict(list)
    for word in words:
        bitmask = word_to_bitmask(word)
        bitmask_to_words[bitmask].append(word)

    # Step 2: Initialize union-find structure
    parent = {}
    size = {}

    for bitmask in bitmask_to_words:
        parent[bitmask] = bitmask
        size[bitmask] = len(bitmask_to_words[bitmask])

    # Step 3: Union connected components
    for bitmask in bitmask_to_words:
        # Check all possible single-bit additions/removals
        for i in range(26):
            # Remove a bit
            neighbor = bitmask ^ (1 << i)
            if neighbor in parent:
                union(bitmask, neighbor)

            # Add a bit
            if not (bitmask & (1 << i)):
                neighbor = bitmask | (1 << i)
                if neighbor in parent:
                    union(bitmask, neighbor)

    # Step 4: Count groups and find the largest group size
    group_count = 0
    largest_group_size = 0
    seen = set()

    for bitmask in bitmask_to_words:
        root = find(bitmask)
        if root not in seen:
            group_count += 1
            largest_group_size = max(largest_group_size, size[root])
            seen.add(root)

    return [group_count, largest_group_size]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["a", "b", "ab", "abc"]
    print(groupStrings(words1))  # Output: [2, 3]

    # Test Case 2
    words2 = ["a", "ab", "abc", "abcd", "abcde"]
    print(groupStrings(words2))  # Output: [1, 5]

    # Test Case 3
    words3 = ["abc", "def", "ghi", "jkl"]
    print(groupStrings(words3))  # Output: [4, 1]

    # Test Case 4
    words4 = ["a", "b", "c", "d"]
    print(groupStrings(words4))  # Output: [4, 1]

"""
Time Complexity:
- Converting each word to a bitmask: O(n * k), where n is the number of words and k is the average length of a word.
- Union-Find operations: O(n * α(n)), where α(n) is the inverse Ackermann function (very small, nearly constant).
- Checking all single-bit additions/removals: O(n * 26) = O(n).
Overall: O(n * k + n * α(n)) ≈ O(n * k).

Space Complexity:
- Storing bitmasks and union-find structures: O(n).
Overall: O(n).

Topic: Union-Find, Bit Manipulation
"""