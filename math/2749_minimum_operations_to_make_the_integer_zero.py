"""
LeetCode Problem 2749: Minimum Operations to Make the Integer Zero

You are given two integers num1 and num2.

In one operation, you can choose integer i where 0 <= i <= 60 and subtract 2^i + num2 from num1.

Return the minimum number of operations to make num1 equal to 0, or -1 if it is impossible.

Example 1:
Input: num1 = 3, num2 = -2
Output: 3
Explanation: We can make num1 equal to 0 with the following operations:
- Operation 1: i = 2, num1 = 3 - (2^2 + (-2)) = 3 - (4 - 2) = 3 - 2 = 1.
- Operation 2: i = 2, num1 = 1 - (2^2 + (-2)) = 1 - (4 - 2) = 1 - 2 = -1.
- Operation 3: i = 0, num1 = -1 - (2^0 + (-2)) = -1 - (1 - 2) = -1 - (-1) = 0.

Example 2:
Input: num1 = 5, num2 = 7
Output: -1
Explanation: It can be shown that it is impossible to make num1 equal to 0 with the given operations.

Constraints:
- 1 <= num1 <= 10^9
- -10^9 <= num2 <= 10^9
"""


def makeTheIntegerZero(num1: int, num2: int) -> int:
    """
    Find minimum operations to make num1 zero by subtracting (2^i + num2).
    
    Key insight: After k operations, we have:
    num1 - k * num2 = sum of k powers of 2
    
    For this to be possible:
    1. num1 - k * num2 > 0 (sum of powers of 2 is positive)
    2. num1 - k * num2 >= k (need at least k bits set to represent k terms)
    3. popcount(num1 - k * num2) <= k (can't have more set bits than terms)
    
    Args:
        num1: Starting number
        num2: Number to subtract along with power of 2
        
    Returns:
        Minimum number of operations, or -1 if impossible
        
    Time Complexity: O(log num1)
    Space Complexity: O(1)
    """
    # Try different values of k (number of operations)
    for k in range(1, 64):  # 64 is enough since 2^60 is very large
        target = num1 - k * num2
        
        # Check if target can be represented as sum of exactly k powers of 2
        if target >= k and bin(target).count('1') <= k:
            return k
    
    return -1


def makeTheIntegerZeroOptimized(num1: int, num2: int) -> int:
    """
    Optimized version with early termination conditions.
    
    Args:
        num1: Starting number
        num2: Number to subtract along with power of 2
        
    Returns:
        Minimum number of operations, or -1 if impossible
        
    Time Complexity: O(log num1)
    Space Complexity: O(1)
    """
    # If num2 is too large positive, we can never reach 0
    if num2 >= num1:
        return -1 if num2 > num1 else 1 if num1 == 1 else -1
    
    # Try different values of k
    for k in range(1, 64):
        target = num1 - k * num2
        
        # Early termination: if target becomes too small, break
        if target < 0:
            break
        
        # Check feasibility conditions
        if target >= k and bin(target).count('1') <= k:
            return k
    
    return -1


def makeTheIntegerZeroMath(num1: int, num2: int) -> int:
    """
    Mathematical approach with better bounds analysis.
    
    The equation is: num1 - k * num2 = sum of k powers of 2
    Let S = num1 - k * num2
    
    Constraints:
    1. S > 0 (sum of powers of 2 is positive)
    2. S >= k (minimum sum is k ones: 2^0 + 2^0 + ... = k)
    3. popcount(S) <= k (can't use more than k powers of 2)
    
    Args:
        num1: Starting number
        num2: Number to subtract along with power of 2
        
    Returns:
        Minimum number of operations, or -1 if impossible
        
    Time Complexity: O(log num1)
    Space Complexity: O(1)
    """
    for k in range(1, 50):  # Reasonable upper bound
        remaining = num1 - k * num2
        
        if remaining <= 0:
            # If remaining is 0 or negative, can't form sum of powers of 2
            continue
        
        # Count number of set bits in remaining
        bit_count = bin(remaining).count('1')
        
        # Check if we can represent 'remaining' as sum of exactly k powers of 2
        # Need: bit_count <= k <= remaining
        if bit_count <= k <= remaining:
            return k
    
    return -1


def makeTheIntegerZeroBruteForce(num1: int, num2: int) -> int:
    """
    Brute force approach for verification on small inputs.
    
    Args:
        num1: Starting number
        num2: Number to subtract along with power of 2
        
    Returns:
        Minimum number of operations, or -1 if impossible
        
    Time Complexity: O(k * 2^k) where k is the answer
    Space Complexity: O(1)
    """
    def can_reach_zero(current: int, operations_left: int, max_ops: int) -> bool:
        """Check if we can reach zero in given operations."""
        if operations_left == 0:
            return current == 0
        
        if operations_left > max_ops or current < 0:
            return False
        
        # Try all possible values of i from 0 to 60
        for i in range(min(61, 64)):  # Reasonable bound
            new_val = current - (2**i + num2)
            if can_reach_zero(new_val, operations_left - 1, max_ops):
                return True
        
        return False
    
    # Try increasing number of operations
    for ops in range(1, 20):  # Reasonable upper bound for brute force
        if can_reach_zero(num1, ops, ops):
            return ops
    
    return -1


