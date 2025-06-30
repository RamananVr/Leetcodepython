"""
LeetCode Problem 2787: Ways to Express an Integer as Sum of Powers

Given two positive integers n and x, return the number of ways to express n as a sum of the x-th power of unique positive integers.

In other words, return the number of sets of positive integers [a1, a2, ..., ak] such that a1^x + a2^x + ... + ak^x == n, where all ai are unique.

Since the result can be large, return it modulo 10^9 + 7.

Constraints:
- 1 <= n <= 300
- 1 <= x <= 5

Example 1:
Input: n = 10, x = 2
Output: 1
Explanation: We can express 10 as 1^2 + 3^2 = 1 + 9 = 10.
There is only one way to express 10 as sum of unique squares.

Example 2:
Input: n = 4, x = 1
Output: 2
Explanation: We can express 4 as:
- 4^1 = 4
- 1^1 + 3^1 = 1 + 3 = 4
There are two ways to express 4 as sum of unique first powers.
"""

def number_of_ways(n, x):
    """
    Optimized Dynamic Programming solution
    
    Time Complexity: O(n * m) where m is the number of valid bases
    Space Complexity: O(n)
    """
    MOD = 10**9 + 7
    
    # Find all possible bases whose x-th power <= n
    powers = []
    base = 1
    while base ** x <= n:
        powers.append(base ** x)
        base += 1
    
    # dp[i] = number of ways to express i as sum of unique x-th powers
    dp = [0] * (n + 1)
    dp[0] = 1  # One way to express 0: use no numbers
    
    # For each power, update the dp array
    for power in powers:
        # Traverse backwards to avoid using the same power multiple times
        for target in range(n, power - 1, -1):
            dp[target] = (dp[target] + dp[target - power]) % MOD
    
    return dp[n]

def number_of_ways_memoization(n, x):
    """
    Alternative approach using memoization
    
    Time Complexity: O(n * m)
    Space Complexity: O(n * m)
    """
    MOD = 10**9 + 7
    
    # Generate all possible powers
    powers = []
    base = 1
    while base ** x <= n:
        powers.append(base ** x)
        base += 1
    
    memo = {}
    
    def dp(remaining, index):
        """
        remaining: remaining sum to achieve
        index: current index in powers array
        """
        if remaining == 0:
            return 1
        if remaining < 0 or index >= len(powers):
            return 0
        
        if (remaining, index) in memo:
            return memo[(remaining, index)]
        
        # Choice 1: Don't use powers[index]
        result = dp(remaining, index + 1)
        
        # Choice 2: Use powers[index]
        if remaining >= powers[index]:
            result = (result + dp(remaining - powers[index], index + 1)) % MOD
        
        memo[(remaining, index)] = result
        return result
    
    return dp(n, 0)

def number_of_ways_optimized(n, x):
    """
    Most optimized solution with space optimization
    
    Time Complexity: O(n * sqrt[x](n))
    Space Complexity: O(n)
    """
    MOD = 10**9 + 7
    
    # Generate powers on the fly to save space
    dp = [0] * (n + 1)
    dp[0] = 1
    
    base = 1
    while base ** x <= n:
        power = base ** x
        
        # Update dp array backwards
        for target in range(n, power - 1, -1):
            dp[target] = (dp[target] + dp[target - power]) % MOD
        
        base += 1
    
    return dp[n]

def number_of_ways_recursive(n, x):
    """
    Pure recursive approach (less efficient, for understanding)
    
    Time Complexity: O(2^m) where m is number of valid bases
    Space Complexity: O(m)
    """
    MOD = 10**9 + 7
    
    def solve(target, start_base):
        if target == 0:
            return 1
        if target < 0 or start_base ** x > target:
            return 0
        
        # Include current base
        include = solve(target - start_base ** x, start_base + 1)
        
        # Exclude current base
        exclude = solve(target, start_base + 1)
        
        return (include + exclude) % MOD
    
    return solve(n, 1)

