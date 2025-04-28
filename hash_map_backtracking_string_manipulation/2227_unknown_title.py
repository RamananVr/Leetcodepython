"""
LeetCode Problem #2227: Encrypt and Decrypt Strings

Problem Statement:
You are tasked to design a data structure that supports encryption and decryption of strings. The encryption and decryption processes work as follows:

1. Encryption:
   - You are given a string `s` consisting of lowercase English letters only.
   - You are also given a dictionary `keys` where each key is a lowercase English letter and its corresponding value is a string representing the encrypted form of that letter.
   - Replace each letter in `s` with its corresponding encrypted value in `keys` to form the encrypted string.

2. Decryption:
   - You are given an encrypted string `s` and a dictionary `values` where each key is an encrypted string and its corresponding value is the original letter.
   - Replace each encrypted substring in `s` with its corresponding original letter in `values` to form the decrypted string.
   - If there are multiple ways to decrypt the string, return the number of possible original strings.

Implement the `Encrypter` class:
- `Encrypter(keys: List[str], values: List[str], dictionary: List[str])` Initializes the `Encrypter` object with a list of keys, a list of values, and a dictionary of valid words.
- `encrypt(word1: str) -> str` Encrypts the string `word1` using the encryption rules and returns the encrypted string.
- `decrypt(word2: str) -> int` Decrypts the string `word2` and returns the number of possible original strings that match a word in the dictionary.

Constraints:
- `1 <= keys.length == values.length <= 26`
- `1 <= dictionary.length <= 100`
- `1 <= keys[i].length, values[i].length, word1.length, word2.length <= 100`
- `keys[i]` and `values[i]` are unique.
- `dictionary` contains only lowercase English letters.
- All strings in `dictionary` are unique.

"""

from collections import defaultdict
from typing import List

class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        # Map for encryption: letter -> encrypted value
        self.encryption_map = {keys[i]: values[i] for i in range(len(keys))}
        
        # Map for decryption: encrypted value -> list of possible letters
        self.decryption_map = defaultdict(list)
        for i in range(len(keys)):
            self.decryption_map[values[i]].append(keys[i])
        
        # Set of valid words in the dictionary
        self.valid_words = set(dictionary)

    def encrypt(self, word1: str) -> str:
        # Encrypt the word by replacing each character with its encrypted value
        return ''.join(self.encryption_map[char] for char in word1)

    def decrypt(self, word2: str) -> int:
        # Helper function to recursively count valid decryptions
        def dfs(index: int, current: str) -> int:
            if index == len(word2):
                return 1 if current in self.valid_words else 0
            
            # Extract the next encrypted substring
            if index + 2 > len(word2):
                return 0
            encrypted_substring = word2[index:index+2]
            
            # Check if the substring can be decrypted
            if encrypted_substring not in self.decryption_map:
                return 0
            
            # Try all possible letters for this encrypted substring
            count = 0
            for letter in self.decryption_map[encrypted_substring]:
                count += dfs(index + 2, current + letter)
            return count
        
        return dfs(0, "")


# Example Test Cases
if __name__ == "__main__":
    # Initialize the Encrypter
    keys = ["a", "b", "c", "d"]
    values = ["aa", "bb", "cc", "dd"]
    dictionary = ["abcd", "aabb", "abcd"]
    encrypter = Encrypter(keys, values, dictionary)

    # Test encrypt
    print(encrypter.encrypt("abcd"))  # Output: "aabbccdd"
    print(encrypter.encrypt("aabb"))  # Output: "aaaabbbb"

    # Test decrypt
    print(encrypter.decrypt("aabbccdd"))  # Output: 1 (only "abcd" matches)
    print(encrypter.decrypt("aaaabbbb"))  # Output: 0 (no valid words match)

"""
Time and Space Complexity Analysis:

1. Encryption:
   - Time Complexity: O(n), where n is the length of the input string `word1`.
   - Space Complexity: O(1), as we are not using any additional space proportional to the input size.

2. Decryption:
   - Time Complexity: O(2^m * k), where m is the length of the encrypted string `word2` divided by 2 (since each encrypted substring is of length 2), and k is the average number of possible letters for each encrypted substring.
   - Space Complexity: O(m), due to the recursion stack used in the DFS.

3. Initialization:
   - Time Complexity: O(k + d), where k is the number of keys and d is the size of the dictionary.
   - Space Complexity: O(k + d), for storing the encryption map, decryption map, and valid words set.

Topic: Hash Map, Backtracking, String Manipulation
"""