"""
LeetCode Problem #1481: Least Number of Unique Integers after K Removals

Problem Statement:
Given an array of integers `arr` and an integer `k`. You need to remove exactly `k` elements from the array such that the number of unique integers in the array is minimized.

Return the minimum number of unique integers in the array after removing exactly `k` elements.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^9
- 0 <= k <= arr.length
"""

from collections import Counter

def findLeastNumOfUniqueInts(arr, k):
    """
    Function to find the minimum number of unique integers in the array after removing exactly k elements.

    :param arr: List[int] - The input array of integers.
    :param k: int - The number of elements to remove.
    :return: int - The minimum number of unique integers remaining.
    """
    # Count the frequency of each integer in the array
    freq = Counter(arr)
    
    # Sort the integers by their frequency (ascending order)
    freq_sorted = sorted(freq.items(), key=lambda x: x[1])
    
    # Remove elements with the smallest frequencies first
    for num, count in freq_sorted:
        if k >= count:
            k -= count
            del freq[num]
        else:
            break
    
    # The remaining keys in the frequency dictionary are the unique integers left
    return len(freq)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [4, 3, 1, 1, 3, 3, 2]
    k1 = 3
    print(findLeastNumOfUniqueInts(arr1, k1))  # Output: 2

    # Test Case 2
    arr2 = [5, 5, 4]
    k2 = 1
    print(findLeastNumOfUniqueInts(arr2, k2))  # Output: 1

    # Test Case 3
    arr3 = [2, 4, 1, 8, 3, 3, 3, 1]
    k3 = 4
    print(findLeastNumOfUniqueInts(arr3, k3))  # Output: 3

    # Test Case 4
    arr4 = [1, 1, 1, 1, 2, 2, 3, 3, 3]
    k4 = 5
    print(findLeastNumOfUniqueInts(arr4, k4))  # Output: 1

"""
Time Complexity Analysis:
- Counting the frequency of elements using `Counter` takes O(n), where n is the length of the array.
- Sorting the frequency dictionary by values takes O(m log m), where m is the number of unique integers in the array.
- Iterating through the sorted frequencies to remove elements takes O(m).
Thus, the overall time complexity is O(n + m log m).

Space Complexity Analysis:
- The space required for the frequency dictionary is O(m), where m is the number of unique integers in the array.
- The sorted list of frequencies also takes O(m) space.
Thus, the overall space complexity is O(m).

Topic: Arrays, Hash Table, Greedy
"""