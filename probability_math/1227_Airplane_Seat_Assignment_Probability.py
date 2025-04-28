"""
LeetCode Problem #1227: Airplane Seat Assignment Probability

Problem Statement:
n passengers board an airplane with exactly n seats. The first passenger has lost their ticket and picks a random seat. 
The rest of the passengers board the plane in the order of their ticket numbers. For each passenger, if their seat is 
already taken, they pick a random available seat. Otherwise, they sit in their assigned seat.

Return the probability that the nth person gets to sit in their assigned seat.

Constraints:
- 1 <= n <= 10^9
"""

def nthPersonGetsNthSeat(n: int) -> float:
    """
    Returns the probability that the nth person gets to sit in their assigned seat.
    """
    # If there's only one passenger, they will sit in their assigned seat.
    if n == 1:
        return 1.0
    # For n > 1, the probability converges to 0.5.
    return 0.5

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Only one passenger
    n = 1
    print(f"Test Case 1: n = {n}, Output: {nthPersonGetsNthSeat(n)}")  # Expected: 1.0

    # Test Case 2: Two passengers
    n = 2
    print(f"Test Case 2: n = {n}, Output: {nthPersonGetsNthSeat(n)}")  # Expected: 0.5

    # Test Case 3: Three passengers
    n = 3
    print(f"Test Case 3: n = {n}, Output: {nthPersonGetsNthSeat(n)}")  # Expected: 0.5

    # Test Case 4: Large number of passengers
    n = 10**9
    print(f"Test Case 4: n = {n}, Output: {nthPersonGetsNthSeat(n)}")  # Expected: 0.5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution runs in O(1) time because it directly returns the result based on the input value of n.

Space Complexity:
- The solution uses O(1) space as it does not require any additional data structures or memory allocation.

Topic: Probability, Math
"""