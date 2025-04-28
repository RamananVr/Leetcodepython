"""
LeetCode Problem #810: Chalkboard XOR Game

Problem Statement:
You are given an array of integers `nums` representing the numbers written on a chalkboard. 
Alice and Bob take turns erasing numbers from the chalkboard, with Alice starting first. 
If erasing a number causes the XOR of all the remaining numbers to become 0, then the player 
whose turn it is loses the game. Assume both players play optimally.

Return `True` if and only if Alice wins the game, assuming both players play optimally.

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 2^16

"""

# Solution
def xorGame(nums):
    """
    Determines if Alice wins the XOR game given the array nums.

    :param nums: List[int] - The array of integers on the chalkboard.
    :return: bool - True if Alice wins, False otherwise.
    """
    # Calculate the XOR of all numbers in the array
    xor_sum = 0
    for num in nums:
        xor_sum ^= num
    
    # Alice wins if:
    # 1. The XOR of all numbers is already 0 (Alice wins immediately).
    # 2. The length of nums is even (Alice can always force a win).
    return xor_sum == 0 or len(nums) % 2 == 0


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Alice wins because the XOR of all numbers is already 0.
    nums1 = [1, 1, 2, 2]
    print(xorGame(nums1))  # Expected output: True

    # Test Case 2: Alice wins because the length of nums is even.
    nums2 = [1, 2, 3, 4]
    print(xorGame(nums2))  # Expected output: True

    # Test Case 3: Alice loses because the XOR is non-zero and the length is odd.
    nums3 = [1, 2, 3]
    print(xorGame(nums3))  # Expected output: False

    # Test Case 4: Alice wins because the XOR of all numbers is already 0.
    nums4 = [0, 0, 0]
    print(xorGame(nums4))  # Expected output: True

    # Test Case 5: Alice wins because the length of nums is even.
    nums5 = [5, 7, 9, 11]
    print(xorGame(nums5))  # Expected output: True


# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the XOR of all numbers in the array takes O(n), where n is the length of nums.
- The rest of the operations (checking conditions) are O(1).
- Overall time complexity: O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space (xor_sum variable).
- Overall space complexity: O(1).
"""

# Topic: Bit Manipulation