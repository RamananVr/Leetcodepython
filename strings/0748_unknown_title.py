"""
LeetCode Problem #748: Shortest Completing Word

Problem Statement:
Given a string `licensePlate` and an array of strings `words`, find the shortest completing word in `words`.

A completing word is a word that contains all the letters in `licensePlate` (ignoring case and non-alphabetic characters). If a letter appears more than once in `licensePlate`, then it must appear in the word at least as many times. The shortest completing word is a completing word with the smallest length. If there is a tie, return the first one that appears in the array.

Example 1:
Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
Output: "steps"
Explanation: The completing words are "step", "steps", "stripe", and "stepple". The shortest completing word is "steps".

Example 2:
Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
Output: "pest"
Explanation: The completing words are "pest", "stew", and "show". The shortest completing word is "pest".

Constraints:
- `1 <= licensePlate.length <= 7`
- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 15`
- `licensePlate` contains digits, spaces, or letters (uppercase or lowercase).
- `words[i]` consists of lowercase English letters.

"""

from collections import Counter

def shortestCompletingWord(licensePlate: str, words: list[str]) -> str:
    # Extract only alphabetic characters from licensePlate and convert to lowercase
    license_count = Counter(char.lower() for char in licensePlate if char.isalpha())
    
    # Initialize the result with a placeholder for the shortest word
    shortest_word = None
    
    for word in words:
        word_count = Counter(word)
        # Check if the word contains all the required characters with sufficient frequency
        if all(word_count[char] >= license_count[char] for char in license_count):
            # Update the shortest word if it's shorter than the current shortest
            if shortest_word is None or len(word) < len(shortest_word):
                shortest_word = word
    
    return shortest_word

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    licensePlate1 = "1s3 PSt"
    words1 = ["step", "steps", "stripe", "stepple"]
    print(shortestCompletingWord(licensePlate1, words1))  # Output: "steps"

    # Test Case 2
    licensePlate2 = "1s3 456"
    words2 = ["looks", "pest", "stew", "show"]
    print(shortestCompletingWord(licensePlate2, words2))  # Output: "pest"

    # Test Case 3
    licensePlate3 = "Ah71752"
    words3 = ["suggest", "letter", "of", "husband", "easy", "education", "drug", "prevent", "writer"]
    print(shortestCompletingWord(licensePlate3, words3))  # Output: "husband"

    # Test Case 4
    licensePlate4 = "OgEu755"
    words4 = ["enough", "these", "play", "wide", "wonder", "box", "arrive", "money", "tax", "thus"]
    print(shortestCompletingWord(licensePlate4, words4))  # Output: "enough"

    # Test Case 5
    licensePlate5 = "iMSlpe4"
    words5 = ["claim", "consumer", "student", "camera", "public", "never", "wonder", "simple", "thought", "use"]
    print(shortestCompletingWord(licensePlate5, words5))  # Output: "simple"

"""
Time Complexity Analysis:
- Extracting alphabetic characters from `licensePlate` and creating the `Counter` takes O(L), where L is the length of `licensePlate`.
- For each word in `words`, creating a `Counter` takes O(W), where W is the average length of a word.
- Checking if a word satisfies the condition takes O(26) = O(1) since there are at most 26 letters in the alphabet.
- Overall, the time complexity is O(L + N * W), where N is the number of words in `words`.

Space Complexity Analysis:
- The space complexity is O(26) = O(1) for the `Counter` objects since there are at most 26 letters in the alphabet.
- Additional space is used for the input `words` and `licensePlate`, but this is not considered extra space.

Topic: Strings
"""