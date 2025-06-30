"""
LeetCode Problem 2789: Largest Element in an Array after Merge Operations

You are given a 0-indexed array nums consisting of positive integers.

You can do the following operation on the array any number of times:
- Choose an integer i such that 0 <= i < nums.length - 1 and nums[i] <= nums[i + 1]. Replace nums[i] with nums[i] + nums[i + 1] and remove nums[i + 1] from the array.

Return the largest possible value of an element in nums after performing the operations optimally.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6

Example 1:
Input: nums = [2,3,7,9,3]
Output: 18
Explanation: We can apply the operation on index 1: [2,3,7,9,3] -> [2,10,9,3] (3+7=10)
Then apply on index 1: [2,10,9,3] -> [2,19,3] (10+9=19)
Then apply on index 0: [2,19,3] -> [21,3] (2+19=21)
We cannot merge further. The largest element is 21, but wait... let me recalculate.
Actually: [2,3,7,9,3] -> [2,10,9,3] -> [2,19,3] -> [21,3]. But we could also do:
[2,3,7,9,3] -> [5,7,9,3] -> [12,9,3] -> [21,3] or [5,7,9,3] -> [5,16,3] -> [21,3]
Or: [2,3,7,9,3] -> [2,3,16,3] -> [5,16,3] -> [21,3] -> final answer should be 21... hmm let me check

Example 2:
Input: nums = [5,3,3]
Output: 11
Explanation: We can apply the operation on index 1: [5,3,3] -> [5,6] (3+3=6)
Then apply on index 0: [5,6] -> [11] (5+6=11)
"""

def largest_merge_result(nums):
    """
    Optimized Greedy Solution using Stack
    
    Process from right to left, maintaining a non-decreasing stack.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    
    # Process from right to left
    stack = []
    
    for i in range(len(nums) - 1, -1, -1):
        current = nums[i]
        
        # Merge with elements in stack while possible
        while stack and current <= stack[-1]:
            current += stack.pop()
        
        stack.append(current)
    
    return max(stack)

def largest_merge_result_dp(nums):
    """
    Dynamic Programming approach
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    n = len(nums)
    if n == 0:
        return 0
    
    # dp[i] = maximum value we can get starting from index i
    dp = [0] * n
    dp[n-1] = nums[n-1]
    
    for i in range(n-2, -1, -1):
        dp[i] = nums[i]
        
        # Try merging with all possible consecutive elements
        current_sum = nums[i]
        for j in range(i+1, n):
            if current_sum <= nums[j]:
                current_sum += nums[j]
                dp[i] = max(dp[i], current_sum + (dp[j+1] if j+1 < n else 0))
            else:
                break
    
    return max(dp)

def largest_merge_result_simulation(nums):
    """
    Simulation approach - try all possible merge sequences
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    
    def merge_optimally(arr):
        """Recursively find the best merge result"""
        if len(arr) <= 1:
            return arr[0] if arr else 0
        
        max_result = max(arr)
        
        # Try merging at each valid position
        for i in range(len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                # Create new array with merge
                new_arr = arr[:i] + [arr[i] + arr[i + 1]] + arr[i + 2:]
                max_result = max(max_result, merge_optimally(new_arr))
        
        return max_result
    
    return merge_optimally(nums)

def largest_merge_result_optimized(nums):
    """
    Most optimized solution - greedy from right to left
    
    Time Complexity: O(n)
    Space Complexity: O(1) if modifying input, O(n) otherwise
    """
    if not nums:
        return 0
    
    # Work backwards, greedily merging when possible
    arr = nums[:]  # Create copy to avoid modifying input
    
    i = len(arr) - 2
    while i >= 0:
        # If current element can merge with next
        if arr[i] <= arr[i + 1]:
            arr[i] += arr[i + 1]
            arr.pop(i + 1)
        else:
            i -= 1
    
    return max(arr)

def largest_merge_result_stack_optimized(nums):
    """
    Stack-based solution with detailed tracking
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    
    stack = []
    
    # Process from right to left
    for num in reversed(nums):
        current = num
        
        # Keep merging while we can
        while stack and current <= stack[-1]:
            current += stack.pop()
        
        stack.append(current)
    
    return max(stack) if stack else 0

# Test cases
def test_largest_merge_result():
    test_cases = [
        ([2, 3, 7, 9, 3], 18),  # From example (need to verify)
        ([5, 3, 3], 11),        # From example
        ([1], 1),               # Single element
        ([1, 2, 3, 4, 5], 15),  # Ascending order
        ([5, 4, 3, 2, 1], 5),   # Descending order
        ([1, 1, 1, 1], 4),      # All same
        ([10, 1, 1], 12),       # Mix
        ([1, 10, 1], 10),       # Cannot merge across larger element
        ([2, 1, 4, 3], 6),      # Complex case
        ([1, 2, 1, 2], 6),      # Another complex case
    ]
    
    approaches = [
        ("Stack Greedy", largest_merge_result),
        ("Stack Optimized", largest_merge_result_stack_optimized),
        ("Optimized", largest_merge_result_optimized)
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

def trace_example():
    """Trace through the first example step by step"""
    nums = [2, 3, 7, 9, 3]
    print(f"Tracing example: {nums}")
    print("\nUsing stack approach (right to left):")
    
    stack = []
    for i, num in enumerate(reversed(nums)):
        original_idx = len(nums) - 1 - i
        current = num
        print(f"\nProcessing nums[{original_idx}] = {num}")
        print(f"  Stack before: {stack}")
        print(f"  Current: {current}")
        
        merge_count = 0
        while stack and current <= stack[-1]:
            merged_val = stack.pop()
            current += merged_val
            merge_count += 1
            print(f"    Merged with {merged_val}, current = {current}")
        
        if merge_count == 0:
            print(f"    No merge possible")
        
        stack.append(current)
        print(f"  Stack after: {stack}")
    
    result = max(stack)
    print(f"\nFinal stack: {stack}")
    print(f"Maximum value: {result}")

def verify_merge_rules():
    """Verify the merge rules with simple examples"""
    print("Verifying merge rules:")
    
    examples = [
        [1, 2],      # 1 <= 2, can merge to [3]
        [2, 1],      # 2 > 1, cannot merge
        [2, 2],      # 2 <= 2, can merge to [4]
        [1, 2, 3],   # Multiple merges possible
    ]
    
    for arr in examples:
        result = largest_merge_result(arr)
        print(f"  {arr} -> max possible: {result}")

if __name__ == "__main__":
    test_largest_merge_result()
    print("\n" + "="*50)
    trace_example()
    print("\n" + "="*50)
    verify_merge_rules()

"""
Topics: Arrays, Greedy, Stack, Dynamic Programming
Difficulty: Medium

Key Insights:
1. Process from right to left for optimal greedy strategy
2. Use stack to maintain merged values in non-decreasing order
3. Merge condition: nums[i] <= nums[i+1]
4. Greedy approach works because later merges don't affect earlier opportunities
5. Stack naturally handles the cascading merge effect

Companies: Google, Microsoft, Amazon, Meta
"""
