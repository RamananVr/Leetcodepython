# filepath: q:\source\AgentGeneratedLeetcode\strings\2719_count_of_integers.py
"""
LeetCode Question #2719: Count of Integers

Problem Statement:
You are given two numeric strings `num1` and `num2` and two integers `min_sum` and `max_sum`. We call an integer `x` good if:
- `num1 <= x <= num2`
- `min_sum <= digit_sum(x) <= max_sum`

Return the number of good integers. Since the answer may be large, return it modulo `10^9 + 7`.

Note that `digit_sum(x)` denotes the sum of the digits of `x`.

Constraints:
- `1 <= num1 <= num2 < 10^22`
- `1 <= min_sum <= max_sum <= 400`

Example:
Input: num1 = "1", num2 = "12", min_sum = 1, max_sum = 8
Output: 11
Explanation: All integers from 1 to 12 have digit sum between 1 and 8, so we return 11.

Input: num1 = "1", num2 = "5", min_sum = 1, max_sum = 5
Output: 5
Explanation: All integers from 1 to 5 have digit sum between 1 and 5, so we return 5.
"""

def count(num1, num2, min_sum, max_sum):
    """
    Count integers between num1 and num2 with digit sum in [min_sum, max_sum].
    
    Args:
        num1: String representing the lower bound
        num2: String representing the upper bound
        min_sum: Minimum digit sum allowed
        max_sum: Maximum digit sum allowed
    
    Returns:
        Number of good integers modulo 10^9 + 7
    """
    MOD = 10**9 + 7
    
    def digit_dp(num_str):
        """
        Count numbers <= num_str with digit sum in [min_sum, max_sum]
        """
        n = len(num_str)
        memo = {}
        
        def dp(pos, sum_so_far, is_limit, is_num):
            if pos == n:
                return 1 if is_num and min_sum <= sum_so_far <= max_sum else 0
            
            if (pos, sum_so_far, is_limit, is_num) in memo:
                return memo[(pos, sum_so_far, is_limit, is_num)]
            
            result = 0
            
            # Option 1: Don't place a digit (leading zeros)
            if not is_num:
                result = dp(pos + 1, sum_so_far, False, False)
            
            # Option 2: Place a digit
            start = 1 if not is_num else 0
            limit = int(num_str[pos]) if is_limit else 9
            
            for digit in range(start, limit + 1):
                new_sum = sum_so_far + digit
                if new_sum <= max_sum:  # Pruning
                    result = (result + dp(pos + 1, new_sum, 
                                        is_limit and digit == limit, True)) % MOD
            
            memo[(pos, sum_so_far, is_limit, is_num)] = result
            return result
        
        return dp(0, 0, True, False)
    
    # Count for num2 - Count for (num1-1)
    count_num2 = digit_dp(num2)
    
    # Calculate num1 - 1
    num1_minus_1 = str(int(num1) - 1) if int(num1) > 0 else "0"
    count_num1_minus_1 = digit_dp(num1_minus_1) if int(num1) > 0 else 0
    
    return (count_num2 - count_num1_minus_1) % MOD

def count_brute_force(num1, num2, min_sum, max_sum):
    """
    Brute force approach for small ranges (for testing).
    
    Args:
        num1: String representing the lower bound
        num2: String representing the upper bound
        min_sum: Minimum digit sum allowed
        max_sum: Maximum digit sum allowed
    
    Returns:
        Number of good integers modulo 10^9 + 7
    """
    MOD = 10**9 + 7
    count_good = 0
    
    start = int(num1)
    end = int(num2)
    
    # Only use for small ranges to avoid timeout
    if end - start > 10000:
        return count(num1, num2, min_sum, max_sum)
    
    for num in range(start, end + 1):
        digit_sum = sum(int(digit) for digit in str(num))
        if min_sum <= digit_sum <= max_sum:
            count_good = (count_good + 1) % MOD
    
    return count_good

