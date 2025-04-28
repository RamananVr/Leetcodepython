"""
LeetCode Problem #365: Water and Jug Problem

Problem Statement:
You are given two jugs with capacities `jug1Capacity` and `jug2Capacity` respectively. There is an infinite amount of water supply available. 
You need to determine whether it is possible to measure exactly `targetCapacity` liters using these two jugs.

If `targetCapacity` liters of water are measurable, you must have `targetCapacity` liters of water contained within one or both buckets by the end.

Operations allowed:
1. Fill any of the jugs completely.
2. Empty any of the jugs.
3. Pour water from one jug into another until one of the jugs is either empty or full.

Constraints:
- 0 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6
"""

# Solution
def canMeasureWater(jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
    """
    Determines if it is possible to measure exactly targetCapacity liters using two jugs.
    """
    # If the target capacity is greater than the total capacity of both jugs, it's impossible
    if targetCapacity > jug1Capacity + jug2Capacity:
        return False
    
    # If the target capacity is zero, it's always possible (no water needed)
    if targetCapacity == 0:
        return True
    
    # Use the mathematical property of GCD (Greatest Common Divisor)
    from math import gcd
    return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Target capacity is achievable
    print(canMeasureWater(3, 5, 4))  # Expected output: True

    # Test Case 2: Target capacity is not achievable
    print(canMeasureWater(2, 6, 5))  # Expected output: False

    # Test Case 3: Target capacity exceeds total capacity
    print(canMeasureWater(1, 2, 4))  # Expected output: False

    # Test Case 4: Target capacity is zero
    print(canMeasureWater(0, 0, 0))  # Expected output: True

    # Test Case 5: Target capacity is equal to one of the jug capacities
    print(canMeasureWater(7, 11, 7))  # Expected output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution uses the `gcd` function, which has a time complexity of O(log(min(jug1Capacity, jug2Capacity))).
- Therefore, the overall time complexity is O(log(min(jug1Capacity, jug2Capacity))).

Space Complexity:
- The solution uses constant space, as no additional data structures are used.
- Therefore, the space complexity is O(1).
"""

# Topic: Math (Greatest Common Divisor)