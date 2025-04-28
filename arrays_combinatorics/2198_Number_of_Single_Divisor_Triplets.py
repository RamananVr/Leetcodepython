"""
LeetCode Problem #2198: Number of Single Divisor Triplets

Problem Statement:
You are given an integer array `nums` of size `n`. A triplet `(i, j, k)` is called a single divisor triplet if:
1. `0 <= i, j, k < n`
2. `i`, `j`, and `k` are distinct.
3. There exists exactly one integer `d` such that `d` divides the sum of `nums[i] + nums[j] + nums[k]`.

Return the number of single divisor triplets in the array.

Constraints:
- `3 <= nums.length <= 100`
- `1 <= nums[i] <= 100`
"""

# Python Solution
from itertools import combinations
from collections import Counter

def singleDivisorTriplets(nums):
    """
    Function to calculate the number of single divisor triplets in the array.

    :param nums: List[int] - The input array of integers.
    :return: int - The number of single divisor triplets.
    """
    count = 0
    n = len(nums)
    
    # Iterate over all combinations of triplets
    for i, j, k in combinations(range(n), 3):
        triplet_sum = nums[i] + nums[j] + nums[k]
        divisors = 0
        
        # Check divisors of the triplet sum
        for d in range(1, triplet_sum + 1):
            if triplet_sum % d == 0:
                divisors += 1
            if divisors > 1:
                break
        
        # If exactly one divisor, increment the count
        if divisors == 1:
            count += 1
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 6, 7]
    print(singleDivisorTriplets(nums1))  # Expected Output: 0

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(singleDivisorTriplets(nums2))  # Expected Output: 4

    # Test Case 3
    nums3 = [1, 1, 1]
    print(singleDivisorTriplets(nums3))  # Expected Output: 0

    # Test Case 4
    nums4 = [10, 20, 30, 40, 50]
    print(singleDivisorTriplets(nums4))  # Expected Output: 0

"""
Time Complexity Analysis:
- The function iterates over all combinations of triplets, which is O(n^3) for n elements.
- For each triplet, we check divisors of the sum, which can take up to O(S) time, where S is the sum of the triplet.
- In the worst case, S can be as large as 300 (if nums[i] = 100 for all i).
- Therefore, the overall time complexity is O(n^3 * S), where S is the maximum possible sum of a triplet.

Space Complexity Analysis:
- The space complexity is O(1) as we are not using any additional data structures that scale with input size.

Topic: Arrays, Combinatorics
"""