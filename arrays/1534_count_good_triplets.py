"""
LeetCode Question #1534: Count Good Triplets

Problem Statement:
Given an array of integers `arr`, and three integers `a`, `b`, and `c`. You need to find the number of good triplets.

A triplet `(arr[i], arr[j], arr[k])` is good if the following conditions are true:
1. `0 <= i < j < k < arr.length`
2. `|arr[i] - arr[j]| <= a`
3. `|arr[j] - arr[k]| <= b`
4. `|arr[i] - arr[k]| <= c`

Return the number of good triplets.

Constraints:
- `3 <= arr.length <= 100`
- `0 <= arr[i] <= 1000`
- `0 <= a, b, c <= 1000`
"""

def countGoodTriplets(arr, a, b, c):
    """
    Function to count the number of good triplets in the array.

    :param arr: List[int] - The input array of integers.
    :param a: int - The maximum allowed difference between arr[i] and arr[j].
    :param b: int - The maximum allowed difference between arr[j] and arr[k].
    :param c: int - The maximum allowed difference between arr[i] and arr[k].
    :return: int - The number of good triplets.
    """
    n = len(arr)
    count = 0

    # Iterate through all possible triplets
    for i in range(n):
        for j in range(i + 1, n):
            if abs(arr[i] - arr[j]) <= a:
                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [3, 0, 1, 1, 9, 7]
    a1, b1, c1 = 7, 2, 3
    print(countGoodTriplets(arr1, a1, b1, c1))  # Expected Output: 4

    # Test Case 2
    arr2 = [1, 1, 2, 2, 3]
    a2, b2, c2 = 0, 0, 1
    print(countGoodTriplets(arr2, a2, b2, c2))  # Expected Output: 0

    # Test Case 3
    arr3 = [1, 2, 3, 4]
    a3, b3, c3 = 1, 1, 1
    print(countGoodTriplets(arr3, a3, b3, c3))  # Expected Output: 0

"""
Time Complexity:
- The solution uses three nested loops to iterate through all possible triplets in the array.
- The number of triplets is O(n^3), where n is the length of the array.
- Therefore, the time complexity is O(n^3).

Space Complexity:
- The solution uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""