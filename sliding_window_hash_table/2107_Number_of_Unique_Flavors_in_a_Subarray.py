"""
LeetCode Problem #2107: Number of Unique Flavors in a Subarray

Problem Statement:
You are given an array `flavors` where `flavors[i]` represents the flavor of the i-th candy. 
You are also given an integer `k`. You want to find the maximum number of unique flavors 
in any subarray of size `k`.

Return the maximum number of unique flavors in any subarray of size `k`.

Constraints:
- 1 <= len(flavors) <= 10^5
- 1 <= flavors[i] <= 10^5
- 1 <= k <= len(flavors)
"""

def maxUniqueFlavors(flavors, k):
    """
    Finds the maximum number of unique flavors in any subarray of size k.

    :param flavors: List[int] - The array of candy flavors.
    :param k: int - The size of the subarray.
    :return: int - The maximum number of unique flavors in any subarray of size k.
    """
    from collections import Counter

    # Initialize a sliding window and a counter to track flavor frequencies
    flavor_count = Counter()
    max_unique = 0
    left = 0

    for right in range(len(flavors)):
        # Add the current flavor to the counter
        flavor_count[flavors[right]] += 1

        # If the window size exceeds k, shrink it from the left
        if right - left + 1 > k:
            flavor_count[flavors[left]] -= 1
            if flavor_count[flavors[left]] == 0:
                del flavor_count[flavors[left]]
            left += 1

        # Update the maximum unique flavors if the window size is exactly k
        if right - left + 1 == k:
            max_unique = max(max_unique, len(flavor_count))

    return max_unique

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    flavors = [1, 2, 3, 2, 2, 1, 4]
    k = 3
    print(maxUniqueFlavors(flavors, k))  # Expected Output: 3

    # Test Case 2
    flavors = [1, 1, 1, 1, 1]
    k = 2
    print(maxUniqueFlavors(flavors, k))  # Expected Output: 1

    # Test Case 3
    flavors = [1, 2, 3, 4, 5]
    k = 5
    print(maxUniqueFlavors(flavors, k))  # Expected Output: 5

    # Test Case 4
    flavors = [1, 2, 1, 3, 4, 2, 3]
    k = 4
    print(maxUniqueFlavors(flavors, k))  # Expected Output: 4

    # Test Case 5
    flavors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3
    print(maxUniqueFlavors(flavors, k))  # Expected Output: 3

"""
Time Complexity:
- The algorithm uses a sliding window approach, where each element is added to and removed from the Counter at most once.
- Therefore, the time complexity is O(n), where n is the length of the `flavors` array.

Space Complexity:
- The space complexity is O(k), as the Counter will store at most `k` unique elements at any given time.

Topic: Sliding Window, Hash Table
"""