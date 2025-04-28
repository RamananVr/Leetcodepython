"""
LeetCode Problem #1395: Count Number of Teams

Problem Statement:
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:
- Choose 3 soldiers with indexes (i, j, k) with 0 <= i < j < k < n.
- A team is valid if:
  - (rating[i] < rating[j] < rating[k]) or
  - (rating[i] > rating[j] > rating[k]) where rating is the array of the soldiers' ratings.

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example 1:
Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams:
- (2,3,4) with indices (0,2,3)
- (5,4,1) with indices (1,3,4)
- (5,3,1) with indices (1,2,4)

Example 2:
Input: rating = [2,1,3]
Output: 0
Explanation: No valid teams can be formed.

Example 3:
Input: rating = [1,2,3,4]
Output: 4

Constraints:
- 3 <= rating.length <= 1000
- 1 <= rating[i] <= 10^5
- All the integers in rating are unique.
"""

def numTeams(rating):
    """
    Function to count the number of valid teams of 3 soldiers.

    :param rating: List[int] - List of soldier ratings
    :return: int - Number of valid teams
    """
    n = len(rating)
    count = 0

    # Iterate through each soldier as the middle soldier in the team
    for j in range(1, n - 1):
        left_smaller = left_larger = right_smaller = right_larger = 0

        # Count soldiers to the left of j
        for i in range(j):
            if rating[i] < rating[j]:
                left_smaller += 1
            elif rating[i] > rating[j]:
                left_larger += 1

        # Count soldiers to the right of j
        for k in range(j + 1, n):
            if rating[k] < rating[j]:
                right_smaller += 1
            elif rating[k] > rating[j]:
                right_larger += 1

        # Calculate the number of valid teams with j as the middle soldier
        count += left_smaller * right_larger + left_larger * right_smaller

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rating1 = [2, 5, 3, 4, 1]
    print(numTeams(rating1))  # Output: 3

    # Test Case 2
    rating2 = [2, 1, 3]
    print(numTeams(rating2))  # Output: 0

    # Test Case 3
    rating3 = [1, 2, 3, 4]
    print(numTeams(rating3))  # Output: 4

    # Test Case 4
    rating4 = [4, 7, 9, 2, 5, 1]
    print(numTeams(rating4))  # Output: 8

    # Test Case 5
    rating5 = [10, 20, 30, 40, 50]
    print(numTeams(rating5))  # Output: 10

"""
Time Complexity:
- The outer loop iterates through each soldier as the middle soldier (O(n)).
- For each middle soldier, we iterate through the left and right sides (O(n) each).
- Thus, the overall time complexity is O(n^2).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""