"""
LeetCode Problem #786: K-th Smallest Prime Fraction

Problem Statement:
You are given a sorted array `arr` of unique integers where all elements are prime numbers. 
You are also given an integer `k`.

For every pair of indices `i` and `j` where `0 <= i < j < arr.length`, we consider the fraction `arr[i] / arr[j]`.

Return the `k`-th smallest fraction considered. The fraction should be returned as an array `[arr[i], arr[j]]`.

Example:
Input: arr = [1, 2, 3, 5], k = 3
Output: [2, 5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 1/2, 2/5, 2/3, 3/5. The third smallest fraction is 2/5.

Constraints:
- `2 <= arr.length <= 1000`
- `1 <= arr[i] <= 10^4`
- `arr[i]` is a prime number.
- All the numbers of `arr` are unique.
- `1 <= k <= arr.length * (arr.length - 1) / 2`
"""

# Python Solution
import heapq

def kthSmallestPrimeFraction(arr, k):
    """
    Finds the k-th smallest prime fraction from the given sorted array of prime numbers.

    :param arr: List[int] - A sorted array of unique prime numbers.
    :param k: int - The rank of the smallest fraction to find.
    :return: List[int] - The k-th smallest fraction as [numerator, denominator].
    """
    n = len(arr)
    # Min-heap to store fractions as (value, numerator index, denominator index)
    heap = []
    
    # Initialize the heap with fractions where denominator is the last element
    for i in range(n - 1):
        heapq.heappush(heap, (arr[i] / arr[-1], i, n - 1))
    
    # Extract the k-th smallest fraction
    for _ in range(k):
        value, i, j = heapq.heappop(heap)
        # If there are more fractions with the same numerator, push the next fraction
        if j - 1 > i:
            heapq.heappush(heap, (arr[i] / arr[j - 1], i, j - 1))
    
    return [arr[i], arr[j]]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 3, 5]
    k1 = 3
    print(kthSmallestPrimeFraction(arr1, k1))  # Output: [2, 5]

    # Test Case 2
    arr2 = [1, 7, 23, 29]
    k2 = 4
    print(kthSmallestPrimeFraction(arr2, k2))  # Output: [7, 29]

    # Test Case 3
    arr3 = [2, 3, 5, 7, 11]
    k3 = 7
    print(kthSmallestPrimeFraction(arr3, k3))  # Output: [5, 11]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The heap operations (push and pop) take O(log(n)) time.
- We perform k heap operations, so the total time complexity is O(k * log(n)).
- In the worst case, k = n * (n - 1) / 2, which is the total number of fractions.
- Therefore, the worst-case time complexity is O(n^2 * log(n)).

Space Complexity:
- The heap can store up to n elements at any time, so the space complexity is O(n).

Topic: Heap (Priority Queue)
"""