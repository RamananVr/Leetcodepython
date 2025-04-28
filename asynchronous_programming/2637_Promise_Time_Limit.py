"""
LeetCode Problem #2637: Promise Time Limit

Problem Statement:
Given an asynchronous function `fn` and a time `t` in milliseconds, return a new time-limited version of the input function. 
The new function should be identical to the input function unless it takes longer than `t` milliseconds to complete. 
In that case, it should reject with the string "Time Limit Exceeded".

Example 1:
Input: 
fn = async (n) => { await new Promise(res => setTimeout(res, 100)); return n * n; }
inputs = [5]
t = 50
Output: {"rejected": "Time Limit Exceeded"}

Example 2:
Input: 
fn = async (n) => { await new Promise(res => setTimeout(res, 100)); return n * n; }
inputs = [5]
t = 150
Output: {"resolved": 25}

Example 3:
Input: 
fn = async (a, b) => { await new Promise(res => setTimeout(res, 120)); return a + b; }
inputs = [10, 20]
t = 150
Output: {"resolved": 30}

Constraints:
- `fn` is a function that returns a promise.
- `t` is a non-negative integer in milliseconds.
- `inputs` is an array of valid arguments for `fn`.

"""

from typing import Callable, Any
import asyncio

def time_limit(fn: Callable, t: int) -> Callable:
    """
    Returns a time-limited version of the input asynchronous function.
    If the function takes longer than `t` milliseconds, it rejects with "Time Limit Exceeded".
    """
    async def wrapper(*args, **kwargs) -> Any:
        try:
            # Run the function with a timeout
            return await asyncio.wait_for(fn(*args, **kwargs), timeout=t / 1000)
        except asyncio.TimeoutError:
            # If timeout occurs, raise the appropriate error
            raise Exception("Time Limit Exceeded")
    return wrapper

# Example Test Cases
async def example_test_cases():
    # Example 1
    async def fn1(n):
        await asyncio.sleep(0.1)  # 100ms
        return n * n

    limited_fn1 = time_limit(fn1, 50)  # 50ms time limit
    try:
        result = await limited_fn1(5)
        print({"resolved": result})
    except Exception as e:
        print({"rejected": str(e)})  # Expected: {"rejected": "Time Limit Exceeded"}

    # Example 2
    limited_fn2 = time_limit(fn1, 150)  # 150ms time limit
    try:
        result = await limited_fn2(5)
        print({"resolved": result})  # Expected: {"resolved": 25}
    except Exception as e:
        print({"rejected": str(e)})

    # Example 3
    async def fn2(a, b):
        await asyncio.sleep(0.12)  # 120ms
        return a + b

    limited_fn3 = time_limit(fn2, 150)  # 150ms time limit
    try:
        result = await limited_fn3(10, 20)
        print({"resolved": result})  # Expected: {"resolved": 30}
    except Exception as e:
        print({"rejected": str(e)})

# Run the test cases
if __name__ == "__main__":
    asyncio.run(example_test_cases())

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The time complexity of the function depends on the input function `fn`.
   - The `asyncio.wait_for` function itself adds negligible overhead, so the time complexity is O(T_fn),
     where T_fn is the time complexity of the input function `fn`.

2. Space Complexity:
   - The space complexity is also dependent on the input function `fn`.
   - The wrapper function and the `asyncio.wait_for` mechanism add negligible space overhead.
   - Therefore, the space complexity is O(S_fn), where S_fn is the space complexity of the input function `fn`.

Topic: Asynchronous Programming
"""