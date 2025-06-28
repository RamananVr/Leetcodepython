"""
LeetCode Problem 2761: Prime Pairs with Target Sum

You are given an integer n. We say that two integers x and y form a prime number pair if:
- 1 <= x <= y <= n
- x + y == n
- x and y are both prime numbers

Return the 2D array containing prime number pairs [x, y] in non-decreasing order of x. If no prime number pairs at all, then return an empty array.

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Constraints:
- 1 <= n <= 10^6

Example 1:
Input: n = 12
Output: [[5,7]]
Explanation: For n = 12, the only prime pair that sums to 12 is [5,7].

Example 2:
Input: n = 4
Output: []
Explanation: There exists no prime pair that sums to 4.

Topics: Math, Number Theory, Sieve of Eratosthenes
"""

class Solution:
    def findPrimePairs(self, n: int) -> list[list[int]]:
        """
        Approach 1: Sieve of Eratosthenes + Two Pointer
        
        1. Use Sieve of Eratosthenes to find all primes up to n
        2. For each prime p <= n//2, check if n-p is also prime
        3. If both are prime, add [p, n-p] to result
        
        Time: O(n log log n) for sieve + O(n) for checking pairs
        Space: O(n) for sieve array
        """
        if n < 4:
            return []
        
        # Sieve of Eratosthenes to find all primes up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        
        result = []
        # Check pairs where x <= y, so x <= n//2
        for x in range(2, n // 2 + 1):
            y = n - x
            if is_prime[x] and is_prime[y]:
                result.append([x, y])
        
        return result
    
    def findPrimePairs_optimized(self, n: int) -> list[list[int]]:
        """
        Approach 2: Optimized with early termination
        
        Same as approach 1 but with some optimizations:
        - Handle even n separately (only valid pair is [2, n-2])
        - For odd n, only check odd primes after 2
        
        Time: O(n log log n)
        Space: O(n)
        """
        if n < 4:
            return []
        
        # Sieve of Eratosthenes
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        
        result = []
        
        # Special case: if n is even, check if 2 and n-2 are both prime
        if n % 2 == 0:
            if is_prime[2] and is_prime[n - 2]:
                result.append([2, n - 2])
        else:
            # For odd n, both numbers must be odd (except for pair with 2)
            # But 2 + odd = odd, so no valid pairs for odd n with 2
            # Check odd primes
            for x in range(3, n // 2 + 1, 2):
                y = n - x
                if is_prime[x] and is_prime[y]:
                    result.append([x, y])
        
        return result

def test_prime_pairs():
    """Test the prime pairs solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.findPrimePairs(12) == [[5, 7]]
    
    # Test case 2: No prime pairs
    assert solution.findPrimePairs(4) == []
    
    # Test case 3: Small even number
    assert solution.findPrimePairs(6) == [[3, 3]]
    
    # Test case 4: Larger number
    result = solution.findPrimePairs(18)
    expected = [[5, 13], [7, 11]]
    assert result == expected
    
    # Test case 5: Edge cases
    assert solution.findPrimePairs(1) == []
    assert solution.findPrimePairs(2) == []
    assert solution.findPrimePairs(3) == []
    
    # Test case 6: Prime number itself
    assert solution.findPrimePairs(10) == [[3, 7], [5, 5]]
    
    # Test optimized version
    assert solution.findPrimePairs_optimized(12) == [[5, 7]]
    assert solution.findPrimePairs_optimized(18) == [[5, 13], [7, 11]]
    
    print("All prime pairs tests passed!")

if __name__ == "__main__":
    test_prime_pairs()
