"""
LeetCode Problem #1554: Strings Differ by One Character

Problem Statement:
Given a list of strings `dict` where all the strings are of the same length, return `True` if there are two strings that differ by exactly one character in the same index, otherwise return `False`.

Example:
Input: dict = ["abcd","acbd", "aacd"]
Output: True
Explanation: Strings "abcd" and "aacd" differ in only the second character.

Constraints:
1. The number of strings in `dict` is in the range [2, 100].
2. The length of each string is in the range [1, 100].
3. All the strings in `dict` are of the same length.
"""

def differ_by_one(dict):
    """
    Function to determine if there are two strings in the list that differ by exactly one character.

    :param dict: List[str] - List of strings of the same length
    :return: bool - True if two strings differ by exactly one character, False otherwise
    """
    seen = set()
    for word in dict:
        for i in range(len(word)):
            # Create a pattern by replacing the i-th character with a placeholder '*'
            pattern = word[:i] + '*' + word[i+1:]
            if pattern in seen:
                return True
            seen.add(pattern)
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    dict1 = ["abcd", "acbd", "aacd"]
    print(differ_by_one(dict1))  # Output: True

    # Test Case 2
    dict2 = ["abcd", "abcd", "abcd"]
    print(differ_by_one(dict2))  # Output: False

    # Test Case 3
    dict3 = ["abc", "bbc", "acc"]
    print(differ_by_one(dict3))  # Output: True

    # Test Case 4
    dict4 = ["abc", "def", "ghi"]
    print(differ_by_one(dict4))  # Output: False

    # Test Case 5
    dict5 = ["a", "b"]
    print(differ_by_one(dict5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- Let n be the number of strings in the list and m be the length of each string.
- For each string, we generate m patterns (one for each character replaced by '*').
- Checking and adding a pattern to the set is O(1) on average.
- Therefore, the overall time complexity is O(n * m).

Space Complexity:
- We use a set to store the patterns. In the worst case, we store n * m patterns.
- Each pattern has a length of m, so the space complexity is O(n * m).

Topic: Hashing
"""