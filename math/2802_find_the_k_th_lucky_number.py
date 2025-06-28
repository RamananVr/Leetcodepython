"""
LeetCode Problem 2802: Find The K-th Lucky Number

We define a lucky number as a number that has exactly two distinct prime factors.

For example, 6 = 2 × 3 has exactly two distinct prime factors 2 and 3, so 6 is a lucky number.
Similarly, 30 = 2 × 3 × 5 has three distinct prime factors, so 30 is not a lucky number.

Given an integer k, return the k-th lucky number.

Constraints:
- 1 <= k <= 10^5

Example 1:
Input: k = 1
Output: 6
Explanation: The first lucky number is 6 = 2 × 3.

Example 2:
Input: k = 2
Output: 10
Explanation: The first two lucky numbers are 6 = 2 × 3 and 10 = 2 × 5.

Example 3:
Input: k = 3
Output: 12
Explanation: The first three lucky numbers are 6 = 2 × 3, 10 = 2 × 5, and 12 = 2² × 3.
"""

def kth_lucky_number(k):
    """
    Approach 1: Sieve + Counting Distinct Prime Factors
    
    Use sieve to find all numbers with exactly 2 distinct prime factors.
    
    Time Complexity: O(n log log n) where n is the upper bound
    Space Complexity: O(n)
    """
    # Estimate upper bound - lucky numbers are fairly dense
    # The k-th lucky number is roughly around k * log(k) * constant
    upper_bound = max(100, k * 20)
    
    # Count distinct prime factors for each number
    distinct_prime_count = [0] * (upper_bound + 1)
    
    for i in range(2, upper_bound + 1):
        if distinct_prime_count[i] == 0:  # i is prime
            # Mark all multiples of i
            for j in range(i, upper_bound + 1, i):
                distinct_prime_count[j] += 1
    
    # Find k-th number with exactly 2 distinct prime factors
    count = 0
    for num in range(2, upper_bound + 1):
        if distinct_prime_count[num] == 2:
            count += 1
            if count == k:
                return num
    
    # If not found, increase upper bound and try again
    return kth_lucky_number_heap(k)

def kth_lucky_number_heap(k):
    """
    Approach 2: Min Heap with Prime Generation
    
    Generate lucky numbers using min heap by combining pairs of primes.
    
    Time Complexity: O(k * log k + p²) where p is number of primes needed
    Space Complexity: O(k + p²)
    """
    import heapq
    
    def sieve(n):
        """Generate primes up to n using sieve"""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n + 1, i):
                    is_prime[j] = False
        
        return [i for i in range(2, n + 1) if is_prime[i]]
    
    # Get enough primes
    primes = sieve(1000)
    heap = []
    seen = set()
    
    # Generate numbers with exactly 2 distinct prime factors
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            p1, p2 = primes[i], primes[j]
            
            # Add p1 * p2
            if p1 * p2 not in seen:
                heapq.heappush(heap, p1 * p2)
                seen.add(p1 * p2)
            
            # Add powers: p1^a * p2^b where a,b >= 1
            power1 = p1
            while power1 * p2 <= 10**8:  # reasonable upper bound
                power2 = p2
                while power1 * power2 <= 10**8:
                    if power1 * power2 not in seen:
                        heapq.heappush(heap, power1 * power2)
                        seen.add(power1 * power2)
                    if p1 == p2:
                        break
                    power2 *= p2
                power1 *= p1
    
    # Extract k-th smallest
    for _ in range(k):
        if heap:
            result = heapq.heappop(heap)
    
    return result

def kth_lucky_number_factorization(k):
    """
    Approach 3: Direct Factorization Check
    
    Check each number sequentially for exactly 2 distinct prime factors.
    
    Time Complexity: O(n * sqrt(n)) where n is the k-th lucky number
    Space Complexity: O(1)
    """
    def count_distinct_prime_factors(n):
        """Count distinct prime factors of n"""
        count = 0
        
        # Check for factor of 2
        if n % 2 == 0:
            count += 1
            while n % 2 == 0:
                n //= 2
        
        # Check for odd factors
        i = 3
        while i * i <= n:
            if n % i == 0:
                count += 1
                while n % i == 0:
                    n //= i
            i += 2
        
        # If n is still > 1, then it's a prime
        if n > 1:
            count += 1
        
        return count
    
    count = 0
    num = 2
    
    while count < k:
        if count_distinct_prime_factors(num) == 2:
            count += 1
            if count == k:
                return num
        num += 1
    
    return num

def kth_lucky_number_optimized(k):
    """
    Approach 4: Optimized with Pre-computed Lucky Numbers
    
    Use mathematical properties to generate lucky numbers more efficiently.
    
    Time Complexity: O(k log k)
    Space Complexity: O(k)
    """
    import heapq
    
    def sieve_prime_factors(n):
        """Get smallest prime factor for each number"""
        spf = list(range(n + 1))
        for i in range(2, int(n**0.5) + 1):
            if spf[i] == i:  # i is prime
                for j in range(i * i, n + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        return spf
    
    upper_bound = k * 15  # Heuristic upper bound
    spf = sieve_prime_factors(upper_bound)
    
    lucky_numbers = []
    
    for num in range(6, upper_bound + 1):  # Start from 6 (first lucky number)
        # Count distinct prime factors using spf
        temp = num
        distinct_primes = set()
        
        while temp > 1:
            distinct_primes.add(spf[temp])
            temp //= spf[temp]
        
        if len(distinct_primes) == 2:
            lucky_numbers.append(num)
            if len(lucky_numbers) == k:
                return lucky_numbers[k-1]
    
    return lucky_numbers[k-1] if len(lucky_numbers) >= k else -1

# Test cases
def test_kth_lucky_number():
    test_cases = [
        (1, 6),    # 6 = 2 × 3
        (2, 10),   # 10 = 2 × 5
        (3, 12),   # 12 = 2² × 3
        (4, 14),   # 14 = 2 × 7
        (5, 15),   # 15 = 3 × 5
        (10, 33),  # 10th lucky number
    ]
    
    for k, expected in test_cases:
        result1 = kth_lucky_number(k)
        result2 = kth_lucky_number_factorization(k)
        result3 = kth_lucky_number_optimized(k)
        
        print(f"Input: k={k}")
        print(f"Expected: {expected}")
        print(f"Sieve: {result1}")
        print(f"Factorization: {result2}")
        print(f"Optimized: {result3}")
        print(f"✓ Passed: {result1 == expected and result2 == expected and result3 == expected}\n")

if __name__ == "__main__":
    test_kth_lucky_number()

"""
Topics: Math, Number Theory, Sieve, Prime Factorization
Difficulty: Medium

Key Insights:
1. Lucky numbers have exactly 2 distinct prime factors
2. Can use sieve to precompute prime factor counts
3. Heap approach generates numbers in sorted order
4. Direct factorization works for smaller k values
5. Numbers like p₁ᵃ × p₂ᵇ (a,b ≥ 1) are lucky numbers

Companies: Google, Facebook, Amazon
"""
