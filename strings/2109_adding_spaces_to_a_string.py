"""
LeetCode Question #2109: Adding Spaces to a String

Problem Statement:
You are given a string `s` and an integer array `spaces` that describes the indices in the original string where spaces will be added. 
Each space should be inserted before the character at the given index in the `spaces` array.

For example, given `s = "LeetcodeHelpsMeLearn"` and `spaces = [8, 13, 15]`, the new string will be `"Leetcode Helps Me Learn"`.
Note that the indices in the `spaces` array are strictly increasing, and all values are within the bounds of the string.

Return the resulting string after adding the spaces.

Constraints:
- `1 <= s.length <= 10^5`
- `0 <= spaces.length <= 10^5`
- `0 <= spaces[i] < s.length`
- All values in `spaces` are strictly increasing.

"""

# Python Solution
def addSpaces(s: str, spaces: list[int]) -> str:
    """
    Adds spaces to the string `s` at the indices specified in the `spaces` array.

    :param s: The original string.
    :param spaces: A list of indices where spaces should be added.
    :return: The resulting string after adding spaces.
    """
    result = []
    space_index = 0
    n = len(spaces)
    
    for i, char in enumerate(s):
        # If the current index matches the next space index, add a space
        if space_index < n and i == spaces[space_index]:
            result.append(" ")
            space_index += 1
        result.append(char)
    
    return "".join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "LeetcodeHelpsMeLearn"
    spaces1 = [8, 13, 15]
    print(addSpaces(s1, spaces1))  # Output: "Leetcode Helps Me Learn"

    # Test Case 2
    s2 = "ProgrammingIsFun"
    spaces2 = [11]
    print(addSpaces(s2, spaces2))  # Output: "Programming IsFun"

    # Test Case 3
    s3 = "HelloWorld"
    spaces3 = [5]
    print(addSpaces(s3, spaces3))  # Output: "Hello World"

    # Test Case 4
    s4 = "SingleWord"
    spaces4 = []
    print(addSpaces(s4, spaces4))  # Output: "SingleWord"

    # Test Case 5
    s5 = "ABCD"
    spaces5 = [1, 2, 3]
    print(addSpaces(s5, spaces5))  # Output: "A B C D"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the string `s` once, which takes O(n) time, where `n` is the length of the string.
- The `spaces` array is accessed in constant time during each iteration, so the overall time complexity is O(n).

Space Complexity:
- The function uses a list `result` to store the characters and spaces, which takes O(n) space.
- Therefore, the space complexity is O(n).

Topic: Strings
"""