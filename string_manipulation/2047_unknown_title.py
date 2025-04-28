"""
LeetCode Problem #2047: Number of Valid Words in a Sentence

A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', ','), and spaces (' '). 
Each sentence can be broken down into one or more tokens separated by spaces. A token is a valid word if:
1. It only contains lowercase letters, hyphens, and/or punctuation (no digits).
2. There is at most one hyphen ('-'). If present, it must be surrounded by lowercase letters (i.e., not at the start or end of the token).
3. There is at most one punctuation mark ('!', '.', ','). If present, it must be at the end of the token.

Implement a function `countValidWords(sentence)` that takes a string `sentence` and returns the number of valid words in the sentence.

Constraints:
- 1 <= sentence.length <= 1000
- sentence consists of lowercase English letters, digits, ' ', '-', '!', '.', ','.
"""

def countValidWords(sentence: str) -> int:
    def is_valid_token(token: str) -> bool:
        # Check for digits
        if any(char.isdigit() for char in token):
            return False
        
        # Check for hyphens
        if token.count('-') > 1:
            return False
        if '-' in token:
            hyphen_index = token.index('-')
            # Hyphen must be surrounded by lowercase letters
            if hyphen_index == 0 or hyphen_index == len(token) - 1:
                return False
            if not (token[hyphen_index - 1].isalpha() and token[hyphen_index + 1].isalpha()):
                return False
        
        # Check for punctuation
        punctuation_marks = {'!', '.', ','}
        if sum(token.count(p) for p in punctuation_marks) > 1:
            return False
        if any(token.endswith(p) for p in punctuation_marks):
            # Punctuation must be at the end
            if not token[-1] in punctuation_marks:
                return False
        elif any(p in token for p in punctuation_marks):
            return False
        
        return True

    # Split sentence into tokens
    tokens = sentence.split()
    valid_count = sum(1 for token in tokens if is_valid_token(token))
    return valid_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sentence1 = "cat and  dog"
    print(countValidWords(sentence1))  # Output: 3

    # Test Case 2
    sentence2 = "!this  1-s b8d!"
    print(countValidWords(sentence2))  # Output: 0

    # Test Case 3
    sentence3 = "alice and  bob are playing stone-game10"
    print(countValidWords(sentence3))  # Output: 5

    # Test Case 4
    sentence4 = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
    print(countValidWords(sentence4))  # Output: 6

    # Test Case 5
    sentence5 = "a-b-c"
    print(countValidWords(sentence5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Splitting the sentence into tokens takes O(n), where n is the length of the sentence.
- For each token, we perform checks for digits, hyphens, and punctuation. Each check is O(k), where k is the length of the token.
- In the worst case, there are O(n) tokens, and each token has O(k) length. Thus, the overall complexity is O(n * k).

Space Complexity:
- The space complexity is O(n) due to the storage of tokens after splitting the sentence.
- Additional space is used for temporary variables during validation, but this is negligible compared to the token storage.

Topic: String Manipulation
"""