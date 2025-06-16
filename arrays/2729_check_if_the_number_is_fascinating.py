"""
2729. Check if The Number is Fascinating

You are given an integer n. We call n fascinating if, after the following modification, 
the resulting number contains all the digits from 1 to 9 exactly once and does not contain any 0s:

Concatenate n with the numbers 2 * n and 3 * n.

Return true if n is fascinating, or false otherwise.

Concatenating two numbers means joining them together. For example, the concatenation of 121 and 371 is 121371.

Example 1:
Input: n = 192
Output: true
Explanation: We concatenate the numbers n = 192 and 2 * n = 384 and 3 * n = 576.
The resulting number is 192384576. This number contains all the digits from 1 to 9 exactly once, so it is fascinating.

Example 2:
Input: n = 100
Output: false
Explanation: We concatenate the numbers n = 100 and 2 * n = 200 and 3 * n = 300.
The resulting number is 100200300. This number contains 0s, so it is not fascinating.

Constraints:
- 100 <= n <= 999
"""

def is_fascinating(n: int) -> bool:
    """
    Check if a number is fascinating by concatenating n, 2*n, and 3*n and checking
    if the result contains all digits 1-9 exactly once with no zeros.
    
    Args:
        n: Integer to check (100 <= n <= 999)
        
    Returns:
        bool: True if n is fascinating, False otherwise
        
    Time Complexity: O(1) - since n is bounded by 999, string operations are constant
    Space Complexity: O(1) - using constant extra space
    """
    # Concatenate n, 2*n, and 3*n
    concatenated = str(n) + str(2 * n) + str(3 * n)
    
    # Check if the result contains exactly digits 1-9 (no 0s, no repeats)
    return set(concatenated) == set('123456789') and len(concatenated) == 9

def is_fascinating_optimized(n: int) -> bool:
    """
    Optimized version using digit counting without string conversion.
    
    Args:
        n: Integer to check
        
    Returns:
        bool: True if n is fascinating, False otherwise
        
    Time Complexity: O(1) - bounded operations
    Space Complexity: O(1) - using array of size 10
    """
    # Count occurrences of each digit
    digit_count = [0] * 10
    
    # Process n, 2*n, and 3*n
    for num in [n, 2 * n, 3 * n]:
        while num > 0:
            digit = num % 10
            if digit == 0:  # Contains 0, not fascinating
                return False
            digit_count[digit] += 1
            num //= 10
    
    # Check if all digits 1-9 appear exactly once
    return all(digit_count[i] == 1 for i in range(1, 10)) and digit_count[0] == 0

def is_fascinating_early_exit(n: int) -> bool:
    """
    Version with early exit optimization for better average case performance.
    
    Args:
        n: Integer to check
        
    Returns:
        bool: True if n is fascinating, False otherwise
        
    Time Complexity: O(1) - bounded operations with early exit
    Space Complexity: O(1) - using set for checking
    """
    concatenated = str(n) + str(2 * n) + str(3 * n)
    
    # Early exit conditions
    if len(concatenated) != 9:
        return False
    if '0' in concatenated:
        return False
    
    # Check if all digits 1-9 are present
    return len(set(concatenated)) == 9

# Test cases
def test_is_fascinating():
    test_cases = [
        # Basic test cases
        (192, True),   # 192384576 contains all digits 1-9
        (100, False),  # 100200300 contains 0s
        (183, True),   # 183366549 contains all digits 1-9
        (199, False),  # 199398597 missing some digits
        
        # Edge cases
        (111, False),  # 111222333 has repeating digits
        (123, False),  # 123246369 has repeating digits
        (219, False),  # 219438657 missing digit 1
        (327, True),   # 327654981 contains all digits 1-9
        
        # Boundary cases
        (999, False),  # Large number case
        (101, False),  # Contains 0
        (102, False),  # Contains 0
        (234, False),  # 234468702 contains 0
    ]
    
    print("Testing is_fascinating function:")
    for i, (n, expected) in enumerate(test_cases):
        result1 = is_fascinating(n)
        result2 = is_fascinating_optimized(n)
        result3 = is_fascinating_early_exit(n)
        
        concatenated = str(n) + str(2 * n) + str(3 * n)
        print(f"Test {i+1}: n={n}")
        print(f"  Concatenated: {concatenated}")
        print(f"  Expected: {expected}")
        print(f"  Basic: {result1}")
        print(f"  Optimized: {result2}")
        print(f"  Early Exit: {result3}")
        
        assert result1 == expected, f"Basic failed for n={n}"
        assert result2 == expected, f"Optimized failed for n={n}"
        assert result3 == expected, f"Early Exit failed for n={n}"
        print(f"  ✓ All passed\n")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_is_fascinating()

"""
Time Complexity Analysis:
- Basic Solution: O(1) - string operations on numbers bounded by 999
- Optimized Solution: O(1) - digit counting with bounded iterations
- Early Exit Solution: O(1) - with early termination for better average case

Space Complexity Analysis:
- Basic Solution: O(1) - using set for constant size input
- Optimized Solution: O(1) - using array of size 10
- Early Exit Solution: O(1) - using set for bounded input

Key Insights:
1. Since n is bounded (100 <= n <= 999), all operations are effectively O(1)
2. String concatenation is simple but digit counting can be more efficient
3. Early exit optimizations help with invalid cases
4. The fascinating property requires exactly 9 digits with no zeros and no repeats

Topics: Arrays, String Manipulation, Number Theory, Set Operations
"""