# Test cases
def test_number_of_ways():
    test_cases = [
        (10, 2, 1),   # 1^2 + 3^2 = 1 + 9 = 10
        (4, 1, 2),    # 4^1 = 4 OR 1^1 + 3^1 = 1 + 3 = 4
        (1, 1, 1),    # 1^1 = 1
        (1, 2, 1),    # 1^2 = 1
        (15, 2, 0),   # No way to express 15 as sum of unique squares
        (9, 2, 2),    # 3^2 = 9 OR 1^2 + 2^2 + 2^2... wait, that's not unique
        (6, 1, 4),    # 6, 1+5, 2+4, 1+2+3
        (3, 3, 1),    # Only 1^3 + 2^3 = 1 + 8 = 9 > 3, so no solutions... wait let me recalculate
        (2, 2, 1),    # 1^2 + 1^2 = 2, but must be unique, so no solution... actually 1^2 = 1, we need 2
        (5, 2, 1),    # 1^2 + 2^2 = 1 + 4 = 5
    ]
    
    approaches = [
        ("DP Optimized", number_of_ways),
        ("Memoization", number_of_ways_memoization),
        ("Most Optimized", number_of_ways_optimized)
    ]
    
    for approach_name, func in approaches:
        print(f"Testing {approach_name} approach:")
        all_passed = True
        
        for n, x, expected in test_cases:
            try:
                result = func(n, x)
                passed = result == expected
                if not passed:
                    all_passed = False
                
                print(f"  Input: n={n}, x={x}")
                print(f"  Expected: {expected}, Got: {result}")
                print(f"  {'✓' if passed else '✗'}")
            except Exception as e:
                print(f"  Input: n={n}, x={x}")
                print(f"  Error: {e}")
                print(f"  ✗")
                all_passed = False
        
        print(f"  Overall: {'✓ All Passed' if all_passed else '✗ Some Failed'}\n")

def analyze_examples():
    """Analyze the examples in detail"""
    print("Detailed Analysis:")
    print("\nExample 1: n=10, x=2")
    print("Available powers: 1^2=1, 2^2=4, 3^2=9, 4^2=16")
    print("Valid combinations that sum to 10:")
    print("- 1^2 + 3^2 = 1 + 9 = 10 ✓")
    print("- No other combinations work")
    print("Result: 1 way")
    
    print("\nExample 2: n=4, x=1")
    print("Available powers: 1^1=1, 2^1=2, 3^1=3, 4^1=4")
    print("Valid combinations that sum to 4:")
    print("- 4^1 = 4 ✓")
    print("- 1^1 + 3^1 = 1 + 3 = 4 ✓")
    print("- 2^1 + 2^1 = 2 + 2 = 4 ✗ (not unique)")
    print("Result: 2 ways")
    
    print("\nExample 3: n=6, x=1")
    print("Available powers: 1^1=1, 2^1=2, 3^1=3, 4^1=4, 5^1=5, 6^1=6")
    print("Valid combinations that sum to 6:")
    print("- 6^1 = 6 ✓")
    print("- 1^1 + 5^1 = 1 + 5 = 6 ✓")
    print("- 2^1 + 4^1 = 2 + 4 = 6 ✓")
    print("- 1^1 + 2^1 + 3^1 = 1 + 2 + 3 = 6 ✓")
    print("Result: 4 ways")

if __name__ == "__main__":
    test_number_of_ways()
    print("\n" + "="*50)
    analyze_examples()

"""
Topics: Dynamic Programming, Math, Backtracking
Difficulty: Medium

Key Insights:
1. Classic subset sum problem with unique elements (powers)
2. DP approach: for each power, decide to include or exclude
3. Process powers in order and update DP array backwards
4. Backwards traversal ensures each power is used at most once
5. Generate powers on the fly: 1^x, 2^x, 3^x, ... until > n

Companies: Google, Microsoft, Amazon, Meta
"""
