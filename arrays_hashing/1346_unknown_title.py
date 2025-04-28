"""
LeetCode Problem #1346: Check If N and Its Double Exist

Problem Statement:
Given an array `arr` of integers, check if there exist two indices `i` and `j` such that:
- `i != j`
- `0 <= i, j < arr.length`
- `arr[i] == 2 * arr[j]`

Return `true` if such indices exist, otherwise return `false`.

Example 1:
Input: arr = [10, 2, 5, 3]
Output: true
Explanation: For i = 2 and j = 1, arr[i] = 5 is double of arr[j] = 2.

Example 2:
Input: arr = [7, 1, 14, 11]
Output: true
Explanation: For i = 1 and j = 2, arr[i] = 14 is double of arr[j] = 7.

Example 3:
Input: arr = [3, 1, 7, 11]
Output: false
Explanation: There is no pair of indices that satisfies the conditions.

Constraints:
- 2 <= arr.length <= 500
- -10^3 <= arr[i] <= 10^3
"""

def checkIfExist(arr):
    """
    Function to check if there exist two indices i and j such that:
    - i != j
    - arr[i] == 2 * arr[j]
    
    :param arr: List[int] - Input array of integers
    :return: bool - True if such indices exist, False otherwise
    """
    seen = set()
    for num in arr:
        if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [10, 2, 5, 3]
    print(checkIfExist(arr1))  # Output: True

    # Test Case 2
    arr2 = [7, 1, 14, 11]
    print(checkIfExist(arr2))  # Output: True

    # Test Case 3
    arr3 = [3, 1, 7, 11]
    print(checkIfExist(arr3))  # Output: False

    # Test Case 4
    arr4 = [0, 0]
    print(checkIfExist(arr4))  # Output: True

    # Test Case 5
    arr5 = [-2, 0, 10, -19, 4, 6, -8]
    print(checkIfExist(arr5))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the array once, performing constant-time operations for each element.
- Checking membership in a set and adding elements to a set are O(1) operations on average.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The function uses a set to store elements of the array. In the worst case, the set will contain all n elements of the array.
- Therefore, the space complexity is O(n).

Topic: Arrays, Hashing
"""