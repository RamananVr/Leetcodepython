"""
LeetCode Question #2636: Promise Time Limit

Problem Statement:
Implement a function `timeLimit` that takes two arguments:
1. A function `fn` that returns a Promise.
2. A time limit in milliseconds `t`.

The function should return a new function that calls `fn`. If `fn` takes longer than `t` milliseconds to resolve, the returned function should reject with the string "Time Limit Exceeded". Otherwise, it should resolve with the result.

Example:
const limited = timeLimit((t) => new Promise(res => setTimeout(() => res('Success'), t)), 100);
limited(150).catch(console.log); // "Time Limit Exceeded"
limited(50).then(console.log); // "Success"

Constraints:
- `fn` is a function that returns a Promise.
- `t` is a positive integer representing the time limit in milliseconds.
"""

# Python Solution
import asyncio

def timeLimit(fn, t):
    async def wrapper(*args, **kwargs):
        try:
            return await asyncio.wait_for(fn(*args, **kwargs), timeout=t / 1000)
        except asyncio.TimeoutError:
            raise Exception("Time Limit Exceeded")
    return wrapper

# Example Test Cases
async def example_function(delay):
    await asyncio.sleep(delay / 1000)
    return "Success"

async def test_time_limit():
    limited = timeLimit(example_function, 100)
    
    try:
        result = await limited(50)  # Should resolve successfully
        print(result)  # Expected Output: "Success"
    except Exception as e:
        print(e)
    
    try:
        result = await limited(150)  # Should reject with "Time Limit Exceeded"
        print(result)
    except Exception as e:
        print(e)  # Expected Output: "Time Limit Exceeded"

# Run the test cases
if __name__ == "__main__":
    asyncio.run(test_time_limit())

"""
Time and Space Complexity Analysis:
1. Time Complexity:
   - The function `timeLimit` itself has negligible overhead.
   - The actual time complexity depends on the execution time of the provided `fn` function.
   - The timeout mechanism adds a constant overhead, so the overall time complexity is O(fn).

2. Space Complexity:
   - The space complexity is primarily determined by the memory usage of the provided `fn` function.
   - The timeout mechanism adds negligible space overhead, so the overall space complexity is O(fn).

Topic: Asynchronous Programming
"""