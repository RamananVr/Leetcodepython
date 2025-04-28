"""
LeetCode Problem #2048: Next Greater Numerically Balanced Number

Problem Statement:
A numerically balanced number is a positive integer where, for every digit d that appears in the number, 
there are exactly d occurrences of that digit in the number. For example:
- 1210 is a numerically balanced number because it contains one '1', two '2's, and zero '0's.
- 22 is not numerically balanced because there are two '2's but there is no '0'.

Given an integer n, find the smallest numerically balanced number strictly greater than n.

Constraints:
- 0 <= n <= 10^6
"""

def nextBeautifulNumber(n: int) -> int:
    """
    Finds the smallest numerically balanced number strictly greater than n.
    """
    def is_balanced(num: int) -> bool:
        """
        Helper function to check if a number is numerically balanced.
        """
        from collections import Counter
        count = Counter(str(num))
        for digit, freq in count.items():
            if int(digit) != freq:
                return False
        return True

    # Start searching from n + 1
    num = n + 1
    while True:
        if is_balanced(num):
            return num
        num += 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 1
    print(nextBeautifulNumber(n1))  # Output: 22

    # Test Case 2
    n2 = 1000
    print(nextBeautifulNumber(n2))  # Output: 1221

    # Test Case 3
    n3 = 3000
    print(nextBeautifulNumber(n3))  # Output: 3133

    # Test Case 4
    n4 = 0
    print(nextBeautifulNumber(n4))  # Output: 1

    # Test Case 5
    n5 = 21
    print(nextBeautifulNumber(n5))  # Output: 22

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The function `is_balanced` checks if a number is numerically balanced by counting the frequency of digits.
     This operation takes O(d), where d is the number of digits in the number.
   - In the worst case, we may need to check multiple numbers until we find the next numerically balanced number.
     The number of checks depends on the gap between n and the next balanced number.
   - Let m be the next balanced number after n. The number of digits in m is approximately O(log10(m)).
   - Therefore, the overall time complexity is O((m - n) * log10(m)) in the worst case.

2. Space Complexity:
   - The space complexity is O(d) due to the `Counter` object used to store digit frequencies, where d is the number of digits in the current number being checked.
   - Since d is small (at most 7 for numbers up to 10^6), the space complexity is effectively O(1).

Topic: Brute Force, String Manipulation
"""