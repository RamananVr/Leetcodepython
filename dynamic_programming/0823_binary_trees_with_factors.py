"""
LeetCode Question #823: Binary Trees With Factors

Problem Statement:
Given an array of unique integers, `arr`, where each integer `arr[i]` is greater than 1, 
we write a binary tree with these integers as nodes. Each integer can be used multiple times 
in the tree. A binary tree is valid if the following conditions are met:

1. The value of each non-leaf node is equal to the product of its two children.
2. Both children are in the array.

Return the number of binary trees we can make. The answer may be large, so return it modulo 10^9 + 7.

Example:
Input: arr = [2, 4]
Output: 3
Explanation: We can make these trees:
- 2
- 4
  - 2
  - 2

Input: arr = [2, 4, 5, 10]
Output: 7
Explanation: We can make these trees:
- 2
- 4
  - 2
  - 2
- 5
- 10
  - 2
  - 5
  - 5
  - 2

Constraints:
- 1 <= arr.length <= 1000
- 2 <= arr[i] <= 10^9
"""

# Python Solution
def numFactoredBinaryTrees(arr):
    MOD = 10**9 + 7
    arr.sort()
    dp = {}
    
    for num in arr:
        dp[num] = 1  # Each number can form a single-node tree
    
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] % arr[j] == 0:  # arr[j] is a factor of arr[i]
                right = arr[i] // arr[j]
                if right in dp:
                    dp[arr[i]] += dp[arr[j]] * dp[right]
                    dp[arr[i]] %= MOD
    
    return sum(dp.values()) % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [2, 4]
    print(numFactoredBinaryTrees(arr1))  # Output: 3

    # Test Case 2
    arr2 = [2, 4, 5, 10]
    print(numFactoredBinaryTrees(arr2))  # Output: 7

    # Test Case 3
    arr3 = [2, 4, 8, 16]
    print(numFactoredBinaryTrees(arr3))  # Output: 23

    # Test Case 4
    arr4 = [18, 3, 6, 2]
    print(numFactoredBinaryTrees(arr4))  # Output: 12

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The nested loops iterate over pairs of elements in the array, resulting in O(n^2) complexity.
- Overall, the time complexity is O(n^2 + n log n), which simplifies to O(n^2) for large n.

Space Complexity:
- The space complexity is O(n) due to the `dp` dictionary storing counts for each element in the array.
"""

# Topic: Dynamic Programming