"""
LeetCode Problem #1775: Equal Sum Arrays With Minimum Number of Operations

Problem Statement:
You are given two arrays of integers `nums1` and `nums2`, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can:
- Increase the value of an element in one of the arrays by 1 (if the value is less than 6), or
- Decrease the value of an element in one of the arrays by 1 (if the value is greater than 1).

Return the minimum number of operations required to make the sums of the two arrays equal. If it is not possible to make the sums equal, return -1.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- 1 <= nums1[i], nums2[i] <= 6
"""

from heapq import heappush, heappop

def minOperations(nums1, nums2):
    # Calculate the sums of both arrays
    sum1, sum2 = sum(nums1), sum(nums2)
    
    # If the sums are already equal, no operations are needed
    if sum1 == sum2:
        return 0
    
    # Ensure sum1 is the smaller sum
    if sum1 > sum2:
        nums1, nums2 = nums2, nums1
        sum1, sum2 = sum2, sum1
    
    # Calculate the difference between the sums
    diff = sum2 - sum1
    
    # Create a max-heap of possible changes (negative values for max-heap behavior)
    changes = []
    for num in nums1:
        heappush(changes, -(6 - num))  # Max increase for nums1
    for num in nums2:
        heappush(changes, -(num - 1))  # Max decrease for nums2
    
    # Perform operations to reduce the difference
    operations = 0
    while changes and diff > 0:
        max_change = -heappop(changes)  # Get the largest possible change
        diff -= max_change
        operations += 1
    
    # If the difference is reduced to 0 or less, return the number of operations
    return operations if diff <= 0 else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5, 6]
    nums2 = [1, 1, 2, 2, 2, 2]
    print(minOperations(nums1, nums2))  # Output: 3

    # Test Case 2
    nums1 = [1, 1, 1, 1, 1, 1, 1]
    nums2 = [6]
    print(minOperations(nums1, nums2))  # Output: -1

    # Test Case 3
    nums1 = [6, 6]
    nums2 = [1]
    print(minOperations(nums1, nums2))  # Output: 3

    # Test Case 4
    nums1 = [1, 1, 1, 1, 1]
    nums2 = [6, 6, 6, 6, 6]
    print(minOperations(nums1, nums2))  # Output: 5

"""
Time Complexity:
- Calculating the sums of nums1 and nums2 takes O(n + m), where n is the length of nums1 and m is the length of nums2.
- Pushing all elements into the heap takes O((n + m) log(n + m)).
- Extracting elements from the heap in the worst case takes O((n + m) log(n + m)).
- Overall time complexity: O((n + m) log(n + m)).

Space Complexity:
- The heap stores up to n + m elements, so the space complexity is O(n + m).

Topic: Arrays, Greedy, Heap (Priority Queue)
"""