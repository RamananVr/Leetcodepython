"""
LeetCode Question #1426: Counting Elements

Problem Statement:
Given an integer array `arr`, count how many elements `x` there are, such that `x + 1` is also in `arr`.
If there are duplicates in `arr`, count them separately.

Example 1:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted because 2 and 3 are in arr.

Example 2:
Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No elements are counted because there is no `x + 1` in arr.

Example 3:
Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1, and 2 are counted because 1, 2, and 3 are in arr.

Example 4:
Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted because 2 is in arr.

Constraints:
- 1 <= arr.length <= 1000
- 0 <= arr[i] <= 1000
"""

# Clean, Correct Python Solution
def countElements(arr):
    """
    Counts the number of elements x in the array such that x + 1 is also in the array.

    :param arr: List[int] - The input array of integers
    :return: int - The count of elements satisfying the condition
    """
    element_set = set(arr)
    count = 0
    for x in arr:
        if x + 1 in element_set:
            count += 1
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 3]
    print(countElements(arr1))  # Output: 2

    # Test Case 2
    arr2 = [1, 1, 3, 3, 5, 5, 7, 7]
    print(countElements(arr2))  # Output: 0

    # Test Case 3
    arr3 = [1, 3, 2, 3, 5, 0]
    print(countElements(arr3))  # Output: 3

    # Test Case 4
    arr4 = [1, 1, 2, 2]
    print(countElements(arr4))  # Output: 2

    # Test Case 5
    arr5 = [0, 0, 1, 1, 2, 2]
    print(countElements(arr5))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the array `arr` once, which takes O(n) time.
- Checking if `x + 1` is in the set `element_set` takes O(1) on average.
- Therefore, the overall time complexity is O(n), where n is the length of the array.

Space Complexity:
- The function uses a set `element_set` to store the unique elements of the array, which takes O(u) space, where u is the number of unique elements in `arr`.
- In the worst case, u = n (all elements are unique), so the space complexity is O(n).
"""

# Topic: Arrays