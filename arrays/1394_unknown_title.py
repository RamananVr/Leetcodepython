"""
LeetCode Problem #1394: Find Lucky Integer in an Array

Problem Statement:
Given an array of integers `arr`, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer, return -1.

Example 1:
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because its frequency is 2.

Example 2:
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1 has a frequency of 1, 2 has a frequency of 2, and 3 has a frequency of 3. 3 is the largest lucky number.

Example 3:
Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.

Constraints:
- 1 <= arr.length <= 500
- 1 <= arr[i] <= 500
"""

from collections import Counter

def findLucky(arr):
    """
    Finds the largest lucky integer in the array.

    :param arr: List[int] - The input array of integers
    :return: int - The largest lucky integer, or -1 if none exists
    """
    # Count the frequency of each number in the array
    freq = Counter(arr)
    
    # Initialize the result as -1 (default if no lucky number is found)
    result = -1
    
    # Iterate through the frequency dictionary
    for num, count in freq.items():
        # Check if the number is a lucky number
        if num == count:
            # Update the result to the maximum lucky number found
            result = max(result, num)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [2, 2, 3, 4]
    print(findLucky(arr1))  # Output: 2

    # Test Case 2
    arr2 = [1, 2, 2, 3, 3, 3]
    print(findLucky(arr2))  # Output: 3

    # Test Case 3
    arr3 = [2, 2, 2, 3, 3]
    print(findLucky(arr3))  # Output: -1

    # Test Case 4
    arr4 = [5]
    print(findLucky(arr4))  # Output: -1

    # Test Case 5
    arr5 = [7, 7, 7, 7, 7, 7, 7]
    print(findLucky(arr5))  # Output: 7

"""
Time Complexity Analysis:
- Counting the frequency of elements in the array using `Counter` takes O(n), where n is the length of the array.
- Iterating through the frequency dictionary takes O(k), where k is the number of unique elements in the array.
- In the worst case, k can be equal to n (if all elements are unique).
- Therefore, the overall time complexity is O(n).

Space Complexity Analysis:
- The space complexity is O(k), where k is the number of unique elements in the array, due to the storage of the frequency dictionary.
- In the worst case, k can be equal to n.
- Therefore, the overall space complexity is O(n).

Topic: Arrays
"""