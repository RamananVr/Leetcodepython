"""
LeetCode Problem #1807: Evaluate the Bracket Pairs of a String

Problem Statement:
You are given a string `s` that contains some bracket pairs, with each pair containing a non-empty key.

- A key is a string consisting of lowercase English letters.
- A bracket pair is written as `(key)` where `key` is the key inside the pair.
- You will be given a dictionary `knowledge` where an entry `(key, value)` means that the key `key` maps to the value `value`.

You need to evaluate all the bracket pairs. When you evaluate a bracket pair `(key)`:
- If `key` exists in `knowledge`, replace `(key)` with the corresponding `value`.
- If `key` does not exist in `knowledge`, replace `(key)` with a question mark `"?"`.

Return the resulting string after evaluating all the bracket pairs.

Constraints:
- `1 <= s.length <= 10^4`
- `0 <= knowledge.length <= 10^4`
- `knowledge[i].length == 2`
- `1 <= key.length, value.length <= 10`
- `s` consists of lowercase English letters and round brackets `'('` and `')'`.
- Every open bracket `'('` in `s` will have a corresponding close bracket `')'`.
- The input `knowledge` is a dictionary with unique keys.

Example:
Input: s = "(name)is(age)yearsold", knowledge = [["name", "bob"], ["age", "two"]]
Output: "bobistwoyearsold"
"""

# Python Solution
def evaluate(s: str, knowledge: list[list[str]]) -> str:
    # Convert knowledge list into a dictionary for fast lookup
    knowledge_dict = {key: value for key, value in knowledge}
    
    result = []
    i = 0
    while i < len(s):
        if s[i] == '(':
            # Find the closing bracket
            j = i + 1
            while j < len(s) and s[j] != ')':
                j += 1
            # Extract the key and replace it with the value or "?"
            key = s[i + 1:j]
            result.append(knowledge_dict.get(key, "?"))
            i = j + 1  # Move past the closing bracket
        else:
            result.append(s[i])
            i += 1
    
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "(name)is(age)yearsold"
    knowledge1 = [["name", "bob"], ["age", "two"]]
    print(evaluate(s1, knowledge1))  # Output: "bobistwoyearsold"

    # Test Case 2
    s2 = "hi(name)"
    knowledge2 = [["name", "alice"]]
    print(evaluate(s2, knowledge2))  # Output: "hialice"

    # Test Case 3
    s3 = "hello(world)"
    knowledge3 = [["planet", "earth"]]
    print(evaluate(s3, knowledge3))  # Output: "hello?"

    # Test Case 4
    s4 = "(a)(b)(c)"
    knowledge4 = [["a", "1"], ["b", "2"], ["c", "3"]]
    print(evaluate(s4, knowledge4))  # Output: "123"

    # Test Case 5
    s5 = "no(brackets)here"
    knowledge5 = [["brackets", "content"]]
    print(evaluate(s5, knowledge5))  # Output: "nocontenthere"

# Time and Space Complexity Analysis
# Time Complexity:
# - Constructing the `knowledge_dict` takes O(K), where K is the length of the `knowledge` list.
# - Iterating through the string `s` takes O(N), where N is the length of `s`.
# - Extracting keys and looking them up in the dictionary takes O(1) per key due to hash table lookup.
# - Overall time complexity: O(N + K).

# Space Complexity:
# - The `knowledge_dict` requires O(K) space.
# - The `result` list requires O(N) space to store the final string.
# - Overall space complexity: O(N + K).

# Topic: String Manipulation