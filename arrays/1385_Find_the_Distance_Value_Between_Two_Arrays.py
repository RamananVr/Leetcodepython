"""
LeetCode Problem #1385: Find the Distance Value Between Two Arrays

Problem Statement:
Given two integer arrays `arr1` and `arr2`, and an integer `d`, return the distance value between the two arrays.

The distance value is defined as the number of elements `arr1[i]` such that there is no element `arr2[j]` where 
|arr1[i] - arr2[j]| <= d.

Constraints:
- 1 <= arr1.length, arr2.length <= 500
- -10^3 <= arr1[i], arr2[j] <= 10^3
- 0 <= d <= 100
"""

# Solution
def findTheDistanceValue(arr1, arr2, d):
    """
    Function to calculate the distance value between two arrays.

    :param arr1: List[int] - First array
    :param arr2: List[int] - Second array
    :param d: int - Distance threshold
    :return: int - Distance value
    """
    distance_value = 0
    for num1 in arr1:
        valid = True
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                valid = False
                break
        if valid:
            distance_value += 1
    return distance_value

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [4, 5, 8]
    arr2 = [10, 9, 1, 8]
    d = 2
    print(findTheDistanceValue(arr1, arr2, d))  # Expected Output: 2

    # Test Case 2
    arr1 = [1, 4, 2, 3]
    arr2 = [-4, -3, 6, 10, 20, 30]
    d = 3
    print(findTheDistanceValue(arr1, arr2, d))  # Expected Output: 2

    # Test Case 3
    arr1 = [2, 1, 100]
    arr2 = [10, 20, 30]
    d = 5
    print(findTheDistanceValue(arr1, arr2, d))  # Expected Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop iterates over each element in arr1 (O(n), where n is the length of arr1).
- The inner loop iterates over each element in arr2 (O(m), where m is the length of arr2).
- Therefore, the overall time complexity is O(n * m).

Space Complexity:
- The algorithm uses a constant amount of extra space (O(1)).
- No additional data structures are used, so the space complexity is O(1).
"""

# Topic: Arrays