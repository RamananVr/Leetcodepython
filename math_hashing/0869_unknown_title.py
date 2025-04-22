"""
LeetCode Problem #869: Reordered Power of 2

Problem Statement:
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can reorder the digits to form a power of 2.

Constraints:
- 1 <= n <= 10^9
"""

# Solution
from collections import Counter

def reorderedPowerOf2(n: int) -> bool:
    """
    Check if the digits of the given number can be reordered to form a power of 2.
    """
    # Generate all possible digit counts for powers of 2 up to 10^9
    power_of_2_digit_counts = {Counter(str(1 << i)) for i in range(31)}
    
    # Check if the digit count of n matches any of the precomputed power of 2 digit counts
    return Counter(str(n)) in power_of_2_digit_counts

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: n = 1
    # Explanation: 1 is a power of 2 (2^0 = 1).
    print(reorderedPowerOf2(1))  # Expected output: True

    # Test Case 2: n = 10
    # Explanation: No reordering of digits of 10 can form a power of 2.
    print(reorderedPowerOf2(10))  # Expected output: False

    # Test Case 3: n = 16
    # Explanation: 16 is a power of 2 (2^4 = 16).
    print(reorderedPowerOf2(16))  # Expected output: True

    # Test Case 4: n = 24
    # Explanation: No reordering of digits of 24 can form a power of 2.
    print(reorderedPowerOf2(24))  # Expected output: False

    # Test Case 5: n = 46
    # Explanation: Reordering digits of 46 can form 64, which is a power of 2 (2^6 = 64).
    print(reorderedPowerOf2(46))  # Expected output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- Generating the digit counts for powers of 2: O(31 * k), where k is the average number of digits in a power of 2 (k <= 10).
- Checking if the digit count of n matches any precomputed digit count: O(k).
- Overall complexity: O(31 * k) ≈ O(1), since 31 is a constant.

Space Complexity:
- The set of digit counts for powers of 2 requires O(31 * k) space, which is constant.
- The Counter object for n requires O(k) space.
- Overall space complexity: O(1), since k is bounded by 10.
"""

# Topic: Math, Hashing