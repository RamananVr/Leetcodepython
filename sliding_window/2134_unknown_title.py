"""
LeetCode Problem #2134: Minimum Swaps to Group All 1's Together II

Problem Statement:
You are given a binary array `data` containing only 0's and 1's. A swap operation 
consists of choosing two indices `i` and `j` (i != j) and swapping the values at 
`data[i]` and `data[j]`.

Return the minimum number of swaps required to group all 1's together in the array.

Note that the 1's do not need to be contiguous in the original array.

Constraints:
- 1 <= data.length <= 10^5
- data[i] is either 0 or 1.

Example 1:
Input: data = [1,0,1,0,1]
Output: 1
Explanation: 
There are 3 1's in the array, and we can group all 1's together by swapping index 1 and 3.

Example 2:
Input: data = [0,0,0,1,0]
Output: 0
Explanation: 
Since there is only one 1 in the array, no swaps are needed.

Example 3:
Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: 
There are 6 1's in the array, and we can group all 1's together by swapping.

"""

# Python Solution
def minSwaps(data):
    """
    Function to calculate the minimum number of swaps required to group all 1's together.
    
    :param data: List[int] - Binary array containing 0's and 1's
    :return: int - Minimum number of swaps required
    """
    # Count the total number of 1's in the array
    total_ones = sum(data)
    
    # If there are no 1's or only one 1, no swaps are needed
    if total_ones <= 1:
        return 0
    
    # Use a sliding window of size `total_ones` to find the maximum number of 1's in any window
    max_ones_in_window = 0
    current_ones_in_window = 0
    n = len(data)
    
    # Initialize the sliding window
    for i in range(total_ones):
        current_ones_in_window += data[i]
    
    max_ones_in_window = current_ones_in_window
    
    # Slide the window across the array
    for i in range(total_ones, n):
        current_ones_in_window += data[i] - data[i - total_ones]
        max_ones_in_window = max(max_ones_in_window, current_ones_in_window)
    
    # The minimum swaps required is the number of 0's in the best window
    return total_ones - max_ones_in_window

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    data1 = [1, 0, 1, 0, 1]
    print(minSwaps(data1))  # Output: 1

    # Test Case 2
    data2 = [0, 0, 0, 1, 0]
    print(minSwaps(data2))  # Output: 0

    # Test Case 3
    data3 = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]
    print(minSwaps(data3))  # Output: 3

    # Test Case 4
    data4 = [1, 1, 1, 1, 1]
    print(minSwaps(data4))  # Output: 0

    # Test Case 5
    data5 = [0, 0, 0, 0, 0]
    print(minSwaps(data5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses a sliding window approach, which involves iterating over the array once.
- The initialization of the sliding window takes O(total_ones) time, and sliding the window across the array takes O(n) time.
- Therefore, the overall time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables.
- Therefore, the space complexity is O(1).

Topic: Sliding Window
"""