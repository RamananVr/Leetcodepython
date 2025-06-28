"""
LeetCode Problem 2769: Find the Maximum Achievable Number

You are given two integers, num and t.

An integer x is called achievable if it can become equal to num after applying the following operation at most t times:
- Increase or decrease x by 1.

Return the maximum achievable number. It can be proven that there exists a unique maximum achievable number.

Constraints:
- 1 <= num, t <= 50

Example 1:
Input: num = 4, t = 1
Output: 6
Explanation: The maximum achievable number is x = 6; it can become equal to num after performing this operation once: 6 - 2 = 4.

Example 2:
Input: num = 3, t = 2
Output: 7
Explanation: The maximum achievable number is x = 7; it can become equal to num after performing this operation twice: 7 - 2 - 2 = 3.

Topics: Math
"""

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        """
        Approach 1: Mathematical Analysis
        
        To maximize x, we want to start as far as possible from num
        while still being able to reach num in t operations.
        
        If we start at x and need to reach num in t operations:
        - We can decrease x by at most t (using all operations to decrease)
        - So the minimum value we can reach from x is (x - t)
        - For this to equal num: x - t = num
        - Therefore: x = num + t
        
        But we can also think of it as: we have t operations to get closer,
        so we can start t steps away in the direction that maximizes x.
        Since we want to maximize x, we start above num.
        
        Actually, the maximum x is when we can reach num by decreasing x by t:
        x - t = num  =>  x = num + t
        
        But wait, we can be even more clever:
        We can start at x, decrease it by some amount, then increase it,
        but that would waste operations. The optimal strategy is to
        start at x = num + t and decrease by t to reach num.
        
        Actually, let's think more carefully:
        We want the maximum x such that |x - num| <= t
        Since we want to maximize x: x = num + t
        
        Time: O(1)
        Space: O(1)
        """
        return num + t
    
    def theMaximumAchievableX_simulation(self, num: int, t: int) -> int:
        """
        Approach 2: Verify by simulation
        
        Try different values of x and check if we can reach num in t operations.
        
        Time: O(t) - try values from num to num + t
        Space: O(1)
        """
        # Try values from largest possible down
        for x in range(num + t, num - 1, -1):
            # Check if we can reach num from x in exactly t operations
            diff = abs(x - num)
            if diff <= t:
                # We can reach num from x
                return x
        
        return num  # Fallback, should not reach here
    
    def theMaximumAchievableX_explanation(self, num: int, t: int) -> int:
        """
        Approach 3: Step by step explanation
        
        The key insight is that we want to maximize our starting position x
        while ensuring we can still reach num within t operations.
        
        If we start at position x:
        - We need |x - num| <= t to reach num
        - To maximize x, we want x > num (start above target)
        - So we want x - num <= t
        - Therefore x <= num + t
        - The maximum value is x = num + t
        
        Time: O(1)
        Space: O(1)
        """
        # The maximum achievable x is simply num + t
        # because we can start at (num + t) and decrease by t to reach num
        return num + t

def test_maximum_achievable_number():
    """Test the maximum achievable number solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.theMaximumAchievableX(4, 1) == 6
    
    # Test case 2: Multiple operations
    assert solution.theMaximumAchievableX(3, 2) == 7
    
    # Test case 3: No operations
    assert solution.theMaximumAchievableX(5, 0) == 5
    
    # Test case 4: Large number of operations
    assert solution.theMaximumAchievableX(10, 15) == 25
    
    # Test case 5: Minimum values
    assert solution.theMaximumAchievableX(1, 1) == 3
    
    # Test case 6: Equal num and t
    assert solution.theMaximumAchievableX(7, 7) == 14
    
    # Test case 7: Large t
    assert solution.theMaximumAchievableX(20, 30) == 50
    
    # Verify with simulation approach
    test_cases = [
        (4, 1),
        (3, 2),
        (5, 0),
        (1, 1),
        (7, 7),
        (10, 5)
    ]
    
    for num, t in test_cases:
        result1 = solution.theMaximumAchievableX(num, t)
        result2 = solution.theMaximumAchievableX_simulation(num, t)
        result3 = solution.theMaximumAchievableX_explanation(num, t)
        assert result1 == result2 == result3, f"Mismatch for num={num}, t={t}: {result1}, {result2}, {result3}"
    
    # Additional verification: check that the result actually works
    for num, t in test_cases:
        max_x = solution.theMaximumAchievableX(num, t)
        # Verify we can reach num from max_x in t operations
        assert abs(max_x - num) <= t, f"Cannot reach {num} from {max_x} in {t} operations"
        
        # Verify that max_x + 1 would not work
        if t < 50:  # Avoid overflow in test
            next_x = max_x + 1
            assert abs(next_x - num) > t, f"Should not be able to reach {num} from {next_x} in {t} operations"
    
    print("All maximum achievable number tests passed!")

if __name__ == "__main__":
    test_maximum_achievable_number()
