"""
LeetCode Question #1103: Distribute Candies to People

Problem Statement:
We distribute some number of candies, `candies`, to a row of `num_people` people in the following way:
- We then give 1 candy to the first person, 2 candies to the second person, and so on until we give `num_people` candies to the last person.
- Then, we start over again, giving 1 candy to the first person, 2 candies to the second person, and so on, until we run out of candies.

The distribution process continues until we cannot distribute the next batch completely. 
If there are not enough candies left to distribute to the next person, we give them all the remaining candies (instead of the number they would have received).

Return an array (of length `num_people`) that represents the final distribution of candies.

Example 1:
Input: candies = 7, num_people = 4
Output: [1, 2, 3, 1]

Example 2:
Input: candies = 10, num_people = 3
Output: [5, 2, 3]

Constraints:
- 1 <= candies <= 10^9
- 1 <= num_people <= 1000
"""

# Clean, Correct Python Solution
def distributeCandies(candies: int, num_people: int) -> list[int]:
    # Initialize the result array with zeros
    result = [0] * num_people
    # Initialize variables for the current candy count and index
    current_candy = 1
    index = 0
    
    # Distribute candies until we run out
    while candies > 0:
        # Determine how many candies to give
        give = min(current_candy, candies)
        # Add candies to the current person
        result[index % num_people] += give
        # Deduct candies from the total
        candies -= give
        # Move to the next person and increment the candy count
        index += 1
        current_candy += 1
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    candies = 7
    num_people = 4
    print(distributeCandies(candies, num_people))  # Output: [1, 2, 3, 1]

    # Test Case 2
    candies = 10
    num_people = 3
    print(distributeCandies(candies, num_people))  # Output: [5, 2, 3]

    # Test Case 3
    candies = 15
    num_people = 5
    print(distributeCandies(candies, num_people))  # Output: [1, 2, 3, 4, 5]

    # Test Case 4
    candies = 1
    num_people = 1
    print(distributeCandies(candies, num_people))  # Output: [1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The loop runs until all candies are distributed. In the worst case, the number of iterations is proportional to the square root of `candies` because the sum of the first `k` natural numbers is `k * (k + 1) / 2`.
- Therefore, the time complexity is O(sqrt(candies)).

Space Complexity:
- The space complexity is O(num_people) because we store the result array of size `num_people`.
"""

# Topic: Arrays