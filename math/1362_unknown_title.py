"""
LeetCode Problem #1362: Closest Divisors

Problem Statement:
Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.

Example 1:
Input: num = 8
Output: [3, 3]
Explanation: For num + 1 = 9, the closest divisors are 3 and 3, and for num + 2 = 10, the closest divisors are 2 and 5. 
Since 3 and 3 are closer in absolute difference, we return [3, 3].

Example 2:
Input: num = 123
Output: [5, 25]

Example 3:
Input: num = 999
Output: [25, 40]

Constraints:
- 1 <= num <= 10^9
"""

def closestDivisors(num):
    """
    Finds the closest two integers whose product equals num + 1 or num + 2.

    :param num: int
    :return: List[int]
    """
    def find_closest_divisors(target):
        # Start from the square root of the target and move downward
        for i in range(int(target**0.5), 0, -1):
            if target % i == 0:
                return [i, target // i]
        return []

    # Check for num + 1 and num + 2
    divisors1 = find_closest_divisors(num + 1)
    divisors2 = find_closest_divisors(num + 2)

    # Compare the absolute differences and return the closer pair
    if abs(divisors1[0] - divisors1[1]) <= abs(divisors2[0] - divisors2[1]):
        return divisors1
    else:
        return divisors2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num = 8
    print(closestDivisors(num))  # Output: [3, 3]

    # Test Case 2
    num = 123
    print(closestDivisors(num))  # Output: [5, 25]

    # Test Case 3
    num = 999
    print(closestDivisors(num))  # Output: [25, 40]

"""
Time Complexity Analysis:
- The function `find_closest_divisors` iterates from the square root of the target down to 1.
  This takes O(sqrt(target)) time.
- Since we call `find_closest_divisors` twice (once for num + 1 and once for num + 2),
  the overall time complexity is O(sqrt(num)).

Space Complexity Analysis:
- The space complexity is O(1) since we only use a constant amount of extra space.

Topic: Math
"""