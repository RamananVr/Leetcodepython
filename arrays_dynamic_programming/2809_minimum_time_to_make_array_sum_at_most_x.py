"""
LeetCode Problem 2809: Minimum Time to Make Array Sum at Most x

You are given two 0-indexed integer arrays nums1 and nums2 of equal length. Every second, for all indices 0 <= i < nums1.length, value of nums1[i] is increased by nums2[i]. After this, you can do at most one operation:

Choose an index 0 <= i < nums1.length and set nums1[i] to 0.

You are also given an integer x. Return the minimum time in which you can make the sum of all elements of nums1 to be less than or equal to x, or -1 if this is impossible.

Constraints:
- 1 <= nums1.length == nums2.length <= 1000
- 1 <= nums1[i] <= 10^3
- 0 <= nums2[i] <= 10^3
- 1 <= x <= 10^6

Example 1:
Input: nums1 = [1,2,3], nums2 = [1,2,3], x = 4
Output: 3
Explanation: 
For the 1st second, we apply the operation on i = 0. After that nums1 = [0,4,6].
For the 2nd second, we apply the operation on i = 1. After that nums1 = [1,0,9].
For the 3rd second, we apply the operation on i = 2. After that nums1 = [2,2,0].
Now sum = 4. It can be proven that these operations are optimal, so we return 3.

Example 2:
Input: nums1 = [1,2,3], nums2 = [0,0,0], x = 4
Output: -1
Explanation: It can be proven that the sum of nums1 will always be greater than x, no matter which operations we perform.
"""

def minimum_time_to_make_array_sum_at_most_x(nums1, nums2, x):
    """
    Approach 1: Dynamic Programming with Sorting
    
    Sort by nums2 values and use DP to find optimal removal sequence.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    n = len(nums1)
    
    # Sort indices by nums2 values (we should remove high increment values first)
    indices = sorted(range(n), key=lambda i: nums2[i])
    
    # Initial sum
    sum1 = sum(nums1)
    sum2 = sum(nums2)
    
    # If already satisfies condition
    if sum1 <= x:
        return 0
    
    # If sum2 is 0, we can't reduce the sum further
    if sum2 == 0:
        return -1 if sum1 > x else 0
    
    # DP: dp[i][j] = minimum sum after considering first i elements and removing j elements
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        idx = indices[i - 1]
        for j in range(i + 1):
            # Don't remove element idx
            if j <= i - 1:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
            
            # Remove element idx at time j
            if j > 0 and dp[i-1][j-1] != float('inf'):
                # When we remove at time j, element has increased by nums2[idx] * j
                removed_value = nums1[idx] + nums2[idx] * j
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + removed_value)
    
    # Find minimum time
    for t in range(n + 1):
        for j in range(t + 1):
            if dp[n][j] != float('inf'):
                # Total sum at time t with j removals
                current_sum = sum1 + sum2 * t - dp[n][j]
                if current_sum <= x:
                    return t
    
    return -1

def minimum_time_to_make_array_sum_at_most_x_optimized(nums1, nums2, x):
    """
    Approach 2: Optimized DP
    
    More efficient DP implementation.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    n = len(nums1)
    
    # Create pairs and sort by nums2 values
    pairs = sorted(zip(nums1, nums2), key=lambda p: p[1])
    
    sum1 = sum(nums1)
    sum2 = sum(nums2)
    
    if sum1 <= x:
        return 0
    
    # DP: dp[j] = maximum reduction possible with j removals
    dp = [0] * (n + 1)
    
    for a, b in pairs:
        # Process in reverse order to avoid using updated values
        for j in range(len(dp) - 1, 0, -1):
            # Remove current element at time j
            # Reduction = a + b * j (initial value + increments)
            dp[j] = max(dp[j], dp[j-1] + a + b * j)
    
    # Check each possible time
    for t in range(n + 1):
        # Sum at time t = initial_sum + increments * t - max_reduction
        current_sum = sum1 + sum2 * t - dp[t]
        if current_sum <= x:
            return t
    
    return -1

