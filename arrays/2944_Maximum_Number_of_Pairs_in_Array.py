"""
LeetCode Problem #2944: Maximum Number of Pairs in Array

Problem Statement:
You are given a 0-indexed integer array `nums`. In one operation, you can pick two numbers from `nums` that are equal, remove both of them from the array, and form a pair.

The operation is performed until no more pairs can be formed. Return a 0-indexed integer array `answer` of size 2 where:
- `answer[0]` is the number of pairs that can be formed.
- `answer[1]` is the number of leftover integers in the array after forming all possible pairs.

Example:
Input: nums = [1, 3, 2, 1, 3, 2, 2]
Output: [3, 1]
Explanation: 
- Form a pair with numbers [1, 1]. Remaining array: [3, 2, 3, 2, 2]
- Form a pair with numbers [3, 3]. Remaining array: [2, 2, 2]
- Form a pair with numbers [2, 2]. Remaining array: [2]
- Total pairs formed = 3, leftover = 1.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100
"""

def numberOfPairs(nums):
    """
    Function to calculate the number of pairs and leftover integers in the array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    List[int]: A list containing the number of pairs and the number of leftover integers.
    """
    from collections import Counter

    # Count the frequency of each number in the array
    freq = Counter(nums)
    
    pairs = 0
    leftovers = 0
    
    # Calculate pairs and leftovers
    for count in freq.values():
        pairs += count // 2  # Number of pairs for this number
        leftovers += count % 2  # Leftover integers for this number
    
    return [pairs, leftovers]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 2, 1, 3, 2, 2]
    print(numberOfPairs(nums1))  # Output: [3, 1]

    # Test Case 2
    nums2 = [1, 1]
    print(numberOfPairs(nums2))  # Output: [1, 0]

    # Test Case 3
    nums3 = [0]
    print(numberOfPairs(nums3))  # Output: [0, 1]

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    print(numberOfPairs(nums4))  # Output: [0, 5]

    # Test Case 5
    nums5 = [1, 1, 1, 1, 1, 1]
    print(numberOfPairs(nums5))  # Output: [3, 0]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of elements using `Counter` takes O(n), where n is the length of the input array.
- Iterating through the frequency dictionary takes O(k), where k is the number of unique elements in the array.
- Overall, the time complexity is O(n + k). Since k <= n, the complexity simplifies to O(n).

Space Complexity:
- The `Counter` object uses O(k) space, where k is the number of unique elements in the array.
- The space complexity is O(k), which is at most O(n) in the worst case.

Topic: Arrays
"""