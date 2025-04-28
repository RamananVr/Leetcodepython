"""
LeetCode Problem #2433: Find The Original Array of Prefix Xor

Problem Statement:
You are given an integer array `pref` of size `n`. Find and return the array `arr` of size `n` that satisfies:
- arr[0] = pref[0]
- arr[i] = pref[i] XOR pref[i-1] for 1 <= i < n (0-indexed).

It can be proven that the answer is unique.

Example 1:
Input: pref = [5, 2, 0, 3, 1]
Output: [5, 7, 2, 3, 2]
Explanation:
From the given `pref` array, we can deduce the `arr` array as follows:
- arr[0] = pref[0] = 5
- arr[1] = pref[1] XOR pref[0] = 2 XOR 5 = 7
- arr[2] = pref[2] XOR pref[1] = 0 XOR 2 = 2
- arr[3] = pref[3] XOR pref[2] = 3 XOR 0 = 3
- arr[4] = pref[4] XOR pref[3] = 1 XOR 3 = 2

Example 2:
Input: pref = [13]
Output: [13]
Explanation:
Since the array contains only one element, arr[0] = pref[0].

Constraints:
- 1 <= pref.length <= 10^5
- 0 <= pref[i] <= 10^6
"""

def findArray(pref):
    """
    Function to find the original array `arr` from the given prefix XOR array `pref`.

    :param pref: List[int] - The prefix XOR array
    :return: List[int] - The original array `arr`
    """
    n = len(pref)
    arr = [0] * n
    arr[0] = pref[0]  # The first element of arr is the same as the first element of pref

    for i in range(1, n):
        arr[i] = pref[i] ^ pref[i - 1]  # XOR current pref with the previous one to get arr[i]

    return arr

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    pref1 = [5, 2, 0, 3, 1]
    print("Input:", pref1)
    print("Output:", findArray(pref1))  # Expected: [5, 7, 2, 3, 2]

    # Test Case 2
    pref2 = [13]
    print("Input:", pref2)
    print("Output:", findArray(pref2))  # Expected: [13]

    # Test Case 3
    pref3 = [1, 3, 0, 4, 7]
    print("Input:", pref3)
    print("Output:", findArray(pref3))  # Expected: [1, 2, 3, 7, 3]

    # Test Case 4
    pref4 = [0, 1, 1, 0, 0]
    print("Input:", pref4)
    print("Output:", findArray(pref4))  # Expected: [0, 1, 0, 1, 0]

"""
Time Complexity Analysis:
- The function iterates through the `pref` array once, performing a constant-time XOR operation for each element.
- Therefore, the time complexity is O(n), where n is the length of the `pref` array.

Space Complexity Analysis:
- The function uses an additional array `arr` of the same size as `pref` to store the result.
- Therefore, the space complexity is O(n).

Topic: Arrays, Bit Manipulation
"""