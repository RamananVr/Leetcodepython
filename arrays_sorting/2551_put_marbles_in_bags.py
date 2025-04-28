"""
LeetCode Question #2551: Put Marbles in Bags

Problem Statement:
You are given a list of integers `weights` representing the weights of marbles, and an integer `k`. 
You want to divide the marbles into `k` bags such that:
1. Each bag contains at least one marble.
2. The score of a bag is defined as the sum of the smallest and largest marble weights in that bag.
3. The total score is the sum of the scores of all bags.

Return the difference between the maximum possible total score and the minimum possible total score.

Constraints:
- 1 <= len(weights) <= 10^5
- 1 <= weights[i] <= 10^9
- 2 <= k <= len(weights)
"""

# Solution
def putMarbles(weights, k):
    """
    Calculate the difference between the maximum and minimum possible total scores
    when dividing marbles into k bags.

    :param weights: List[int] - List of marble weights
    :param k: int - Number of bags
    :return: int - Difference between maximum and minimum total scores
    """
    n = len(weights)
    if k == 1:
        return 0  # If k == 1, all marbles go into one bag, so max and min scores are the same.

    # Calculate pair sums (weights[i] + weights[i+1])
    pair_sums = [weights[i] + weights[i + 1] for i in range(n - 1)]

    # Sort pair sums to find the smallest and largest k-1 sums
    pair_sums.sort()

    # Maximum score: Sum of the largest (k-1) pair sums
    max_score = sum(pair_sums[-(k - 1):])

    # Minimum score: Sum of the smallest (k-1) pair sums
    min_score = sum(pair_sums[:k - 1])

    # Return the difference between max and min scores
    return max_score - min_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    weights = [1, 3, 5, 1]
    k = 2
    print(putMarbles(weights, k))  # Expected Output: 4

    # Test Case 2
    weights = [1, 3]
    k = 2
    print(putMarbles(weights, k))  # Expected Output: 0

    # Test Case 3
    weights = [10, 20, 30, 40, 50]
    k = 3
    print(putMarbles(weights, k))  # Expected Output: 60

    # Test Case 4
    weights = [5, 1, 2, 6, 3, 4]
    k = 4
    print(putMarbles(weights, k))  # Expected Output: 7

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating pair sums takes O(n), where n is the length of the weights array.
- Sorting the pair sums takes O(n log n).
- Summing the k-1 smallest and largest pair sums takes O(k).
- Overall time complexity: O(n log n).

Space Complexity:
- The pair_sums list requires O(n) space.
- Overall space complexity: O(n).

Topic: Arrays, Sorting
"""