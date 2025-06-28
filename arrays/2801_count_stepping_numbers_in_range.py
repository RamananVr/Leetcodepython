"""
LeetCode Problem 2801: Count Stepping Numbers in Range

Given two positive integers low and high, find the count of stepping numbers in the range [low, high] inclusive.

A stepping number is an integer such that all of its adjacent digits have an absolute difference of exactly 1.
For example, 321 is a stepping number while 421 is not.

Constraints:
- 1 <= low <= high <= 2 * 10^15

Example 1:
Input: low = "1", high = "11"
Output: 10
Explanation: The stepping numbers in the range [1,11] are 1, 2, 3, 4, 5, 6, 7, 8, 9 and 10. There are a total of 10 stepping numbers.

Example 2:
Input: low = "90", high = "101"
Output: 2
Explanation: The stepping numbers in the range [90,101] are 98 and 101. There are a total of 2 stepping numbers.
"""

def count_stepping_numbers(low, high):
    """
    Approach 1: Digit DP (Dynamic Programming)
    
    Use digit DP to count stepping numbers in range.
    For each position, we can only place digits that differ by 1 from the previous digit.
    
    Time Complexity: O(log(high) * 10 * 2 * 2)
    Space Complexity: O(log(high) * 10 * 2 * 2)
    """
    def digit_dp(pos, prev_digit, tight, started, num_str, memo):
        if pos == len(num_str):
            return 1 if started else 0
        
        state = (pos, prev_digit, tight, started)
        if state in memo:
            return memo[state]
        
        limit = int(num_str[pos]) if tight else 9
        result = 0
        
        for digit in range(0, limit + 1):
            new_tight = tight and (digit == limit)
            new_started = started or (digit > 0)
            
            if not started and digit == 0:
                # Leading zero case
                result += digit_dp(pos + 1, -1, new_tight, new_started, num_str, memo)
            elif not started:
                # First non-zero digit
                result += digit_dp(pos + 1, digit, new_tight, new_started, num_str, memo)
            else:
                # Must be stepping number
                if abs(digit - prev_digit) == 1:
                    result += digit_dp(pos + 1, digit, new_tight, new_started, num_str, memo)
        
        memo[state] = result
        return result
    
    def count_up_to(num_str):
        memo = {}
        return digit_dp(0, -1, True, False, num_str, memo)
    
    return count_up_to(high) - count_up_to(str(int(low) - 1))

def count_stepping_numbers_bfs(low, high):
    """
    Approach 2: BFS Generation
    
    Generate all stepping numbers using BFS and count those in range.
    
    Time Complexity: O(2^d) where d is number of digits
    Space Complexity: O(2^d)
    """
    from collections import deque
    
    low_int = int(low)
    high_int = int(high)
    
    if high_int < low_int:
        return 0
    
    count = 0
    queue = deque(range(1, 10))  # Start with single digits 1-9
    
    # Count single digit numbers in range
    for i in range(1, 10):
        if low_int <= i <= high_int:
            count += 1
    
    # Generate multi-digit stepping numbers
    while queue:
        num = queue.popleft()
        
        if num > high_int:
            continue
        
        # Get last digit
        last_digit = num % 10
        
        # Add next stepping numbers
        for next_digit in [last_digit - 1, last_digit + 1]:
            if 0 <= next_digit <= 9:
                next_num = num * 10 + next_digit
                if next_num <= high_int:
                    if next_num >= low_int:
                        count += 1
                    queue.append(next_num)
    
    return count

def count_stepping_numbers_dfs(low, high):
    """
    Approach 3: DFS with Pruning
    
    Use DFS to generate stepping numbers with early pruning.
    
    Time Complexity: O(2^d) where d is number of digits
    Space Complexity: O(d) for recursion stack
    """
    low_int = int(low)
    high_int = int(high)
    
    def dfs(num):
        if num > high_int:
            return 0
        
        count = 1 if num >= low_int else 0
        last_digit = num % 10
        
        # Try adding digits that differ by 1
        for next_digit in [last_digit - 1, last_digit + 1]:
            if 0 <= next_digit <= 9:
                next_num = num * 10 + next_digit
                if next_num <= high_int:
                    count += dfs(next_num)
        
        return count
    
    total = 0
    # Start with each single digit
    for start_digit in range(1, 10):
        if start_digit <= high_int:
            total += dfs(start_digit)
    
    return total

# Test cases
def test_count_stepping_numbers():
    test_cases = [
        ("1", "11", 10),
        ("90", "101", 2),
        ("0", "21", 13),
        ("10", "15", 1),
        ("1", "1", 1)
    ]
    
    for low, high, expected in test_cases:
        result1 = count_stepping_numbers(low, high)
        result2 = count_stepping_numbers_bfs(low, high)
        result3 = count_stepping_numbers_dfs(low, high)
        
        print(f"Input: low={low}, high={high}")
        print(f"Expected: {expected}")
        print(f"Digit DP: {result1}")
        print(f"BFS: {result2}")
        print(f"DFS: {result3}")
        print(f"✓ Passed: {result1 == expected and result2 == expected and result3 == expected}\n")

if __name__ == "__main__":
    test_count_stepping_numbers()

"""
Topics: Arrays, Dynamic Programming, Math
Difficulty: Hard

Key Insights:
1. Use digit DP to efficiently count numbers with constraints
2. BFS can generate all stepping numbers level by level
3. DFS with pruning can be more memory efficient
4. Handle leading zeros carefully in digit DP
5. Single digit numbers (1-9) are all stepping numbers

Companies: Google, Amazon, Microsoft
"""
