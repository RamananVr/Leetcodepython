"""
LeetCode Question #271: Encode and Decode Strings

Problem Statement:
Design an algorithm to encode a list of strings to a single string. The encoded string should be able to be decoded back to the original list of strings.

Implement the `Codec` class:
- `Codec()` Initializes the object of the codec.
- `encode(strs: List[str]) -> str`: Encodes a list of strings to a single string.
- `decode(s: str) -> List[str]`: Decodes a single string to a list of strings.

The encoded string is guaranteed to be decodable back to the original list of strings.

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 10^4
- strs[i] consists of any possible characters out of 256 valid ASCII characters.

"""

from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        We use the length of each string followed by a delimiter '#' to encode each string.
        """
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        We parse the encoded string by reading the length of each string and extracting it.
        """
        decoded = []
        i = 0
        while i < len(s):
            # Find the delimiter '#'
            j = s.find('#', i)
            # Extract the length of the string
            length = int(s[i:j])
            # Extract the string using the length
            decoded.append(s[j+1:j+1+length])
            # Move the pointer to the next encoded string
            i = j + 1 + length
        return decoded

# Example Test Cases
if __name__ == "__main__":
    codec = Codec()

    # Test Case 1
    strs = ["hello", "world"]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    print(f"Original: {strs}, Encoded: {encoded}, Decoded: {decoded}")
    assert decoded == strs

    # Test Case 2
    strs = ["", "a", "abc", "123#456"]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    print(f"Original: {strs}, Encoded: {encoded}, Decoded: {decoded}")
    assert decoded == strs

    # Test Case 3
    strs = ["", ""]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    print(f"Original: {strs}, Encoded: {encoded}, Decoded: {decoded}")
    assert decoded == strs

    # Test Case 4
    strs = ["longstring" * 1000, "anotherlongstring" * 500]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    print(f"Original: {strs[:2]}, Encoded: {encoded[:50]}..., Decoded: {decoded[:2]}")
    assert decoded == strs

"""
Time Complexity Analysis:
- Encoding:
  - For each string in the list, we compute its length (O(1)) and append it to the result.
  - Let n = len(strs) and m = total number of characters in all strings combined.
  - Time complexity: O(n + m), where n is the number of strings and m is the total length of all strings.

- Decoding:
  - We iterate through the encoded string, parsing the length and extracting each string.
  - Time complexity: O(m), where m is the total length of the encoded string.

Space Complexity Analysis:
- Encoding:
  - The encoded string requires O(m) space, where m is the total length of all strings.
- Decoding:
  - The decoded list requires O(n + m) space, where n is the number of strings and m is the total length of all strings.

Topic: Strings
"""