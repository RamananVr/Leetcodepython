"""
LeetCode Problem #2293: Min Max Game

Problem Statement:
You are given a 0-indexed integer array nums whose length is a power of 2.

Apply the following algorithm on nums:
1. Let n be the length of nums. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n / 2.
2. For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as:
   - min(nums[2 * i], nums[2 * i + 1]) if i is even.
   - max(nums[2 * i], nums[2 * i + 1]) if i is odd.
3. Replace the array nums with newNums.
4. Repeat the entire process starting from step 1.

Return the last number that remains in nums after applying the algorithm.

Constraints:
- 1 <= nums.length <= 1024
- 1 <= nums[i] <= 10^9
- nums.length is a power of 2.
"""

def minMaxGame(nums):
    """
    Function to solve the Min Max Game problem.

    :param nums: List[int] - The input array of integers.
    :return: int - The last remaining number after applying the algorithm.
    """
    while len(nums) > 1:
        newNums = []
        for i in range(len(nums) // 2):
            if i % 2 == 0:
                newNums.append(min(nums[2 * i], nums[2 * i + 1]))
            else:
                newNums.append(max(nums[2 * i], nums[2 * i + 1]))
        nums = newNums
    return nums[0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 5, 2, 4, 8, 2, 2]
    print(minMaxGame(nums1))  # Expected Output: 1

    # Test Case 2
    nums2 = [3, 5, 2, 1]
    print(minMaxGame(nums2))  # Expected Output: 2

    # Test Case 3
    nums3 = [70, 38, 21, 22]
    print(minMaxGame(nums3))  # Expected Output: 21

    # Test Case 4
    nums4 = [1]
    print(minMaxGame(nums4))  # Expected Output: 1

    # Test Case 5
    nums5 = [10, 20, 30, 40, 50, 60, 70, 80]
    print(minMaxGame(nums5))  # Expected Output: 10

"""
Time Complexity Analysis:
- At each step, the size of the array is halved. If the initial size of the array is n, the number of iterations is log(n).
- Within each iteration, we process all elements of the current array, which takes O(n) time in the first iteration, O(n/2) in the second, and so on.
- The total time complexity is O(n + n/2 + n/4 + ...) = O(n).

Space Complexity Analysis:
- The algorithm uses a new array `newNums` in each iteration, which has a size of n/2, n/4, ..., down to 1.
- The space complexity is O(n) for the largest intermediate array.

Topic: Arrays
"""