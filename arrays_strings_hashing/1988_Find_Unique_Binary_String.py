"""
LeetCode Problem #1988: Find Unique Binary String

Problem Statement:
Given an array of binary strings nums where each binary string is of length n, 
return a binary string of length n that is not in nums. If there are multiple answers, 
you may return any of them.

You must implement a solution with a time complexity better than O(2^n) to generate 
all possible binary strings of length n.

Constraints:
- 1 <= nums.length <= 16
- nums[i].length == n
- nums[i] consists of only '0' and '1'.

Example:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" is not in nums. "00" is also not in nums, but "11" is returned.

Input: nums = ["00","01"]
Output: "10"
Explanation: "10" is not in nums. "11" is also not in nums, but "10" is returned.

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" is not in nums. "000" is also not in nums, but "101" is returned.

"""

# Solution
def findDifferentBinaryString(nums):
    """
    Finds a binary string of length n that is not in the given list of binary strings.

    Args:
    nums (List[str]): List of binary strings.

    Returns:
    str: A binary string of length n that is not in nums.
    """
    n = len(nums)
    seen = set(nums)
    
    # Generate a binary string using the diagonal approach
    result = ''.join('1' if nums[i][i] == '0' else '0' for i in range(n))
    
    # Ensure the result is not in the set
    if result not in seen:
        return result
    
    # Fallback (shouldn't be needed due to constraints)
    for i in range(2**n):
        candidate = bin(i)[2:].zfill(n)
        if candidate not in seen:
            return candidate

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = ["01", "10"]
    print(findDifferentBinaryString(nums1))  # Output: "11"

    # Test Case 2
    nums2 = ["00", "01"]
    print(findDifferentBinaryString(nums2))  # Output: "10"

    # Test Case 3
    nums3 = ["111", "011", "001"]
    print(findDifferentBinaryString(nums3))  # Output: "101"

    # Test Case 4
    nums4 = ["0"]
    print(findDifferentBinaryString(nums4))  # Output: "1"

    # Test Case 5
    nums5 = ["00", "11"]
    print(findDifferentBinaryString(nums5))  # Output: "01" or "10"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a diagonal approach to generate a binary string in O(n) time.
- Checking if the generated string is in the set takes O(1) (average case for hash set lookup).
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(n) for storing the result string and O(m) for the set of binary strings, 
  where m is the number of strings in the input list.
- Overall, the space complexity is O(n + m).

Topic: Arrays, Strings, Hashing
"""