"""
LeetCode Problem #1460: Make Two Arrays Equal by Reversing Sub-arrays

Problem Statement:
Given two integer arrays `target` and `arr`, you are asked to form `target` array using the elements of array `arr`.
You are allowed to rearrange the elements of `arr` and you can use as many reversals of sub-arrays as you want.

Return `true` if you can form the `target` array, and `false` otherwise.

Constraints:
1. `target.length == arr.length`
2. `1 <= target.length <= 1000`
3. `1 <= target[i] <= 1000`
4. `1 <= arr[i] <= 1000`
"""

def canBeEqual(target, arr):
    """
    Determines if the target array can be formed by rearranging the elements of arr.

    Args:
    target (List[int]): The target array.
    arr (List[int]): The array to be rearranged.

    Returns:
    bool: True if target can be formed, False otherwise.
    """
    # Sort both arrays and compare
    return sorted(target) == sorted(arr)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    print(canBeEqual(target, arr))  # Expected Output: True

    # Test Case 2
    target = [7]
    arr = [7]
    print(canBeEqual(target, arr))  # Expected Output: True

    # Test Case 3
    target = [1, 12]
    arr = [12, 1]
    print(canBeEqual(target, arr))  # Expected Output: True

    # Test Case 4
    target = [3, 7, 9]
    arr = [3, 7, 11]
    print(canBeEqual(target, arr))  # Expected Output: False

    # Test Case 5
    target = [1, 1, 1, 1]
    arr = [1, 1, 1, 1]
    print(canBeEqual(target, arr))  # Expected Output: True

"""
Time Complexity Analysis:
- Sorting both `target` and `arr` takes O(n log n), where n is the length of the arrays.
- Comparing the two sorted arrays takes O(n).
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- Sorting requires additional space for the sorted arrays, which is O(n).
- Overall space complexity: O(n).

Topic: Arrays
"""