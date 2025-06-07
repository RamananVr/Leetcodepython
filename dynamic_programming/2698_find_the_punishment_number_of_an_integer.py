"""
2698. Find the Punishment Number of an Integer

PROBLEM STATEMENT:
Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers i such that:
- 1 <= i <= n
- The decimal representation of i * i can be partitioned into one or more contiguous substrings 
  such that the sum of the integer values of these substrings equals i.

EXAMPLES:
Example 1:
Input: n = 10
Output: 182
Explanation: There are exactly 4 integers i such that 1 <= i <= 10 and the sum of the squares equals to i itself.
i = 1: 1 * 1 = 1, which can be partitioned as [1]. Sum = 1 = i.
i = 9: 9 * 9 = 81, which can be partitioned as [8, 1]. Sum = 8 + 1 = 9 = i.
i = 10: 10 * 10 = 100, which can be partitioned as [10, 0]. Sum = 10 + 0 = 10 = i.
               or [1, 0, 0]. Sum = 1 + 0 + 0 = 1 ≠ i.
               or [100]. Sum = 100 ≠ i.
So the punishment number of 10 is 1^2 + 9^2 + 10^2 = 1 + 81 + 100 = 182.

Example 2:
Input: n = 37
Output: 1478
Explanation: There are exactly 4 integers i such that 1 <= i <= 37 and the sum of the squares equals to i itself.

CONSTRAINTS:
- 1 <= n <= 1000
"""

def punishment_number(n):
    """
    Calculate the punishment number for integer n.
    
    Args:
        n: Positive integer
    
    Returns:
        Sum of squares of all valid integers
    """
    def can_partition(s, target, index=0, current_sum=0):
        """
        Check if string s can be partitioned such that sum equals target.
        
        Args:
            s: String representation of the square
            target: Target sum to achieve
            index: Current position in string
            current_sum: Current sum of partitions
        
        Returns:
            True if valid partition exists, False otherwise
        """
        # Base case: reached end of string
        if index == len(s):
            return current_sum == target
        
        # Try all possible partitions starting from current index
        for end in range(index + 1, len(s) + 1):
            substring = s[index:end]
            # Skip if substring has leading zeros (except "0" itself)
            if len(substring) > 1 and substring[0] == '0':
                continue
            
            value = int(substring)
            # Early termination if current sum exceeds target
            if current_sum + value > target:
                continue
            
            # Recursively check remaining string
            if can_partition(s, target, end, current_sum + value):
                return True
        
        return False
    
    def is_punishment_number(i):
        """
        Check if i satisfies the punishment number condition.
        
        Args:
            i: Integer to check
        
        Returns:
            True if i is a punishment number, False otherwise
        """
        square = i * i
        square_str = str(square)
        return can_partition(square_str, i)
    
    total = 0
    for i in range(1, n + 1):
        if is_punishment_number(i):
            total += i * i
    
    return total

def punishment_number_with_memoization(n):
    """
    Optimized version with memoization for partition checking.
    
    Args:
        n: Positive integer
    
    Returns:
        Sum of squares of all valid integers
    """
    def can_partition_memo(s, target, index=0, current_sum=0, memo=None):
        if memo is None:
            memo = {}
        
        # Create memoization key
        key = (index, current_sum)
        if key in memo:
            return memo[key]
        
        # Base case
        if index == len(s):
            result = (current_sum == target)
            memo[key] = result
            return result
        
        # Try all partitions
        for end in range(index + 1, len(s) + 1):
            substring = s[index:end]
            if len(substring) > 1 and substring[0] == '0':
                continue
            
            value = int(substring)
            if current_sum + value > target:
                continue
            
            if can_partition_memo(s, target, end, current_sum + value, memo):
                memo[key] = True
                return True
        
        memo[key] = False
        return False
    
    total = 0
    for i in range(1, n + 1):
        square_str = str(i * i)
        if can_partition_memo(square_str, i):
            total += i * i
    
    return total

def find_all_punishment_numbers(n):
    """
    Find all individual punishment numbers up to n.
    
    Args:
        n: Positive integer
    
    Returns:
        List of all punishment numbers and their squares
    """
    def can_partition(s, target, index=0, current_sum=0):
        if index == len(s):
            return current_sum == target
        
        for end in range(index + 1, len(s) + 1):
            substring = s[index:end]
            if len(substring) > 1 and substring[0] == '0':
                continue
            
            value = int(substring)
            if current_sum + value > target:
                continue
            
            if can_partition(s, target, end, current_sum + value):
                return True
        
        return False
    
    punishment_numbers = []
    
    for i in range(1, n + 1):
        square = i * i
        square_str = str(square)
        if can_partition(square_str, i):
            punishment_numbers.append((i, square))
    
    return punishment_numbers

