"""
LeetCode Problem #1207: Unique Number of Occurrences

Problem Statement:
Given an array of integers `arr`, write a function that returns `true` if the number of occurrences of each value in the array is unique, or `false` otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 occurrences, and 3 has 1 occurrence. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:
- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000
"""

def uniqueOccurrences(arr):
    """
    Determines if the number of occurrences of each value in the array is unique.

    :param arr: List[int] - The input array of integers.
    :return: bool - True if the occurrences are unique, False otherwise.
    """
    from collections import Counter

    # Count the occurrences of each number in the array
    count = Counter(arr)

    # Extract the frequencies of occurrences
    frequencies = list(count.values())

    # Check if the frequencies are unique by comparing the length of the set
    return len(frequencies) == len(set(frequencies))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 2, 1, 1, 3]
    print(uniqueOccurrences(arr1))  # Output: True

    # Test Case 2
    arr2 = [1, 2]
    print(uniqueOccurrences(arr2))  # Output: False

    # Test Case 3
    arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    print(uniqueOccurrences(arr3))  # Output: True

    # Additional Test Case 4
    arr4 = [1, 1, 1, 1]
    print(uniqueOccurrences(arr4))  # Output: True

    # Additional Test Case 5
    arr5 = [1, 2, 3, 4, 5]
    print(uniqueOccurrences(arr5))  # Output: False


"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the occurrences using `Counter` takes O(n), where n is the length of the array.
- Extracting the values from the Counter object takes O(k), where k is the number of unique elements in the array.
- Checking the uniqueness of the frequencies using a set takes O(k).
- Overall, the time complexity is O(n), as n >= k.

Space Complexity:
- The Counter object requires O(k) space to store the counts of unique elements.
- The set used to check uniqueness also requires O(k) space.
- Overall, the space complexity is O(k), where k is the number of unique elements in the array.

Topic: Arrays, Hash Table
"""