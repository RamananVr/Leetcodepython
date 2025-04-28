"""
LeetCode Problem #1526: Minimum Number of Increments on Subarrays to Form a Target Array

Problem Statement:
You are given an integer array `target`. You have an integer array `arr` of the same length, initially with all zeros.

In one operation, you can choose any subarray of `arr` and increment each value by 1.

Return the minimum number of operations needed to form `target` from `arr`.

Constraints:
- `1 <= target.length <= 10^5`
- `0 <= target[i] <= 10^5`
"""

def minNumberOperations(target):
    """
    Calculate the minimum number of operations to form the target array.

    :param target: List[int] - The target array
    :return: int - Minimum number of operations
    """
    operations = target[0]  # Start with the first element
    for i in range(1, len(target)):
        if target[i] > target[i - 1]:
            operations += target[i] - target[i - 1]
    return operations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    target1 = [1, 2, 3, 2, 1]
    print(minNumberOperations(target1))  # Expected Output: 3

    # Test Case 2
    target2 = [3, 1, 1, 2]
    print(minNumberOperations(target2))  # Expected Output: 4

    # Test Case 3
    target3 = [3, 3, 3]
    print(minNumberOperations(target3))  # Expected Output: 3

    # Test Case 4
    target4 = [1, 2, 1, 2, 1]
    print(minNumberOperations(target4))  # Expected Output: 3

"""
Time Complexity:
- The solution iterates through the `target` array once, so the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The solution uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""