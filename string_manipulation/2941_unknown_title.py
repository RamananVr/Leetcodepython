"""
LeetCode Problem #2941: Decode the Slashes

Problem Statement:
You are given a string `command` that consists of an encoded sequence of commands. The string is encoded using the following rules:
1. `"G"` represents the command "G".
2. `"()"` represents the command "o".
3. `"(al)"` represents the command "al".

Your task is to decode the string `command` and return the decoded string.

Example:
Input: command = "G()(al)"
Output: "Goal"

Constraints:
- 1 <= command.length <= 100
- The string `command` consists of "G", "()", and/or "(al)" in some order.
"""

# Solution
def interpret(command: str) -> str:
    """
    Decodes the given command string based on the rules provided.

    Args:
    command (str): The encoded command string.

    Returns:
    str: The decoded command string.
    """
    return command.replace("()", "o").replace("(al)", "al")

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    command = "G()(al)"
    print(interpret(command))  # Output: "Goal"

    # Test Case 2
    command = "G()()()()(al)"
    print(interpret(command))  # Output: "Gooooal"

    # Test Case 3
    command = "(al)G(al)()()G"
    print(interpret(command))  # Output: "alGalooG"

    # Test Case 4
    command = "G"
    print(interpret(command))  # Output: "G"

    # Test Case 5
    command = "()"
    print(interpret(command))  # Output: "o"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The `replace` method is called twice on the input string. Each call to `replace` has a time complexity of O(n), where n is the length of the string.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The `replace` method creates a new string each time it is called, but no additional data structures are used.
- The space complexity is O(n), where n is the length of the input string.

Overall:
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Topic: String Manipulation