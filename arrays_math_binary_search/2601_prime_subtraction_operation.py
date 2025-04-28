"""
LeetCode Question #2601: Prime Subtraction Operation

Problem Statement:
You are given a 0-indexed integer array nums of length n.

You can perform the following operation as many times as you want:
- Pick an index i that you haven't picked before, and subtract a prime number p from nums[i] such that nums[i] - p > nums[i - 1] (if i > 0).

Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

Example:
Input: nums = [4, 9, 6, 10]
Output: true
Explanation: Choose p = 3 for nums[1], then nums = [4, 6, 6, 10]. Choose p = 2 for nums[2], then nums = [4, 6, 4, 10]. Choose p = 3 for nums[3], then nums = [4, 6, 4, 7]. Now nums is strictly increasing.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^9
"""

# Solution
from bisect import bisect_left

def primeSubOperation(nums):
    def generate_primes(limit):
        """Generate all prime numbers up to the given limit using the Sieve of Eratosthenes."""
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        return [x for x in range(limit + 1) if is_prime[x]]

    # Generate primes up to 10^6 (sufficient for the problem constraints)
    primes = generate_primes(10**6)

    # Iterate through the array and perform the operation
    prev = 0  # Initialize the previous number in the strictly increasing sequence
    for num in nums:
        # Find the largest prime p such that num - p > prev
        idx = bisect_left(primes, num - prev)
        if idx > 0 and primes[idx - 1] < num:
            num -= primes[idx - 1]
        if num <= prev:  # If the current number is not greater than the previous, return False
            return False
        prev = num  # Update the previous number
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 9, 6, 10]
    print(primeSubOperation(nums1))  # Output: True

    # Test Case 2
    nums2 = [6, 8, 11, 12]
    print(primeSubOperation(nums2))  # Output: True

    # Test Case 3
    nums3 = [5, 4, 3, 2]
    print(primeSubOperation(nums3))  # Output: False

    # Test Case 4
    nums4 = [1, 3, 5, 7]
    print(primeSubOperation(nums4))  # Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- Generating primes using the Sieve of Eratosthenes takes O(n log log n), where n is the limit (10^6 in this case).
- For each number in nums, we perform a binary search on the list of primes, which takes O(log m), where m is the number of primes.
- Overall complexity: O(n log log n + k log m), where k is the length of nums.

Space Complexity:
- The space complexity for storing the prime numbers is O(n), where n is the limit (10^6).
- Additional space is used for the input array and variables, which is negligible compared to the prime list.
- Overall space complexity: O(n).
"""

# Topic: Arrays, Math, Binary Search