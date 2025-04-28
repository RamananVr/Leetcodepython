"""
LeetCode Problem #825: Friends Of Appropriate Ages

Problem Statement:
Some people will make friend requests. The list of their ages is given and sorted in non-decreasing order. 
A person A will only send a friend request to person B if the following conditions are met:
1. age[B] <= age[A]
2. age[B] > 0.5 * age[A] + 7
3. age[B] <= 100 or age[A] >= 100

Otherwise, A will not send a friend request to B.

Given an array `ages` where `ages[i]` is the age of the ith person, return the total number of friend requests made.

Constraints:
- 1 <= ages.length <= 2000
- 1 <= ages[i] <= 120
"""

# Solution
def numFriendRequests(ages):
    """
    Calculate the total number of friend requests based on the given conditions.

    :param ages: List[int] - List of ages of people
    :return: int - Total number of friend requests
    """
    from collections import Counter

    # Count the frequency of each age
    age_count = Counter(ages)
    total_requests = 0

    for age_a in age_count:
        for age_b in age_count:
            # Check the conditions for sending a friend request
            if age_b <= age_a and age_b > 0.5 * age_a + 7:
                # If age_a == age_b, we need to account for multiple people of the same age
                if age_a == age_b:
                    total_requests += age_count[age_a] * (age_count[age_a] - 1)
                else:
                    total_requests += age_count[age_a] * age_count[age_b]

    return total_requests

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    ages1 = [16, 16]
    print(numFriendRequests(ages1))  # Expected Output: 2

    # Test Case 2
    ages2 = [16, 17, 18]
    print(numFriendRequests(ages2))  # Expected Output: 2

    # Test Case 3
    ages3 = [20, 30, 100, 110, 120]
    print(numFriendRequests(ages3))  # Expected Output: 3

    # Test Case 4
    ages4 = [8, 85, 24, 85, 21]
    print(numFriendRequests(ages4))  # Expected Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop iterates over all unique ages in the `age_count` dictionary, and the inner loop does the same.
- If there are `k` unique ages, the complexity is O(k^2).
- In the worst case, `k` can be up to 120 (the maximum age), so the complexity is O(120^2), which is effectively constant.

Space Complexity:
- We use a Counter to store the frequency of ages, which requires O(k) space, where `k` is the number of unique ages.
- Thus, the space complexity is O(k), which is effectively O(120) in the worst case.
"""

# Topic: Arrays, Hash Table