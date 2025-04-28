"""
LeetCode Question #2715: Timeout Error

Problem Statement:
You are given a function `timeout_error()` that simulates a timeout error. Your task is to implement a retry mechanism that calls the function up to `n` times until it succeeds. If the function succeeds, return its result. If it fails all `n` times, return "Timeout Error".

The function `timeout_error()` is provided and may raise an exception. You need to handle the exception and implement the retry logic.

Constraints:
- `timeout_error()` may succeed randomly or fail with an exception.
- You must retry the function up to `n` times.
- If the function succeeds, return its result immediately.
- If the function fails all `n` times, return "Timeout Error".
"""

# Solution
import random

def timeout_error():
    """Simulates a function that randomly succeeds or raises an exception."""
    if random.random() < 0.5:  # 50% chance of success
        return "Success"
    else:
        raise Exception("Timeout Error")

def retry_timeout_error(n):
    """
    Retries the `timeout_error` function up to `n` times until it succeeds.
    
    Args:
        n (int): Number of retry attempts.
    
    Returns:
        str: The result of the function if it succeeds, or "Timeout Error" if all retries fail.
    """
    for attempt in range(n):
        try:
            return timeout_error()
        except Exception as e:
            if attempt == n - 1:  # Last attempt
                return str(e)
    return "Timeout Error"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Retry 5 times
    print(retry_timeout_error(5))  # Output: "Success" or "Timeout Error"

    # Test Case 2: Retry 1 time
    print(retry_timeout_error(1))  # Output: "Success" or "Timeout Error"

    # Test Case 3: Retry 10 times
    print(retry_timeout_error(10))  # Output: "Success" or "Timeout Error"

"""
Time and Space Complexity Analysis:
- Time Complexity: O(n)
  The function `timeout_error()` is called up to `n` times in the worst case, where `n` is the number of retry attempts.
  
- Space Complexity: O(1)
  The solution uses a constant amount of space regardless of the number of retries.

Topic: Exception Handling
"""