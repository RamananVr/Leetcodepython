"""
LeetCode Question #804: Unique Morse Code Words

Problem Statement:
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
'a' maps to ".-", 'b' maps to "-...", 'c' maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:
[".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

Given an array of strings `words` where each word can be written as a concatenation of the Morse code of each letter, return the number of different transformations among all words in the array.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 12
- words[i] consists of lowercase English letters.

"""

# Python Solution
def uniqueMorseRepresentations(words):
    morse_code = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."
    ]
    # Create a mapping of letters to Morse code
    char_to_morse = {chr(i + ord('a')): morse_code[i] for i in range(26)}
    
    # Transform each word into its Morse code representation
    transformations = set()
    for word in words:
        morse_word = ''.join(char_to_morse[char] for char in word)
        transformations.add(morse_word)
    
    # Return the number of unique transformations
    return len(transformations)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["gin", "zen", "gig", "msg"]
    print(uniqueMorseRepresentations(words1))  # Output: 2

    # Test Case 2
    words2 = ["a", "b", "c", "d"]
    print(uniqueMorseRepresentations(words2))  # Output: 4

    # Test Case 3
    words3 = ["hello", "world", "hello"]
    print(uniqueMorseRepresentations(words3))  # Output: 2

    # Test Case 4
    words4 = ["abc", "def", "ghi"]
    print(uniqueMorseRepresentations(words4))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the `char_to_morse` dictionary takes O(26) = O(1) since the alphabet size is fixed.
- For each word in the `words` list, transforming it into Morse code takes O(L), where L is the length of the word.
- If there are N words in the list, the total transformation time is O(N * L), where L is the average length of the words.
- Adding each transformation to the set takes O(1) on average.
- Overall time complexity: O(N * L).

Space Complexity:
- The `char_to_morse` dictionary uses O(26) = O(1) space.
- The `transformations` set stores up to N unique Morse code strings, each of length up to L. This requires O(N * L) space in the worst case.
- Overall space complexity: O(N * L).

Topic: Hashing
"""