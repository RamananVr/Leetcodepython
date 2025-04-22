"""
LeetCode Question #717: 1-bit and 2-bit Characters

Problem Statement:
We have two special characters:
- The first character can be represented by a single bit `0`.
- The second character can be represented by two bits (`10` or `11`).

Given a binary array `bits` where the last character is always a `0`, determine if the last character is a one-bit character or not.

Return `True` if the last character is a one-bit character, otherwise return `False`.

Example 1:
Input: bits = [1, 0, 0]
Output: True
Explanation: The only way to decode it is [10, 0]. So the last character is a one-bit character.

Example 2:
Input: bits = [1, 1, 1, 0]
Output: False
Explanation: The only way to decode it is [11, 10]. So the last character is not a one-bit character.

Constraints:
- `1 <= bits.length <= 1000`
- `bits[i] is either 0 or 1`.
"""

def isOneBitCharacter(bits):
    """
    Determines if the last character in the binary array `bits` is a one-bit character.

    :param bits: List[int] - A binary array where the last character is always 0.
    :return: bool - True if the last character is a one-bit character, False otherwise.
    """
    n = len(bits)
    i = 0

    # Traverse the array
    while i < n - 1:
        # If the current bit is 1, skip the next bit (2-bit character)
        if bits[i] == 1:
            i += 2
        else:
            # If the current bit is 0, move to the next bit (1-bit character)
            i += 1

    # If we end at the last bit, it is a one-bit character
    return i == n - 1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    bits1 = [1, 0, 0]
    print(isOneBitCharacter(bits1))  # Output: True

    # Test Case 2
    bits2 = [1, 1, 1, 0]
    print(isOneBitCharacter(bits2))  # Output: False

    # Test Case 3
    bits3 = [0]
    print(isOneBitCharacter(bits3))  # Output: True

    # Test Case 4
    bits4 = [1, 0]
    print(isOneBitCharacter(bits4))  # Output: True

    # Test Case 5
    bits5 = [1, 1, 0, 0]
    print(isOneBitCharacter(bits5))  # Output: True


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the array once, so the time complexity is O(n), where n is the length of the `bits` array.

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""