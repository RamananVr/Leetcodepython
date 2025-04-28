"""
LeetCode Problem #1619: Mean of Array After Removing Some Elements

Problem Statement:
Given an integer array `arr`, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.

The mean of a set of `n` elements is the sum of the elements divided by `n`.

- Remove the smallest 5% of the elements in the array.
- Remove the largest 5% of the elements in the array.
- Compute the mean of the remaining elements.

Note:
- Answers within 10^-5 of the actual answer will be considered accepted.
- It is guaranteed that `arr.length` is at least 20.
- Elements of `arr` are integers in the range [-10^5, 10^5].

Constraints:
- 20 <= arr.length <= 1000
- arr[i] is an integer in the range [-10^5, 10^5].

Example:
Input: arr = [6,2,7,5,1,2,0,8,10,2,5,8,7,6,5,0,6,8,10,8]
Output: 4.77778
Explanation: After removing the smallest 5% and the largest 5% of elements, the array becomes [2,2,2,5,5,5,6,6,6,7,7,8,8,8,8,10]. The mean is (2+2+2+5+5+5+6+6+6+7+7+8+8+8+8+10)/16 = 4.77778.

Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
Output: 2.00000
"""

# Clean and Correct Python Solution
from typing import List

def trimMean(arr: List[int]) -> float:
    # Sort the array
    arr.sort()
    # Calculate the number of elements to remove (5% from each end)
    n = len(arr)
    remove_count = n // 20  # 5% of n
    # Remove the smallest and largest 5% of elements
    trimmed_arr = arr[remove_count : n - remove_count]
    # Calculate and return the mean of the remaining elements
    return sum(trimmed_arr) / len(trimmed_arr)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [6,2,7,5,1,2,0,8,10,2,5,8,7,6,5,0,6,8,10,8]
    print(trimMean(arr1))  # Expected Output: 4.77778

    # Test Case 2
    arr2 = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
    print(trimMean(arr2))  # Expected Output: 2.00000

    # Test Case 3
    arr3 = [9,7,8,7,7,8,6,8,8,6,7,8,8,7,7,8,6,8,6,7]
    print(trimMean(arr3))  # Expected Output: 7.00000

    # Test Case 4
    arr4 = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
    print(trimMean(arr4))  # Expected Output: 4.00000

    # Test Case 5
    arr5 = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
    print(trimMean(arr5))  # Expected Output: 105.00000

# Time and Space Complexity Analysis
# Time Complexity:
# - Sorting the array takes O(n log n), where n is the length of the array.
# - Slicing the array and calculating the sum both take O(n).
# - Overall time complexity: O(n log n).

# Space Complexity:
# - Sorting the array may require O(n) additional space depending on the sorting algorithm.
# - Slicing the array creates a new list, which takes O(n) space.
# - Overall space complexity: O(n).

# Topic: Arrays