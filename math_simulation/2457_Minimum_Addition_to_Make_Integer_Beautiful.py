"""
LeetCode Problem #2457: Minimum Addition to Make Integer Beautiful

Problem Statement:
You are given two positive integers `n` and `target`.

An integer is considered beautiful if the sum of its digits is less than or equal to `target`.

You are allowed to do the following operation any number of times:
- Increase `n` by 1.

Return the minimum number of increments required to make `n` beautiful.

Constraints:
- 1 <= n <= 10^12
- 1 <= target <= 150
"""

def makeIntegerBeautiful(n: int, target: int) -> int:
    """
    Function to calculate the minimum number of increments required to make n beautiful.
    """
    def digit_sum(x: int) -> int:
        """Helper function to calculate the sum of digits of a number."""
        return sum(int(d) for d in str(x))
    
    increment = 0
    base = 1  # Used to handle carry-over when incrementing
    
    while digit_sum(n) > target:
        # Find the next multiple of 10^k (where k is the current digit position)
        remainder = n % (10 * base)
        increment += (10 * base - remainder)
        n += (10 * base - remainder)
        base *= 10  # Move to the next digit position
    
    return increment

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, target1 = 16, 6
    print(makeIntegerBeautiful(n1, target1))  # Expected Output: 4

    # Test Case 2
    n2, target2 = 467, 6
    print(makeIntegerBeautiful(n2, target2))  # Expected Output: 33

    # Test Case 3
    n3, target3 = 1, 1
    print(makeIntegerBeautiful(n3, target3))  # Expected Output: 0

    # Test Case 4
    n4, target4 = 123456789, 45
    print(makeIntegerBeautiful(n4, target4))  # Expected Output: 0

    # Test Case 5
    n5, target5 = 999999999, 10
    print(makeIntegerBeautiful(n5, target5))  # Expected Output: 1_000_000_001

"""
Time Complexity Analysis:
- The main loop runs until the sum of the digits of `n` becomes less than or equal to `target`.
- In each iteration, the number of digits in `n` increases by at most 1.
- Since `n` can grow up to 10^12, the number of iterations is proportional to the number of digits in `n`, which is O(log(n)).
- Calculating the digit sum takes O(log(n)) time as well (since there are log(n) digits in `n`).
- Therefore, the overall time complexity is O(log(n) * log(n)).

Space Complexity Analysis:
- The space complexity is O(log(n)) due to the storage of digits during the digit sum calculation.

Topic: Math, Simulation
"""