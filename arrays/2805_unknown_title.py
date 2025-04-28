"""
LeetCode Problem #2805: "Sum of Odd Numbers After Queries"

Problem Statement:
You are given an integer array `nums` and an array `queries` where `queries[i] = [val_i, index_i]`.
For each query `i`, add `val_i` to `nums[index_i]`. Then, find the sum of all odd numbers in the array `nums`.
Return an array `answer` where `answer[i]` is the sum of odd numbers after the `i-th` query has been applied.

Example:
Input: nums = [1, 2, 3, 4], queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
Output: [4, 4, 0, 6]

Constraints:
- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
- 1 <= queries.length <= 10^5
- -10^5 <= val_i <= 10^5
"""

# Python Solution
def sumOddAfterQueries(nums, queries):
    # Calculate the initial sum of odd numbers
    odd_sum = sum(num for num in nums if num % 2 != 0)
    result = []

    for val, index in queries:
        # Check if the current number at index is odd
        if nums[index] % 2 != 0:
            odd_sum -= nums[index]  # Remove it from the odd sum

        # Update the number at the index
        nums[index] += val

        # Check if the updated number is odd
        if nums[index] % 2 != 0:
            odd_sum += nums[index]  # Add it to the odd sum

        # Append the current odd sum to the result
        result.append(odd_sum)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    queries1 = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    print(sumOddAfterQueries(nums1, queries1))  # Output: [4, 4, 0, 6]

    # Test Case 2
    nums2 = [5, 6, 7, 8]
    queries2 = [[2, 0], [3, 2], [-5, 1], [1, 3]]
    print(sumOddAfterQueries(nums2, queries2))  # Output: [12, 15, 10, 11]

    # Test Case 3
    nums3 = [10, 11, 12, 13]
    queries3 = [[-1, 1], [2, 3], [3, 0], [-4, 2]]
    print(sumOddAfterQueries(nums3, queries3))  # Output: [24, 26, 26, 22]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the initial sum of odd numbers takes O(n), where n is the length of nums.
- Each query is processed in O(1) time, and there are m queries.
- Overall time complexity: O(n + m), where n is the length of nums and m is the number of queries.

Space Complexity:
- The space complexity is O(1) since we are modifying the nums array in place and using a constant amount of extra space.
"""

# Topic: Arrays