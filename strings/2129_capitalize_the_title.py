"""
LeetCode Question #2129: Capitalize the Title

Problem Statement:
You are given a string `title` consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:
- If the length of the word is 1 or 2 letters, change all letters to lowercase.
- Otherwise, change the first letter to uppercase and the remaining letters to lowercase.

Return the capitalized `title`.

Example 1:
Input: title = "capiTalIze tHe titLe"
Output: "Capitalize The Title"

Example 2:
Input: title = "First leTTeR of EACH Word"
Output: "First Letter of Each Word"

Example 3:
Input: title = "i lOve leetcode"
Output: "i Love Leetcode"

Constraints:
- 1 <= title.length <= 100
- title consists of words separated by a single space with no leading or trailing spaces.
- Each word consists of uppercase and lowercase English letters and is non-empty.
"""

# Solution
def capitalizeTitle(title: str) -> str:
    """
    Capitalizes the title according to the rules:
    - Words with length 1 or 2 are converted to lowercase.
    - Words with length greater than 2 are capitalized (first letter uppercase, rest lowercase).
    """
    words = title.split()
    result = []
    
    for word in words:
        if len(word) <= 2:
            result.append(word.lower())
        else:
            result.append(word[0].upper() + word[1:].lower())
    
    return " ".join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    title1 = "capiTalIze tHe titLe"
    print(capitalizeTitle(title1))  # Output: "Capitalize The Title"

    # Test Case 2
    title2 = "First leTTeR of EACH Word"
    print(capitalizeTitle(title2))  # Output: "First Letter of Each Word"

    # Test Case 3
    title3 = "i lOve leetcode"
    print(capitalizeTitle(title3))  # Output: "i Love Leetcode"

    # Test Case 4 (Edge Case: Single word with length <= 2)
    title4 = "a"
    print(capitalizeTitle(title4))  # Output: "a"

    # Test Case 5 (Edge Case: Single word with length > 2)
    title5 = "hello"
    print(capitalizeTitle(title5))  # Output: "Hello"

    # Test Case 6 (Edge Case: All words are short)
    title6 = "a b c d e"
    print(capitalizeTitle(title6))  # Output: "a b c d e"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting the string into words takes O(n), where n is the length of the input string.
- Iterating through each word and processing it takes O(n) in total since each word is processed once.
- Joining the processed words back into a single string also takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- The space required for the `words` list and the `result` list is proportional to the number of words in the input string.
- In the worst case, the space complexity is O(n), where n is the length of the input string.
- Overall space complexity: O(n).
"""

# Topic: Strings