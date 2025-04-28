"""
LeetCode Problem #2226: Maximum Candies Allocated to K Children

Problem Statement:
You are given a 0-indexed integer array `candies` of size `n`, where `candies[i]` represents the number of candies in the ith pile. 
You can divide each pile of candies into any number of smaller piles, or leave it as it is. However, you cannot combine piles together.

You are also given an integer `k`, representing the number of children. You need to determine the maximum number of candies each child can get 
if you distribute all the candies optimally. Each child must receive exactly the same number of candies.

Return the maximum number of candies each child can get.

Constraints:
- `1 <= candies.length <= 10^5`
- `1 <= candies[i] <= 10^7`
- `1 <= k <= 10^9`
"""

# Solution
def maximumCandies(candies, k):
    def canDistribute(mid):
        # Check if it's possible to distribute `mid` candies to `k` children
        return sum(candy // mid for candy in candies) >= k

    if sum(candies) < k:
        return 0  # Not enough candies to give at least 1 to each child

    left, right = 1, max(candies)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if canDistribute(mid):
            result = mid  # Update result and try for a larger value
            left = mid + 1
        else:
            right = mid - 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    candies = [5, 8, 6]
    k = 3
    print(maximumCandies(candies, k))  # Output: 5

    # Test Case 2
    candies = [2, 5]
    k = 11
    print(maximumCandies(candies, k))  # Output: 0

    # Test Case 3
    candies = [9, 7, 3]
    k = 4
    print(maximumCandies(candies, k))  # Output: 3

    # Test Case 4
    candies = [1, 2, 3, 4, 10]
    k = 5
    print(maximumCandies(candies, k))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search runs in O(log(max(candies))) iterations, where max(candies) is the largest number of candies in a pile.
- For each iteration, we calculate the total number of children that can be served using a single pass through the `candies` array, which takes O(n) time.
- Therefore, the overall time complexity is O(n * log(max(candies))).

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Binary Search
"""