"""
LeetCode Question #1442: Count Triplets That Can Form Two Arrays of Equal XOR

Problem Statement:
Given an array of integers `arr`, return the number of triplets `(i, j, k)` 
such that `i < j < k` and `arr[i] ^ arr[i+1] ^ ... ^ arr[j-1] == arr[j] ^ arr[j+1] ^ ... ^ arr[k]`.

Constraints:
- 1 <= arr.length <= 300
- 1 <= arr[i] <= 10^8

Example:
Input: arr = [2, 3, 1, 6, 7]
Output: 4
Explanation: The triplets are (0, 1, 2), (0, 2, 3), (2, 3, 4), and (0, 3, 4).
"""

# Solution
def countTriplets(arr):
    """
    Count the number of triplets (i, j, k) such that i < j < k and the XOR of
    subarrays satisfies the given condition.

    :param arr: List[int] - Input array of integers
    :return: int - Number of valid triplets
    """
    n = len(arr)
    prefix_xor = [0] * (n + 1)
    
    # Compute prefix XOR
    for i in range(n):
        prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
    
    count = 0
    
    # Iterate over all possible pairs (i, k)
    for i in range(n):
        for k in range(i + 1, n):
            # If prefix_xor[i] == prefix_xor[k + 1], it means the XOR condition is satisfied
            if prefix_xor[i] == prefix_xor[k + 1]:
                # Add the number of valid j values (j ranges from i+1 to k)
                count += (k - i)
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [2, 3, 1, 6, 7]
    print(countTriplets(arr1))  # Output: 4

    # Test Case 2
    arr2 = [1, 1, 1, 1, 1]
    print(countTriplets(arr2))  # Output: 10

    # Test Case 3
    arr3 = [2, 3]
    print(countTriplets(arr3))  # Output: 0

    # Test Case 4
    arr4 = [7, 11, 12, 9, 5, 2, 7, 17, 22]
    print(countTriplets(arr4))  # Output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
- Computing the prefix XOR takes O(n).
- The nested loops iterate over all pairs (i, k), which takes O(n^2).
- Thus, the overall time complexity is O(n^2).

Space Complexity:
- The prefix_xor array requires O(n) space.
- Thus, the overall space complexity is O(n).

Topic: Arrays, Prefix XOR
"""