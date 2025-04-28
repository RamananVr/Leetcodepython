"""
LeetCode Problem #1983: Minimum Number of Days to Make m Bouquets

Problem Statement:
You are given an integer array `bloomDay`, an integer `m`, and an integer `k`.

You want to make `m` bouquets. To make a bouquet, you need to use `k` adjacent flowers from the garden. The garden consists of `n` flowers, the `i-th` flower will bloom in the `bloomDay[i]` and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make `m` bouquets from the garden. If it is impossible to make `m` bouquets, return -1.

Example 1:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. 
- Day 1: The garden looks like [bloom, 10, 3, 10, 2]. You can only make 1 bouquet.
- Day 2: The garden looks like [bloom, 10, 3, 10, bloom]. You can only make 2 bouquets.
- Day 3: The garden looks like [bloom, 10, bloom, 10, bloom]. You can make 3 bouquets.
Thus, the minimum number of days is 3.

Example 2:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: It is impossible to make 3 bouquets since there are not enough flowers.

Example 3:
Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: To make 2 bouquets, you need 3 adjacent flowers in each bouquet. Here is the garden after 12 days:
[bloom, bloom, bloom, bloom, bloom, bloom, bloom]. Thus, the minimum number of days is 12.

Constraints:
- `bloomDay.length == n`
- `1 <= n <= 10^5`
- `1 <= bloomDay[i] <= 10^9`
- `1 <= m <= 10^6`
- `1 <= k <= n`
"""

# Clean and Correct Python Solution
def minDays(bloomDay, m, k):
    def canMakeBouquets(days):
        bouquets = 0
        flowers = 0
        for bloom in bloomDay:
            if bloom <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m

    if m * k > len(bloomDay):
        return -1

    left, right = min(bloomDay), max(bloomDay)
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if canMakeBouquets(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 1
    print(minDays(bloomDay, m, k))  # Output: 3

    # Test Case 2
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 2
    print(minDays(bloomDay, m, k))  # Output: -1

    # Test Case 3
    bloomDay = [7, 7, 7, 7, 12, 7, 7]
    m = 2
    k = 3
    print(minDays(bloomDay, m, k))  # Output: 12

    # Test Case 4
    bloomDay = [100, 200, 300, 400, 500]
    m = 1
    k = 5
    print(minDays(bloomDay, m, k))  # Output: 500

    # Test Case 5
    bloomDay = [1, 2, 4, 9, 3, 4, 1]
    m = 2
    k = 2
    print(minDays(bloomDay, m, k))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- The binary search runs in O(log(max(bloomDay))) iterations.
- For each iteration, the `canMakeBouquets` function is called, which takes O(n) time to iterate through the bloomDay array.
- Therefore, the overall time complexity is O(n * log(max(bloomDay))).

Space Complexity:
- The algorithm uses O(1) additional space as it only uses a few variables for computation.
- Thus, the space complexity is O(1).
"""

# Topic: Binary Search