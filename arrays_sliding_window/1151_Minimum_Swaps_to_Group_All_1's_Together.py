"""
LeetCode Problem #1151: Minimum Swaps to Group All 1's Together

Problem Statement:
Given a binary array `data`, return the minimum number of swaps required to group all `1`s present in the array together in any place in the array.

A swap is defined as exchanging the positions of two elements in the array.

Example 1:
Input: data = [1,0,1,0,1]
Output: 1
Explanation: 
There are 3 ones in the array, so we need to group all 1's together in a subarray of length 3. 
The only way to achieve this is by swapping the second and third elements.

Example 2:
Input: data = [0,0,0,1,0]
Output: 0
Explanation: 
Since there is only one 1 in the array, no swaps are needed.

Example 3:
Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: 
There are 5 ones in the array, so we need to group all 1's together in a subarray of length 5. 
The minimum number of swaps required is 3.

Constraints:
- 1 <= data.length <= 10^5
- data[i] is either 0 or 1.
"""

def minSwaps(data):
    """
    Function to calculate the minimum number of swaps required to group all 1's together.
    
    Args:
    data (List[int]): A binary array containing 0s and 1s.

    Returns:
    int: The minimum number of swaps required.
    """
    # Count the total number of 1's in the array
    total_ones = sum(data)
    
    # If there are no 1's or only one 1, no swaps are needed
    if total_ones <= 1:
        return 0
    
    # Use a sliding window of size `total_ones` to find the maximum number of 1's in any subarray of that size
    max_ones_in_window = 0
    current_ones_in_window = 0
    left = 0
    
    for right in range(len(data)):
        # Expand the window by adding the current element
        current_ones_in_window += data[right]
        
        # If the window size exceeds `total_ones`, shrink it from the left
        if right - left + 1 > total_ones:
            current_ones_in_window -= data[left]
            left += 1
        
        # Update the maximum number of 1's in any valid window
        max_ones_in_window = max(max_ones_in_window, current_ones_in_window)
    
    # The minimum swaps required is the difference between total 1's and the maximum 1's in any window
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
Time Complexity Analysis:
- Calculating the total number of 1's takes O(n), where n is the length of the array.
- The sliding window traversal also takes O(n).
- Thus, the overall time complexity is O(n).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays, Sliding Window
"""