"""
LeetCode Problem #2431: Maximize Total Tastiness of Fruits

Problem Statement:
You are given an array `tastiness` where `tastiness[i]` represents the tastiness of the i-th fruit. 
You are also given an integer `k`. You want to maximize the total tastiness of the fruits you pick, 
but you can only pick at most `k` fruits, and you cannot pick two consecutive fruits.

Return the maximum total tastiness you can achieve.

Constraints:
- 1 <= tastiness.length <= 10^5
- 1 <= tastiness[i] <= 10^4
- 1 <= k <= tastiness.length
"""

def maximizeTastiness(tastiness, k):
    """
    Function to maximize the total tastiness of fruits while adhering to the constraints.
    
    :param tastiness: List[int] - List of tastiness values of fruits.
    :param k: int - Maximum number of fruits that can be picked.
    :return: int - Maximum total tastiness.
    """
    n = len(tastiness)
    
    # Edge case: If k is 0, no fruits can be picked.
    if k == 0:
        return 0
    
    # Dynamic Programming approach
    # dp[i][j] represents the maximum tastiness we can achieve by considering the first i fruits
    # and picking exactly j fruits.
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # Option 1: Skip the current fruit
            dp[i][j] = dp[i - 1][j]
            
            # Option 2: Pick the current fruit (if it's not consecutive to the previous one)
            if i > 1:
                dp[i][j] = max(dp[i][j], dp[i - 2][j - 1] + tastiness[i - 1])
            else:
                dp[i][j] = max(dp[i][j], tastiness[i - 1])
    
    # The answer is the maximum tastiness we can achieve by considering all n fruits and picking at most k fruits.
    return dp[n][k]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tastiness = [1, 2, 3, 4, 5]
    k = 2
    print(maximizeTastiness(tastiness, k))  # Expected Output: 8 (Pick 3 and 5)

    # Test Case 2
    tastiness = [5, 1, 1, 5]
    k = 2
    print(maximizeTastiness(tastiness, k))  # Expected Output: 10 (Pick 5 and 5)

    # Test Case 3
    tastiness = [10, 1, 10, 1, 10]
    k = 3
    print(maximizeTastiness(tastiness, k))  # Expected Output: 30 (Pick 10, 10, and 10)

    # Test Case 4
    tastiness = [1, 2, 3]
    k = 1
    print(maximizeTastiness(tastiness, k))  # Expected Output: 3 (Pick 3)

    # Test Case 5
    tastiness = [1]
    k = 1
    print(maximizeTastiness(tastiness, k))  # Expected Output: 1 (Pick 1)

"""
Time Complexity Analysis:
- The outer loop runs for `n` iterations (number of fruits).
- The inner loop runs for `k` iterations (maximum number of fruits to pick).
- Each iteration involves constant-time operations.
- Therefore, the time complexity is O(n * k).

Space Complexity Analysis:
- The DP table requires O(n * k) space.
- Therefore, the space complexity is O(n * k).

Topic: Dynamic Programming
"""