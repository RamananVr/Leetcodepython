"""
LeetCode Problem #1414: Find the Minimum Number of Fibonacci Numbers Whose Sum Is K

Problem Statement:
---------------------------------
Given an integer `k`, return the minimum number of Fibonacci numbers whose sum is equal to `k`. 
The same Fibonacci number can be used multiple times.

The Fibonacci numbers are defined as:
    F1 = 1, F2 = 1, F3 = 2, F4 = 3, F5 = 5, and so on.
    The sequence starts with 1 and 1, and each subsequent number is the sum of the two preceding ones.

It is guaranteed that for the given input `k`, the answer always exists.

Example 1:
Input: k = 7
Output: 2
Explanation: The sum of the Fibonacci numbers 2 and 5 is equal to 7.

Example 2:
Input: k = 10
Output: 2
Explanation: The sum of the Fibonacci numbers 2 and 8 is equal to 10.

Example 3:
Input: k = 19
Output: 3
Explanation: The sum of the Fibonacci numbers 1, 5, and 13 is equal to 19.

Constraints:
- 1 <= k <= 10^9
"""

# Python Solution
def findMinFibonacciNumbers(k: int) -> int:
    # Generate all Fibonacci numbers less than or equal to k
    fibs = [1, 1]
    while fibs[-1] <= k:
        fibs.append(fibs[-1] + fibs[-2])
    
    # Remove the last Fibonacci number if it exceeds k
    fibs.pop()
    
    count = 0
    while k > 0:
        # Use the largest Fibonacci number less than or equal to k
        for i in range(len(fibs) - 1, -1, -1):
            if fibs[i] <= k:
                k -= fibs[i]
                count += 1
                break
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    k1 = 7
    print(findMinFibonacciNumbers(k1))  # Output: 2

    # Test Case 2
    k2 = 10
    print(findMinFibonacciNumbers(k2))  # Output: 2

    # Test Case 3
    k3 = 19
    print(findMinFibonacciNumbers(k3))  # Output: 3

    # Additional Test Case
    k4 = 1
    print(findMinFibonacciNumbers(k4))  # Output: 1

    k5 = 100
    print(findMinFibonacciNumbers(k5))  # Output: 3

"""
Time and Space Complexity Analysis:
---------------------------------
Time Complexity:
- Generating the Fibonacci sequence takes O(log(k)) because the Fibonacci numbers grow exponentially.
- The greedy approach iterates through the Fibonacci list, which has at most O(log(k)) elements.
- Therefore, the overall time complexity is O(log(k)).

Space Complexity:
- The space required to store the Fibonacci sequence is O(log(k)), as the number of Fibonacci numbers less than or equal to k is proportional to log(k).
- Thus, the space complexity is O(log(k)).

Topic: Greedy Algorithm
"""