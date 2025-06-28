"""
LeetCode Problem 2798: Number of Employees Who Met the Target

There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.

The company requires each employee to work for at least target hours.

Return the number of employees who met the target.

Constraints:
- 1 <= n <= 50
- 0 <= hours[i], target <= 10^5

Example 1:
Input: hours = [0,1,2,3,4], target = 2
Output: 3
Explanation: The company wants each employee to work for at least 2 hours.
- Employee 0 worked for 0 hours and didn't meet the target.
- Employee 1 worked for 1 hour and didn't meet the target.
- Employee 2 worked for 2 hours and met the target.
- Employee 3 worked for 3 hours and met the target.
- Employee 4 worked for 4 hours and met the target.
The number of employees who met the target is 3.

Example 2:
Input: hours = [5,1,4,2,2], target = 6
Output: 0
Explanation: The company wants each employee to work for at least 6 hours.
There are no employees who met the target.

Topics: Array, Counting
"""

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        """
        Approach 1: Simple counting
        
        Count employees whose hours >= target.
        
        Time: O(n) - single pass through array
        Space: O(1) - only using constant extra space
        """
        count = 0
        for hour in hours:
            if hour >= target:
                count += 1
        return count
    
    def numberOfEmployeesWhoMetTarget_functional(self, hours: list[int], target: int) -> int:
        """
        Approach 2: Functional programming approach
        
        Use sum with generator expression for concise code.
        
        Time: O(n)
        Space: O(1)
        """
        return sum(1 for hour in hours if hour >= target)
    
    def numberOfEmployeesWhoMetTarget_filter(self, hours: list[int], target: int) -> int:
        """
        Approach 3: Using filter function
        
        Filter hours that meet target and count them.
        
        Time: O(n)
        Space: O(k) where k is number of employees who met target
        """
        return len(list(filter(lambda hour: hour >= target, hours)))
    
    def numberOfEmployeesWhoMetTarget_comprehension(self, hours: list[int], target: int) -> int:
        """
        Approach 4: List comprehension
        
        Create list of employees who met target and return length.
        
        Time: O(n)
        Space: O(k)
        """
        return len([hour for hour in hours if hour >= target])
    
    def numberOfEmployeesWhoMetTarget_builtin_sum(self, hours: list[int], target: int) -> int:
        """
        Approach 5: Using sum with boolean conversion
        
        Use the fact that True is treated as 1 and False as 0.
        
        Time: O(n)
        Space: O(1)
        """
        return sum(hour >= target for hour in hours)
    
    def numberOfEmployeesWhoMetTarget_enumerated(self, hours: list[int], target: int) -> int:
        """
        Approach 6: Using enumerate for index tracking
        
        Useful if we also need to track which employees met the target.
        
        Time: O(n)
        Space: O(1)
        """
        count = 0
        met_target_employees = []
        
        for i, hour in enumerate(hours):
            if hour >= target:
                count += 1
                met_target_employees.append(i)  # Track employee index
        
        return count

def test_number_of_employees_who_met_target():
    """Test the number of employees who met target solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.numberOfEmployeesWhoMetTarget([0, 1, 2, 3, 4], 2) == 3
    
    # Test case 2: No one meets target
    assert solution.numberOfEmployeesWhoMetTarget([5, 1, 4, 2, 2], 6) == 0
    
    # Test case 3: Everyone meets target
    assert solution.numberOfEmployeesWhoMetTarget([10, 20, 30], 5) == 3
    
    # Test case 4: Target is 0 (everyone meets it)
    assert solution.numberOfEmployeesWhoMetTarget([0, 1, 2], 0) == 3
    
    # Test case 5: Single employee meets target
    assert solution.numberOfEmployeesWhoMetTarget([5], 5) == 1
    
    # Test case 6: Single employee doesn't meet target
    assert solution.numberOfEmployeesWhoMetTarget([3], 5) == 0
    
    # Test case 7: Exact match cases
    assert solution.numberOfEmployeesWhoMetTarget([1, 2, 3, 4, 5], 3) == 3
    # Employees with 3, 4, 5 hours meet target
    
    # Test case 8: All same hours
    assert solution.numberOfEmployeesWhoMetTarget([8, 8, 8, 8], 8) == 4
    assert solution.numberOfEmployeesWhoMetTarget([7, 7, 7], 8) == 0
    
    # Test case 9: Mixed case with zeros
    assert solution.numberOfEmployeesWhoMetTarget([0, 0, 1, 1, 2, 2], 1) == 4
    
    # Test case 10: Large numbers
    assert solution.numberOfEmployeesWhoMetTarget([1000, 500, 2000, 100], 750) == 2
    
    # Compare all approaches
    test_cases = [
        ([0, 1, 2, 3, 4], 2),
        ([5, 1, 4, 2, 2], 6),
        ([10, 20, 30], 5),
        ([0, 1, 2], 0),
        ([5], 5),
        ([3], 5),
        ([1, 2, 3, 4, 5], 3),
        ([8, 8, 8, 8], 8),
        ([7, 7, 7], 8),
        ([0, 0, 1, 1, 2, 2], 1),
        ([1000, 500, 2000, 100], 750)
    ]
    
    for hours, target in test_cases:
        result1 = solution.numberOfEmployeesWhoMetTarget(hours, target)
        result2 = solution.numberOfEmployeesWhoMetTarget_functional(hours, target)
        result3 = solution.numberOfEmployeesWhoMetTarget_filter(hours, target)
        result4 = solution.numberOfEmployeesWhoMetTarget_comprehension(hours, target)
        result5 = solution.numberOfEmployeesWhoMetTarget_builtin_sum(hours, target)
        result6 = solution.numberOfEmployeesWhoMetTarget_enumerated(hours, target)
        
        assert result1 == result2 == result3 == result4 == result5 == result6, \
            f"Mismatch for hours={hours}, target={target}: {result1}, {result2}, {result3}, {result4}, {result5}, {result6}"
    
    # Test edge cases
    assert solution.numberOfEmployeesWhoMetTarget([0], 0) == 1
    assert solution.numberOfEmployeesWhoMetTarget([100000], 100000) == 1
    assert solution.numberOfEmployeesWhoMetTarget([100000], 100001) == 0
    
    # Test performance on larger input
    large_hours = [i for i in range(50)]  # [0, 1, 2, ..., 49]
    assert solution.numberOfEmployeesWhoMetTarget(large_hours, 25) == 25
    assert solution.numberOfEmployeesWhoMetTarget(large_hours, 0) == 50
    assert solution.numberOfEmployeesWhoMetTarget(large_hours, 50) == 0
    
    print("All number of employees who met target tests passed!")

if __name__ == "__main__":
    test_number_of_employees_who_met_target()
