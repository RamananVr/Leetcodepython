"""
LeetCode Problem #1410: HTML Entity Parser

Problem Statement:
An HTML entity parser is a special parser that takes HTML code as input and replaces all the entities of the special characters by the characters they represent.

The HTML entity parser will replace the following entities according to the given table:

| Entity | Character |
|--------|-----------|
| &quot; | "         |
| &apos; | '         |
| &amp;  | &         |
| &gt;   | >         |
| &lt;   | <         |
| &frasl;| /         |

Given the input string `text` containing the HTML entities, you are to implement a function `entityParser` that returns the text after replacing the entities by the characters they represent.

Example 1:
Input: text = "&amp; is an HTML entity but &ambassador; is not."
Output: "& is an HTML entity but &ambassador; is not."

Example 2:
Input: text = "and I quote: &quot;...&quot;"
Output: "and I quote: \"...\""

Constraints:
- 1 <= text.length <= 10^5
- The string may contain any possible characters out of the 256 ASCII characters.

"""

def entityParser(text: str) -> str:
    """
    Replaces HTML entities in the input text with their corresponding characters.
    """
    # Dictionary mapping HTML entities to their corresponding characters
    html_entities = {
        "&quot;": '"',
        "&apos;": "'",
        "&amp;": "&",
        "&gt;": ">",
        "&lt;": "<",
        "&frasl;": "/"
    }
    
    # Iterate through the dictionary and replace all occurrences of entities
    for entity, char in html_entities.items():
        text = text.replace(entity, char)
    
    return text

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    text1 = "&amp; is an HTML entity but &ambassador; is not."
    print(entityParser(text1))  # Output: "& is an HTML entity but &ambassador; is not."

    # Test Case 2
    text2 = "and I quote: &quot;...&quot;"
    print(entityParser(text2))  # Output: "and I quote: \"...\""

    # Test Case 3
    text3 = "Stay &lt;strong&gt; and keep learning &frasl; coding!"
    print(entityParser(text3))  # Output: "Stay <strong> and keep learning / coding!"

    # Test Case 4
    text4 = "No entities here!"
    print(entityParser(text4))  # Output: "No entities here!"

    # Test Case 5
    text5 = "&apos;Single quotes&apos; and &quot;double quotes&quot;."
    print(entityParser(text5))  # Output: "'Single quotes' and \"double quotes\"."

"""
Time and Space Complexity Analysis:

Time Complexity:
- Let n be the length of the input string `text`.
- For each HTML entity in the dictionary (constant size, 6 entities), we perform a `replace` operation.
- Each `replace` operation scans the string, which takes O(n) time.
- Since there are 6 entities, the total time complexity is O(6 * n) = O(n).

Space Complexity:
- The space complexity is O(1) additional space, as we are modifying the string in place and not using any extra data structures proportional to the input size.

Topic: String Manipulation
"""