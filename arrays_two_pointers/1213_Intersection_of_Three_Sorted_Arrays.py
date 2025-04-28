"""
LeetCode Problem #1213: Intersection of Three Sorted Arrays

Problem Statement:
Given three integer arrays `arr1`, `arr2`, and `arr3` sorted in strictly increasing order, 
return a sorted array of only the integers that appeared in all three arrays.

Example 1:
Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in all three arrays.

Constraints:
- 1 <= arr1.length, arr2.length, arr3.length <= 1000
- 1 <= arr1[i], arr2[i], arr3[i] <= 2000
- arr1, arr2, and arr3 are sorted in strictly increasing order.
"""

# Python Solution
def arraysIntersection(arr1, arr2, arr3):
    """
    Finds the intersection of three sorted arrays.

    :param arr1: List[int] - First sorted array
    :param arr2: List[int] - Second sorted array
    :param arr3: List[int] - Third sorted array
    :return: List[int] - Sorted array of integers that appear in all three arrays
    """
    # Use three pointers to traverse the arrays
    i, j, k = 0, 0, 0
    result = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        # If all three elements are equal, add to result
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        # Increment the pointer of the smallest element
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 5, 7, 9]
    arr3 = [1, 3, 4, 5, 8]
    print(arraysIntersection(arr1, arr2, arr3))  # Output: [1, 5]

    # Test Case 2
    arr1 = [1, 2, 3]
    arr2 = [2, 3, 4]
    arr3 = [3, 4, 5]
    print(arraysIntersection(arr1, arr2, arr3))  # Output: [3]

    # Test Case 3
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8, 9, 10]
    arr3 = [11, 12, 13, 14, 15]
    print(arraysIntersection(arr1, arr2, arr3))  # Output: []

    # Test Case 4
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 4, 5]
    arr3 = [1, 2, 3, 4, 5]
    print(arraysIntersection(arr1, arr2, arr3))  # Output: [1, 2, 3, 4, 5]

# Time and Space Complexity Analysis
# Time Complexity: O(n1 + n2 + n3), where n1, n2, and n3 are the lengths of arr1, arr2, and arr3 respectively.
#                  This is because we traverse each array at most once using the three pointers.
# Space Complexity: O(1) additional space, as we only use a result list to store the output.

# Topic: Arrays, Two Pointers