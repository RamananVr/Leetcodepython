# LeetCode Problem #2640: Find the Score of All Prefixes of an Array

class Solution:
    def findPrefixScore(self, nums):
        """
        Given an array nums, calculate the score of all prefixes of the array.
        The score of a prefix is defined as the sum of the prefix elements plus
        the maximum element in the prefix.

        Args:
        nums (List[int]): The input array.

        Returns:
        List[int]: A list containing the scores of all prefixes.
        """
        n = len(nums)
        prefix_scores = []
        max_so_far = float('-inf')
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            max_so_far = max(max_so_far, num)
            prefix_scores.append(prefix_sum + max_so_far)

        return prefix_scores

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1 = [2, 3, 7, 5]
    # Prefix scores: [2+2, 2+3+3, 2+3+7+7, 2+3+7+5+7] = [4, 8, 19, 26]
    print(solution.findPrefixScore(nums1))  # Output: [4, 8, 19, 26]

    # Test Case 2
    nums2 = [1, 2, 3]
    # Prefix scores: [1+1, 1+2+2, 1+2+3+3] = [2, 5, 9]
    print(solution.findPrefixScore(nums2))  # Output: [2, 5, 9]

    # Test Case 3
    nums3 = [5, 1, 2, 4]
    # Prefix scores: [5+5, 5+1+5, 5+1+2+5, 5+1+2+4+5] = [10, 16, 23, 32]
    print(solution.findPrefixScore(nums3))  # Output: [10, 16, 23, 32]

# Time Complexity Analysis:
# The solution iterates through the array once, performing O(1) operations for each element.
# Therefore, the time complexity is O(n), where n is the length of the input array.

# Space Complexity Analysis:
# The solution uses a list to store the prefix scores, which requires O(n) space.
# Apart from this, only a few variables are used, so the overall space complexity is O(n).

# Topic: Arrays