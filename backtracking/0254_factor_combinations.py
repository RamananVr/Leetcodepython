"""
LeetCode Question #254: Factor Combinations

Problem Statement:
Numbers can be regarded as the product of their factors. For example, 8 = 2 x 4 = 2 x 2 x 2.
Write a function that takes an integer n and returns all possible combinations of its factors 
excluding 1 and n itself.

Note:
- You may assume that n is always greater than 1.
- Factors should be listed in ascending order.

Example:
Input: n = 12
Output: [[2, 6], [2, 2, 3], [3, 4]]

Input: n = 32
Output: [[2, 16], [2, 2, 8], [2, 2, 2, 4], [2, 2, 2, 2, 2], [4, 8]]

Constraints:
- 1 <= n <= 10^8
"""

# Solution
def getFactors(n):
    def dfs(start, target):
        # Base case: if target is 1, we stop recursion
        if target == 1:
            return
        
        for i in range(start, int(target**0.5) + 1):
            if target % i == 0:
                # Add the current factor combination
                result.append(path + [i, target // i])
                # Continue searching for factors
                path.append(i)
                dfs(i, target // i)
                path.pop()
    
    result = []
    path = []
    dfs(2, n)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 12
    print(f"Factors of {n1}: {getFactors(n1)}")  # Expected Output: [[2, 6], [2, 2, 3], [3, 4]]

    # Test Case 2
    n2 = 32
    print(f"Factors of {n2}: {getFactors(n2)}")  # Expected Output: [[2, 16], [2, 2, 8], [2, 2, 2, 4], [2, 2, 2, 2, 2], [4, 8]]

    # Test Case 3
    n3 = 15
    print(f"Factors of {n3}: {getFactors(n3)}")  # Expected Output: [[3, 5]]

    # Test Case 4
    n4 = 1
    print(f"Factors of {n4}: {getFactors(n4)}")  # Expected Output: []

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through all possible factors up to sqrt(n) for each recursive call.
- In the worst case, the number of recursive calls and factor combinations grows exponentially 
  with the number of factors of n. However, the pruning of invalid paths reduces the number of calls.
- Overall complexity is approximately O(k * sqrt(n)), where k is the number of valid factor combinations.

Space Complexity:
- The space complexity is determined by the recursion depth and the storage of results.
- The recursion depth is proportional to the number of factors, which is O(log(n)) in the worst case.
- The result list stores all valid combinations, which can grow to O(k), where k is the number of combinations.
- Overall space complexity is O(k + log(n)).
"""

# Topic: Backtracking