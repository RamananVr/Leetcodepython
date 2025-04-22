"""
LeetCode Problem #991: Broken Calculator

Problem Statement:
Given two integers `startValue` and `target`, you have a broken calculator that can only perform two operations:
1. Multiply the number on the display by 2.
2. Subtract 1 from the number on the display.

Initially, the calculator is displaying `startValue`. Return the minimum number of operations needed to display `target`.

Constraints:
- 1 <= startValue, target <= 10^9
"""

def brokenCalc(startValue: int, target: int) -> int:
    """
    This function calculates the minimum number of operations required to transform startValue into target
    using the broken calculator operations.
    """
    operations = 0
    while target > startValue:
        # If target is even, divide by 2 (reverse of multiplication by 2)
        if target % 2 == 0:
            target //= 2
        else:
            # If target is odd, add 1 (reverse of subtracting 1)
            target += 1
        operations += 1
    
    # Once target <= startValue, we need to subtract 1 repeatedly to match startValue
    return operations + (startValue - target)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    startValue = 2
    target = 3
    print(brokenCalc(startValue, target))  # Output: 2

    # Test Case 2
    startValue = 5
    target = 8
    print(brokenCalc(startValue, target))  # Output: 2

    # Test Case 3
    startValue = 3
    target = 10
    print(brokenCalc(startValue, target))  # Output: 3

    # Test Case 4
    startValue = 1024
    target = 1
    print(brokenCalc(startValue, target))  # Output: 1023

"""
Time and Space Complexity Analysis:

Time Complexity:
- The while loop runs until `target` becomes less than or equal to `startValue`.
- In each iteration, the value of `target` is halved (if even) or incremented (if odd).
- This results in logarithmic behavior for the halving operation, so the time complexity is O(log(target)).

Space Complexity:
- The algorithm uses a constant amount of space, as no additional data structures are used.
- Space complexity is O(1).

Topic: Greedy
"""