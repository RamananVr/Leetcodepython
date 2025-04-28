"""
LeetCode Problem #2860: Happy Students

Problem Statement:
You are given an array `candies` where `candies[i]` represents the number of candies the i-th student has. 
You are also given an integer `extraCandies`. A student is considered happy if, after receiving the extra candies, 
they have at least as many candies as the student with the maximum candies in the class.

Return the number of students who can be happy after receiving the extra candies.

Example:
Input: candies = [2, 3, 5, 1, 3], extraCandies = 3
Output: 3
Explanation: 
- Student 0: 2 + 3 = 5 (happy)
- Student 1: 3 + 3 = 6 (happy)
- Student 2: 5 + 3 = 8 (happy)
- Student 3: 1 + 3 = 4 (not happy)
- Student 4: 3 + 3 = 6 (happy)
Thus, 3 students are happy.

Constraints:
- 1 <= candies.length <= 100
- 1 <= candies[i] <= 100
- 1 <= extraCandies <= 50
"""

# Python Solution
def happyStudents(candies, extraCandies):
    """
    Function to calculate the number of happy students after distributing extra candies.

    :param candies: List[int] - List of candies each student has.
    :param extraCandies: int - Number of extra candies to distribute.
    :return: int - Number of happy students.
    """
    max_candies = max(candies)  # Find the maximum candies any student currently has
    happy_count = 0

    for candy in candies:
        if candy + extraCandies >= max_candies:
            happy_count += 1

    return happy_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(happyStudents(candies, extraCandies))  # Output: 3

    # Test Case 2
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    print(happyStudents(candies, extraCandies))  # Output: 1

    # Test Case 3
    candies = [12, 1, 12]
    extraCandies = 10
    print(happyStudents(candies, extraCandies))  # Output: 3

    # Test Case 4
    candies = [1, 2, 3, 4, 5]
    extraCandies = 2
    print(happyStudents(candies, extraCandies))  # Output: 3

    # Test Case 5
    candies = [5, 5, 5, 5]
    extraCandies = 0
    print(happyStudents(candies, extraCandies))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- Finding the maximum value in the candies array takes O(n), where n is the length of the candies array.
- Iterating through the candies array to count happy students also takes O(n).
- Thus, the overall time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Arrays