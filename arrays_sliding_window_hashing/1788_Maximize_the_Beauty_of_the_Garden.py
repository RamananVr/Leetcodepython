"""
LeetCode Problem #1788: Maximize the Beauty of the Garden

Problem Statement:
You are given an array `flowers` where `flowers[i]` represents the type of flower at position `i`. 
The beauty of a subarray is defined as the number of distinct flower types in that subarray. 
You are allowed to pick at most one subarray and reverse it. Your task is to maximize the beauty of the garden.

Return the maximum beauty of the garden you can achieve.

Constraints:
- 1 <= flowers.length <= 10^5
- 1 <= flowers[i] <= 10^5
"""

# Solution
def maximumBeauty(flowers):
    """
    This function calculates the maximum beauty of the garden by considering the reversal of at most one subarray.
    
    :param flowers: List[int] - The array of flower types.
    :return: int - The maximum beauty of the garden.
    """
    from collections import defaultdict

    # Step 1: Calculate the prefix and suffix distinct counts
    n = len(flowers)
    prefix_distinct = [0] * n
    suffix_distinct = [0] * n

    seen = set()
    for i in range(n):
        seen.add(flowers[i])
        prefix_distinct[i] = len(seen)

    seen.clear()
    for i in range(n - 1, -1, -1):
        seen.add(flowers[i])
        suffix_distinct[i] = len(seen)

    # Step 2: Calculate the maximum beauty
    max_beauty = max(prefix_distinct[-1], suffix_distinct[0])  # No reversal case

    # Use a dictionary to track the last occurrence of each flower type
    last_occurrence = defaultdict(int)
    for i in range(n):
        last_occurrence[flowers[i]] = i

    # Iterate through the array to consider reversing subarrays
    for i in range(n):
        # If we reverse a subarray ending at index i, calculate the beauty
        if i > 0:
            max_beauty = max(max_beauty, prefix_distinct[i - 1] + suffix_distinct[i])

    return max_beauty

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    flowers = [1, 2, 3, 2, 1]
    print(maximumBeauty(flowers))  # Expected Output: 3

    # Test Case 2
    flowers = [1, 2, 2, 2, 1]
    print(maximumBeauty(flowers))  # Expected Output: 2

    # Test Case 3
    flowers = [1, 1, 1, 1, 1]
    print(maximumBeauty(flowers))  # Expected Output: 1

    # Test Case 4
    flowers = [1, 2, 3, 4, 5]
    print(maximumBeauty(flowers))  # Expected Output: 5

"""
Time Complexity Analysis:
- Calculating prefix_distinct and suffix_distinct takes O(n) time.
- The main loop to calculate the maximum beauty also takes O(n) time.
- Overall, the time complexity is O(n).

Space Complexity Analysis:
- The space complexity is O(n) for the prefix_distinct and suffix_distinct arrays.
- Additionally, the `seen` set and `last_occurrence` dictionary use O(n) space in the worst case.
- Overall, the space complexity is O(n).

Topic: Arrays, Sliding Window, Hashing
"""