def minimum_time_to_make_array_sum_at_most_x_greedy(nums1, nums2, x):
    """
    Approach 3: Greedy with Binary Search
    
    Use greedy strategy with binary search on time.
    
    Time Complexity: O(n^2 * log(time_limit))
    Space Complexity: O(n)
    """
    n = len(nums1)
    sum1 = sum(nums1)
    sum2 = sum(nums2)
    
    if sum1 <= x:
        return 0
    
    def can_achieve_in_time(time_limit):
        """Check if we can achieve sum <= x in given time"""
        # Create pairs and sort by nums2 (descending for greedy removal)
        pairs = [(nums1[i], nums2[i], i) for i in range(n)]
        pairs.sort(key=lambda p: p[1], reverse=True)
        
        # Try removing elements greedily
        current_sum = sum1 + sum2 * time_limit
        removals = 0
        
        for a, b, idx in pairs:
            if removals >= time_limit:
                break
            
            # If we remove this element at time (removals + 1)
            removal_time = removals + 1
            if removal_time <= time_limit:
                reduction = a + b * removal_time
                current_sum -= reduction
                removals += 1
                
                if current_sum <= x:
                    return True
        
        return current_sum <= x
    
    # Binary search on time
    left, right = 0, n
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if can_achieve_in_time(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result

def minimum_time_to_make_array_sum_at_most_x_simulation(nums1, nums2, x):
    """
    Approach 4: Direct Simulation (Brute Force for Small Inputs)
    
    Simulate the process directly for verification.
    
    Time Complexity: O(n! * n) in worst case
    Space Complexity: O(n)
    """
    n = len(nums1)
    
    if sum(nums1) <= x:
        return 0
    
    # Try all possible sequences of removals
    from itertools import permutations
    
    min_time = float('inf')
    
    # Try different numbers of removals
    for num_removals in range(1, n + 1):
        # Try all permutations of removing num_removals elements
        for indices in permutations(range(n), num_removals):
            # Simulate the process
            current_nums1 = nums1[:]
            current_time = 0
            
            for removal_idx in indices:
                current_time += 1
                
                # Increment all elements
                for i in range(n):
                    current_nums1[i] += nums2[i]
                
                # Remove the chosen element
                current_nums1[removal_idx] = 0
                
                # Check if condition is satisfied
                if sum(current_nums1) <= x:
                    min_time = min(min_time, current_time)
                    break
            
            if min_time <= num_removals:
                break
        
        if min_time <= num_removals:
            break
    
    return min_time if min_time != float('inf') else -1

def minimum_time_to_make_array_sum_at_most_x_memoization(nums1, nums2, x):
    """
    Approach 5: Memoized Recursion
    
    Use memoization to avoid recomputing subproblems.
    
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n * 2^n)
    """
    n = len(nums1)
    
    # Memoization: (mask, time) -> minimum sum achievable
    memo = {}
    
    def dp(mask, time):
        """
        mask: bitmask representing which elements are removed
        time: current time
        Returns: minimum sum achievable
        """
        if (mask, time) in memo:
            return memo[(mask, time)]
        
        # Calculate current sum
        current_sum = 0
        for i in range(n):
            if mask & (1 << i):  # Element i is removed
                continue
            current_sum += nums1[i] + nums2[i] * time
        
        if current_sum <= x:
            memo[(mask, time)] = current_sum
            return current_sum
        
        if time >= n:  # Can't remove more elements
            memo[(mask, time)] = current_sum
            return current_sum
        
        # Try removing any unremoved element at next time step
        min_sum = current_sum
        for i in range(n):
            if not (mask & (1 << i)):  # Element i not yet removed
                new_mask = mask | (1 << i)
                result = dp(new_mask, time + 1)
                min_sum = min(min_sum, result)
        
        memo[(mask, time)] = min_sum
        return min_sum
    
    # Try each possible ending time
    for t in range(n + 1):
        if dp(0, 0) <= x:
            return 0
        
        # Check if we can achieve target in exactly t steps
        initial_sum = sum(nums1)
        final_sum = dp(0, 0)
        
        if final_sum <= x:
            return t
    
    return -1

# Test cases
def test_minimum_time_to_make_array_sum_at_most_x():
    test_cases = [
        ([1, 2, 3], [1, 2, 3], 4, 3),
        ([1, 2, 3], [0, 0, 0], 4, -1),
        ([2, 1], [3, 4], 3, 1),
        ([1, 1, 1], [1, 1, 1], 2, 1),
        ([5], [1], 4, -1),
        ([1], [0], 1, 0),
        ([3, 1, 4], [2, 1, 3], 8, 2)
    ]
    
    approaches = [
        ("DP with Sorting", minimum_time_to_make_array_sum_at_most_x),
        ("Optimized DP", minimum_time_to_make_array_sum_at_most_x_optimized),
        ("Greedy Binary Search", minimum_time_to_make_array_sum_at_most_x_greedy)
    ]
    
    for approach_name, func in approaches:
        print(f"Testing {approach_name} approach:")
        all_passed = True
        
        for nums1, nums2, x, expected in test_cases:
            try:
                result = func(nums1[:], nums2[:], x)
                passed = result == expected
                if not passed:
                    all_passed = False
                
                print(f"  Input: nums1={nums1}, nums2={nums2}, x={x}")
                print(f"  Expected: {expected}, Got: {result}")
                print(f"  {'✓' if passed else '✗'}")
            except Exception as e:
                print(f"  Input: nums1={nums1}, nums2={nums2}, x={x}")
                print(f"  Error: {e}")
                print(f"  ✗")
                all_passed = False
        
        print(f"  Overall: {'✓ All Passed' if all_passed else '✗ Some Failed'}\n")

if __name__ == "__main__":
    test_minimum_time_to_make_array_sum_at_most_x()

"""
Topics: Arrays, Dynamic Programming, Greedy, Binary Search
Difficulty: Hard

Key Insights:
1. Elements with higher increment rates should be removed first
2. DP tracks maximum reduction possible with k removals
3. Sort by nums2 values for optimal removal order
4. Binary search can optimize the time search
5. Trade-off between removal timing and accumulated increments

Companies: Google, Microsoft, Amazon, Meta
"""
