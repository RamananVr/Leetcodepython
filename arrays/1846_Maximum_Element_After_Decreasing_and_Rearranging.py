"""
LeetCode Problem #1846: Maximum Element After Decreasing and Rearranging

Problem Statement:
You are given an array `arr` consisting of positive integers. You can perform the following operation on the array any number of times:
- Decrease the value of any element of the array to a positive integer.

Rearrange the elements of the array to maximize the value of the smallest element, such that the array satisfies the following condition:
- The absolute difference between any two adjacent elements is at most 1.

Return the maximum possible value of the smallest element.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^9
"""

def maximumElementAfterDecrementingAndRearranging(arr):
    """
    Function to find the maximum possible value of the smallest element
    after rearranging and decrementing the array.

    :param arr: List[int] - Input array of positive integers
    :return: int - Maximum possible value of the smallest element
    """
    # Step 1: Sort the array
    arr.sort()

    # Step 2: Ensure the first element is 1
    arr[0] = 1

    # Step 3: Iterate through the array and adjust elements
    for i in range(1, len(arr)):
        arr[i] = min(arr[i], arr[i - 1] + 1)

    # Step 4: Return the last element, which is the maximum possible value of the smallest element
    return arr[-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [2, 2, 1, 2, 1]
    print(maximumElementAfterDecrementingAndRearranging(arr1))  # Output: 2

    # Test Case 2
    arr2 = [100, 1, 1000]
    print(maximumElementAfterDecrementingAndRearranging(arr2))  # Output: 3

    # Test Case 3
    arr3 = [1, 2, 3, 4, 5]
    print(maximumElementAfterDecrementingAndRearranging(arr3))  # Output: 5

    # Test Case 4
    arr4 = [10, 20, 30, 40, 50]
    print(maximumElementAfterDecrementingAndRearranging(arr4))  # Output: 5

    # Test Case 5
    arr5 = [1]
    print(maximumElementAfterDecrementingAndRearranging(arr5))  # Output: 1

"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Iterating through the array to adjust elements takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation may require O(n) additional space depending on the sorting algorithm used.
- No additional data structures are used, so the space complexity is O(1) apart from the input.

Primary Topic: Arrays
"""