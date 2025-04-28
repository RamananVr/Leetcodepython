"""
LeetCode Problem #1089: Duplicate Zeros

Problem Statement:
Given a fixed-length integer array `arr`, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to [1,0,0,2,3,0,0,4].

Example 2:
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: No zero found in the array, so no modification is made.

Constraints:
- 1 <= arr.length <= 10^4
- 0 <= arr[i] <= 9
"""

def duplicateZeros(arr):
    """
    Modify the input array in-place to duplicate each occurrence of zero.
    """
    # Count the number of zeros in the array
    zeros = arr.count(0)
    n = len(arr)
    
    # Traverse the array from the end
    for i in range(n - 1, -1, -1):
        # If the current index + zeros is within bounds, copy the value
        if i + zeros < n:
            arr[i + zeros] = arr[i]
        
        # If the current value is zero, decrement the zero count and duplicate it
        if arr[i] == 0:
            zeros -= 1
            if i + zeros < n:
                arr[i + zeros] = 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicateZeros(arr1)
    print(arr1)  # Output: [1, 0, 0, 2, 3, 0, 0, 4]

    # Test Case 2
    arr2 = [1, 2, 3]
    duplicateZeros(arr2)
    print(arr2)  # Output: [1, 2, 3]

    # Test Case 3
    arr3 = [0, 0, 0, 0]
    duplicateZeros(arr3)
    print(arr3)  # Output: [0, 0, 0, 0]

    # Test Case 4
    arr4 = [8, 4, 5, 0, 0, 0, 7]
    duplicateZeros(arr4)
    print(arr4)  # Output: [8, 4, 5, 0, 0, 0, 0]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array twice: once to count the zeros and once to shift elements.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm modifies the array in place and does not use any additional space.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""