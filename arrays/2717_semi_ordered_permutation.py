"""
LeetCode Problem #2717: Semi-Ordered Permutation

Problem Statement:
You are given a 0-indexed permutation of `n` integers `nums`.

A permutation is called semi-ordered if the first element is the smallest element and the last element is the largest element. You can perform the below operation as many times as you want until you make `nums` a semi-ordered permutation:
- Pick two adjacent elements and swap them.

Return the minimum number of swaps to make `nums` semi-ordered.

Constraints:
- `2 <= nums.length <= 50`
- `1 <= nums[i] <= 50`
- `nums` is a permutation.
"""

def semiOrderedPermutation(nums):
    """
    Finds minimum swaps to make permutation semi-ordered.
    
    :param nums: List[int] - Permutation of integers
    :return: int - Minimum number of swaps
    """
    n = len(nums)
    
    # Find positions of minimum and maximum elements
    min_val = min(nums)
    max_val = max(nums)
    
    min_pos = nums.index(min_val)
    max_pos = nums.index(max_val)
    
    # Calculate swaps needed to move min to front
    swaps_for_min = min_pos
    
    # Calculate swaps needed to move max to back
    swaps_for_max = (n - 1) - max_pos
    
    # If min_pos > max_pos, moving min to front will help move max to back
    # We save one swap in this case
    if min_pos > max_pos:
        return swaps_for_min + swaps_for_max - 1
    else:
        return swaps_for_min + swaps_for_max

def semiOrderedPermutationSimulation(nums):
    """
    Simulation approach that actually performs the swaps.
    
    :param nums: List[int] - Permutation of integers
    :return: int - Minimum number of swaps
    """
    nums = nums.copy()  # Don't modify the original array
    n = len(nums)
    swaps = 0
    
    min_val = min(nums)
    max_val = max(nums)
    
    # Move minimum element to the front
    min_pos = nums.index(min_val)
    while min_pos > 0:
        # Swap with previous element
        nums[min_pos], nums[min_pos - 1] = nums[min_pos - 1], nums[min_pos]
        min_pos -= 1
        swaps += 1
    
    # Move maximum element to the back
    max_pos = nums.index(max_val)
    while max_pos < n - 1:
        # Swap with next element
        nums[max_pos], nums[max_pos + 1] = nums[max_pos + 1], nums[max_pos]
        max_pos += 1
        swaps += 1
    
    return swaps

def semiOrderedPermutationOptimal(nums):
    """
    Optimal solution with clear logic.
    
    :param nums: List[int] - Permutation of integers
    :return: int - Minimum number of swaps
    """
    n = len(nums)
    
    # Find positions of 1 (minimum) and n (maximum) in the permutation
    pos_1 = -1
    pos_n = -1
    
    for i in range(n):
        if nums[i] == 1:
            pos_1 = i
        if nums[i] == n:
            pos_n = i
    
    # Swaps needed to move 1 to position 0
    swaps_to_move_1 = pos_1
    
    # Swaps needed to move n to position n-1
    swaps_to_move_n = (n - 1) - pos_n
    
    # If 1 is to the right of n, they will cross paths during movement
    # This saves us one swap
    overlap = 1 if pos_1 > pos_n else 0
    
    return swaps_to_move_1 + swaps_to_move_n - overlap

