"""
LeetCode Problem #2417: Closest Fair Integer

Problem Statement:
You are given a positive integer `n`. A fair integer is an integer that has an equal number of even and odd digits. 
Find the smallest fair integer that is greater than or equal to `n`.

Constraints:
- 1 <= n <= 10^18
"""

def closestFairInteger(n: int) -> int:
    def is_fair(num: int) -> bool:
        """Helper function to check if a number is fair."""
        even_count = 0
        odd_count = 0
        for digit in str(num):
            if int(digit) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        return even_count == odd_count

    # Start checking from n and increment until we find a fair integer
    while True:
        if is_fair(n):
            return n
        n += 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 1
    print(f"Closest fair integer to {n1}: {closestFairInteger(n1)}")  # Expected: 10

    # Test Case 2
    n2 = 10
    print(f"Closest fair integer to {n2}: {closestFairInteger(n2)}")  # Expected: 10

    # Test Case 3
    n3 = 123
    print(f"Closest fair integer to {n3}: {closestFairInteger(n3)}")  # Expected: 131

    # Test Case 4
    n4 = 1000
    print(f"Closest fair integer to {n4}: {closestFairInteger(n4)}")  # Expected: 1001

    # Test Case 5
    n5 = 2222
    print(f"Closest fair integer to {n5}: {closestFairInteger(n5)}")  # Expected: 2233

"""
Time Complexity Analysis:
- The `is_fair` function runs in O(d), where d is the number of digits in the number.
- In the worst case, we may need to increment `n` multiple times until we find a fair integer. 
  The number of increments depends on the input, but in the worst case, it could be proportional to the value of `n`.
- Therefore, the overall time complexity is O(k * d), where k is the number of increments and d is the number of digits.

Space Complexity Analysis:
- The space complexity is O(d) due to the string conversion of the number in the `is_fair` function.

Topic: Math, Simulation
"""