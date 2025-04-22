"""
LeetCode Problem #917: Reverse Only Letters

Problem Statement:
Given a string `s`, reverse the string according to the following rules:
1. All the characters that are not English letters remain in the same position.
2. All the English letters (lowercase or uppercase) should be reversed.

Return the reversed string.

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:
- 1 <= s.length <= 100
- `s` consists of characters with ASCII values in the range [33, 122].
- `s` does not contain backslashes.

"""

def reverseOnlyLetters(s: str) -> str:
    """
    Reverse only the letters in the string while keeping non-letter characters in place.
    
    :param s: Input string
    :return: String with letters reversed and non-letters in the same position
    """
    # Extract all the letters from the string
    letters = [char for char in s if char.isalpha()]
    
    # Create a list to store the result
    result = []
    
    # Iterate through the string and replace letters with reversed ones
    for char in s:
        if char.isalpha():
            result.append(letters.pop())  # Pop from the end of the letters list
        else:
            result.append(char)  # Keep non-letters as is
    
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "ab-cd"
    print(reverseOnlyLetters(s1))  # Output: "dc-ba"

    # Test Case 2
    s2 = "a-bC-dEf-ghIj"
    print(reverseOnlyLetters(s2))  # Output: "j-Ih-gfE-dCba"

    # Test Case 3
    s3 = "Test1ng-Leet=code-Q!"
    print(reverseOnlyLetters(s3))  # Output: "Qedo1ct-eeLg=ntse-T!"

    # Test Case 4 (Edge Case: Single letter)
    s4 = "a"
    print(reverseOnlyLetters(s4))  # Output: "a"

    # Test Case 5 (Edge Case: No letters)
    s5 = "123-456!"
    print(reverseOnlyLetters(s5))  # Output: "123-456!"

"""
Time Complexity Analysis:
- Extracting all letters from the string takes O(n), where n is the length of the string.
- Iterating through the string to construct the result also takes O(n).
- Popping from the end of the list of letters is O(1) for each letter.
- Overall, the time complexity is O(n).

Space Complexity Analysis:
- The `letters` list stores only the letters from the string, which can be at most O(n) in size.
- The `result` list also takes O(n) space.
- Therefore, the space complexity is O(n).

Topic: String Manipulation
"""