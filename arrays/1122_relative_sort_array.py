"""
LeetCode Question #1122: Relative Sort Array

Problem Statement:
Given two arrays `arr1` and `arr2`, the elements of `arr2` are all distinct, and `arr2` is a subset of `arr1`.
Sort the elements of `arr1` such that the relative ordering of items in `arr1` are the same as in `arr2`. 
Elements that do not appear in `arr2` should be placed at the end of `arr1` in ascending order.

Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3]
Output: [2,2,2,1,4,3,3,6,7,9,19]

Constraints:
- `arr1.length <= 1000`
- `arr2.length <= 1000`
- `0 <= arr1[i], arr2[i] <= 1000`
- All the elements of `arr2` are distinct.
- Each `arr2[i]` is in `arr1`.
"""

# Solution
def relativeSortArray(arr1, arr2):
    # Create a dictionary to store the rank of each element in arr2
    rank = {value: index for index, value in enumerate(arr2)}
    
    # Sort arr1 based on the rank in arr2, and for elements not in arr2, sort them by their value
    return sorted(arr1, key=lambda x: (rank.get(x, len(arr2)), x))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3]
    print(relativeSortArray(arr1, arr2))  # Output: [2,2,2,1,4,3,3,6,7,9,19]

    # Test Case 2
    arr1 = [28,6,22,8,44,17]
    arr2 = [22,28,8,6]
    print(relativeSortArray(arr1, arr2))  # Output: [22,28,8,6,17,44]

    # Test Case 3
    arr1 = [1,2,3,4,5]
    arr2 = [3,1]
    print(relativeSortArray(arr1, arr2))  # Output: [3,1,2,4,5]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting `arr1` takes O(n log n), where n is the length of `arr1`.
- Creating the rank dictionary takes O(m), where m is the length of `arr2`.
- Overall time complexity: O(n log n + m).

Space Complexity:
- The rank dictionary takes O(m) space.
- The sorting operation may require O(n) space for intermediate storage.
- Overall space complexity: O(n + m).

Primary Topic: Arrays
"""