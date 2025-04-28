"""
LeetCode Problem #2189: Find the K Beauty of a Number

Problem Statement:
The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string 
that meet the following conditions:
1. It has a length of k.
2. It is a divisor of num.

Given integers num and k, return the k-beauty of num.

Notes:
- Leading zeros are allowed in the substrings.
- 0 is not a divisor of any number.

Example:
Input: num = 240, k = 2
Output: 2
Explanation:
The following are the substrings of num of length k:
- "24" from "240": 24 is a divisor of 240.
- "40" from "240": 40 is a divisor of 240.
Therefore, the k-beauty is 2.

Constraints:
- 1 <= num <= 10^9
- 1 <= k <= num.length (the number of digits in num)
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
        divisor = int(substring)
        if divisor != 0 and num % divisor == 0:
            k_beauty += 1

    return k_beauty

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num = 240
    k = 2
    print(divisorSubstrings(num, k))  # Output: 2

    # Test Case 2
    num = 430043
    k = 2
    print(divisorSubstrings(num, k))  # Output: 2

    # Test Case 3
    num = 120
    k = 1
    print(divisorSubstrings(num, k))  # Output: 2

    # Test Case 4
    num = 555
    k = 1
    print(divisorSubstrings(num, k))  # Output: 3

    # Test Case 5
    num = 100000
    k = 3
    print(divisorSubstrings(num, k))  # Output: 0

"""
Time Complexity Analysis:
- Converting the number to a string takes O(d), where d is the number of digits in num.
- The loop iterates (n - k + 1) times, where n is the number of digits in num. For each iteration:
  - Extracting a substring takes O(k).
  - Converting the substring to an integer and performing modulo operation both take O(1).
Thus, the overall time complexity is O(d * k), where d is the number of digits in num.

Space Complexity Analysis:
- The space complexity is O(d) for storing the string representation of num.
- Additional space is used for the substring, which is O(k).
Thus, the overall space complexity is O(d + k).

Topic: Strings, Sliding Window
"""