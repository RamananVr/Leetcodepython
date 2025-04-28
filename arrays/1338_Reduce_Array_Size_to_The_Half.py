"""
LeetCode Problem #1338: Reduce Array Size to The Half

Problem Statement:
You are given an integer array `arr`. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

Constraints:
- 1 <= arr.length <= 10^5
- arr.length is even.
- 1 <= arr[i] <= 10^5
"""

from collections import Counter

def minSetSize(arr):
    """
    Function to find the minimum size of the set such that at least half of the integers in the array are removed.

    :param arr: List[int] - The input array
    :return: int - The minimum size of the set
    """
    # Count the frequency of each element in the array
    freq = Counter(arr)
    
    # Sort the frequencies in descending order
    sorted_freq = sorted(freq.values(), reverse=True)
    
    # Initialize variables to track the number of elements removed and the size of the set
    removed_elements = 0
    set_size = 0
    half_size = len(arr) // 2
    
    # Iterate through the sorted frequencies
    for count in sorted_freq:
        removed_elements += count
        set_size += 1
        # Stop once we've removed at least half of the elements
        if removed_elements >= half_size:
            break
    
    return set_size

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [3,3,3,3,5,5,5,2,2,7]
    print(minSetSize(arr1))  # Expected Output: 2

    # Test Case 2
    arr2 = [7,7,7,7,7,7]
    print(minSetSize(arr2))  # Expected Output: 1

    # Test Case 3
    arr3 = [1,9]
    print(minSetSize(arr3))  # Expected Output: 1

    # Test Case 4
    arr4 = [1000,1000,3,7]
    print(minSetSize(arr4))  # Expected Output: 1

    # Test Case 5
    arr5 = [1,2,3,4,5,6,7,8,9,10]
    print(minSetSize(arr5))  # Expected Output: 5

"""
Time Complexity Analysis:
- Counting the frequency of elements using `Counter` takes O(n), where n is the length of the array.
- Sorting the frequencies takes O(k log k), where k is the number of unique elements in the array.
  In the worst case, k = n (all elements are unique), so sorting takes O(n log n).
- Iterating through the sorted frequencies takes O(k), which is O(n) in the worst case.
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- The `Counter` object stores the frequency of each unique element, which takes O(k) space.
  In the worst case, k = n, so the space complexity is O(n).
- Overall space complexity: O(n).

Topic: Arrays
"""