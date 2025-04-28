"""
LeetCode Problem #932: Beautiful Array

Problem Statement:
An array `nums` of length `n` is called a beautiful array if for every triplet `(i, j, k)` 
such that `0 <= i < j < k < n`, we have `nums[j] * 2 != nums[i] + nums[k]`.

Given an integer `n`, return any beautiful array `nums` of length `n`. There will be at least one valid answer for the given `n`.

Constraints:
- 1 <= n <= 1000
"""

def beautifulArray(n: int) -> list:
    """
    Generate a beautiful array of length n.
    """
    def helper(nums):
        if len(nums) <= 1:
            return nums
        # Divide the array into odd and even indexed elements
        odd = helper(nums[::2])
        even = helper(nums[1::2])
        return odd + even

    return helper(list(range(1, n + 1)))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    print(f"Beautiful Array for n={n}: {beautifulArray(n)}")
    # Output: [1, 3, 2, 4] (or any other valid beautiful array)

    # Test Case 2
    n = 5
    print(f"Beautiful Array for n={n}: {beautifulArray(n)}")
    # Output: [1, 5, 3, 2, 4] (or any other valid beautiful array)

    # Test Case 3
    n = 1
    print(f"Beautiful Array for n={n}: {beautifulArray(n)}")
    # Output: [1]

    # Test Case 4
    n = 10
    print(f"Beautiful Array for n={n}: {beautifulArray(n)}")
    # Output: [1, 3, 5, 7, 9, 2, 4, 6, 8, 10] (or any other valid beautiful array)


"""
Time and Space Complexity Analysis:

Time Complexity:
- The function recursively divides the array into halves, which is similar to the divide-and-conquer approach in merge sort.
- At each level of recursion, we process all elements in the array.
- The total time complexity is O(n log n), where n is the size of the input.

Space Complexity:
- The recursion stack depth is O(log n) due to the divide-and-conquer approach.
- Additionally, we create new lists at each level of recursion, which requires O(n) space.
- Therefore, the total space complexity is O(n).

Topic: Divide and Conquer
"""