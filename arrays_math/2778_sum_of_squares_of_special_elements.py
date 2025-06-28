"""
LeetCode Problem 2778: Sum of Squares of Special Elements

You are given a 1-indexed array nums of positive integers. An element nums[i] is called special if i divides n where n is the length of the array.

Return the sum of the squares of all special elements.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 50

Example 1:
Input: nums = [1,2,3,4]
Output: 21
Explanation: There are exactly 3 special elements: nums[1], nums[2], and nums[4] since 1 divides 4, 2 divides 4, and 4 divides 4. 
Hence, the sum of the squares is nums[1]^2 + nums[2]^2 + nums[4]^2 = 1 + 4 + 16 = 21.

Example 2:
Input: nums = [2,7,1,19,18,3]
Output: 63
Explanation: There are exactly 4 special elements: nums[1], nums[2], nums[3], and nums[6] since 1 divides 6, 2 divides 6, 3 divides 6, and 6 divides 6.
Hence, the sum of the squares is nums[1]^2 + nums[2]^2 + nums[3]^2 + nums[6]^2 = 4 + 49 + 1 + 9 = 63.

Topics: Array, Math
"""

class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        """
        Approach 1: Direct iteration checking divisibility
        
        Iterate through indices and check if each index divides n.
        Sum squares of elements at special indices.
        
        Time: O(n) - single pass through array
        Space: O(1) - only using constant extra space
        """
        n = len(nums)
        total_sum = 0
        
        # Check each 1-indexed position
        for i in range(1, n + 1):
            if n % i == 0:  # i divides n
                # nums is 0-indexed, so use (i-1)
                total_sum += nums[i - 1] ** 2
        
        return total_sum
    
    def sumOfSquares_divisors(self, nums: list[int]) -> int:
        """
        Approach 2: Find all divisors first, then sum
        
        Find all divisors of n, then sum squares of corresponding elements.
        
        Time: O(sqrt(n) + d) where d is number of divisors
        Space: O(d) for storing divisors
        """
        n = len(nums)
        divisors = []
        
        # Find all divisors of n
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:  # Avoid duplicates for perfect squares
                    divisors.append(n // i)
        
        # Sum squares of elements at divisor positions
        total_sum = 0
        for divisor in divisors:
            total_sum += nums[divisor - 1] ** 2
        
        return total_sum
    
    def sumOfSquares_functional(self, nums: list[int]) -> int:
        """
        Approach 3: Functional programming approach
        
        Use list comprehension and sum function.
        
        Time: O(n)
        Space: O(n) for intermediate list
        """
        n = len(nums)
        return sum(nums[i - 1] ** 2 for i in range(1, n + 1) if n % i == 0)
    
    def sumOfSquares_enumerate(self, nums: list[int]) -> int:
        """
        Approach 4: Using enumerate for cleaner code
        
        Use enumerate to get both index and value.
        
        Time: O(n)
        Space: O(1)
        """
        n = len(nums)
        total_sum = 0
        
        for i, value in enumerate(nums, 1):  # Start enumeration from 1
            if n % i == 0:
                total_sum += value ** 2
        
        return total_sum

def test_sum_of_squares():
    """Test the sum of squares solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.sumOfSquares([1, 2, 3, 4]) == 21
    # Divisors of 4: 1, 2, 4
    # Special elements: nums[1]=1, nums[2]=2, nums[4]=4
    # Sum: 1^2 + 2^2 + 4^2 = 1 + 4 + 16 = 21
    
    # Test case 2: Another example
    assert solution.sumOfSquares([2, 7, 1, 19, 18, 3]) == 63
    # Divisors of 6: 1, 2, 3, 6
    # Special elements: nums[1]=2, nums[2]=7, nums[3]=1, nums[6]=3
    # Sum: 2^2 + 7^2 + 1^2 + 3^2 = 4 + 49 + 1 + 9 = 63
    
    # Test case 3: Single element
    assert solution.sumOfSquares([5]) == 25
    # Only divisor of 1 is 1
    # Sum: 5^2 = 25
    
    # Test case 4: Prime length array
    nums4 = [1, 2, 3, 4, 5]  # length = 5 (prime)
    # Divisors of 5: 1, 5
    # Special elements: nums[1]=1, nums[5]=5
    # Sum: 1^2 + 5^2 = 1 + 25 = 26
    assert solution.sumOfSquares(nums4) == 26
    
    # Test case 5: Perfect square length
    nums5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # length = 9
    # Divisors of 9: 1, 3, 9
    # Special elements: nums[1]=1, nums[3]=3, nums[9]=9
    # Sum: 1^2 + 3^2 + 9^2 = 1 + 9 + 81 = 91
    assert solution.sumOfSquares(nums5) == 91
    
    # Test case 6: Two elements
    assert solution.sumOfSquares([3, 7]) == 58
    # Divisors of 2: 1, 2
    # Special elements: nums[1]=3, nums[2]=7
    # Sum: 3^2 + 7^2 = 9 + 49 = 58
    
    # Test case 7: Highly composite number length
    nums7 = [1] * 12  # length = 12, many divisors
    # Divisors of 12: 1, 2, 3, 4, 6, 12
    # Sum: 6 * (1^2) = 6
    assert solution.sumOfSquares(nums7) == 6
    
    # Test case 8: All same elements
    nums8 = [5, 5, 5, 5, 5, 5]  # length = 6
    # Divisors of 6: 1, 2, 3, 6
    # Special elements: nums[1]=5, nums[2]=5, nums[3]=5, nums[6]=5
    # Sum: 4 * (5^2) = 4 * 25 = 100
    assert solution.sumOfSquares(nums8) == 100
    
    # Compare different approaches
    test_cases = [
        [1, 2, 3, 4],
        [2, 7, 1, 19, 18, 3],
        [5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [3, 7],
        [1] * 12,
        [5, 5, 5, 5, 5, 5]
    ]
    
    for nums in test_cases:
        result1 = solution.sumOfSquares(nums)
        result2 = solution.sumOfSquares_divisors(nums)
        result3 = solution.sumOfSquares_functional(nums)
        result4 = solution.sumOfSquares_enumerate(nums)
        assert result1 == result2 == result3 == result4, \
            f"Mismatch for {nums}: {result1}, {result2}, {result3}, {result4}"
    
    print("All sum of squares tests passed!")

if __name__ == "__main__":
    test_sum_of_squares()
