"""
LeetCode Question #2171: Removing Minimum Number of Magic Beans

Problem Statement:
You are given an array `beans` where `beans[i]` represents the number of magic beans in the ith bag.

You can remove any number of beans from any bag, but you must remove the same number of beans from all bags in one operation. Your goal is to minimize the total number of beans removed.

Return the minimum number of beans you have to remove.

Constraints:
- 1 <= beans.length <= 10^5
- 1 <= beans[i] <= 10^9
"""

# Solution
def minimumRemoval(beans):
    """
    Function to calculate the minimum number of beans to remove.

    Args:
    beans (List[int]): List of integers representing the number of beans in each bag.

    Returns:
    int: Minimum number of beans to remove.
    """
    # Sort the array to make calculations easier
    beans.sort()
    
    # Calculate the total number of beans
    total_beans = sum(beans)
    
    # Initialize the minimum removal variable
    min_removal = float('inf')
    
    # Iterate through the sorted array
    for i in range(len(beans)):
        # Calculate the number of beans left if we keep all beans in bags from index i onward
        beans_left = beans[i] * (len(beans) - i)
        
        # Calculate the number of beans removed
        removal = total_beans - beans_left
        
        # Update the minimum removal
        min_removal = min(min_removal, removal)
    
    return min_removal

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    beans1 = [4, 1, 6, 5]
    print(minimumRemoval(beans1))  # Expected Output: 4

    # Test Case 2
    beans2 = [2, 10, 3, 2]
    print(minimumRemoval(beans2))  # Expected Output: 7

    # Test Case 3
    beans3 = [1, 1, 1, 1]
    print(minimumRemoval(beans3))  # Expected Output: 0

    # Test Case 4
    beans4 = [1000000000, 1, 1, 1]
    print(minimumRemoval(beans4))  # Expected Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The iteration through the array takes O(n).
- Therefore, the overall time complexity is O(n log n).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures apart from a few variables.

Topic: Arrays, Sorting
"""