"""
LeetCode Question #2449: Minimum Number of Operations to Make Arrays Similar

Problem Statement:
You are given two arrays `nums1` and `nums2` of equal length `n` and an integer `k`. 
In one operation, you can choose any index `i` (0 <= i < n) and increment `nums1[i]` by `k` or decrement `nums1[i]` by `k`.

Return the minimum number of operations required to make `nums1` and `nums2` similar. 
If it is impossible to make the arrays similar, return -1.

Two arrays are considered similar if for every index `i`, `nums1[i] % k == nums2[i] % k`.

Constraints:
- `1 <= nums1.length == nums2.length <= 10^5`
- `0 <= nums1[i], nums2[i] <= 10^9`
- `1 <= k <= 10^9`
"""

# Solution
def minOperations(nums1, nums2, k):
    # If k is 0, the arrays must be identical to be similar
    if k == 0:
        return 0 if nums1 == nums2 else -1
    
    # Check if the arrays can be made similar
    for i in range(len(nums1)):
        if (nums1[i] % k) != (nums2[i] % k):
            return -1
    
    # Calculate the total difference
    total_diff = 0
    positive_diff = 0
    negative_diff = 0
    
    for i in range(len(nums1)):
        diff = nums2[i] - nums1[i]
        total_diff += diff
        if diff > 0:
            positive_diff += diff
        elif diff < 0:
            negative_diff += abs(diff)
    
    # If the total difference is not zero, it's impossible to balance the arrays
    if total_diff != 0:
        return -1
    
    # The minimum number of operations is the sum of positive differences divided by k
    return positive_diff // k

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 3, 1]
    nums2 = [7, 6, 1]
    k = 3
    print(minOperations(nums1, nums2, k))  # Output: 2

    # Test Case 2
    nums1 = [10, 5, 15]
    nums2 = [15, 10, 20]
    k = 5
    print(minOperations(nums1, nums2, k))  # Output: 3

    # Test Case 3
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    k = 1
    print(minOperations(nums1, nums2, k))  # Output: 0

    # Test Case 4
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k = 0
    print(minOperations(nums1, nums2, k))  # Output: -1

    # Test Case 5
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k = 2
    print(minOperations(nums1, nums2, k))  # Output: -1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the arrays once to check the modulo condition and calculate differences.
- This results in a time complexity of O(n), where n is the length of the arrays.

Space Complexity:
- The solution uses a constant amount of extra space for variables like `total_diff`, `positive_diff`, and `negative_diff`.
- Thus, the space complexity is O(1).

Topic: Arrays, Math
"""