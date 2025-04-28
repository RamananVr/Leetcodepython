"""
LeetCode Question #2325: Decode the Message

Problem Statement:
You are given the strings `key` and `message`, which represent a cipher key and a message that has been encoded using it.

The `key` string consists of lowercase English letters and contains every letter of the English alphabet at least once. Each letter in the `key` is mapped to a unique letter in the English alphabet in order of appearance. The `message` string is encoded using this mapping.

You need to decode the `message` string using the `key` and return the decoded string.

Example:
Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"

Constraints:
1. `key.length == 26`
2. `message.length >= 1`
3. `message` consists of lowercase English letters and spaces.
"""

# Solution
def decodeMessage(key: str, message: str) -> str:
    # Create a mapping from the key to the alphabet
    mapping = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index = 0
    
    # Build the mapping using the key
    for char in key:
        if char.isalpha() and char not in mapping:
            mapping[char] = alphabet[index]
            index += 1
    
    # Decode the message using the mapping
    decoded_message = []
    for char in message:
        if char.isalpha():
            decoded_message.append(mapping[char])
        else:
            decoded_message.append(char)  # Preserve spaces
    
    return ''.join(decoded_message)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    print(decodeMessage(key, message))  # Output: "this is a secret"

    # Test Case 2
    key = "eljuxhpwnyrdgtqkviszcfmabo"
    message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
    print(decodeMessage(key, message))  # Output: "the five boxing wizards jump quickly"

    # Test Case 3
    key = "abcdefghijklmnopqrstuvwxyz"
    message = "abc xyz"
    print(decodeMessage(key, message))  # Output: "abc xyz"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Building the mapping: O(n), where n is the length of the `key` string (26 in this case).
- Decoding the message: O(m), where m is the length of the `message` string.
- Overall: O(n + m), which simplifies to O(m) since n is constant (26).

Space Complexity:
- The mapping dictionary uses O(26) space for storing the key-to-alphabet mapping.
- The decoded_message list uses O(m) space for storing the decoded characters.
- Overall: O(m).
"""

# Topic: Hash Table