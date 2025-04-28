"""
LeetCode Problem #1640: Check Array Formation Through Concatenation

Problem Statement:
You are given an array of distinct integers `arr` and an array of integer arrays `pieces`, where the integers in `pieces` are distinct. Your goal is to form `arr` by concatenating the arrays in `pieces` in any order. However, you are not allowed to reorder the integers within each array in `pieces`.

Return `true` if it is possible to form the array `arr` from `pieces`. Otherwise, return `false`.

Example 1:
Input: arr = [85], pieces = [[85]]
Output: true

Example 2:
Input: arr = [15, 88], pieces = [[88], [15]]
Output: true
Explanation: Concatenate [15] then [88].

Example 3:
Input: arr = [49, 18, 16], pieces = [[16, 18, 49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].

Constraints:
- 1 <= arr.length <= 100
- 1 <= pieces.length <= 100
- 1 <= pieces[i].length <= arr.length
- 1 <= arr[i], pieces[i][j] <= 100
- The integers in `arr` are distinct.
- The integers in `pieces` are distinct (i.e., if we flatten `pieces`, all integers are unique).
"""

# Clean, Correct Python Solution
def canFormArray(arr, pieces):
    # Create a dictionary to map the first element of each piece to the piece itself
    piece_map = {piece[0]: piece for piece in pieces}
    
    i = 0
    while i < len(arr):
        # Check if the current element in arr exists as the first element in any piece
        if arr[i] not in piece_map:
            return False
        
        # Retrieve the corresponding piece
        piece = piece_map[arr[i]]
        
        # Check if the piece matches the corresponding segment in arr
        if arr[i:i+len(piece)] != piece:
            return False
        
        # Move the pointer forward by the length of the piece
        i += len(piece)
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [85]
    pieces1 = [[85]]
    print(canFormArray(arr1, pieces1))  # Output: True

    # Test Case 2
    arr2 = [15, 88]
    pieces2 = [[88], [15]]
    print(canFormArray(arr2, pieces2))  # Output: True

    # Test Case 3
    arr3 = [49, 18, 16]
    pieces3 = [[16, 18, 49]]
    print(canFormArray(arr3, pieces3))  # Output: False

    # Test Case 4
    arr4 = [91, 4, 64, 78]
    pieces4 = [[78], [4, 64], [91]]
    print(canFormArray(arr4, pieces4))  # Output: True

    # Test Case 5
    arr5 = [1, 3, 5, 7]
    pieces5 = [[2, 4, 6, 8]]
    print(canFormArray(arr5, pieces5))  # Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the `piece_map` dictionary takes O(p), where p is the total number of elements in `pieces`.
- Iterating through `arr` takes O(n), where n is the length of `arr`.
- For each element in `arr`, we perform a dictionary lookup and slice comparison, both of which are O(1) operations.
- Overall, the time complexity is O(n + p).

Space Complexity:
- The `piece_map` dictionary requires O(p) space, where p is the total number of elements in `pieces`.
- No additional space is used apart from the dictionary.
- Overall, the space complexity is O(p).
"""

# Topic: Arrays