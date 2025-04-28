"""
LeetCode Problem #1702: Maximum Binary String After Change

Problem Statement:
You are given a binary string `binary` consisting only of '0's and '1's. You can perform the following operation any number of times:

- Choose two adjacent indices i and j, where binary[i] == '0' and binary[j] == '1'.
- Set binary[i] = '1' and binary[j] = '0'.

Return the string after making all the moves. It can be shown that the string can always be transformed into a string with a single '0' (if any) and all '1's.

Constraints:
- 1 <= binary.length <= 10^5
- binary[i] is either '0' or '1'.
"""

def maximumBinaryString(binary: str) -> str:
    """
    This function transforms the given binary string into the lexicographically largest binary string
    by performing the allowed operations.
    """
    # Count the number of leading '1's
    n = len(binary)
    first_zero = binary.find('0')
    
    # If there are no '0's or the string is all '1's, return the original string
    if first_zero == -1:
        return binary
    
    # Count the total number of '0's in the string
    zero_count = binary.count('0')
    
    # The result will have all '1's except for one '0' at the correct position
    # The position of the single '0' will be at `first_zero + zero_count - 1`
    result = ['1'] * n
    result[first_zero + zero_count - 1] = '0'
    
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    binary = "000110"
    print(maximumBinaryString(binary))  # Expected Output: "111011"

    # Test Case 2
    binary = "01"
    print(maximumBinaryString(binary))  # Expected Output: "10"

    # Test Case 3
    binary = "111"
    print(maximumBinaryString(binary))  # Expected Output: "111"

    # Test Case 4
    binary = "0000"
    print(maximumBinaryString(binary))  # Expected Output: "1110"

    # Test Case 5
    binary = "100101"
    print(maximumBinaryString(binary))  # Expected Output: "111110"

"""
Time Complexity Analysis:
- Finding the first '0' using `binary.find('0')` takes O(n) time.
- Counting the number of '0's using `binary.count('0')` also takes O(n) time.
- Constructing the result string takes O(n) time.
- Overall, the time complexity is O(n).

Space Complexity Analysis:
- The space complexity is O(n) due to the creation of the `result` list.

Topic: Strings, Greedy
"""