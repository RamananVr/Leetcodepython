"""
LeetCode Problem #2028: Find Missing Observations

Problem Statement:
You have observations of `n` dice rolls with each face numbered from 1 to 6. 
You are given an integer array `rolls` of length `n` where `rolls[i]` is the value of the ith roll. 
You are also given two integers `mean` and `k`.

Return an array of length `k` containing the missing rolls such that the mean of all `n + k` rolls is exactly `mean`. 
If there are multiple valid answers, return any of them. If no such array exists, return an empty array.

The mean of a set of integers is the sum of the integers divided by how many integers there are. 
For example, the mean of `[2, 3, 4]` is `(2 + 3 + 4) / 3 = 3.0`.

Note that `mean` is an integer, so the sum of the `n + k` rolls must be divisible by `n + k`.

Constraints:
- `n == rolls.length`
- `1 <= n, k <= 10^5`
- `1 <= rolls[i], mean <= 6`
"""

from typing import List

def missingRolls(rolls: List[int], mean: int, k: int) -> List[int]:
    # Calculate the total sum required for all rolls
    total_sum = mean * (len(rolls) + k)
    
    # Calculate the sum of the observed rolls
    observed_sum = sum(rolls)
    
    # Calculate the sum required for the missing rolls
    missing_sum = total_sum - observed_sum
    
    # If the missing sum is not achievable, return an empty array
    if missing_sum < k or missing_sum > 6 * k:
        return []
    
    # Distribute the missing sum across k rolls
    result = [missing_sum // k] * k
    remainder = missing_sum % k
    
    # Distribute the remainder to make the sum exactly equal to missing_sum
    for i in range(remainder):
        result[i] += 1
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rolls = [3, 2, 4, 3]
    mean = 4
    k = 2
    print(missingRolls(rolls, mean, k))  # Output: [6, 6] or any valid distribution

    # Test Case 2
    rolls = [1, 5, 6]
    mean = 3
    k = 4
    print(missingRolls(rolls, mean, k))  # Output: [2, 2, 2, 2] or any valid distribution

    # Test Case 3
    rolls = [1, 2, 3, 4]
    mean = 6
    k = 4
    print(missingRolls(rolls, mean, k))  # Output: [] (not possible)

    # Test Case 4
    rolls = [6, 6, 6, 6]
    mean = 5
    k = 4
    print(missingRolls(rolls, mean, k))  # Output: [4, 4, 4, 4] or any valid distribution

"""
Time Complexity:
- Calculating the sum of `rolls` takes O(n).
- Distributing the missing sum across `k` rolls takes O(k).
- Overall time complexity: O(n + k).

Space Complexity:
- The result array takes O(k) space.
- Overall space complexity: O(k).

Topic: Arrays
"""