"""
LeetCode Question #927: Three Equal Parts

Problem Statement:
You are given a binary array `arr` which is a list of 0s and 1s. We want to split the array into three non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any `[i, j]` with `i + 1 < j`, such that:
- `arr[0], arr[1], ..., arr[i]` is the first part,
- `arr[i + 1], arr[i + 2], ..., arr[j - 1]` is the second part, and
- `arr[j], arr[j + 1], ..., arr[arr.length - 1]` is the third part.
- All three parts have the same binary value.

If it is not possible, return `[-1, -1]`.

Note that the binary value represented by a part includes leading zeros, so `0001` and `1` are considered equal. A binary array is valid if and only if it can be split into three parts with equal binary values.

Constraints:
- `3 <= arr.length <= 3 * 10^4`
- `arr[i]` is `0` or `1`.

Example 1:
Input: arr = [1,0,1,0,1]
Output: [0,3]

Example 2:
Input: arr = [1,1,0,1,1]
Output: [-1,-1]

Example 3:
Input: arr = [1,1,0,0,1]
Output: [0,2]
"""

def threeEqualParts(arr):
    # Count the total number of 1s in the array
    total_ones = sum(arr)
    
    # If the total number of 1s is not divisible by 3, it's impossible to split
    if total_ones % 3 != 0:
        return [-1, -1]
    
    # If there are no 1s, any split is valid
    if total_ones == 0:
        return [0, len(arr) - 1]
    
    # Each part must contain exactly target_ones 1s
    target_ones = total_ones // 3
    first = second = third = -1
    ones_count = 0
    
    # Find the starting index of each part
    for i, bit in enumerate(arr):
        if bit == 1:
            ones_count += 1
            if ones_count == 1:
                first = i
            elif ones_count == target_ones + 1:
                second = i
            elif ones_count == 2 * target_ones + 1:
                third = i
    
    # Compare the three parts
    while third < len(arr) and arr[first] == arr[second] == arr[third]:
        first += 1
        second += 1
        third += 1
    
    # If we reached the end, the split is valid
    if third == len(arr):
        return [first - 1, second]
    
    return [-1, -1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 0, 1, 0, 1]
    print(threeEqualParts(arr1))  # Output: [0, 3]

    # Test Case 2
    arr2 = [1, 1, 0, 1, 1]
    print(threeEqualParts(arr2))  # Output: [-1, -1]

    # Test Case 3
    arr3 = [1, 1, 0, 0, 1]
    print(threeEqualParts(arr3))  # Output: [0, 2]

    # Test Case 4
    arr4 = [0, 0, 0, 0, 0]
    print(threeEqualParts(arr4))  # Output: [0, 4]

    # Test Case 5
    arr5 = [1, 0, 0, 1, 0, 0, 1]
    print(threeEqualParts(arr5))  # Output: [2, 5]

"""
Time Complexity:
- The algorithm iterates through the array multiple times, but each iteration is O(n), where n is the length of the array.
- Thus, the overall time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""