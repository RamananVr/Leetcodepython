"""
LeetCode Problem #2607: Make K-Subarray Sums Equal

Problem Statement:
You are given an integer array `arr` and an integer `k`. The array is circular, meaning the first element is adjacent to the last element. You can perform the following operation any number of times:

- Choose any subarray of length `k` and increase or decrease each element of the subarray by 1.

Return the minimum number of operations required to make all the `k`-subarray sums equal.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= k <= arr.length
- 1 <= arr[i] <= 10^9
"""

# Solution
from typing import List

def makeSubKSumEqual(arr: List[int], k: int) -> int:
    from math import gcd
    from statistics import median

    n = len(arr)
    g = gcd(n, k)  # Find the greatest common divisor of n and k
    result = 0

    # Group elements into `g` groups based on their indices modulo `g`
    for i in range(g):
        group = []
        for j in range(i, n, g):
            group.append(arr[j])
        
        # Sort the group and find the median
        group.sort()
        med = median(group)
        
        # Calculate the cost to make all elements in the group equal to the median
        result += sum(abs(x - med) for x in group)
    
    return int(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 4, 1, 3]
    k1 = 2
    print(makeSubKSumEqual(arr1, k1))  # Expected Output: 1

    # Test Case 2
    arr2 = [2, 5, 5, 7]
    k2 = 3
    print(makeSubKSumEqual(arr2, k2))  # Expected Output: 5

    # Test Case 3
    arr3 = [1, 2, 3, 4, 5]
    k3 = 1
    print(makeSubKSumEqual(arr3, k3))  # Expected Output: 0

    # Test Case 4
    arr4 = [10, 20, 30, 40]
    k4 = 4
    print(makeSubKSumEqual(arr4, k4))  # Expected Output: 60

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the GCD takes O(log(min(n, k))).
- Grouping elements into `g` groups takes O(n).
- Sorting each group takes O((n/g) * log(n/g)) on average, and there are `g` groups, so the total sorting cost is O(n * log(n/g)).
- Calculating the cost to make all elements equal to the median takes O(n).
- Overall time complexity: O(n * log(n/g)).

Space Complexity:
- The space required to store the groups is O(n).
- Overall space complexity: O(n).

Topic: Arrays, Math, Greedy
"""