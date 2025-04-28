"""
LeetCode Question #1592: Rearrange Spaces Between Words

Problem Statement:
You are given a string `text` of words that are separated by spaces. 
The string contains at least one word. Return a string of the words in the same order, 
but with exactly one space between each pair of adjacent words and all extra spaces at the end of the result.

Input:
- `text` consists of English letters and spaces.
- There is at least one word in `text`.

Output:
- Return the rearranged string as described.

Example:
Input: text = "  this   is  a sentence "
Output: "this   is   a   sentence"

Constraints:
- 1 <= text.length <= 100
- text consists of lowercase English letters and spaces.
- text contains at least one word.
"""

def reorderSpaces(text: str) -> str:
    # Count the total number of spaces in the input string
    total_spaces = text.count(' ')
    
    # Split the text into words (ignoring extra spaces)
    words = text.split()
    num_words = len(words)
    
    # If there's only one word, all spaces go to the end
    if num_words == 1:
        return words[0] + ' ' * total_spaces
    
    # Calculate spaces between words and remaining spaces
    spaces_between = total_spaces // (num_words - 1)
    extra_spaces = total_spaces % (num_words - 1)
    
    # Join the words with the calculated spaces and add extra spaces at the end
    return (' ' * spaces_between).join(words) + ' ' * extra_spaces

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    text1 = "  this   is  a sentence "
    print(reorderSpaces(text1))  # Output: "this   is   a   sentence"
    
    # Test Case 2
    text2 = " practice   makes   perfect"
    print(reorderSpaces(text2))  # Output: "practice   makes   perfect "
    
    # Test Case 3
    text3 = "hello"
    print(reorderSpaces(text3))  # Output: "hello"
    
    # Test Case 4
    text4 = "  walks  udp package   into  bar a"
    print(reorderSpaces(text4))  # Output: "walks  udp  package  into  bar  a "
    
    # Test Case 5
    text5 = "a"
    print(reorderSpaces(text5))  # Output: "a"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Splitting the string into words using `split()` takes O(n), where n is the length of the input string.
- Counting spaces using `count(' ')` also takes O(n).
- Joining the words with spaces takes O(n) as well.
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(n) due to the storage of the list of words created by `split()`.

Topic: String Manipulation
"""