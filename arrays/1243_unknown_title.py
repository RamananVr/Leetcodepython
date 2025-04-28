"""
LeetCode Problem #1243: Array Transformation

Problem Statement:
Given an initial array `arr`, every day you produce a new array using the following rules:
1. If an element is smaller than both its left and right neighbors, then this element increases by 1.
2. If an element is larger than both its left and right neighbors, then this element decreases by 1.
3. Otherwise, the element does not change.

After some days, the array does not change. Return that final array.

Example:
Input: arr = [6, 2, 3, 4]
Output: [6, 3, 3, 4]

Input: arr = [1, 6, 3, 4, 3, 5]
Output: [1, 4, 4, 4, 4, 5]

Constraints:
- 1 <= arr.length <= 100
- 0 <= arr[i] <= 100
"""

# Solution
def transformArray(arr):
    """
    Transform the array until it stabilizes.

    :param arr: List[int] - The initial array
    :return: List[int] - The final stabilized array
    """
    while True:
        # Create a copy of the array to track changes
        new_arr = arr[:]
        for i in range(1, len(arr) - 1):
            if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                new_arr[i] += 1
            elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                new_arr[i] -= 1
        # If no changes occur, break the loop
        if new_arr == arr:
            break
        arr = new_arr
    return arr

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [6, 2, 3, 4]
    print(transformArray(arr1))  # Output: [6, 3, 3, 4]

    # Test Case 2
    arr2 = [1, 6, 3, 4, 3, 5]
    print(transformArray(arr2))  # Output: [1, 4, 4, 4, 4, 5]

    # Test Case 3
    arr3 = [1, 2, 3, 4, 5]
    print(transformArray(arr3))  # Output: [1, 2, 3, 4, 5]

    # Test Case 4
    arr4 = [5, 4, 3, 2, 1]
    print(transformArray(arr4))  # Output: [5, 4, 3, 2, 1]

    # Test Case 5
    arr5 = [1, 1, 1, 1, 1]
    print(transformArray(arr5))  # Output: [1, 1, 1, 1, 1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each iteration of the transformation loop processes the array in O(n) time, where n is the length of the array.
- In the worst case, the loop runs until the array stabilizes, which could take O(n) iterations (since each element can change at most n times).
- Therefore, the overall time complexity is O(n^2).

Space Complexity:
- The algorithm uses O(n) space for the `new_arr` copy of the array.
- Thus, the space complexity is O(n).

Topic: Arrays
"""