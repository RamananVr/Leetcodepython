"""
LeetCode Problem #1835: Find XOR Sum of All Pairs Bitwise AND

Problem Statement:
You are given two integer arrays `arr1` and `arr2` of length `m` and `n` respectively. The XOR sum of all pairs `(a, b)` where `a` is from `arr1` and `b` is from `arr2` is defined as:
    (a AND b) XOR (a AND b) XOR ... (for all pairs)

Return the XOR sum of all pairs bitwise AND.

Constraints:
- 1 <= arr1.length, arr2.length <= 10^5
- 0 <= arr1[i], arr2[j] <= 10^9
"""

# Python Solution
def getXORSum(arr1, arr2):
    """
    Calculate the XOR sum of all pairs bitwise AND.

    :param arr1: List[int] - First array
    :param arr2: List[int] - Second array
    :return: int - XOR sum of all pairs bitwise AND
    """
    # Compute the XOR of all elements in arr1
    xor1 = 0
    for num in arr1:
        xor1 ^= num

    # Compute the XOR of all elements in arr2
    xor2 = 0
    for num in arr2:
        xor2 ^= num

    # The result is the AND of the two XORs
    return xor1 & xor2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 3]
    arr2 = [6, 5]
    print(getXORSum(arr1, arr2))  # Expected Output: 0

    # Test Case 2
    arr1 = [12]
    arr2 = [4]
    print(getXORSum(arr1, arr2))  # Expected Output: 4

    # Test Case 3
    arr1 = [7, 8, 9]
    arr2 = [1, 2, 3]
    print(getXORSum(arr1, arr2))  # Expected Output: 0

    # Test Case 4
    arr1 = [0, 0, 0]
    arr2 = [1, 1, 1]
    print(getXORSum(arr1, arr2))  # Expected Output: 0

    # Test Case 5
    arr1 = [5, 7, 9]
    arr2 = [3, 6, 10]
    print(getXORSum(arr1, arr2))  # Expected Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- Computing the XOR of all elements in `arr1` takes O(m), where m is the length of `arr1`.
- Computing the XOR of all elements in `arr2` takes O(n), where n is the length of `arr2`.
- The final AND operation takes O(1).
- Overall time complexity: O(m + n).

Space Complexity:
- The algorithm uses a constant amount of extra space, regardless of the input size.
- Overall space complexity: O(1).

Topic: Bit Manipulation
"""