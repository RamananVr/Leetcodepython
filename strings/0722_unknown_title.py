"""
LeetCode Problem #722: Remove Comments

Problem Statement:
Given a C++ program, remove the comments from it. The program source code is an array of strings where `source[i]` is the `i-th` line of the code. This represents the source code of the program. 

Comments can appear in two forms:
1. Line comments: Start with `//` and terminate at the end of the line.
2. Block comments: Start with `/*` and end with `*/`. The block comment can span multiple lines and can be nested within the source code.

You need to remove all comments from the source code and return the code as a list of strings. The returned code should preserve the original formatting of the source code (i.e., each line should appear in the same order as in the original source code, and no extra spaces should be added).

Constraints:
- `1 <= source.length <= 100`
- `0 <= source[i].length <= 80`
- `source[i]` consists of printable ASCII characters.

Example 1:
Input:
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a", "   multiline", "   comment for", "   testing */", "a = b + c;", "}"]
Output:
["int main()", "{ ", "int a, b, c;", "a = b + c;", "}"]

Example 2:
Input:
source = ["a/*comment", "line", "more_comment*/b"]
Output:
["ab"]

Follow-up:
Can you implement this in a single pass through the source code?
"""

# Python Solution
def removeComments(source):
    """
    Removes comments from the given source code.

    :param source: List[str] - The source code as a list of strings.
    :return: List[str] - The source code with comments removed.
    """
    result = []
    in_block = False
    buffer = ""

    for line in source:
        i = 0
        while i < len(line):
            if in_block:
                # Check for the end of a block comment
                if line[i:i+2] == "*/":
                    in_block = False
                    i += 2
                else:
                    i += 1
            else:
                # Check for the start of a block comment
                if line[i:i+2] == "/*":
                    in_block = True
                    i += 2
                # Check for the start of a line comment
                elif line[i:i+2] == "//":
                    break
                else:
                    buffer += line[i]
                    i += 1
        # If not in a block comment, add the buffer to the result
        if not in_block and buffer:
            result.append(buffer)
            buffer = ""

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    source1 = [
        "/*Test program */", 
        "int main()", 
        "{ ", 
        "  // variable declaration ", 
        "int a, b, c;", 
        "/* This is a", 
        "   multiline", 
        "   comment for", 
        "   testing */", 
        "a = b + c;", 
        "}"
    ]
    print(removeComments(source1))  # Expected Output: ["int main()", "{ ", "int a, b, c;", "a = b + c;", "}"]

    # Test Case 2
    source2 = ["a/*comment", "line", "more_comment*/b"]
    print(removeComments(source2))  # Expected Output: ["ab"]

    # Test Case 3
    source3 = ["int x = 1; // initialize x", "/* block comment */", "x++;"]
    print(removeComments(source3))  # Expected Output: ["int x = 1;", "x++;"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each character in the source code is processed exactly once.
- Let `n` be the total number of characters across all lines in the source code.
- The time complexity is O(n).

Space Complexity:
- The space used is proportional to the size of the result list and the buffer string.
- The space complexity is O(n), where `n` is the total number of characters in the source code.
"""

# Topic: Strings