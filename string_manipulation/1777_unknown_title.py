"""
LeetCode Problem #1777: Evaluate the Bracket Pairs of a String

Problem Statement:
You are given a string `s` that contains some bracket pairs, with each pair containing a key. You are also given a `knowledge` list of key-value pairs, where each key is a string and each value is a string.

The bracket pairs in `s` should be evaluated by replacing each key inside the brackets with the corresponding value from the `knowledge` list. If a key does not exist in the `knowledge` list, you should replace it with a question mark ("?").

You are tasked with returning the resulting string after evaluating all the bracket pairs.

Constraints:
1. `1 <= s.length <= 10^5`
2. `0 <= knowledge.length <= 10^5`
3. `knowledge[i].length == 2`
4. `1 <= key.length, value.length <= 10`
5. `s` consists of lowercase English letters, '(', and ')'.
6. Every open bracket '(' in `s` will have a corresponding closing bracket ')'.
7. The input is guaranteed to be valid.

Example:
Input: s = "(name)is(age)yearsold", knowledge = [["name", "bob"], ["age", "two"]]
Output: "bobistwoyearsold"

Input: s = "hi(name)", knowledge = [["a", "b"]]
Output: "hi?"

Input: s = "(a)(a)(a)aaa", knowledge = [["a", "yes"]]
Output: "yesyesyesaaa"
"""

# Solution
def evaluate(s: str, knowledge: list[list[str]]) -> str:
    # Convert the knowledge list into a dictionary for O(1) lookups
    knowledge_dict = {key: value for key, value in knowledge}
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        if s[i] == '(':
            # Start of a key
            j = i + 1
            while j < n and s[j] != ')':
                j += 1
            # Extract the key
            key = s[i + 1:j]
            # Append the corresponding value or "?" if the key is not found
            result.append(knowledge_dict.get(key, "?"))
            # Move the pointer past the closing bracket
            i = j + 1
        else:
            # Append regular characters
            result.append(s[i])
            i += 1
    
    # Join the result list into a single string
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "(name)is(age)yearsold"
    knowledge1 = [["name", "bob"], ["age", "two"]]
    print(evaluate(s1, knowledge1))  # Output: "bobistwoyearsold"

    # Test Case 2
    s2 = "hi(name)"
    knowledge2 = [["a", "b"]]
    print(evaluate(s2, knowledge2))  # Output: "hi?"

    # Test Case 3
    s3 = "(a)(a)(a)aaa"
    knowledge3 = [["a", "yes"]]
    print(evaluate(s3, knowledge3))  # Output: "yesyesyesaaa"

    # Test Case 4
    s4 = "no(brackets)here"
    knowledge4 = [["brackets", "content"]]
    print(evaluate(s4, knowledge4))  # Output: "nocontenthere"

    # Test Case 5
    s5 = "(key1)(key2)"
    knowledge5 = [["key1", "value1"], ["key2", "value2"]]
    print(evaluate(s5, knowledge5))  # Output: "value1value2"

# Time and Space Complexity Analysis
# Time Complexity:
# - Constructing the dictionary from the `knowledge` list takes O(k), where k is the length of the `knowledge` list.
# - Iterating through the string `s` takes O(n), where n is the length of the string.
# - Extracting keys and looking them up in the dictionary takes O(1) per key.
# Overall time complexity: O(n + k).

# Space Complexity:
# - The dictionary requires O(k) space to store the key-value pairs.
# - The result list requires O(n) space to store the characters of the resulting string.
# Overall space complexity: O(n + k).

# Topic: String Manipulation