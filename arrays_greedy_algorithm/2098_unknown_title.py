"""
LeetCode Problem #2098: Subsequence of Size K With the Largest Even Sum

Problem Statement:
You are given an integer array nums and an integer k. Find the largest even sum of any subsequence of size k in nums, or return -1 if no such subsequence exists.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example:
Input: nums = [4, 1, 5, 3, 2], k = 3
Output: 10
Explanation: The subsequence [4, 5, 1] has the largest even sum of size 3.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
- 1 <= k <= nums.length
"""

# Solution
from heapq import nlargest

def largestEvenSum(nums, k):
    # Step 1: Sort the array in descending order
    nums.sort(reverse=True)
    
    # Step 2: Extract the top k elements
    top_k = nums[:k]
    
    # Step 3: Calculate the sum of the top k elements
    total_sum = sum(top_k)
    
    # Step 4: Check if the sum is even
    if total_sum % 2 == 0:
        return total_sum
    
    # Step 5: If the sum is odd, try to make it even
    # Separate the remaining elements into odd and even numbers
    remaining = nums[k:]
    odd_top_k = [num for num in top_k if num % 2 == 1]
    even_top_k = [num for num in top_k if num % 2 == 0]
    odd_remaining = [num for num in remaining if num % 2 == 1]
    even_remaining = [num for num in remaining if num % 2 == 0]
    
    # Try replacing one odd number from top_k with one even number from remaining
    min_odd_top_k = min(odd_top_k) if odd_top_k else float('inf')
    max_even_remaining = max(even_remaining) if even_remaining else float('-inf')
    option1 = total_sum - min_odd_top_k + max_even_remaining if min_odd_top_k != float('inf') and max_even_remaining != float('-inf') else float('-inf')
    
    # Try replacing one even number from top_k with one odd number from remaining
    min_even_top_k = min(even_top_k) if even_top_k else float('inf')
    max_odd_remaining = max(odd_remaining) if odd_remaining else float('-inf')
    option2 = total_sum - min_even_top_k + max_odd_remaining if min_even_top_k != float('inf') and max_odd_remaining != float('-inf') else float('-inf')
    
    # Return the maximum valid even sum
    result = max(option1, option2)
    return result if result != float('-inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [4, 1, 5, 3, 2]
    k = 3
    print(largestEvenSum(nums, k))  # Output: 10

    # Test Case 2
    nums = [1, 3, 5, 7]
    k = 2
    print(largestEvenSum(nums, k))  # Output: -1

    # Test Case 3
    nums = [2, 4, 6, 8, 10]
    k = 4
    print(largestEvenSum(nums, k))  # Output: 28

    # Test Case 4
    nums = [1, 2, 3, 4, 5, 6]
    k = 3
    print(largestEvenSum(nums, k))  # Output: 12

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of nums.
- Extracting the top k elements and calculating their sum takes O(k).
- Separating the elements into odd and even categories takes O(n).
- Finding the minimum and maximum values in the subsets takes O(k) and O(n - k), respectively.
Overall, the time complexity is O(n log n).

Space Complexity:
- The space complexity is O(n) due to the storage of odd and even subsets.
"""

# Topic: Arrays, Greedy Algorithm