# Test cases
def test_makeTheIntegerZero():
    """Test the makeTheIntegerZero function with various inputs."""
    
    test_cases = [
        {
            "num1": 3, "num2": -2,
            "expected": 3,
            "description": "Example 1: Positive result"
        },
        {
            "num1": 5, "num2": 7,
            "expected": -1,
            "description": "Example 2: Impossible case"
        },
        {
            "num1": 1, "num2": 0,
            "expected": 1,
            "description": "Simple case: 1 - (2^0 + 0) = 0"
        },
        {
            "num1": 4, "num2": 0,
            "expected": 1,
            "description": "Power of 2: 4 - (2^2 + 0) = 0"
        },
        {
            "num1": 7, "num2": 0,
            "expected": 3,
            "description": "7 = 2^2 + 2^1 + 2^0, need 3 operations"
        },
        {
            "num1": 10, "num2": -5,
            "expected": 2,
            "description": "With negative num2"
        },
        {
            "num1": 2, "num2": 1,
            "expected": 2,
            "description": "Need multiple operations"
        },
        {
            "num1": 1000000000, "num2": 1000000000,
            "expected": -1,
            "description": "Large numbers, impossible"
        },
        {
            "num1": 15, "num2": 0,
            "expected": 4,
            "description": "15 = 2^3 + 2^2 + 2^1 + 2^0"
        }
    ]
    
    for i, test in enumerate(test_cases):
        num1 = test["num1"]
        num2 = test["num2"]
        expected = test["expected"]
        
        # Test main solution
        result1 = makeTheIntegerZero(num1, num2)
        print(f"Test {i+1}: {test['description']}")
        print(f"  Input: num1 = {num1}, num2 = {num2}")
        print(f"  Expected: {expected}")
        print(f"  Basic approach: {result1}")
        
        # Test optimized solution
        result2 = makeTheIntegerZeroOptimized(num1, num2)
        print(f"  Optimized: {result2}")
        
        # Test mathematical solution
        result3 = makeTheIntegerZeroMath(num1, num2)
        print(f"  Mathematical: {result3}")
        
        # Test brute force for small inputs
        if num1 <= 1000 and abs(num2) <= 1000:
            result4 = makeTheIntegerZeroBruteForce(num1, num2)
            print(f"  Brute force: {result4}")
            assert result4 == expected, f"Brute force failed for test {i+1}"
        
        # Verify results
        assert result1 == expected, f"Basic approach failed for test {i+1}"
        assert result2 == expected, f"Optimized failed for test {i+1}"
        assert result3 == expected, f"Mathematical failed for test {i+1}"
        
        # Show the solution path for successful cases
        if expected != -1 and expected <= 5:
            print(f"  Solution verification for k = {expected}:")
            target = num1 - expected * num2
            bit_count = bin(target).count('1') if target > 0 else 0
            print(f"    target = {num1} - {expected} * {num2} = {target}")
            print(f"    bit_count = {bit_count}, k = {expected}")
            print(f"    Conditions: target >= k? {target >= expected}, bit_count <= k? {bit_count <= expected}")
        
        print(f"  ✓ All solutions passed!")
        print()


if __name__ == "__main__":
    test_makeTheIntegerZero()

"""
Complexity Analysis:

1. Basic Approach (makeTheIntegerZero):
   - Time Complexity: O(log num1) - check at most 64 values of k
   - Space Complexity: O(1) - constant extra space

2. Optimized (makeTheIntegerZeroOptimized):
   - Time Complexity: O(log num1) - early termination improves average case
   - Space Complexity: O(1) - constant extra space

3. Mathematical (makeTheIntegerZeroMath):
   - Time Complexity: O(log num1) - bounded iteration with mathematical insights
   - Space Complexity: O(1) - constant extra space

4. Brute Force (makeTheIntegerZeroBruteForce):
   - Time Complexity: O(k * 60^k) - exponential in number of operations
   - Space Complexity: O(k) - recursion stack depth

Key Insights:
- After k operations: num1 - k * num2 = sum of k powers of 2
- The sum must be positive and have at most k set bits
- The sum must be at least k (minimum is k ones)
- Binary representation analysis is crucial for feasibility check

Mathematical Constraints:
- Let S = num1 - k * num2
- S > 0 (sum of powers of 2 is positive)
- popcount(S) ≤ k (can't exceed k terms)
- S ≥ k (minimum sum with k terms is k)

Edge Cases:
- num2 > num1 (likely impossible)
- num2 = 0 (simple power of 2 decomposition)
- Large values requiring careful bounds
- Negative num2 (can help reach target faster)

Topics: Math, Bit Manipulation, Greedy Algorithms, Number Theory
"""
