"""
LeetCode Problem #2053: Kth Distinct String in an Array

Problem Statement:
A distinct string is a string that is present only once in an array.

Given an array of strings `arr`, and an integer `k`, return the `kth` distinct string present in `arr`. 
If there are fewer than `k` distinct strings, return an empty string `""`.

Note that the strings are considered in the order in which they appear in the array.

Constraints:
- `1 <= arr.length <= 1000`
- `1 <= arr[i].length <= 100`
- `arr[i]` consists of lowercase English letters.
- `1 <= k <= arr.length`
"""

def kthDistinct(arr, k):
    """
    Finds the kth distinct string in the array.

    :param arr: List[str] - The input array of strings.
    :param k: int - The position of the distinct string to find.
    :return: str - The kth distinct string, or an empty string if there are fewer than k distinct strings.
    """
    # Step 1: Count the frequency of each string in the array
    from collections import Counter
    freq = Counter(arr)
    
    # Step 2: Iterate through the array to find the kth distinct string
    distinct_count = 0
    for string in arr:
        if freq[string] == 1:  # Check if the string is distinct
            distinct_count += 1
            if distinct_count == k:
                return string
    
    # If fewer than k distinct strings exist, return an empty string
    return ""

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = ["a", "b", "a", "c", "b", "d"]
    k1 = 2
    print(kthDistinct(arr1, k1))  # Expected Output: "c"

    # Test Case 2
    arr2 = ["a", "b", "c", "d"]
    k2 = 3
    print(kthDistinct(arr2, k2))  # Expected Output: "c"

    # Test Case 3
    arr3 = ["a", "a", "a"]
    k3 = 1
    print(kthDistinct(arr3, k3))  # Expected Output: ""

    # Test Case 4
    arr4 = ["x", "y", "z"]
    k4 = 2
    print(kthDistinct(arr4, k4))  # Expected Output: "y"

    # Test Case 5
    arr5 = ["apple", "banana", "apple", "cherry", "banana", "date"]
    k5 = 1
    print(kthDistinct(arr5, k5))  # Expected Output: "cherry"

"""
Time Complexity Analysis:
- Counting the frequency of each string using `Counter` takes O(n), where n is the length of the array.
- Iterating through the array to find the kth distinct string takes O(n) in the worst case.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The `Counter` object stores the frequency of each string, which requires O(u) space, where u is the number of unique strings in the array.
- Overall space complexity: O(u).

Topic: Arrays, Hash Table
"""