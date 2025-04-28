"""
LeetCode Problem #1331: Rank Transform of an Array

Problem Statement:
Given an array of integers `arr`, replace each element with its rank.
The rank represents how large the element is. The rank has the following rules:
1. Rank is an integer starting from 1.
2. The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
3. Ranks should be assigned in ascending order of the elements.

Example 1:
Input: arr = [40, 10, 20, 30]
Output: [4, 1, 2, 3]
Explanation: 40 is the largest, so its rank is 4. 10 is the smallest, so its rank is 1. 20 is the second smallest, so its rank is 2. 30 is the third smallest, so its rank is 3.

Example 2:
Input: arr = [100, 100, 100]
Output: [1, 1, 1]
Explanation: All elements are the same, so they all have the same rank.

Example 3:
Input: arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
Output: [5, 3, 4, 2, 8, 6, 7, 1, 3]

Constraints:
- 0 <= arr.length <= 10^5
- -10^9 <= arr[i] <= 10^9
"""

def arrayRankTransform(arr):
    """
    Function to compute the rank transform of an array.

    :param arr: List[int] - Input array of integers
    :return: List[int] - Array with ranks assigned
    """
    # Step 1: Sort the unique elements of the array
    sorted_unique = sorted(set(arr))
    
    # Step 2: Create a mapping of element to its rank
    rank_map = {num: rank + 1 for rank, num in enumerate(sorted_unique)}
    
    # Step 3: Replace each element in the array with its rank
    return [rank_map[num] for num in arr]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [40, 10, 20, 30]
    print(arrayRankTransform(arr1))  # Output: [4, 1, 2, 3]

    # Test Case 2
    arr2 = [100, 100, 100]
    print(arrayRankTransform(arr2))  # Output: [1, 1, 1]

    # Test Case 3
    arr3 = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    print(arrayRankTransform(arr3))  # Output: [5, 3, 4, 2, 8, 6, 7, 1, 3]

    # Test Case 4 (Edge Case: Empty Array)
    arr4 = []
    print(arrayRankTransform(arr4))  # Output: []

    # Test Case 5 (Edge Case: Single Element)
    arr5 = [42]
    print(arrayRankTransform(arr5))  # Output: [1]

"""
Time Complexity Analysis:
1. Sorting the unique elements of the array takes O(n log n), where n is the length of the array.
2. Creating the rank map takes O(u), where u is the number of unique elements in the array.
3. Replacing each element in the array with its rank takes O(n).

Overall time complexity: O(n log n), dominated by the sorting step.

Space Complexity Analysis:
1. The `sorted_unique` list takes O(u) space, where u is the number of unique elements.
2. The `rank_map` dictionary takes O(u) space.
3. The output array takes O(n) space.

Overall space complexity: O(n + u), where n is the length of the array and u is the number of unique elements.

Topic: Arrays
"""