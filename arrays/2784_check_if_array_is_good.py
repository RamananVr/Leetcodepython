"""
LeetCode Problem 2784: Check if Array is Good

You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].

base[n] = [1, 2, 3, ..., n, n] (in other words, it is an array of length n + 1 which contains 1 to n exactly once, plus one additional occurrence of n).

For example, base[1] = [1, 1], base[3] = [1, 2, 3, 3].

Return true if the given array is good, otherwise return false.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 200

Example 1:
Input: nums = [2, 1, 3]
Output: false
Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. However, base[3] has four elements but array nums has three. Therefore, it cannot be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

Example 2:
Input: nums = [1, 3, 3, 2]
Output: true
Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. It can be seen that nums is a permutation of base[3] = [1, 2, 3, 3] (by swapping the second and fourth elements in nums, we reach base[3]). Therefore, the answer is true.
"""

def is_good_array(nums):
    """
    Optimized solution using frequency counting
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not nums:
        return False
    
    n = max(nums)
    
    # A good array of base[n] should have length n + 1
    if len(nums) != n + 1:
        return False
    
    # Count frequency of each number
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    # Check the pattern: 1 to n-1 should appear once, n should appear twice
    for i in range(1, n):
        if freq.get(i, 0) != 1:
            return False
    
    # n should appear exactly twice
    if freq.get(n, 0) != 2:
        return False
    
    # No other numbers should be present
    for num in freq:
        if num < 1 or num > n:
            return False
    
    return True

def is_good_array_sorting(nums):
    """
    Alternative solution using sorting
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if not nums:
        return False
    
    n = max(nums)
    
    # Check length
    if len(nums) != n + 1:
        return False
    
    # Create expected base array and sort both
    expected = list(range(1, n)) + [n, n]  # [1, 2, ..., n-1, n, n]
    nums_sorted = sorted(nums)
    
    return nums_sorted == sorted(expected)

def is_good_array_optimized(nums):
    """
    Most optimized solution - single pass with early termination
    
    Time Complexity: O(n)
    Space Complexity: O(1) if we modify input, O(n) for freq array
    """
    if not nums:
        return False
    
    n = max(nums)
    
    # Quick length check
    if len(nums) != n + 1:
        return False
    
    # Use array for frequency counting (faster than dict for small ranges)
    freq = [0] * (n + 1)
    
    for num in nums:
        if num < 1 or num > n:
            return False
        freq[num] += 1
        # Early termination if any number appears more than twice
        if freq[num] > 2:
            return False
    
    # Check pattern: freq[i] = 1 for i in [1, n-1], freq[n] = 2
    for i in range(1, n):
        if freq[i] != 1:
            return False
    
    return freq[n] == 2

def is_good_array_mathematical(nums):
    """
    Mathematical approach using sum properties
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not nums:
        return False
    
    n = max(nums)
    
    if len(nums) != n + 1:
        return False
    
    # Expected sum: 1 + 2 + ... + n + n = n(n+1)/2 + n = n(n+3)/2
    expected_sum = n * (n + 3) // 2
    actual_sum = sum(nums)
    
    if actual_sum != expected_sum:
        return False
    
    # Sum check passed, now verify the actual pattern
    seen = set()
    n_count = 0
    
    for num in nums:
        if num < 1 or num > n:
            return False
        
        if num == n:
            n_count += 1
        elif num in seen:
            return False  # Duplicate of non-n number
        else:
            seen.add(num)
    
    # Should have n appearing exactly twice and all other numbers 1 to n-1
    return n_count == 2 and len(seen) == n - 1

# Test cases
def test_is_good_array():
    test_cases = [
        ([2, 1, 3], False),
        ([1, 3, 3, 2], True),
        ([1, 1], True),  # base[1] = [1, 1]
        ([1, 2, 3, 3], True),  # base[3] = [1, 2, 3, 3]
        ([1], False),  # Not enough elements
        ([2, 2, 1], False),  # Missing 1, extra 2
        ([1, 2, 2], True),  # base[2] = [1, 2, 2]
        ([3, 1, 2, 3], True),  # Permutation of base[3]
        ([1, 2, 3, 4, 4], True),  # base[4] = [1, 2, 3, 4, 4]
        ([1, 2, 3, 4, 5], False),  # Missing duplicate of max
        ([], False),  # Empty array
        ([5], False),  # Single element that's not 1
    ]
    
    approaches = [
        ("Frequency Counting", is_good_array),
        ("Sorting", is_good_array_sorting),
        ("Optimized", is_good_array_optimized),
        ("Mathematical", is_good_array_mathematical)
    ]
    
    for approach_name, func in approaches:
        print(f"Testing {approach_name} approach:")
        all_passed = True
        
        for nums, expected in test_cases:
            try:
                result = func(nums[:])  # Pass copy to avoid modification
                passed = result == expected
                if not passed:
                    all_passed = False
                
                print(f"  Input: {nums}")
                print(f"  Expected: {expected}, Got: {result}")
                print(f"  {'✓' if passed else '✗'}")
            except Exception as e:
                print(f"  Input: {nums}")
                print(f"  Error: {e}")
                print(f"  ✗")
                all_passed = False
        
        print(f"  Overall: {'✓ All Passed' if all_passed else '✗ Some Failed'}\n")

if __name__ == "__main__":
    test_is_good_array()

"""
Topics: Arrays, Hash Table, Sorting, Math
Difficulty: Easy

Key Insights:
1. Good array base[n] = [1, 2, ..., n-1, n, n] has length n+1
2. Maximum element determines n, then check if it's a valid permutation
3. Frequency counting: numbers 1 to n-1 appear once, n appears twice
4. Can use sum property for additional validation
5. Early termination optimizes performance

Companies: Google, Microsoft, Amazon, Apple
"""
