"""
LeetCode Problem #1013: Partition Array Into Three Parts With Equal Sum

Problem Statement:
Given an array of integers `arr`, return `true` if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indices `i`, `j` (with `i + 1 < j`) such that:
- `sum(arr[0:i+1]) == sum(arr[i+1:j]) == sum(arr[j:])`

If it is not possible, return `false`.

Constraints:
- 3 <= arr.length <= 5 * 10^4
- -10^4 <= arr[i] <= 10^4
"""

def canThreePartsEqualSum(arr):
    """
    Function to determine if the array can be partitioned into three parts with equal sum.

    :param arr: List[int] - The input array of integers
    :return: bool - True if the array can be partitioned into three parts with equal sum, False otherwise
    """
    total_sum = sum(arr)
    
    # If the total sum is not divisible by 3, we cannot partition the array
    if total_sum % 3 != 0:
        return False
    
    target = total_sum // 3
    current_sum = 0
    partitions = 0

    for num in arr:
        current_sum += num
        # When we find a subarray with the target sum, reset current_sum and increment partitions
        if current_sum == target:
            partitions += 1
            current_sum = 0
            # If we already found 2 partitions, the rest of the array must form the third partition
            if partitions == 2:
                return True

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Example from the problem statement
    arr1 = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
    print(canThreePartsEqualSum(arr1))  # Expected Output: True

    # Test Case 2: Another valid partition
    arr2 = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
    print(canThreePartsEqualSum(arr2))  # Expected Output: False

    # Test Case 3: Array with all zeros
    arr3 = [0, 0, 0, 0]
    print(canThreePartsEqualSum(arr3))  # Expected Output: True

    # Test Case 4: Array with no valid partition
    arr4 = [1, -1, 1, -1]
    print(canThreePartsEqualSum(arr4))  # Expected Output: False

    # Test Case 5: Large array with valid partition
    arr5 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(canThreePartsEqualSum(arr5))  # Expected Output: True

"""
Time Complexity Analysis:
- Calculating the total sum of the array takes O(n), where n is the length of the array.
- Iterating through the array to find partitions also takes O(n).
- Thus, the overall time complexity is O(n).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space (variables like `total_sum`, `target`, `current_sum`, and `partitions`).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""