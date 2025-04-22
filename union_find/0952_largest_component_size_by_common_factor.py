"""
LeetCode Question #952: Largest Component Size by Common Factor

Problem Statement:
You are given an array of unique integers nums. Consider the following graph:
- There are nums.length nodes, labeled nums[0] to nums[nums.length - 1].
- There is an edge between nums[i] and nums[j] if and only if nums[i] and nums[j] share a common factor greater than 1.

Return the size of the largest connected component in the graph.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- 1 <= nums[i] <= 10^5
"""

from collections import defaultdict
import math

class Solution:
    def largestComponentSize(self, nums):
        def find(x):
            """Find the root of x with path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            """Union two sets."""
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        # Step 1: Initialize Union-Find structure
        max_num = max(nums)
        parent = list(range(max_num + 1))

        # Step 2: Connect numbers with their factors
        for num in nums:
            for factor in range(2, int(math.sqrt(num)) + 1):
                if num % factor == 0:
                    union(num, factor)
                    union(num, num // factor)

        # Step 3: Count the size of each connected component
        component_size = defaultdict(int)
        for num in nums:
            root = find(num)
            component_size[root] += 1

        # Step 4: Return the largest component size
        return max(component_size.values())


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1 = [4, 6, 15, 35]
    print(solution.largestComponentSize(nums1))  # Output: 4

    # Test Case 2
    nums2 = [20, 50, 9, 63]
    print(solution.largestComponentSize(nums2))  # Output: 2

    # Test Case 3
    nums3 = [2, 3, 6, 7, 4, 12, 21, 39]
    print(solution.largestComponentSize(nums3))  # Output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
- Finding factors for each number: O(n * sqrt(m)), where n is the length of nums and m is the maximum value in nums.
- Union-Find operations: Nearly O(n * α(n)), where α(n) is the inverse Ackermann function (very small, almost constant).
Overall: O(n * sqrt(m)).

Space Complexity:
- Union-Find parent array: O(m), where m is the maximum value in nums.
- Component size dictionary: O(n).
Overall: O(m + n).

Topic: Union-Find
"""