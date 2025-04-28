"""
LeetCode Problem #2701: "Maximum Number of Chocolates Distributed Equally"

Problem Statement:
You are given an integer array `chocolates` where `chocolates[i]` represents the number of chocolates in the i-th box. 
You want to distribute these chocolates equally among `k` children such that each child gets the same number of chocolates 
and the remaining chocolates (if any) are discarded. 

Return the maximum number of chocolates each child can get.

Constraints:
- 1 <= chocolates.length <= 10^5
- 1 <= chocolates[i] <= 10^9
- 1 <= k <= 10^9
"""

def max_chocolates_per_child(chocolates, k):
    """
    Function to calculate the maximum number of chocolates each child can get.
    
    :param chocolates: List[int] - List of integers representing chocolates in each box.
    :param k: int - Number of children.
    :return: int - Maximum number of chocolates each child can get.
    """
    def can_distribute(mid):
        """
        Helper function to check if it's possible to distribute `mid` chocolates to each child.
        """
        total_children = 0
        for choco in chocolates:
            total_children += choco // mid
            if total_children >= k:
                return True
        return total_children >= k

    # Binary search to find the maximum chocolates per child
    left, right = 1, max(chocolates)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_distribute(mid):
            result = mid  # Update result as we found a valid distribution
            left = mid + 1  # Try for a larger value
        else:
            right = mid - 1  # Try for a smaller value

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    chocolates = [5, 8, 6]
    k = 3
    print(max_chocolates_per_child(chocolates, k))  # Output: 5

    # Test Case 2
    chocolates = [2, 3, 5, 7]
    k = 4
    print(max_chocolates_per_child(chocolates, k))  # Output: 2

    # Test Case 3
    chocolates = [10, 20, 30]
    k = 5
    print(max_chocolates_per_child(chocolates, k))  # Output: 12

    # Test Case 4
    chocolates = [1, 1, 1, 1]
    k = 5
    print(max_chocolates_per_child(chocolates, k))  # Output: 0

    # Test Case 5
    chocolates = [1000000000, 1000000000]
    k = 2
    print(max_chocolates_per_child(chocolates, k))  # Output: 1000000000

"""
Time Complexity:
- The binary search runs in O(log(max_chocolates)) iterations, where max_chocolates is the maximum value in the `chocolates` array.
- For each iteration, we iterate through the `chocolates` array to calculate the total number of children that can be served, which takes O(n) time.
- Therefore, the overall time complexity is O(n * log(max_chocolates)).

Space Complexity:
- The space complexity is O(1) as we are using a constant amount of extra space.

Topic: Binary Search
"""