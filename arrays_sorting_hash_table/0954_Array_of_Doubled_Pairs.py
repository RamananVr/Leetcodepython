"""
LeetCode Problem #954: Array of Doubled Pairs

Problem Statement:
Given an integer array `arr` of size `n`, return `true` if and only if you can reorder it such that 
for every `i` in the reordered array, `arr[2*i] = 2 * arr[i]`.

Constraints:
1. `1 <= arr.length <= 3 * 10^4`
2. `-10^5 <= arr[i] <= 10^5`

Example:
Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can reorder the array as [-2,-4,2,4] such that -2 * 2 = -4 and 2 * 2 = 4.

Input: arr = [3,1,3,6]
Output: false
Explanation: No valid reordering exists.

Input: arr = [2,1,2,6]
Output: false
Explanation: No valid reordering exists.

Follow-up:
Can you solve the problem in O(n log n) time complexity?
"""

# Solution
from collections import Counter

def canReorderDoubled(arr):
    """
    Determines if the array can be reordered such that for every i, arr[2*i] = 2 * arr[i].

    :param arr: List[int] - The input array
    :return: bool - True if the array can be reordered, False otherwise
    """
    # Count the frequency of each number
    count = Counter(arr)
    
    # Sort the array by absolute value
    for x in sorted(count, key=abs):
        # If there are more x than 2*x, it's impossible to pair them
        if count[x] > count[2 * x]:
            return False
        # Reduce the count of 2*x by the count of x
        count[2 * x] -= count[x]
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [4, -2, 2, -4]
    print(canReorderDoubled(arr1))  # Output: True

    # Test Case 2
    arr2 = [3, 1, 3, 6]
    print(canReorderDoubled(arr2))  # Output: False

    # Test Case 3
    arr3 = [2, 1, 2, 6]
    print(canReorderDoubled(arr3))  # Output: False

    # Test Case 4
    arr4 = [1, 2, 4, 8]
    print(canReorderDoubled(arr4))  # Output: True

    # Test Case 5
    arr5 = [0, 0, 0, 0]
    print(canReorderDoubled(arr5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array by absolute value takes O(n log n), where n is the length of the array.
- Iterating through the sorted array and updating counts takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The Counter object uses O(n) space to store the frequency of elements.
- Overall space complexity: O(n).

Topic: Arrays, Sorting, Hash Table
"""