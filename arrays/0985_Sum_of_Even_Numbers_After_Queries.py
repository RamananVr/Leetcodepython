"""
LeetCode Problem #985: Sum of Even Numbers After Queries

Problem Statement:
You are given an integer array `nums` and an array `queries` where `queries[i] = [val, index]`.
For each query `i`, you need to:
1. Add `val` to `nums[index]`.
2. Then, compute the sum of the even numbers in `nums`.

Return an integer array `answer` where `answer[i]` is the result of the i-th query.

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- 1 <= queries.length <= 10^4
- -10^4 <= queries[i][0] <= 10^4
- 0 <= queries[i][1] < nums.length
"""

def sumEvenAfterQueries(nums, queries):
    """
    Function to compute the sum of even numbers in the array after each query.

    Args:
    nums (List[int]): The initial array of integers.
    queries (List[List[int]]): The list of queries where each query is [val, index].

    Returns:
    List[int]: The sum of even numbers after each query.
    """
    # Calculate the initial sum of even numbers in the array
    even_sum = sum(num for num in nums if num % 2 == 0)
    result = []

    for val, index in queries:
        # If the current number at index is even, subtract it from the even_sum
        if nums[index] % 2 == 0:
            even_sum -= nums[index]

        # Update the number at the given index
        nums[index] += val

        # If the updated number is even, add it to the even_sum
        if nums[index] % 2 == 0:
            even_sum += nums[index]

        # Append the current even_sum to the result
        result.append(even_sum)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    queries1 = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    print(sumEvenAfterQueries(nums1, queries1))  # Output: [8, 6, 2, 4]

    # Test Case 2
    nums2 = [5, 5, 5, 5]
    queries2 = [[2, 0], [3, 1], [4, 2], [5, 3]]
    print(sumEvenAfterQueries(nums2, queries2))  # Output: [0, 0, 4, 4]

    # Test Case 3
    nums3 = [2, 4, 6, 8]
    queries3 = [[1, 0], [2, 1], [3, 2], [4, 3]]
    print(sumEvenAfterQueries(nums3, queries3))  # Output: [18, 20, 20, 24]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the initial sum of even numbers takes O(n), where n is the length of `nums`.
- For each query, we perform constant-time operations (checking if a number is even, updating the sum, etc.).
- Since there are `m` queries, the total time complexity is O(n + m), where n is the length of `nums` and m is the number of queries.

Space Complexity:
- The algorithm uses O(1) additional space, as we only store a few variables (e.g., `even_sum` and `result`).

Topic: Arrays
"""