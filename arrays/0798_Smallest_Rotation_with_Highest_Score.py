"""
LeetCode Problem #798: Smallest Rotation with Highest Score

Problem Statement:
You are given an array `nums`. You can rotate it by moving the first element of the array to the end of the array any number of times.

Return the rotation index `k` that maximizes the score after rotation. The score of an array is defined as the number of indices `i` such that `nums[i] <= i`.

If there are multiple valid `k`s, return the smallest such index `k`.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] < nums.length
"""

def bestRotation(nums):
    """
    Function to find the smallest rotation index k that maximizes the score.
    
    Args:
    nums (List[int]): The input array.

    Returns:
    int: The smallest rotation index k.
    """
    n = len(nums)
    change = [0] * n

    # Calculate the change array
    for i, num in enumerate(nums):
        # When the element is in its valid range
        low = (i - num + 1 + n) % n
        high = (i + 1) % n
        change[low] += 1
        change[high] -= 1
        if low > high:
            change[0] += 1

    # Find the rotation index with the maximum score
    max_score = 0
    score = 0
    best_k = 0
    for k in range(n):
        score += change[k]
        if score > max_score:
            max_score = score
            best_k = k

    return best_k

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 1, 4, 0]
    print(bestRotation(nums1))  # Expected Output: 3

    # Test Case 2
    nums2 = [1, 3, 0, 2, 4]
    print(bestRotation(nums2))  # Expected Output: 0

    # Test Case 3
    nums3 = [0, 0, 0, 0]
    print(bestRotation(nums3))  # Expected Output: 0

    # Test Case 4
    nums4 = [4, 3, 2, 1, 0]
    print(bestRotation(nums4))  # Expected Output: 0

"""
Time Complexity Analysis:
- Calculating the `change` array takes O(n) time since we iterate through the array once.
- Calculating the best rotation index also takes O(n) time as we iterate through the `change` array.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The `change` array requires O(n) space.
- Overall space complexity: O(n).

Topic: Arrays
"""