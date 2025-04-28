"""
LeetCode Problem #2269: Find the K-Beauty of a Number

Problem Statement:
The k-beauty of an integer num is defined as the number of substrings of num of length k 
that meet the following conditions:
    - The substring is a divisor of num.
    - The substring does not have leading zeros.

Given integers num and k, return the k-beauty of num.

Note:
    - A substring is a contiguous sequence of characters in the string.
    - num is guaranteed to be a positive integer.

Constraints:
    - 1 <= num <= 10^9
    - 1 <= k <= 9
"""

def divisorSubstrings(num: int, k: int) -> int:
    """
    Function to calculate the k-beauty of a number.

    Args:
    num (int): The number whose k-beauty is to be calculated.
    k (int): The length of substrings to consider.

    Returns:
    int: The k-beauty of the number.
    """
    num_str = str(num)
    n = len(num_str)
    k_beauty = 0

    for i in range(n - k + 1):
        substring = num_str[i:i + k]
        substring_int = int(substring)
        if substring_int != 0 and num % substring_int == 0:
            k_beauty += 1

    return k_beauty


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num = 240
    k = 2
    print(divisorSubstrings(num, k))  # Expected Output: 2

    # Test Case 2
    num = 430043
    k = 2
    print(divisorSubstrings(num, k))  # Expected Output: 2

    # Test Case 3
    num = 123456
    k = 3
    print(divisorSubstrings(num, k))  # Expected Output: 0

    # Test Case 4
    num = 11111
    k = 2
    print(divisorSubstrings(num, k))  # Expected Output: 4

    # Test Case 5
    num = 10
    k = 1
    print(divisorSubstrings(num, k))  # Expected Output: 1


"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through all possible substrings of length k in the number `num`.
- If the length of `num` is n, there are (n - k + 1) substrings to check.
- For each substring, we perform a constant-time operation to check divisibility.
- Therefore, the time complexity is O(n), where n is the number of digits in `num`.

Space Complexity:
- The function uses a string representation of the number, which takes O(n) space.
- Other variables (e.g., `substring`, `substring_int`) use constant space.
- Therefore, the space complexity is O(n), where n is the number of digits in `num`.

Topic: Strings
"""