"""
LeetCode Question #833: Find And Replace in String

Problem Statement:
You are given a 0-indexed string `s` and two 0-indexed arrays `indices` and `sources` and `targets` of the same length.

You need to perform `n` replacement operations on `s`. Each replacement operation is given by three values:
- `indices[i]`: the starting index of the substring in `s` that we want to replace.
- `sources[i]`: the substring we want to match in `s` starting from `indices[i]`.
- `targets[i]`: the string to replace the matched substring.

The replacement operation is applied only if the substring `sources[i]` matches the substring in `s` starting from `indices[i]`. If it does not match, no replacement is done.

For example, if `s = "abcd"`, `indices = [0, 2]`, `sources = ["a", "cd"]`, and `targets = ["eee", "ffff"]`, then:
- "a" matches the substring starting at index 0, so it is replaced by "eee".
- "cd" matches the substring starting at index 2, so it is replaced by "ffff".

Thus, the resulting string will be "eeebffff".

Return the resulting string after applying all the replacement operations. The replacement operations should be applied in such a way that the higher indices are considered first. In other words, the replacements should not affect the indices of earlier replacements.

Constraints:
1. `1 <= s.length <= 1000`
2. `n == indices.length == sources.length == targets.length`
3. `1 <= n <= 100`
4. `0 <= indices[i] < s.length`
5. `1 <= sources[i].length, targets[i].length <= 50`
6. `s` consists of only lowercase English letters.
"""

def findReplaceString(s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
    # Combine indices, sources, and targets into a single list of tuples and sort by indices in descending order
    replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0], reverse=True)
    
    # Convert the string to a list of characters for easier modification
    s_list = list(s)
    
    # Apply replacements
    for index, source, target in replacements:
        # Check if the substring matches the source
        if s[index:index + len(source)] == source:
            # Replace the substring
            s_list[index:index + len(source)] = list(target)
    
    # Join the list back into a string and return
    return ''.join(s_list)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcd"
    indices1 = [0, 2]
    sources1 = ["a", "cd"]
    targets1 = ["eee", "ffff"]
    print(findReplaceString(s1, indices1, sources1, targets1))  # Output: "eeebffff"

    # Test Case 2
    s2 = "abcd"
    indices2 = [0, 2]
    sources2 = ["ab", "ec"]
    targets2 = ["eee", "ffff"]
    print(findReplaceString(s2, indices2, sources2, targets2))  # Output: "abcd"

    # Test Case 3
    s3 = "abcde"
    indices3 = [2, 0]
    sources3 = ["cde", "ab"]
    targets3 = ["xyz", "uv"]
    print(findReplaceString(s3, indices3, sources3, targets3))  # Output: "uvxyz"

    # Test Case 4
    s4 = "hello"
    indices4 = [1, 0]
    sources4 = ["e", "h"]
    targets4 = ["a", "b"]
    print(findReplaceString(s4, indices4, sources4, targets4))  # Output: "ballo"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the replacements list takes O(n log n), where n is the length of the `indices` array.
- For each replacement, we check if the substring matches, which takes O(m) in the worst case, where m is the length of the source string.
- In total, the time complexity is O(n log n + n * m), where n is the number of replacements and m is the average length of the source strings.

Space Complexity:
- The space complexity is O(n + m), where n is the space used for the sorted list of replacements and m is the space used for the modified string as a list.

Topic: Strings
"""