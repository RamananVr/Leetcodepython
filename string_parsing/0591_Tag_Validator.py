"""
LeetCode Problem #591: Tag Validator

Problem Statement:
A valid XML string consists of tags, content, and proper nesting. The rules for a valid XML string are as follows:

1. The string must start with a "<TAG>" and end with a "</TAG>", where "TAG" is a valid tag name.
2. A valid tag name consists of uppercase letters only, and its length is between 1 and 9 inclusive.
3. The content between the opening and closing tags can be:
   - Other nested valid tags.
   - Characters other than "<" and ">".
4. "<![CDATA[" and "]]>" are used to define CDATA sections, which can contain any characters except the string "]]>".
5. CDATA sections are treated as content and do not affect the validity of the tags.
6. Tags must be properly nested and closed.

Write a function `isValid(code: str) -> bool` that determines whether the given string `code` is a valid XML string.

Constraints:
- The input string `code` has a length between 1 and 5000.

"""

def isValid(code: str) -> bool:
    def is_valid_tag_name(tag_name):
        return 1 <= len(tag_name) <= 9 and tag_name.isupper()

    stack = []
    i = 0
    n = len(code)

    while i < n:
        if code[i] == '<':
            if i + 1 < n and code[i + 1] == '/':  # Closing tag
                j = code.find('>', i)
                if j == -1:
                    return False
                tag_name = code[i + 2:j]
                if not stack or not is_valid_tag_name(tag_name) or stack[-1] != tag_name:
                    return False
                stack.pop()
                i = j + 1
                if not stack and i != n:  # Extra content after root tag
                    return False
            elif i + 8 < n and code[i + 1:i + 9] == '![CDATA[':  # CDATA section
                j = code.find(']]>', i)
                if j == -1:
                    return False
                i = j + 3
            else:  # Opening tag
                j = code.find('>', i)
                if j == -1:
                    return False
                tag_name = code[i + 1:j]
                if not is_valid_tag_name(tag_name):
                    return False
                stack.append(tag_name)
                i = j + 1
        else:
            if not stack:  # Content outside of root tag
                return False
            i += 1

    return not stack


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Valid XML string
    code1 = "<A><B><![CDATA[content]]></B></A>"
    print(isValid(code1))  # Expected output: True

    # Test Case 2: Invalid XML string (extra content after root tag)
    code2 = "<A><B></B></A>extra"
    print(isValid(code2))  # Expected output: False

    # Test Case 3: Invalid XML string (invalid tag name)
    code3 = "<A><123></123></A>"
    print(isValid(code3))  # Expected output: False

    # Test Case 4: Valid XML string with nested tags
    code4 = "<A><B><C></C></B></A>"
    print(isValid(code4))  # Expected output: True

    # Test Case 5: Invalid XML string (unclosed tag)
    code5 = "<A><B></A>"
    print(isValid(code5))  # Expected output: False

    # Test Case 6: Valid XML string with CDATA section
    code6 = "<A><![CDATA[<not a tag>]]></A>"
    print(isValid(code6))  # Expected output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the input string `code` once, performing operations like `find` and `isupper` on substrings.
- The `find` operation is O(n) in the worst case, but since the input is processed sequentially, the overall complexity is O(n).

Space Complexity:
- The stack used to store open tags has a maximum size proportional to the nesting depth of the tags, which is O(d), where `d` is the depth of nesting.
- In the worst case, the stack size is O(n) if all tags are nested.

Overall:
Time Complexity: O(n)
Space Complexity: O(n)

Topic: String Parsing
"""