def find_partition_ways(square_str, target):
    """
    Find all ways to partition a square string to sum to target.
    
    Args:
        square_str: String representation of the square
        target: Target sum
    
    Returns:
        List of all valid partitions
    """
    def backtrack(index, current_partition, current_sum):
        if index == len(square_str):
            if current_sum == target:
                partitions.append(current_partition.copy())
            return
        
        for end in range(index + 1, len(square_str) + 1):
            substring = square_str[index:end]
            if len(substring) > 1 and substring[0] == '0':
                continue
            
            value = int(substring)
            if current_sum + value > target:
                continue
            
            current_partition.append(value)
            backtrack(end, current_partition, current_sum + value)
            current_partition.pop()
    
    partitions = []
    backtrack(0, [], 0)
    return partitions

def test_punishment_number():
    """Test the punishment number implementation."""
    
    # Test 1: Example 1
    n1 = 10
    result1 = punishment_number(n1)
    assert result1 == 182
    assert result1 == punishment_number_with_memoization(n1)
    
    # Verify individual numbers for n=10
    punishment_nums = find_all_punishment_numbers(10)
    expected_nums = [(1, 1), (9, 81), (10, 100)]
    assert punishment_nums == expected_nums
    
    # Test 2: Example 2
    n2 = 37
    result2 = punishment_number(n2)
    assert result2 == 1478
    assert result2 == punishment_number_with_memoization(n2)
    
    # Test 3: Small cases
    assert punishment_number(1) == 1   # Only 1
    assert punishment_number(9) == 82  # 1 + 81
    
    # Test 4: Check specific numbers
    # 1: 1^2 = 1, [1] -> 1 ✓
    assert find_partition_ways("1", 1) == [[1]]
    
    # 9: 9^2 = 81, [8,1] -> 9 ✓
    partitions_9 = find_partition_ways("81", 9)
    assert [8, 1] in partitions_9
    
    # 10: 10^2 = 100, [10,0] -> 10 ✓
    partitions_10 = find_partition_ways("100", 10)
    assert [10, 0] in partitions_10
    assert [1, 0, 0] in partitions_10  # This sums to 1, not 10
    
    # Test 5: More complex cases
    # Let's check 45: 45^2 = 2025
    # Can we partition "2025" to sum to 45?
    # [20, 25] = 45 ✓
    partitions_45 = find_partition_ways("2025", 45)
    if [20, 25] in partitions_45:
        print("45 is a punishment number")
    
    # Test 6: Check 55: 55^2 = 3025
    # [30, 25] = 55 ✓
    partitions_55 = find_partition_ways("3025", 55)
    if [30, 25] in partitions_55:
        print("55 is a punishment number")
    
    # Test 7: Verify some known punishment numbers
    known_punishment_numbers = [1, 9, 10, 36, 45, 55, 82, 91, 99, 100]
    
    for num in known_punishment_numbers[:5]:  # Test first few
        square_str = str(num * num)
        partitions = find_partition_ways(square_str, num)
        assert len(partitions) > 0, f"{num} should be a punishment number"
    
    # Test 8: Edge cases
    # Check that leading zeros are handled correctly
    # 100: 100^2 = 10000
    # Valid: [100, 0, 0] -> 100 ✓
    # Invalid: [01, 0, 0, 0] (leading zero)
    partitions_100 = find_partition_ways("10000", 100)
    valid_partitions = [p for p in partitions_100 if sum(p) == 100]
    assert len(valid_partitions) > 0
    
    print("All test cases passed!")

def analyze_punishment_numbers(max_n=100):
    """Analyze punishment numbers up to max_n."""
    
    print(f"Analysis of punishment numbers up to {max_n}")
    print("=" * 50)
    
    all_punishment_nums = find_all_punishment_numbers(max_n)
    
    print(f"Found {len(all_punishment_nums)} punishment numbers:")
    
    total_sum = 0
    for i, (num, square) in enumerate(all_punishment_nums, 1):
        partitions = find_partition_ways(str(square), num)
        total_sum += square
        
        print(f"{i:2d}. i={num:3d}, i²={square:5d}, partitions: {partitions[0] if partitions else 'None'}")
    
    print(f"\nTotal punishment number for {max_n}: {total_sum}")
    
    # Verify with our function
    calculated = punishment_number(max_n)
    print(f"Function result: {calculated}")
    print(f"Match: {total_sum == calculated}")

if __name__ == "__main__":
    test_punishment_number()
    analyze_punishment_numbers(50)

"""
COMPLEXITY ANALYSIS:
- Time Complexity: O(n * 2^d) where n is the input and d is the number of digits in i²
  - For each i from 1 to n, we check all possible partitions of str(i²)
  - Number of partitions is at most 2^(d-1) where d is length of str(i²)
- Space Complexity: O(d) for recursion depth where d is number of digits

TOPICS: Dynamic Programming, Backtracking, String Partitioning, Number Theory

KEY INSIGHTS:
1. Partition problem can be solved with backtracking and memoization
2. Early termination when current sum exceeds target improves efficiency
3. Leading zeros must be handled carefully (only "0" is valid, not "01", "001", etc.)
4. The problem combines number theory with string manipulation
5. Some numbers have multiple valid partitions, but we only need to find one
"""
