"""
LeetCode Problem #443: String Compression

Problem Statement:
Given an array of characters `chars`, compress it using the following algorithm:
- Begin with an empty string `s`. For each group of consecutive repeating characters in `chars`:
  - If the group's length is 1, append the character to `s`.
  - Otherwise, append the character followed by the group's length.
- The compressed string `s` should not be returned directly. Instead, modify the input array `chars` in-place to store the compressed string.
- After modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Constraints:
- `1 <= chars.length <= 2000`
- `chars[i]` is a lowercase English letter, digit, or symbol.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"]
"""

def compress(chars):
    """
    Compresses the input list of characters in-place and returns the new length.

    :param chars: List[str] - The input list of characters
    :return: int - The new length of the compressed list
    """
    write = 0  # Pointer to write the compressed characters
    read = 0   # Pointer to read the characters

    while read < len(chars):
        char = chars[read]
        count = 0

        # Count the occurrences of the current character
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1

        # Write the character
        chars[write] = char
        write += 1

        # Write the count if greater than 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    chars1 = ["a", "a", "b", "b", "c", "c", "c"]
    result1 = compress(chars1)
    print(f"Output: {result1}, Compressed: {chars1[:result1]}")  # Output: 6, Compressed: ["a", "2", "b", "2", "c", "3"]

    # Test Case 2
    chars2 = ["a"]
    result2 = compress(chars2)
    print(f"Output: {result2}, Compressed: {chars2[:result2]}")  # Output: 1, Compressed: ["a"]

    # Test Case 3
    chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    result3 = compress(chars3)
    print(f"Output: {result3}, Compressed: {chars3[:result3]}")  # Output: 4, Compressed: ["a", "b", "1", "2"]

    # Test Case 4
    chars4 = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
    result4 = compress(chars4)
    print(f"Output: {result4}, Compressed: {chars4[:result4]}")  # Output: 3, Compressed: ["a", "1", "3"]

# Time Complexity Analysis:
# The algorithm processes each character in the input array exactly once, so the time complexity is O(n),
# where n is the length of the input array.

# Space Complexity Analysis:
# The algorithm uses only constant extra space (O(1)) since it modifies the input array in-place.

# Topic: Arrays, Two Pointers