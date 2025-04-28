"""
LeetCode Problem #2996: Encrypt and Decrypt Strings

Problem Statement:
You are tasked with designing a data structure that can encrypt and decrypt strings. The encryption and decryption processes are defined as follows:

1. Encryption:
   - You are given a string `s` and a mapping `encryption_map` where each character in `s` is mapped to a unique string.
   - Replace each character in `s` with its corresponding string from the `encryption_map`.

2. Decryption:
   - You are given an encrypted string `encrypted_s` and a mapping `decryption_map` where each string in the encrypted string is mapped back to its original character.
   - Replace each substring in `encrypted_s` with its corresponding character from the `decryption_map`.

Implement the following methods:
- `encrypt(s: str, encryption_map: Dict[str, str]) -> str`: Encrypts the string `s` using the `encryption_map`.
- `decrypt(encrypted_s: str, decryption_map: Dict[str, str]) -> str`: Decrypts the string `encrypted_s` using the `decryption_map`.

Constraints:
- The input string `s` consists of lowercase English letters.
- The `encryption_map` and `decryption_map` are valid and consistent.
- The length of the encrypted string will not exceed 10^4.

Example:
Input:
    encryption_map = {'a': '1', 'b': '2', 'c': '3'}
    decryption_map = {'1': 'a', '2': 'b', '3': 'c'}
    s = "abc"
    encrypted_s = "123"

Output:
    encrypt(s, encryption_map) -> "123"
    decrypt(encrypted_s, decryption_map) -> "abc"
"""

from typing import Dict

class EncryptDecrypt:
    @staticmethod
    def encrypt(s: str, encryption_map: Dict[str, str]) -> str:
        """
        Encrypts the string `s` using the `encryption_map`.
        """
        encrypted = []
        for char in s:
            if char in encryption_map:
                encrypted.append(encryption_map[char])
            else:
                raise ValueError(f"Character '{char}' not found in encryption_map.")
        return ''.join(encrypted)

    @staticmethod
    def decrypt(encrypted_s: str, decryption_map: Dict[str, str]) -> str:
        """
        Decrypts the string `encrypted_s` using the `decryption_map`.
        """
        decrypted = []
        i = 0
        while i < len(encrypted_s):
            found = False
            for key, value in decryption_map.items():
                if encrypted_s.startswith(key, i):
                    decrypted.append(value)
                    i += len(key)
                    found = True
                    break
            if not found:
                raise ValueError(f"Substring starting at index {i} not found in decryption_map.")
        return ''.join(decrypted)

# Example Test Cases
if __name__ == "__main__":
    encryption_map = {'a': '1', 'b': '2', 'c': '3'}
    decryption_map = {'1': 'a', '2': 'b', '3': 'c'}
    
    # Test Case 1
    s = "abc"
    encrypted_s = EncryptDecrypt.encrypt(s, encryption_map)
    print(f"Encrypted '{s}' -> '{encrypted_s}'")  # Output: "123"
    
    # Test Case 2
    decrypted_s = EncryptDecrypt.decrypt(encrypted_s, decryption_map)
    print(f"Decrypted '{encrypted_s}' -> '{decrypted_s}'")  # Output: "abc"
    
    # Test Case 3
    s = "cab"
    encrypted_s = EncryptDecrypt.encrypt(s, encryption_map)
    print(f"Encrypted '{s}' -> '{encrypted_s}'")  # Output: "312"
    
    decrypted_s = EncryptDecrypt.decrypt(encrypted_s, decryption_map)
    print(f"Decrypted '{encrypted_s}' -> '{decrypted_s}'")  # Output: "cab"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Encryption: O(n), where n is the length of the input string `s`. Each character is processed once.
- Decryption: O(m * k), where m is the length of the encrypted string and k is the average length of keys in the decryption_map. For each position in the encrypted string, we may need to check multiple keys.

Space Complexity:
- Encryption: O(n), where n is the length of the encrypted string (output).
- Decryption: O(m), where m is the length of the decrypted string (output).

The space used for the maps is not included in the analysis as they are considered input.
"""

# Topic: Strings, Hash Map