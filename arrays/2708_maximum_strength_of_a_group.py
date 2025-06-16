"""
LeetCode Problem #2708: Maximum Strength of a Group

Problem Statement:
You are given a 0-indexed integer array `nums` representing the score of students in an exam. The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices `i0, i1, i2, ... , ik` is defined as `nums[i0] * nums[i1] * nums[i2] * ... * nums[ik]`.

Return the maximum strength of a group the teacher can create.

Constraints:
- 1 <= nums.length <= 13
- -9 <= nums[i] <= 9
"""

def maxStrength(nums):
    """
    Finds the maximum strength by considering all possible non-empty subsets.
    
    :param nums: List[int] - Array of student scores
    :return: int - Maximum strength of a group
    """
    n = len(nums)
    max_strength = float('-inf')
    
    # Try all possible non-empty subsets (2^n - 1 subsets)
    for mask in range(1, 1 << n):
        strength = 1
        for i in range(n):
            if mask & (1 << i):
                strength *= nums[i]
        max_strength = max(max_strength, strength)
    
    return max_strength

def maxStrengthOptimized(nums):
    """
    Optimized solution by categorizing numbers and applying greedy strategy.
    
    :param nums: List[int] - Array of student scores
    :return: int - Maximum strength of a group
    """
    positives = [x for x in nums if x > 0]
    negatives = [x for x in nums if x < 0]
    zeros = [x for x in nums if x == 0]
    
    # Sort negatives in ascending order (most negative first)
    negatives.sort()
    
    # If we have only one number and it's negative or zero
    if len(nums) == 1:
        return nums[0]
    
    # Start with product of all positive numbers
    result = 1
    used_any = False
    
    # Include all positive numbers
    for num in positives:
        result *= num
        used_any = True
    
    # Include pairs of negative numbers (even count)
    neg_count = len(negatives)
    if neg_count >= 2:
        # Use pairs of negatives (even count)
        pairs = neg_count // 2 * 2
        for i in range(pairs):
            result *= negatives[i]
            used_any = True
    
    # Special case: if no numbers used yet
    if not used_any:
        if zeros:
            return 0
        elif len(negatives) == 1:
            return negatives[0]
        else:
            # This shouldn't happen given constraints
            return 0
    
    return result

def maxStrengthGreedy(nums):
    """
    Greedy approach with careful handling of edge cases.
    
    :param nums: List[int] - Array of student scores
    :return: int - Maximum strength of a group
    """
    # Separate numbers by sign
    pos = [x for x in nums if x > 0]
    neg = [x for x in nums if x < 0]
    zero_count = nums.count(0)
    
    # If only one element
    if len(nums) == 1:
        return nums[0]
    
    # Sort negatives in ascending order (most negative first)
    neg.sort()
    
    result = 1
    has_factors = False
    
    # Multiply all positive numbers
    for p in pos:
        result *= p
        has_factors = True
    
    # Multiply pairs of negative numbers
    for i in range(0, len(neg) - 1, 2):
        result *= neg[i] * neg[i + 1]
        has_factors = True
    
    # If no factors used yet, handle special cases
    if not has_factors:
        if zero_count > 0:
            return 0  # Choose zero over negative
        else:
            return max(neg)  # Choose the least negative
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [3, -1, -5, 2, 5, -9]
    print(f"nums: {nums}")
    print(f"maxStrength: {maxStrength(nums)}")  # Output: 1350
    print(f"maxStrengthOptimized: {maxStrengthOptimized(nums)}")  # Output: 1350
    print(f"maxStrengthGreedy: {maxStrengthGreedy(nums)}")  # Output: 1350
    print()

    # Test Case 2
    nums = [-4, -5, -4]
    print(f"nums: {nums}")
    print(f"maxStrength: {maxStrength(nums)}")  # Output: 20
    print(f"maxStrengthOptimized: {maxStrengthOptimized(nums)}")  # Output: 20
    print(f"maxStrengthGreedy: {maxStrengthGreedy(nums)}")  # Output: 20
    print()

    # Test Case 3
    nums = [0, -1]
    print(f"nums: {nums}")
    print(f"maxStrength: {maxStrength(nums)}")  # Output: 0
    print(f"maxStrengthOptimized: {maxStrengthOptimized(nums)}")  # Output: 0
    print(f"maxStrengthGreedy: {maxStrengthGreedy(nums)}")  # Output: 0
    print()

    # Test Case 4
    nums = [1, 2, 3, 4]
    print(f"nums: {nums}")
    print(f"maxStrength: {maxStrength(nums)}")  # Output: 24
    print(f"maxStrengthOptimized: {maxStrengthOptimized(nums)}")  # Output: 24
    print(f"maxStrengthGreedy: {maxStrengthGreedy(nums)}")  # Output: 24
    print()

    # Test Case 5
    nums = [-9]
    print(f"nums: {nums}")
    print(f"maxStrength: {maxStrength(nums)}")  # Output: -9
    print(f"maxStrengthOptimized: {maxStrengthOptimized(nums)}")  # Output: -9
    print(f"maxStrengthGreedy: {maxStrengthGreedy(nums)}")  # Output: -9

    # Validation
    assert maxStrength([3, -1, -5, 2, 5, -9]) == 1350
    assert maxStrengthOptimized([-4, -5, -4]) == 20
    assert maxStrengthGreedy([0, -1]) == 0
    print("All test cases passed!")

"""
Time Complexity Analysis:
Brute Force:
- Time complexity: O(2^n * n) where n is the length of array.

Optimized/Greedy:
- Time complexity: O(n log n) due to sorting of negatives.

Space Complexity Analysis:
- Space complexity: O(n) for storing separated positive/negative numbers.

Topic: Arrays, Greedy, Bit Manipulation, Math
"""
