"""
LeetCode Problem #760: Find Anagram Mappings

Problem Statement:
You are given two integer arrays `nums1` and `nums2` where `nums2` is an anagram of `nums1`. 
Both arrays may contain duplicates. Return an array `mapping` of size `nums1.length` such that 
`mapping[i] = j` means the `i-th` element of `nums1` appears in `nums2` at index `j`. 
If there are multiple valid answers, return any of them.

Example 1:
Input: nums1 = [12, 28, 46, 32, 50], nums2 = [50, 12, 32, 46, 28]
Output: [1, 4, 3, 2, 0]

Explanation: 
For nums1[0] = 12, nums2[1] = 12, so mapping[0] = 1.
For nums1[1] = 28, nums2[4] = 28, so mapping[1] = 4.
For nums1[2] = 46, nums2[3] = 46, so mapping[2] = 3.
For nums1[3] = 32, nums2[2] = 32, so mapping[3] = 2.
For nums1[4] = 50, nums2[0] = 50, so mapping[4] = 0.

Example 2:
Input: nums1 = [84, 84, 84], nums2 = [84, 84, 84]
Output: [0, 1, 2]

Constraints:
- `nums1.length == nums2.length`
- `1 <= nums1.length <= 100`
- `0 <= nums1[i], nums2[i] <= 10^5`
- `nums2` is an anagram of `nums1`.
"""

# Solution
def anagramMappings(nums1, nums2):
    """
    Find the anagram mappings from nums1 to nums2.

    Args:
    nums1 (List[int]): The first list of integers.
    nums2 (List[int]): The second list of integers, an anagram of nums1.

    Returns:
    List[int]: The mapping of indices from nums1 to nums2.
    """
    # Create a dictionary to store the index of each element in nums2
    index_map = {num: i for i, num in enumerate(nums2)}
    
    # Map each element in nums1 to its index in nums2
    return [index_map[num] for num in nums1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [12, 28, 46, 32, 50]
    nums2 = [50, 12, 32, 46, 28]
    print(anagramMappings(nums1, nums2))  # Output: [1, 4, 3, 2, 0]

    # Test Case 2
    nums1 = [84, 84, 84]
    nums2 = [84, 84, 84]
    print(anagramMappings(nums1, nums2))  # Output: [0, 1, 2]

    # Test Case 3
    nums1 = [1, 2, 3]
    nums2 = [3, 2, 1]
    print(anagramMappings(nums1, nums2))  # Output: [2, 1, 0]

    # Test Case 4
    nums1 = [5, 5, 5]
    nums2 = [5, 5, 5]
    print(anagramMappings(nums1, nums2))  # Output: [0, 1, 2]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the `index_map` dictionary takes O(n), where n is the length of nums2.
- Mapping each element in nums1 to its index in nums2 takes O(n), as we iterate through nums1.
- Overall time complexity: O(n).

Space Complexity:
- The `index_map` dictionary requires O(n) space to store the indices of nums2.
- The output list requires O(n) space.
- Overall space complexity: O(n).
"""

# Topic: Arrays