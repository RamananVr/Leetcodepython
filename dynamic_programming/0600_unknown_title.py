"""
LeetCode Problem #600: Non-negative Integers without Consecutive Ones

Problem Statement:
Given a positive integer n, return the number of non-negative integers less than or equal to n, whose binary representations do NOT contain consecutive ones.

Example 1:
Input: n = 5
Output: 5
Explanation: The numbers less than or equal to 5 are [0, 1, 2, 3, 4, 5]. 
Among them, only 3 (binary: 11) has consecutive ones. So the answer is 5.

Example 2:
Input: n = 1
Output: 2

Example 3:
Input: n = 2
Output: 3

Constraints:
- 1 <= n <= 10^9
"""

def findIntegers(n: int) -> int:
    """
    Function to calculate the number of non-negative integers less than or equal to n
    whose binary representations do not contain consecutive ones.
    """
    # Precompute Fibonacci numbers up to 30 (since n <= 10^9, max binary length is 30)
    fib = [0] * 31
    fib[0], fib[1] = 1, 2
    for i in range(2, 31):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    # Convert n to binary and process each bit
    binary = bin(n)[2:]
    length = len(binary)
    result = 0
    prev_bit = 0
    
    for i in range(length):
        if binary[i] == '1':
            # Add Fibonacci number corresponding to the remaining bits
            result += fib[length - i - 1]
            # Check for consecutive ones
            if prev_bit == 1:
                return result
            prev_bit = 1
        else:
            prev_bit = 0
    
    # Include n itself if it doesn't have consecutive ones
    return result + 1

# Example Test Cases
if __name__ == "__main__":
    print(findIntegers(5))  # Output: 5
    print(findIntegers(1))  # Output: 2
    print(findIntegers(2))  # Output: 3
    print(findIntegers(10)) # Output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function precomputes Fibonacci numbers up to 30, which takes O(30) = O(1) time.
- The binary representation of n is processed in O(log(n)) time, as the length of the binary representation is proportional to log(n).
- Overall, the time complexity is O(log(n)).

Space Complexity:
- The function uses an array to store Fibonacci numbers, which has a fixed size of 31. This requires O(1) space.
- The binary representation of n is stored as a string, which requires O(log(n)) space.
- Overall, the space complexity is O(log(n)).

Topic: Dynamic Programming
"""