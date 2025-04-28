"""
LeetCode Problem #1356: Sort Integers by The Number of 1 Bits

Problem Statement:
You are given an integer array `arr`. Sort the integers in the array in ascending order by the number of 1's in their binary representation and, in case of two or more integers have the same number of 1's, by their value.

Return the sorted array.

Example 1:
Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explanation: [0] has 0 ones; [1,2,4,8] have 1 one; [3,5,6] have 2 ones; [7] has 3 ones.
              The sorted array by bits is [0,1,2,4,8,3,5,6,7]

Example 2:
Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explanation: All numbers have 1 one in their binary representation. Sorted by value.

Constraints:
- 1 <= arr.length <= 500
- 0 <= arr[i] <= 10^4
"""

# Python Solution
from typing import List

def sortByBits(arr: List[int]) -> List[int]:
    # Sort by the number of 1 bits, then by the value itself
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(sortByBits(arr1))  # Output: [0, 1, 2, 4, 8, 3, 5, 6, 7]

    # Test Case 2
    arr2 = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    print(sortByBits(arr2))  # Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    # Test Case 3
    arr3 = [10000, 10000]
    print(sortByBits(arr3))  # Output: [10000, 10000]

    # Test Case 4
    arr4 = [2, 3, 5, 7, 11, 13, 17, 19]
    print(sortByBits(arr4))  # Output: [2, 3, 5, 17, 7, 11, 13, 19]

    # Test Case 5
    arr5 = [10, 100, 1000, 10000]
    print(sortByBits(arr5))  # Output: [10, 100, 10000, 1000]

"""
Time Complexity Analysis:
- Calculating the binary representation and counting the number of 1's for each number takes O(k), where k is the number of bits in the largest number (at most 14 for 10^4).
- Sorting the array takes O(n log n), where n is the length of the array.
- Overall time complexity: O(n * k + n log n), which simplifies to O(n log n) since k is small and constant.

Space Complexity Analysis:
- The sorting operation requires O(n) additional space for the sorted array.
- Overall space complexity: O(n).

Topic: Sorting
"""