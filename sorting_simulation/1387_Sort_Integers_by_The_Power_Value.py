"""
LeetCode Problem #1387: Sort Integers by The Power Value

Problem Statement:
The power of an integer x is defined as the number of steps needed to transform x into 1 using the following process:
- If x is even, divide it by 2.
- If x is odd, multiply it by 3 and add 1.

For example, the power of x = 3 is 7 because the sequence goes as follows: 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1.

Given three integers lo, hi, and k, return the k-th integer in the range [lo, hi] sorted by the power value. If two integers have the same power value, sort them by ascending order.

The test cases are guaranteed to have a unique answer.

Constraints:
- 1 <= lo <= hi <= 1000
- 1 <= k <= hi - lo + 1
"""

# Python Solution
def getKth(lo: int, hi: int, k: int) -> int:
    def power_value(x: int) -> int:
        steps = 0
        while x != 1:
            if x % 2 == 0:
                x //= 2
            else:
                x = 3 * x + 1
            steps += 1
        return steps

    # Create a list of tuples (power_value, number) for all numbers in range [lo, hi]
    power_list = [(power_value(x), x) for x in range(lo, hi + 1)]
    
    # Sort by power value first, then by number if power values are equal
    power_list.sort()
    
    # Return the k-th number (1-indexed)
    return power_list[k - 1][1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    lo, hi, k = 12, 15, 2
    print(getKth(lo, hi, k))  # Expected Output: 13

    # Test Case 2
    lo, hi, k = 1, 1, 1
    print(getKth(lo, hi, k))  # Expected Output: 1

    # Test Case 3
    lo, hi, k = 7, 11, 4
    print(getKth(lo, hi, k))  # Expected Output: 10

    # Test Case 4
    lo, hi, k = 10, 20, 5
    print(getKth(lo, hi, k))  # Expected Output: 13

    # Test Case 5
    lo, hi, k = 1, 1000, 777
    print(getKth(lo, hi, k))  # Expected Output: 570

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the power value for a single number takes O(log(x)) steps, where x is the number being processed.
- For all numbers in the range [lo, hi], we calculate the power value, which takes O((hi - lo + 1) * log(hi)).
- Sorting the list of numbers by power value takes O((hi - lo + 1) * log(hi - lo + 1)).
- Overall time complexity: O((hi - lo + 1) * log(hi)).

Space Complexity:
- The space used for storing the list of tuples is O(hi - lo + 1).
- Overall space complexity: O(hi - lo + 1).
"""

# Topic: Sorting, Simulation