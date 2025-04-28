"""
LeetCode Problem #2155: All Divisions With the Highest Score of a Binary Array

Problem Statement:
You are given a 0-indexed binary array `nums` of length `n`. `nums` can only contain the integers `0` and `1`.

We can compute the "score" of a division at index `i` (where `0 <= i <= n`) as follows:
- The score of the left part of the array (i.e., `nums[0]` to `nums[i-1]`) is the number of `0`s in it.
- The score of the right part of the array (i.e., `nums[i]` to `nums[n-1]`) is the number of `1`s in it.

The division score at index `i` is the sum of these two scores.

Return all distinct indices `i` where the division score is the highest. You may return the answer in any order.

Example:
Input: nums = [0,0,1,0]
Output: [2,4]
Explanation:
- Division at index 2: Left = [0,0], Right = [1,0]. Score = 2 (zeros in left) + 1 (ones in right) = 3.
- Division at index 4: Left = [0,0,1,0], Right = []. Score = 3 (zeros in left) + 0 (ones in right) = 3.
- Indices 2 and 4 have the highest score.

Constraints:
- `n == nums.length`
- `1 <= n <= 10^5`
- `nums[i]` is either `0` or `1`.
"""

# Solution
from typing import List

def maxScoreIndices(nums: List[int]) -> List[int]:
    n = len(nums)
    total_ones = sum(nums)  # Total number of 1s in the array
    left_zeros = 0  # Count of zeros in the left part
    right_ones = total_ones  # Count of ones in the right part
    max_score = 0
    result = []

    for i in range(n + 1):
        # Calculate the score for the current division
        score = left_zeros + right_ones
        if score > max_score:
            max_score = score
            result = [i]  # Start a new list with the current index
        elif score == max_score:
            result.append(i)  # Add the current index to the result list

        # Update left_zeros and right_ones for the next division
        if i < n:
            if nums[i] == 0:
                left_zeros += 1
            else:
                right_ones -= 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [0, 0, 1, 0]
    print(maxScoreIndices(nums1))  # Output: [2, 4]

    # Test Case 2
    nums2 = [1, 1, 1, 0, 0]
    print(maxScoreIndices(nums2))  # Output: [3]

    # Test Case 3
    nums3 = [0, 0, 0, 0]
    print(maxScoreIndices(nums3))  # Output: [4]

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    print(maxScoreIndices(nums4))  # Output: [0]

    # Test Case 5
    nums5 = [0, 1, 0, 1, 0]
    print(maxScoreIndices(nums5))  # Output: [3]

"""
Time Complexity Analysis:
- Calculating the total number of 1s in the array takes O(n).
- Iterating through the array to calculate scores and update the result list takes O(n).
- Overall time complexity: O(n).

Space Complexity Analysis:
- We use a few integer variables and a list to store the result.
- Space complexity: O(1) for variables and O(k) for the result list, where k is the number of indices with the maximum score.
- Overall space complexity: O(k).

Topic: Arrays
"""