"""
LeetCode Problem #1720: Decode XORed Array

Problem Statement:
There is a hidden integer array `arr` that consists of `n` non-negative integers.

It was encoded into another integer array `encoded` of length `n - 1`, such that `encoded[i] = arr[i] XOR arr[i + 1]`. 
For example, if `arr = [1, 0, 2, 1]`, then `encoded = [1, 2, 3]`.

You are given the `encoded` array and an integer `first`, which is the first element of `arr`. 
Return the original array `arr`. It can be proven that the answer exists and is unique.

Constraints:
- `2 <= encoded.length + 1 <= 10^4`
- `0 <= encoded[i] <= 10^5`
- `0 <= first <= 10^5`
"""

# Solution
def decode(encoded, first):
    """
    Decodes the XORed array to retrieve the original array.

    Args:
    encoded (List[int]): The encoded array.
    first (int): The first element of the original array.

    Returns:
    List[int]: The original array.
    """
    arr = [first]  # Initialize the original array with the first element
    for num in encoded:
        arr.append(arr[-1] ^ num)  # XOR the last element of arr with the current encoded value
    return arr

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    encoded = [1, 2, 3]
    first = 1
    print(decode(encoded, first))  # Output: [1, 0, 2, 1]

    # Test Case 2
    encoded = [6, 2, 7, 3]
    first = 4
    print(decode(encoded, first))  # Output: [4, 2, 0, 7, 4]

    # Test Case 3
    encoded = [5]
    first = 10
    print(decode(encoded, first))  # Output: [10, 15]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `encoded` array once, performing a constant-time XOR operation for each element.
- Therefore, the time complexity is O(n), where n is the length of the `encoded` array.

Space Complexity:
- The function uses a list `arr` to store the original array, which has a size of n + 1 (length of `encoded` + 1).
- No additional space is used apart from the output array.
- Therefore, the space complexity is O(n).
"""

# Topic: Arrays