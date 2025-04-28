"""
LeetCode Problem #2305: Fair Distribution of Cookies

Problem Statement:
You are given an integer array `cookies`, where `cookies[i]` denotes the number of cookies in the i-th bag. 
You are also given an integer `k` that denotes the number of children to distribute the cookies to. 
All the cookies in the same bag must go to the same child, and the distribution of cookies must be fair.

The fairness of a distribution is defined as the maximum number of cookies received by any child in the distribution.

Return the minimum fairness of all distributions.

Example 1:
Input: cookies = [8, 15, 10, 20, 8], k = 2
Output: 31
Explanation: One optimal distribution is [8, 15, 8] and [10, 20]. The fairness is max(31, 30) = 31.

Example 2:
Input: cookies = [6, 1, 3, 2, 2, 4, 1, 2], k = 3
Output: 7
Explanation: One optimal distribution is [6, 1], [3, 2, 2], [4, 1, 2]. The fairness is max(7, 7, 7) = 7.

Constraints:
- 2 <= cookies.length <= 8
- 1 <= cookies[i] <= 10^5
- 1 <= k <= cookies.length
"""

# Solution
from typing import List

def distributeCookies(cookies: List[int], k: int) -> int:
    def backtrack(index, children):
        # Base case: all cookies have been distributed
        if index == len(cookies):
            return max(children)
        
        # Initialize the minimum unfairness
        min_unfairness = float('inf')
        
        # Try giving the current bag of cookies to each child
        for i in range(k):
            children[i] += cookies[index]
            min_unfairness = min(min_unfairness, backtrack(index + 1, children))
            children[i] -= cookies[index]
            
        return min_unfairness
    
    # Start the backtracking process
    return backtrack(0, [0] * k)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cookies = [8, 15, 10, 20, 8]
    k = 2
    print(distributeCookies(cookies, k))  # Output: 31

    # Test Case 2
    cookies = [6, 1, 3, 2, 2, 4, 1, 2]
    k = 3
    print(distributeCookies(cookies, k))  # Output: 7

    # Test Case 3
    cookies = [1, 2, 3, 4, 5]
    k = 2
    print(distributeCookies(cookies, k))  # Output: 9

    # Test Case 4
    cookies = [10, 10, 10]
    k = 3
    print(distributeCookies(cookies, k))  # Output: 10

# Time and Space Complexity Analysis
"""
Time Complexity:
- The number of possible distributions is k^n, where n is the number of cookie bags and k is the number of children.
- For each distribution, we calculate the maximum unfairness, which is O(k).
- Therefore, the overall time complexity is O(k^n * k), which simplifies to O(k^(n+1)).

Space Complexity:
- The space complexity is O(k) for the `children` array used in the backtracking process.
- Additionally, the recursion stack can go up to O(n) depth.
- Therefore, the overall space complexity is O(k + n).
"""

# Topic: Backtracking