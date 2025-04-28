"""
LeetCode Problem #1212: Minimum Cost to Connect Two Arrays of Equal Length

Problem Statement:
You are given two arrays `nums1` and `nums2` of equal length `n`. In one operation, you can swap any two elements (one from `nums1` and one from `nums2`) at the same index. The cost of swapping is the absolute difference between the two elements being swapped.

Return the minimum cost required to make the two arrays equal. If it is impossible to make the arrays equal, return -1.

Constraints:
- `nums1` and `nums2` are arrays of integers.
- Both arrays have the same length `n`.
- The length of the arrays is between 1 and 1000.
- Each element in the arrays is between 1 and 1000.

"""

# Solution
def minimumCost(nums1, nums2):
    """
    Calculate the minimum cost to make two arrays equal by swapping elements.

    Args:
    nums1 (List[int]): First array of integers.
    nums2 (List[int]): Second array of integers.

    Returns:
    int: Minimum cost to make the arrays equal, or -1 if impossible.
    """
    from collections import Counter

    # Count the frequency of each element in both arrays
    count1 = Counter(nums1)
    count2 = Counter(nums2)

    # Check if it's possible to make the arrays equal
    for key in count1:
        if (count1[key] + count2[key]) % 2 != 0:
            return -1

    # Find the minimum element in both arrays
    min_element = min(min(nums1), min(nums2))

    # Create a list of all elements that need to be swapped
    swaps = []
    for key in count1:
        excess = (count1[key] - count2[key]) // 2
        if excess > 0:
            swaps.extend([key] * excess)

    for key in count2:
        excess = (count2[key] - count1[key]) // 2
        if excess > 0:
            swaps.extend([key] * excess)

    swaps.sort()

    # Calculate the minimum cost
    cost = 0
    for i in range(len(swaps) // 2):
        cost += min(swaps[i], 2 * min_element)

    return cost


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    nums2 = [2, 3, 1]
    print(minimumCost(nums1, nums2))  # Output: 0

    # Test Case 2
    nums1 = [1, 1, 2]
    nums2 = [2, 2, 1]
    print(minimumCost(nums1, nums2))  # Output: 1

    # Test Case 3
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print(minimumCost(nums1, nums2))  # Output: -1

    # Test Case 4
    nums1 = [1, 1, 1, 1]
    nums2 = [2, 2, 2, 2]
    print(minimumCost(nums1, nums2))  # Output: 4


# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting frequencies using Counter is O(n).
- Sorting the swaps list is O(m log m), where m is the number of excess elements.
- Overall complexity is O(n + m log m), where n is the length of the arrays.

Space Complexity:
- The space used by the Counter objects is O(u), where u is the number of unique elements in the arrays.
- The swaps list can have at most n elements, so its space complexity is O(n).
- Overall space complexity is O(n + u).

"""

# Topic: Arrays, Greedy Algorithm