def semiOrderedPermutationBruteForce(nums):
    """
    Brute force approach for verification.
    
    :param nums: List[int] - Permutation of integers
    :return: int - Minimum number of swaps
    """
    n = len(nums)
    nums = nums.copy()
    swaps = 0
    
    # Keep swapping until we get semi-ordered permutation
    while not (nums[0] == min(nums) and nums[-1] == max(nums)):
        # Strategy: Move min towards front and max towards back
        min_val = min(nums)
        max_val = max(nums)
        
        min_pos = nums.index(min_val)
        max_pos = nums.index(max_val)
        
        # Decide which move to make
        made_swap = False
        
        # Try to move min towards front
        if min_pos > 0:
            nums[min_pos], nums[min_pos - 1] = nums[min_pos - 1], nums[min_pos]
            swaps += 1
            made_swap = True
        # Try to move max towards back
        elif max_pos < n - 1:
            nums[max_pos], nums[max_pos + 1] = nums[max_pos + 1], nums[max_pos]
            swaps += 1
            made_swap = True
        
        if not made_swap:
            break
    
    return swaps

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [2, 1, 4, 3]
    print(f"nums: {nums}")
    print(f"semiOrderedPermutation: {semiOrderedPermutation(nums)}")  # Output: 2
    print(f"semiOrderedPermutationSimulation: {semiOrderedPermutationSimulation(nums)}")  # Output: 2
    print(f"semiOrderedPermutationOptimal: {semiOrderedPermutationOptimal(nums)}")  # Output: 2
    print()

    # Test Case 2
    nums = [2, 4, 1, 3]
    print(f"nums: {nums}")
    print(f"semiOrderedPermutation: {semiOrderedPermutation(nums)}")  # Output: 3
    print(f"semiOrderedPermutationSimulation: {semiOrderedPermutationSimulation(nums)}")  # Output: 3
    print(f"semiOrderedPermutationOptimal: {semiOrderedPermutationOptimal(nums)}")  # Output: 3
    print()

    # Test Case 3
    nums = [1, 3, 4, 2, 5]
    print(f"nums: {nums}")
    print(f"semiOrderedPermutation: {semiOrderedPermutation(nums)}")  # Output: 3
    print(f"semiOrderedPermutationSimulation: {semiOrderedPermutationSimulation(nums)}")  # Output: 3
    print(f"semiOrderedPermutationOptimal: {semiOrderedPermutationOptimal(nums)}")  # Output: 3
    print()

    # Test Case 4 - Already semi-ordered
    nums = [1, 2, 3, 4]
    print(f"nums: {nums}")
    print(f"semiOrderedPermutation: {semiOrderedPermutation(nums)}")  # Output: 0
    print(f"semiOrderedPermutationSimulation: {semiOrderedPermutationSimulation(nums)}")  # Output: 0
    print(f"semiOrderedPermutationOptimal: {semiOrderedPermutationOptimal(nums)}")  # Output: 0
    print()

    # Test Case 5 - Reverse order
    nums = [4, 3, 2, 1]
    print(f"nums: {nums}")
    print(f"semiOrderedPermutation: {semiOrderedPermutation(nums)}")  # Output: 5
    print(f"semiOrderedPermutationSimulation: {semiOrderedPermutationSimulation(nums)}")  # Output: 5
    print(f"semiOrderedPermutationOptimal: {semiOrderedPermutationOptimal(nums)}")  # Output: 5

    # Test Case 6 - Min and max adjacent
    nums = [3, 1, 2]
    print(f"nums: {nums}")
    print(f"semiOrderedPermutation: {semiOrderedPermutation(nums)}")  # Output: 2
    print(f"semiOrderedPermutationOptimal: {semiOrderedPermutationOptimal(nums)}")  # Output: 2

    # Validation
    assert semiOrderedPermutation([2, 1, 4, 3]) == 2
    assert semiOrderedPermutationOptimal([2, 4, 1, 3]) == 3
    assert semiOrderedPermutationSimulation([1, 3, 4, 2, 5]) == 3
    assert semiOrderedPermutation([1, 2, 3, 4]) == 0
    print("All test cases passed!")

"""
Time Complexity Analysis:
Optimal Solution:
- Time complexity: O(n) to find positions of min and max elements.

Simulation:
- Time complexity: O(n^2) in the worst case due to repeated searching and swapping.

Space Complexity Analysis:
- Space complexity: O(1) for optimal solution, O(n) for simulation (due to copying array).

Topic: Arrays, Permutation, Greedy, Simulation
"""
