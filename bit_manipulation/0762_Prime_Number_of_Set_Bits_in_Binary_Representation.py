"""
LeetCode Problem #762: Prime Number of Set Bits in Binary Representation

Problem Statement:
Given two integers left and right, return the count of numbers in the inclusive range [left, right] 
having a prime number of set bits in their binary representation.

- An integer has a prime number of set bits if the number of 1's in its binary representation is a prime number.
- For example, 21 (in binary 10101) has 3 set bits, and 3 is a prime number.

Constraints:
- 1 <= left <= right <= 10^6
- 0 <= right - left <= 10^4

Example:
Input: left = 6, right = 10
Output: 4
Explanation:
- 6 (110) has 2 set bits (prime).
- 7 (111) has 3 set bits (prime).
- 8 (1000) has 1 set bit (not prime).
- 9 (1001) has 2 set bits (prime).
- 10 (1010) has 2 set bits (prime).
Thus, 4 numbers in the range [6, 10] have a prime number of set bits.
"""

# Python Solution
def countPrimeSetBits(left: int, right: int) -> int:
    def is_prime(n: int) -> bool:
        """Helper function to check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Precompute primes for the range of possible set bits (0 to 20)
    # Since the maximum number of set bits for numbers up to 10^6 is 20 (binary of 10^6 is ~20 bits)
    prime_set = {i for i in range(21) if is_prime(i)}

    count = 0
    for num in range(left, right + 1):
        # Count the number of set bits in the binary representation of num
        set_bits = bin(num).count('1')
        if set_bits in prime_set:
            count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    left = 6
    right = 10
    print(countPrimeSetBits(left, right))  # Output: 4

    # Test Case 2
    left = 10
    right = 15
    print(countPrimeSetBits(left, right))  # Output: 5

    # Test Case 3
    left = 1
    right = 20
    print(countPrimeSetBits(left, right))  # Output: 10

    # Test Case 4
    left = 990
    right = 1000
    print(countPrimeSetBits(left, right))  # Output: 2

"""
Time Complexity Analysis:
- The range of numbers to iterate over is (right - left + 1), which is at most 10^4.
- For each number, we compute the binary representation and count the set bits, which takes O(log(num)) time.
  Since num is at most 10^6, this is O(log(10^6)) = O(20).
- Checking if the number of set bits is in the precomputed prime set is O(1).
- Thus, the overall time complexity is O((right - left + 1) * log(right)).

Space Complexity Analysis:
- The space complexity is O(1) for the prime set (constant size of 21 elements).
- No additional space is used apart from a few variables.

Primary Topic: Bit Manipulation
"""