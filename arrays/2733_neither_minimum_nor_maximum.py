"""
2733. Neither Minimum nor Maximum

Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

Return the selected number.

Example 1:
Input: nums = [3,2,1,4]
Output: 2
Explanation: In this example, the minimum value is 1 and the maximum value is 4. Therefore, either 2 or 3 can be valid answers.

Example 2:
Input: nums = [1,2]
Output: -1
Explanation: Since there is no number in nums that is neither the maximum nor the minimum, we cannot select a number that satisfies the given condition. Therefore, we return -1.

Example 3:
Input: nums = [2,1,3]
Output: 2
Explanation: Since 2 is neither the minimum (1) nor the maximum (3), it is a valid answer.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
- All values in nums are distinct.
"""

def neither_min_nor_max(nums: list[int]) -> int:
    """
    Find any number that is neither minimum nor maximum in the array.
    
    Args:
        nums: Array of distinct positive integers
        
    Returns:
        int: Any number that is neither min nor max, or -1 if no such number exists
        
    Time Complexity: O(n) - single pass to find min and max
    Space Complexity: O(1) - using constant extra space
    """
    if len(nums) <= 2:
        return -1
    
    min_val = min(nums)
    max_val = max(nums)
    
    # Find any element that is neither min nor max
    for num in nums:
        if num != min_val and num != max_val:
            return num
    
    return -1

def neither_min_nor_max_one_pass(nums: list[int]) -> int:
    """
    One-pass solution that finds min, max, and a middle value simultaneously.
    
    Args:
        nums: Array of distinct positive integers
        
    Returns:
        int: Any number that is neither min nor max, or -1 if no such number exists
        
    Time Complexity: O(n) - single pass
    Space Complexity: O(1) - constant space
    """
    if len(nums) <= 2:
        return -1
    
    min_val = float('inf')
    max_val = float('-inf')
    candidate = -1
    
    for num in nums:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    # Find any number that is neither min nor max
    for num in nums:
        if num != min_val and num != max_val:
            return num
    
    return -1

def neither_min_nor_max_optimized(nums: list[int]) -> int:
    """
    Optimized solution using partial sorting (finding first 3 elements).
    
    Args:
        nums: Array of distinct positive integers
        
    Returns:
        int: Any number that is neither min nor max, or -1 if no such number exists
        
    Time Complexity: O(1) for small arrays, O(n) worst case
    Space Complexity: O(1) - constant space
    """
    if len(nums) <= 2:
        return -1
    
    # For small arrays, we can check first few elements
    if len(nums) == 3:
        # For exactly 3 elements, the middle one is neither min nor max
        sorted_first_three = sorted(nums)
        return sorted_first_three[1]
    
    # For larger arrays, find min and max, then return any other element
    min_val = min(nums)
    max_val = max(nums)
    
    for num in nums:
        if num != min_val and num != max_val:
            return num
    
    return -1

def neither_min_nor_max_three_elements(nums: list[int]) -> int:
    """
    Solution that only examines first three elements for efficiency.
    
    Args:
        nums: Array of distinct positive integers
        
    Returns:
        int: Any number that is neither min nor max, or -1 if no such number exists
        
    Time Complexity: O(1) - only looks at first 3 elements
    Space Complexity: O(1) - constant space
    """
    if len(nums) <= 2:
        return -1
    
    # Take first three elements and find the middle one
    a, b, c = nums[0], nums[1], nums[2]
    
    # Find the element that is neither min nor max among first 3
    if a < b < c or c < b < a:
        return b
    elif b < a < c or c < a < b:
        return a
    else:  # b < c < a or a < c < b
        return c

# Test cases
def test_neither_min_nor_max():
    test_cases = [
        # Basic test cases
        ([3, 2, 1, 4], 2),     # 2 or 3 are valid
        ([1, 2], -1),          # No valid answer
        ([2, 1, 3], 2),        # 2 is the middle value
        
        # Edge cases
        ([1], -1),             # Single element
        ([5, 1, 3], 3),        # 3 is neither min(1) nor max(5)
        ([10, 5, 15], 5),      # 5 is the middle value
        
        # Larger arrays
        ([1, 2, 3, 4, 5], 2),  # Many valid options (2, 3, 4)
        ([10, 1, 20, 5], 10),  # 10 or 5 are valid
        ([100, 50, 1], 50),    # 50 is the middle value
        
        # Different arrangements
        ([4, 1, 3, 2], 4),     # Any of 4, 3, 2 are valid
        ([7, 9, 8], 8),        # 8 is the middle value
        ([15, 25, 20], 20),    # 20 is the middle value
    ]
    
    print("Testing neither_min_nor_max function:")
    for i, (nums, expected_type) in enumerate(test_cases):
        result1 = neither_min_nor_max(nums)
        result2 = neither_min_nor_max_one_pass(nums)
        result3 = neither_min_nor_max_optimized(nums)
        result4 = neither_min_nor_max_three_elements(nums)
        
        print(f"Test {i+1}: nums={nums}")
        print(f"  Basic: {result1}")
        print(f"  One Pass: {result2}")
        print(f"  Optimized: {result3}")
        print(f"  Three Elements: {result4}")
        
        # Validate results
        def is_valid_result(nums, result):
            if len(nums) <= 2:
                return result == -1
            if result == -1:
                return len(nums) <= 2
            min_val = min(nums)
            max_val = max(nums)
            return result in nums and result != min_val and result != max_val
        
        assert is_valid_result(nums, result1), f"Basic failed for test {i+1}"
        assert is_valid_result(nums, result2), f"One Pass failed for test {i+1}"
        assert is_valid_result(nums, result3), f"Optimized failed for test {i+1}"
        assert is_valid_result(nums, result4), f"Three Elements failed for test {i+1}"
        
        print(f"  ✓ All results are valid\n")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_neither_min_nor_max()

"""
Time Complexity Analysis:
- Basic Solution: O(n) - two passes (min/max + search)
- One Pass: O(n) - single pass to find min/max, then another to find middle
- Optimized: O(n) - similar to basic but with some optimizations for small cases
- Three Elements: O(1) - only examines first 3 elements

Space Complexity Analysis:
- All solutions: O(1) - using constant extra space

Key Insights:
1. For arrays with length <= 2, no valid answer exists
2. For arrays with length >= 3, there's always at least one valid answer
3. We can optimize by only checking the first few elements in some cases
4. The problem allows returning any valid answer, not a specific one
5. Since all values are distinct, we don't need to handle duplicates

Topics: Arrays, Math, Sorting
"""
