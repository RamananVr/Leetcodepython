"""
LeetCode Problem #1497: Check If Array Pairs Are Divisible by k

Problem Statement:
Given an array of integers `arr` and an integer `k`, return `true` if it is possible to divide the array into pairs such that:
1. Each pair has a sum divisible by `k`.
2. Each element of the array is used exactly once.

Otherwise, return `false`.

Example 1:
Input: arr = [3, 8, 17, 2], k = 10
Output: true
Explanation: Pairs are (3, 17) and (8, 2), both of which sum to 20 and are divisible by 10.

Example 2:
Input: arr = [1, 2, 3, 4, 5, 10], k = 5
Output: false
Explanation: No valid pairing exists.

Constraints:
- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 10^9`
- `1 <= k <= 10^9`
"""

# Solution
def canArrange(arr, k):
    """
    Determines if the array can be divided into pairs such that the sum of each pair is divisible by k.

    :param arr: List[int] - The input array of integers.
    :param k: int - The divisor.
    :return: bool - True if valid pairs exist, False otherwise.
    """
    # Create a frequency map for remainders
    remainder_count = [0] * k
    
    # Count the frequency of each remainder
    for num in arr:
        remainder = num % k
        if remainder < 0:  # Handle negative remainders
            remainder += k
        remainder_count[remainder] += 1
    
    # Check if pairs can be formed
    for i in range(1, k):
        if remainder_count[i] != remainder_count[k - i]:
            return False
    
    # Special case for remainder 0
    if remainder_count[0] % 2 != 0:
        return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [3, 8, 17, 2]
    k1 = 10
    print(canArrange(arr1, k1))  # Output: True

    # Test Case 2
    arr2 = [1, 2, 3, 4, 5, 10]
    k2 = 5
    print(canArrange(arr2, k2))  # Output: False

    # Test Case 3
    arr3 = [1, 2, 3, 4, 5, 6]
    k3 = 7
    print(canArrange(arr3, k3))  # Output: True

    # Test Case 4
    arr4 = [1, 2, 3, 4, 5, 6]
    k4 = 10
    print(canArrange(arr4, k4))  # Output: False

    # Test Case 5
    arr5 = [10, -10, 20, -20]
    k5 = 10
    print(canArrange(arr5, k5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating remainders for all elements in `arr` takes O(n), where `n` is the length of the array.
- Checking the remainder counts takes O(k), where `k` is the divisor.
- Overall time complexity: O(n + k).

Space Complexity:
- The `remainder_count` array requires O(k) space.
- Overall space complexity: O(k).

Topic: Arrays, Hashing
"""