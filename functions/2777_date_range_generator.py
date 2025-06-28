"""
LeetCode Problem 2777: Date Range Generator

Write a generator function that yields dates between start and end (inclusive).

The function should accept two parameters:
- start: A Date object representing the start date
- end: A Date object representing the end date

The generator should yield Date objects for each day in the range.

Constraints:
- start and end are valid Date objects
- start <= end
- The range can span multiple years

Example 1:
Input: start = Date('2023-01-01'), end = Date('2023-01-03')
Output: [Date('2023-01-01'), Date('2023-01-02'), Date('2023-01-03')]

Example 2:
Input: start = Date('2023-12-30'), end = Date('2024-01-02')
Output: [Date('2023-12-30'), Date('2023-12-31'), Date('2024-01-01'), Date('2024-01-02')]

Topics: Generator, Date Manipulation, Iteration
"""

from datetime import datetime, timedelta
from typing import Iterator

class Solution:
    def dateRangeGenerator(self, start: datetime, end: datetime) -> Iterator[datetime]:
        """
        Approach 1: Simple Generator with timedelta
        
        Yield dates from start to end by incrementing by one day.
        
        Time: O(n) where n is number of days in range
        Space: O(1) - generator uses constant space
        """
        current = start
        while current <= end:
            yield current
            current += timedelta(days=1)
    
    def dateRangeGenerator_list(self, start: datetime, end: datetime) -> list[datetime]:
        """
        Approach 2: Return list instead of generator
        
        Create and return a list of all dates in range.
        
        Time: O(n)
        Space: O(n) - stores all dates in memory
        """
        dates = []
        current = start
        while current <= end:
            dates.append(current)
            current += timedelta(days=1)
        return dates
    
    def dateRangeGenerator_optimized(self, start: datetime, end: datetime) -> Iterator[datetime]:
        """
        Approach 3: Optimized generator with day calculation
        
        Calculate total days first, then generate dates.
        
        Time: O(n)
        Space: O(1)
        """
        total_days = (end - start).days + 1
        
        for i in range(total_days):
            yield start + timedelta(days=i)
    
    def dateRangeGenerator_with_step(self, start: datetime, end: datetime, step_days: int = 1) -> Iterator[datetime]:
        """
        Approach 4: Generator with custom step
        
        Allow custom step size for more flexibility.
        
        Time: O(n/step)
        Space: O(1)
        """
        current = start
        while current <= end:
            yield current
            current += timedelta(days=step_days)
    
    def dateRangeGenerator_reverse(self, start: datetime, end: datetime) -> Iterator[datetime]:
        """
        Approach 5: Reverse generator (end to start)
        
        Generate dates from end to start (backwards).
        
        Time: O(n)
        Space: O(1)
        """
        current = end
        while current >= start:
            yield current
            current -= timedelta(days=1)

def test_date_range_generator():
    """Test the date range generator solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic range
    start1 = datetime(2023, 1, 1)
    end1 = datetime(2023, 1, 3)
    result1 = list(solution.dateRangeGenerator(start1, end1))
    expected1 = [
        datetime(2023, 1, 1),
        datetime(2023, 1, 2),
        datetime(2023, 1, 3)
    ]
    assert result1 == expected1
    
    # Test case 2: Cross year boundary
    start2 = datetime(2023, 12, 30)
    end2 = datetime(2024, 1, 2)
    result2 = list(solution.dateRangeGenerator(start2, end2))
    expected2 = [
        datetime(2023, 12, 30),
        datetime(2023, 12, 31),
        datetime(2024, 1, 1),
        datetime(2024, 1, 2)
    ]
    assert result2 == expected2
    
    # Test case 3: Single day
    start3 = datetime(2023, 5, 15)
    end3 = datetime(2023, 5, 15)
    result3 = list(solution.dateRangeGenerator(start3, end3))
    expected3 = [datetime(2023, 5, 15)]
    assert result3 == expected3
    
    # Test case 4: Cross month boundary
    start4 = datetime(2023, 1, 30)
    end4 = datetime(2023, 2, 2)
    result4 = list(solution.dateRangeGenerator(start4, end4))
    expected4 = [
        datetime(2023, 1, 30),
        datetime(2023, 1, 31),
        datetime(2023, 2, 1),
        datetime(2023, 2, 2)
    ]
    assert result4 == expected4
    
    # Test case 5: Leap year February
    start5 = datetime(2024, 2, 28)  # 2024 is a leap year
    end5 = datetime(2024, 3, 1)
    result5 = list(solution.dateRangeGenerator(start5, end5))
    expected5 = [
        datetime(2024, 2, 28),
        datetime(2024, 2, 29),  # Leap day
        datetime(2024, 3, 1)
    ]
    assert result5 == expected5
    
    # Test case 6: Longer range
    start6 = datetime(2023, 1, 1)
    end6 = datetime(2023, 1, 10)
    result6 = list(solution.dateRangeGenerator(start6, end6))
    assert len(result6) == 10
    assert result6[0] == start6
    assert result6[-1] == end6
    
    # Compare different approaches
    test_cases = [
        (datetime(2023, 1, 1), datetime(2023, 1, 3)),
        (datetime(2023, 12, 30), datetime(2024, 1, 2)),
        (datetime(2023, 5, 15), datetime(2023, 5, 15)),
        (datetime(2023, 1, 30), datetime(2023, 2, 2))
    ]
    
    for start, end in test_cases:
        result1 = list(solution.dateRangeGenerator(start, end))
        result2 = solution.dateRangeGenerator_list(start, end)
        result3 = list(solution.dateRangeGenerator_optimized(start, end))
        assert result1 == result2 == result3, f"Mismatch for {start} to {end}"
    
    # Test step generator
    start_step = datetime(2023, 1, 1)
    end_step = datetime(2023, 1, 10)
    result_step = list(solution.dateRangeGenerator_with_step(start_step, end_step, 2))
    expected_step = [
        datetime(2023, 1, 1),
        datetime(2023, 1, 3),
        datetime(2023, 1, 5),
        datetime(2023, 1, 7),
        datetime(2023, 1, 9)
    ]
    assert result_step == expected_step
    
    # Test reverse generator
    result_reverse = list(solution.dateRangeGenerator_reverse(start1, end1))
    expected_reverse = [
        datetime(2023, 1, 3),
        datetime(2023, 1, 2),
        datetime(2023, 1, 1)
    ]
    assert result_reverse == expected_reverse
    
    # Test that generator is lazy (doesn't compute all at once)
    gen = solution.dateRangeGenerator(datetime(2023, 1, 1), datetime(2023, 12, 31))
    first_date = next(gen)
    assert first_date == datetime(2023, 1, 1)
    
    print("All date range generator tests passed!")

if __name__ == "__main__":
    test_date_range_generator()
