"""
LeetCode Problem #824: Goat Latin

Problem Statement:
A sentence `sentence` is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin). The rules of Goat Latin are as follows:

1. If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u', in lowercase or uppercase), append "ma" to the end of the word.
   - For example, the word "apple" becomes "applema".

2. If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
   - For example, the word "goat" becomes "oatgma".

3. Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
   - For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.

Return the final sentence representing the conversion of `sentence` to Goat Latin.

Constraints:
- 1 <= sentence.length <= 150
- sentence consists of English letters and spaces.
- There will be at most one space between two words.
"""

# Solution
def toGoatLatin(sentence: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    words = sentence.split()
    result = []

    for i, word in enumerate(words):
        if word[0] in vowels:
            goat_word = word + "ma"
        else:
            goat_word = word[1:] + word[0] + "ma"
        goat_word += "a" * (i + 1)
        result.append(goat_word)

    return " ".join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sentence1 = "I speak Goat Latin"
    print(toGoatLatin(sentence1))  # Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

    # Test Case 2
    sentence2 = "The quick brown fox jumped over the lazy dog"
    print(toGoatLatin(sentence2))  
    # Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa veroaaaaaaa hetmaaaaaaaaa azylmaaaaaaaaaa ogdmaaaaaaaaaaa"

    # Test Case 3
    sentence3 = "Apple"
    print(toGoatLatin(sentence3))  # Output: "Applema"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting the sentence into words takes O(n), where n is the length of the sentence.
- Iterating through each word and performing operations (checking the first character, appending strings) takes O(k), 
  where k is the total number of characters in all words combined.
- Overall, the time complexity is O(n + k), which simplifies to O(n) since k <= n.

Space Complexity:
- The space required to store the split words is O(n).
- The result list also takes O(n) space.
- Therefore, the overall space complexity is O(n).
"""

# Topic: String Manipulation