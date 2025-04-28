"""
LeetCode Problem #1327: International Morse Code Decoding

Problem Statement:
You are given a list of strings `words` where each string represents a word in English. Each word can be encoded into Morse code using the following mapping:

    'a' -> ".-", 'b' -> "-...", 'c' -> "-.-.", 'd' -> "-..", 'e' -> ".", 'f' -> "..-.",
    'g' -> "--.", 'h' -> "....", 'i' -> "..", 'j' -> ".---", 'k' -> "-.-", 'l' -> ".-..",
    'm' -> "--", 'n' -> "-.", 'o' -> "---", 'p' -> ".--.", 'q' -> "--.-", 'r' -> ".-.",
    's' -> "...", 't' -> "-", 'u' -> "..-", 'v' -> "...-", 'w' -> ".--", 'x' -> "-..-",
    'y' -> "-.--", 'z' -> "--.."

Write a function `uniqueMorseRepresentations(words)` that returns the number of unique Morse code representations among all the words in the list.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 12
- words[i] consists of lowercase English letters.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word into Morse code is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 unique transformations: "--...-." and "--...--."
"""

# Solution
def uniqueMorseRepresentations(words):
    # Define the Morse code mapping for each letter
    morse_map = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."
    ]
    
    # Create a dictionary to map letters to Morse code
    letter_to_morse = {chr(i + ord('a')): morse_map[i] for i in range(26)}
    
    # Transform each word into its Morse code representation
    morse_transformations = set()
    for word in words:
        morse_code = ''.join(letter_to_morse[char] for char in word)
        morse_transformations.add(morse_code)
    
    # Return the number of unique Morse code representations
    return len(morse_transformations)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["gin", "zen", "gig", "msg"]
    print(uniqueMorseRepresentations(words1))  # Output: 2

    # Test Case 2
    words2 = ["a", "b", "c", "d"]
    print(uniqueMorseRepresentations(words2))  # Output: 4

    # Test Case 3
    words3 = ["hello", "world", "hello", "leet"]
    print(uniqueMorseRepresentations(words3))  # Output: 3

    # Test Case 4
    words4 = ["abc", "def", "ghi", "jkl"]
    print(uniqueMorseRepresentations(words4))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the `letter_to_morse` dictionary takes O(26) = O(1) since there are 26 letters in the English alphabet.
- For each word in the list `words`, we iterate through its characters to construct the Morse code representation. 
  This takes O(L) time per word, where L is the average length of a word.
- Since there are N words in the list, the total time complexity is O(N * L).

Space Complexity:
- The `letter_to_morse` dictionary takes O(26) = O(1) space.
- The `morse_transformations` set stores unique Morse code representations, which in the worst case can be equal to the number of words (N). 
  Thus, the space complexity is O(N).
"""

# Topic: Hashing, Strings