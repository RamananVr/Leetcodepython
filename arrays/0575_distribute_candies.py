"""
LeetCode Question #575: Distribute Candies

Problem Statement:
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

Constraints:
- n == candyType.length
- 2 <= n <= 10^4
- n is even.
- -10^5 <= candyType[i] <= 10^5
"""

# Python Solution
def distributeCandies(candyType):
    """
    :type candyType: List[int]
    :rtype: int
    """
    # Calculate the maximum number of candies Alice can eat
    max_candies = len(candyType) // 2
    
    # Calculate the number of unique candy types
    unique_candies = len(set(candyType))
    
    # Return the minimum of the two
    return min(max_candies, unique_candies)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    candyType1 = [1, 1, 2, 2, 3, 3]
    print(distributeCandies(candyType1))  # Expected Output: 3

    # Test Case 2
    candyType2 = [1, 1, 2, 3]
    print(distributeCandies(candyType2))  # Expected Output: 2

    # Test Case 3
    candyType3 = [6, 6, 6, 6]
    print(distributeCandies(candyType3))  # Expected Output: 1

    # Test Case 4
    candyType4 = [1, 2, 3, 4, 5, 6]
    print(distributeCandies(candyType4))  # Expected Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the unique candy types using `set(candyType)` takes O(n), where n is the length of the candyType array.
- Calculating the length of the set and performing the min operation are O(1).
- Overall time complexity: O(n).

Space Complexity:
- The space required to store the set of unique candy types is O(k), where k is the number of unique candy types.
- In the worst case, k = n (all candies are unique), so the space complexity is O(n).
- Overall space complexity: O(n).
"""

# Topic: Arrays