def count_optimized(num1, num2, min_sum, max_sum):
    """
    Optimized digit DP with better memory usage.
    
    Args:
        num1: String representing the lower bound
        num2: String representing the upper bound
        min_sum: Minimum digit sum allowed
        max_sum: Maximum digit sum allowed
    
    Returns:
        Number of good integers modulo 10^9 + 7
    """
    MOD = 10**9 + 7
    
    def count_up_to(num_str):
        if not num_str or num_str == "0":
            return 0
            
        n = len(num_str)
        # dp[pos][sum][tight][started]
        dp = {}
        
        def solve(pos, current_sum, tight, started):
            if pos == n:
                return 1 if started and min_sum <= current_sum <= max_sum else 0
            
            if (pos, current_sum, tight, started) in dp:
                return dp[(pos, current_sum, tight, started)]
            
            limit = int(num_str[pos]) if tight else 9
            result = 0
            
            for digit in range(0, limit + 1):
                new_tight = tight and (digit == limit)
                new_started = started or (digit > 0)
                new_sum = current_sum + digit if new_started else 0
                
                if new_sum <= max_sum:  # Early pruning
                    result = (result + solve(pos + 1, new_sum, new_tight, new_started)) % MOD
            
            dp[(pos, current_sum, tight, started)] = result
            return result
        
        return solve(0, 0, True, False)
    
    # Count numbers <= num2 with valid digit sum
    count2 = count_up_to(num2)
    
    # Count numbers <= num1-1 with valid digit sum
    num1_int = int(num1)
    if num1_int > 0:
        count1 = count_up_to(str(num1_int - 1))
    else:
        count1 = 0
    
    return (count2 - count1) % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "1"
    num2 = "12"
    min_sum = 1
    max_sum = 8
    result = count(num1, num2, min_sum, max_sum)
    print(f"Test 1 - Expected: 11, Got: {result}")
    assert result == 11
    
    # Test Case 2
    num1 = "1"
    num2 = "5"
    min_sum = 1
    max_sum = 5
    result = count(num1, num2, min_sum, max_sum)
    print(f"Test 2 - Expected: 5, Got: {result}")
    assert result == 5
    
    # Test Case 3
    num1 = "10"
    num2 = "20"
    min_sum = 2
    max_sum = 5
    result = count(num1, num2, min_sum, max_sum)
    print(f"Test 3 - Expected: 6, Got: {result}")
    assert result == 6  # 11, 12, 13, 14, 20
    
    # Test Case 4 - Single number
    num1 = "5"
    num2 = "5"
    min_sum = 5
    max_sum = 5
    result = count(num1, num2, min_sum, max_sum)
    print(f"Test 4 - Expected: 1, Got: {result}")
    assert result == 1
    
    # Test Case 5 - No valid numbers
    num1 = "1"
    num2 = "9"
    min_sum = 15
    max_sum = 20
    result = count(num1, num2, min_sum, max_sum)
    print(f"Test 5 - Expected: 0, Got: {result}")
    assert result == 0
    
    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

Digit DP Solution:
1. Time Complexity: O(n * max_sum * 2 * 2) where n is the number of digits
   - For each position, we have max_sum possible sums, 2 tight states, 2 started states
   - Each state is computed at most once due to memoization

2. Space Complexity: O(n * max_sum)
   - Memoization table stores states for position, sum, tight, and started flags

Brute Force Solution:
1. Time Complexity: O((num2 - num1) * log(num2))
   - For each number in range, calculate digit sum
   - Only practical for small ranges

2. Space Complexity: O(1)

Key Insights:
- Use digit DP to count numbers with constraints
- Handle leading zeros carefully with the 'started' flag
- Prune states where current sum exceeds max_sum
- Use inclusion-exclusion: count(<=num2) - count(<=num1-1)

Topic: Dynamic Programming, Digit DP, String Processing
"""
