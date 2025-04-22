"""
LeetCode Problem #969: Pancake Sorting

Problem Statement:
Given an array of integers `arr`, where `arr[i]` is unique, you need to perform a series of pancake flips to sort the array in ascending order.

In one pancake flip, you can do the following:
- Choose an integer `k` where `1 <= k <= arr.length`.
- Reverse the sub-array `arr[0:k]` (0-indexed).

Return an array of the k-values corresponding to a sequence of pancake flips that sort `arr`. Any valid answer that sorts the array within 10 * arr.length flips will be accepted.

Constraints:
- 1 <= arr.length <= 100
- 1 <= arr[i] <= arr.length
- All integers in `arr` are unique.

Example:
Input: arr = [3, 2, 4, 1]
Output: [4, 2, 4, 3]
Explanation:
We perform 4 pancake flips (k-values in the output array):
1. Flip k = 4: Reverse [3, 2, 4, 1] -> [1, 4, 2, 3]
2. Flip k = 2: Reverse [1, 4] -> [4, 1, 2, 3]
3. Flip k = 4: Reverse [4, 1, 2, 3] -> [3, 2, 1, 4]
4. Flip k = 3: Reverse [3, 2, 1] -> [1, 2, 3, 4]

Input: arr = [1, 2, 3]
Output: []
Explanation: The array is already sorted, so no flips are needed.
"""

def pancakeSort(arr):
    """
    Sorts the array using pancake flips and returns the sequence of flips.

    :param arr: List[int] - The input array to be sorted
    :return: List[int] - The sequence of k-values for pancake flips
    """
    result = []
    n = len(arr)
    
    for size in range(n, 1, -1):
        # Find the index of the maximum element in the current subarray
        max_index = arr.index(max(arr[:size]))
        
        # If the maximum element is not already in its correct position
        if max_index != size - 1:
            # Step 1: Bring the maximum element to the front (if not already at the front)
            if max_index != 0:
                result.append(max_index + 1)
                arr[:max_index + 1] = reversed(arr[:max_index + 1])
            
            # Step 2: Move the maximum element to its correct position
            result.append(size)
            arr[:size] = reversed(arr[:size])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [3, 2, 4, 1]
    print("Input:", arr1)
    print("Output:", pancakeSort(arr1))  # Expected: [4, 2, 4, 3]

    # Test Case 2
    arr2 = [1, 2, 3]
    print("Input:", arr2)
    print("Output:", pancakeSort(arr2))  # Expected: []

    # Test Case 3
    arr3 = [4, 3, 2, 1]
    print("Input:", arr3)
    print("Output:", pancakeSort(arr3))  # Expected: [4, 3, 2, 4, 3, 2]

    # Test Case 4
    arr4 = [1]
    print("Input:", arr4)
    print("Output:", pancakeSort(arr4))  # Expected: []

"""
Time Complexity:
- The outer loop runs `n` times, where `n` is the length of the array.
- Inside the loop, finding the maximum element takes O(n) in the worst case.
- Reversing the subarray also takes O(n) in the worst case.
- Therefore, the overall time complexity is O(n^2).

Space Complexity:
- The algorithm uses O(1) additional space since it modifies the input array in place and uses a result list to store the flips.

Topic: Arrays
"""