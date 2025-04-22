"""
LeetCode Problem #412: Fizz Buzz

Problem Statement:
Given an integer n, return a string array answer (1-indexed) where:

- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i (as a string) if none of the above conditions are true.

Example 1:
Input: n = 3
Output: ["1", "2", "Fizz"]

Example 2:
Input: n = 5
Output: ["1", "2", "Fizz", "4", "Buzz"]

Example 3:
Input: n = 15
Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]

Constraints:
- 1 <= n <= 10^4
"""

def fizzBuzz(n: int) -> list[str]:
    """
    Returns a list of strings representing the FizzBuzz sequence for numbers from 1 to n.
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 3
    print(fizzBuzz(n1))  # Output: ["1", "2", "Fizz"]

    # Test Case 2
    n2 = 5
    print(fizzBuzz(n2))  # Output: ["1", "2", "Fizz", "4", "Buzz"]

    # Test Case 3
    n3 = 15
    print(fizzBuzz(n3))  # Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through numbers from 1 to n, performing constant-time operations for each number.
- Therefore, the time complexity is O(n).

Space Complexity:
- The function uses a list to store the results, which requires O(n) space.
- Thus, the space complexity is O(n).
"""

# Topic: Strings, Simulation