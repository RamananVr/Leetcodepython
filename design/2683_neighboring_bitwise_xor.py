"""
LeetCode Question #2683: Neighboring Bitwise XOR

Problem Statement:
A 0-indexed array derived with length n is derived by computing the bitwise XOR (⊕) of adjacent values in some array original of length n.

Specifically, derived[i] = original[i] ⊕ original[i + 1] for each valid i. The last element, derived[n - 1], is computed using original[n - 1] ⊕ original[0].

Given an array derived, your task is to determine whether there exists a valid original array that could have resulted in derived.

Return true if such an array exists, or false otherwise.

Examples:
Example 1:
Input: derived = [1,1,0]
Output: true
Explanation: A valid original array is [0,1,0]:
- derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1
- derived[1] = original[1] ⊕ original[2] = 1 ⊕ 0 = 1  
- derived[2] = original[2] ⊕ original[0] = 0 ⊕ 0 = 0

Example 2:
Input: derived = [1,1]
Output: true
Explanation: A valid original array is [0,1]:
- derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1
- derived[1] = original[1] ⊕ original[0] = 1 ⊕ 0 = 1

Example 3:
Input: derived = [1,0]
Output: false
Explanation: There is no valid original array.

Constraints:
- n == derived.length
- 1 <= n <= 10^5
- Each value in derived is either 0 or 1
"""

from typing import List

def doesValidArrayExist(derived: List[int]) -> bool:
    """
    Check if a valid original array exists for the given derived array.
    
    Key insight: For a valid original array to exist, the XOR of all elements
    in derived must be 0. This is because:
    derived[0] ⊕ derived[1] ⊕ ... ⊕ derived[n-1] = 
    (original[0] ⊕ original[1]) ⊕ (original[1] ⊕ original[2]) ⊕ ... ⊕ (original[n-1] ⊕ original[0])
    
    Each original[i] appears exactly twice in this expression, so they all cancel out.
    Therefore, the XOR sum must be 0.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    xor_sum = 0
    for val in derived:
        xor_sum ^= val
    return xor_sum == 0

def doesValidArrayExistConstruction(derived: List[int]) -> bool:
    """
    Alternative approach: Try to construct the original array.
    
    We can assume original[0] = 0 or original[0] = 1 and see if we can
    construct a valid original array that satisfies all constraints.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(derived)
    
    # Try with original[0] = 0
    if tryConstruct(derived, 0):
        return True
    
    # Try with original[0] = 1
    if tryConstruct(derived, 1):
        return True
    
    return False

def tryConstruct(derived: List[int], first_val: int) -> bool:
    """
    Helper function to try constructing original array with given first value.
    """
    n = len(derived)
    original = [0] * n
    original[0] = first_val
    
    # Construct the rest of the array
    for i in range(n - 1):
        # derived[i] = original[i] ⊕ original[i + 1]
        # So original[i + 1] = derived[i] ⊕ original[i]
        original[i + 1] = derived[i] ^ original[i]
    
    # Check if the last constraint is satisfied
    # derived[n-1] should equal original[n-1] ⊕ original[0]
    return derived[n - 1] == (original[n - 1] ^ original[0])

def doesValidArrayExistBruteForce(derived: List[int]) -> bool:
    """
    Brute force approach: Try all possible original arrays.
    Only feasible for small arrays due to exponential complexity.
    
    Time Complexity: O(2^n * n)
    Space Complexity: O(n)
    """
    n = len(derived)
    
    # Try all possible original arrays (2^n possibilities)
    for mask in range(1 << n):
        original = []
        for i in range(n):
            original.append((mask >> i) & 1)
        
        # Check if this original array produces the given derived array
        valid = True
        for i in range(n):
            next_idx = (i + 1) % n
            if (original[i] ^ original[next_idx]) != derived[i]:
                valid = False
                break
        
        if valid:
            return True
    
    return False

def doesValidArrayExistMath(derived: List[int]) -> bool:
    """
    Mathematical approach using properties of XOR.
    
    The key insight is that for a circular XOR pattern to be valid,
    the XOR of all derived values must be 0.
    
    Proof:
    Let original = [a0, a1, ..., an-1]
    Then derived = [a0⊕a1, a1⊕a2, ..., an-1⊕a0]
    
    XOR of all derived values:
    (a0⊕a1) ⊕ (a1⊕a2) ⊕ ... ⊕ (an-1⊕a0)
    = a0⊕a1⊕a1⊕a2⊕...⊕an-1⊕a0
    = (a0⊕a0) ⊕ (a1⊕a1) ⊕ ... ⊕ (an-1⊕an-1)
    = 0 ⊕ 0 ⊕ ... ⊕ 0
    = 0
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    result = 0
    for bit in derived:
        result ^= bit
    return result == 0

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 0], True),
        ([1, 1], True),
        ([1, 0], False),
        ([0], True),
        ([1], False),
        ([0, 0, 0], True),
        ([1, 1, 1], False),
        ([1, 0, 1, 0], True),
        ([1, 0, 0, 1], True),
        ([0, 1, 1, 0], True)
    ]
    
    print("Testing main approach:")
    for derived, expected in test_cases:
        result = doesValidArrayExist(derived)
        print(f"doesValidArrayExist({derived}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting construction approach:")
    for derived, expected in test_cases:
        result = doesValidArrayExistConstruction(derived)
        print(f"doesValidArrayExistConstruction({derived}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting mathematical approach:")
    for derived, expected in test_cases:
        result = doesValidArrayExistMath(derived)
        print(f"doesValidArrayExistMath({derived}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    # Test brute force on small arrays only
    print("\nTesting brute force approach (small arrays only):")
    small_test_cases = [case for case in test_cases if len(case[0]) <= 4]
    for derived, expected in small_test_cases:
        result = doesValidArrayExistBruteForce(derived)
        print(f"doesValidArrayExistBruteForce({derived}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    # Demonstration with construction
    print("\nDemonstration of construction:")
    test_derived = [1, 1, 0]
    print(f"Derived array: {test_derived}")
    
    # Try with first element = 0
    n = len(test_derived)
    original = [0] * n
    original[0] = 0
    for i in range(n - 1):
        original[i + 1] = test_derived[i] ^ original[i]
    
    print(f"Original array (starting with 0): {original}")
    
    # Verify
    reconstructed = []
    for i in range(n):
        next_idx = (i + 1) % n
        reconstructed.append(original[i] ^ original[next_idx])
    
    print(f"Reconstructed derived: {reconstructed}")
    print(f"Matches original derived: {reconstructed == test_derived}")

"""
Time and Space Complexity Analysis:

Main Approach (XOR Sum):
Time Complexity: O(n) - Single pass through the array
Space Complexity: O(1) - Only using constant extra space

Construction Approach:
Time Complexity: O(n) - Try both possible starting values
Space Complexity: O(n) - Store the constructed original array

Brute Force Approach:
Time Complexity: O(2^n * n) - Try all possible original arrays
Space Complexity: O(n) - Store each candidate original array

Mathematical Approach:
Time Complexity: O(n) - Single pass to compute XOR
Space Complexity: O(1) - Constant space

Key Insights:
1. The problem has a beautiful mathematical property: XOR sum must be 0
2. This is because each element in the original array appears exactly twice in the XOR expression
3. Construction approach validates the mathematical insight
4. XOR properties: a ⊕ a = 0, a ⊕ 0 = a, XOR is commutative and associative

Applications:
- Error detection in communication systems
- Cryptography and hash functions
- Puzzle solving and constraint satisfaction

Topic: Bit Manipulation, XOR Properties, Mathematical Proof, Array Construction
"""
