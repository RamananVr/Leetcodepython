"""
LeetCode Problem 2767: Partition String Into Minimum Beautiful Substrings

Given a binary string s, partition s into one or more substrings such that each substring is beautiful.

A string is beautiful if:
- It starts with 1.
- It is a binary representation of a power of 5.

Return the minimum number of substrings in such partition. If no such partition exists, return -1.

A substring is a contiguous sequence of characters in a string.

Constraints:
- 1 <= s.length <= 15
- s[i] is either '0' or '1'.

Example 1:
Input: s = "1011"
Output: 2
Explanation: We can partition s into ["101", "1"].
- "101" is beautiful (5^2 = 25 in binary is "11001", but "101" is 5^1 = 5).
- "1" is beautiful (5^0 = 1 in binary is "1").

Example 2:
Input: s = "111"
Output: 3
Explanation: We can partition s into ["1", "1", "1"].

Example 3:
Input: s = "0"
Output: -1
Explanation: There is no way to partition s.

Topics: String, Dynamic Programming, Backtracking
"""

class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        """
        Approach 1: Dynamic Programming + Precomputed Powers of 5
        
        1. Precompute all powers of 5 that fit in the constraint
        2. Use DP: dp[i] = minimum partitions for s[i:]
        3. For each position, try all possible beautiful substrings
        
        Time: O(n^2) where n = len(s)
        Space: O(n) for DP array
        """
        n = len(s)
        if not s or s[0] == '0':
            return -1
        
        # Precompute powers of 5 in binary (up to 5^6 for constraint n <= 15)
        powers_of_5 = set()
        power = 1
        while len(bin(power)[2:]) <= n:  # Remove '0b' prefix
            powers_of_5.add(bin(power)[2:])
            power *= 5
        
        # DP: dp[i] = minimum partitions for s[i:]
        dp = [float('inf')] * (n + 1)
        dp[n] = 0  # Empty string needs 0 partitions
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                continue  # Can't start with '0'
            
            # Try all possible substrings starting at i
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if substring in powers_of_5:
                    dp[i] = min(dp[i], 1 + dp[j])
        
        return dp[0] if dp[0] != float('inf') else -1
    
    def minimumBeautifulSubstrings_backtrack(self, s: str) -> int:
        """
        Approach 2: Backtracking with memoization
        
        Try all possible ways to partition the string and find minimum.
        
        Time: O(2^n) in worst case, but pruned by memoization
        Space: O(n) for recursion stack and memoization
        """
        n = len(s)
        if not s or s[0] == '0':
            return -1
        
        # Precompute powers of 5
        powers_of_5 = set()
        power = 1
        while len(bin(power)[2:]) <= n:
            powers_of_5.add(bin(power)[2:])
            power *= 5
        
        memo = {}
        
        def backtrack(start):
            if start == n:
                return 0
            
            if start in memo:
                return memo[start]
            
            if s[start] == '0':
                memo[start] = float('inf')
                return float('inf')
            
            min_partitions = float('inf')
            
            # Try all possible substrings starting at 'start'
            for end in range(start + 1, n + 1):
                substring = s[start:end]
                if substring in powers_of_5:
                    result = 1 + backtrack(end)
                    min_partitions = min(min_partitions, result)
            
            memo[start] = min_partitions
            return min_partitions
        
        result = backtrack(0)
        return result if result != float('inf') else -1
    
    def minimumBeautifulSubstrings_bruteforce(self, s: str) -> int:
        """
        Approach 3: Brute force with validation
        
        Generate all possible partitions and check validity.
        
        Time: O(2^n * n) - 2^n partitions, n to validate each
        Space: O(n) for recursion
        """
        n = len(s)
        if not s or s[0] == '0':
            return -1
        
        def is_power_of_5(binary_str):
            """Check if binary string represents a power of 5."""
            if not binary_str or binary_str[0] == '0':
                return False
            
            value = int(binary_str, 2)
            if value == 1:
                return True
            
            while value > 1:
                if value % 5 != 0:
                    return False
                value //= 5
            
            return value == 1
        
        def backtrack(start, partitions):
            if start == n:
                return partitions
            
            min_partitions = float('inf')
            
            for end in range(start + 1, n + 1):
                substring = s[start:end]
                if is_power_of_5(substring):
                    result = backtrack(end, partitions + 1)
                    min_partitions = min(min_partitions, result)
            
            return min_partitions
        
        result = backtrack(0, 0)
        return result if result != float('inf') else -1

def test_minimum_beautiful_substrings():
    """Test the minimum beautiful substrings solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.minimumBeautifulSubstrings("1011") == 2
    
    # Test case 2: All ones
    assert solution.minimumBeautifulSubstrings("111") == 3
    
    # Test case 3: Starts with zero
    assert solution.minimumBeautifulSubstrings("0") == -1
    
    # Test case 4: Single '1' (5^0 = 1)
    assert solution.minimumBeautifulSubstrings("1") == 1
    
    # Test case 5: "101" (5^1 = 5 in binary)
    assert solution.minimumBeautifulSubstrings("101") == 1
    
    # Test case 6: "11001" (5^2 = 25 in binary)
    assert solution.minimumBeautifulSubstrings("11001") == 1
    
    # Test case 7: Cannot be partitioned
    assert solution.minimumBeautifulSubstrings("100") == -1
    
    # Test case 8: Complex case
    assert solution.minimumBeautifulSubstrings("1011101") == 3  # "101" + "1" + "101"
    
    # Test case 9: "110110110" - powers of 5: 1, 101, 11001
    # This should be partitionable as "1" + "101" + "101" + "1" + "0" (invalid due to 0)
    # Or other combinations
    result = solution.minimumBeautifulSubstrings("110110110")
    # Let's check if it's partitionable at all
    
    # Compare different approaches on smaller inputs
    test_cases = [
        "1011",
        "111",
        "0",
        "1",
        "101",
        "11001",
        "100",
        "11011"
    ]
    
    for s in test_cases:
        result1 = solution.minimumBeautifulSubstrings(s)
        result2 = solution.minimumBeautifulSubstrings_backtrack(s)
        assert result1 == result2, f"Mismatch for {s}: {result1} vs {result2}"
    
    print("All minimum beautiful substrings tests passed!")

if __name__ == "__main__":
    test_minimum_beautiful_substrings()
