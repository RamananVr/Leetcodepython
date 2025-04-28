"""
LeetCode Problem #1505: Minimum Possible Integer After at Most K Adjacent Swaps On Digits

Problem Statement:
You are given a string `num` representing a large integer and an integer `k`. You are allowed to swap any two adjacent digits of the string at most `k` times.

Return the minimum integer you can obtain by applying at most `k` swaps on the string.

Example 1:
Input: num = "4321", k = 4
Output: "1342"
Explanation: The steps to obtain the minimum integer are:
- Swap 3 and 2, num becomes "4231".
- Swap 2 and 1, num becomes "4213".
- Swap 4 and 2, num becomes "2413".
- Swap 2 and 1, num becomes "1342".

Example 2:
Input: num = "100", k = 1
Output: "010"
Explanation: Swap 1 and 0, num becomes "010". Note that the leading zero is allowed.

Constraints:
- 1 <= num.length <= 40
- num consists of digits only and does not have leading zeros.
- 1 <= k <= 10^9
"""

from collections import deque

def minInteger(num: str, k: int) -> str:
    """
    Returns the minimum possible integer after at most k adjacent swaps on digits.
    """
    if k == 0 or not num:
        return num

    # Create a list of queues to store the indices of each digit (0-9)
    digit_positions = [deque() for _ in range(10)]
    for i, digit in enumerate(num):
        digit_positions[int(digit)].append(i)

    result = []
    visited = [False] * len(num)

    for _ in range(len(num)):
        for digit in range(10):
            if digit_positions[digit]:
                pos = digit_positions[digit][0]
                # Count the number of unvisited digits before the current position
                swaps_needed = sum(1 for i in range(pos) if not visited[i])
                if swaps_needed <= k:
                    # Use this digit
                    k -= swaps_needed
                    result.append(num[pos])
                    visited[pos] = True
                    digit_positions[digit].popleft()
                    break

    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "4321"
    k1 = 4
    print(minInteger(num1, k1))  # Output: "1342"

    # Test Case 2
    num2 = "100"
    k2 = 1
    print(minInteger(num2, k2))  # Output: "010"

    # Test Case 3
    num3 = "36789"
    k3 = 1000
    print(minInteger(num3, k3))  # Output: "36789"

    # Test Case 4
    num4 = "9438957234785635408"
    k4 = 23
    print(minInteger(num4, k4))  # Output: "0345989723478563548"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates over the digits of the input string `num` and processes each digit at most once.
- For each digit, it checks the number of unvisited digits before the current position, which can take O(n) in the worst case.
- Therefore, the overall time complexity is O(n^2), where n is the length of the string `num`.

Space Complexity:
- The space complexity is O(n) due to the `digit_positions` list of deques and the `visited` list.

Topic: Greedy, Priority Queue
"""