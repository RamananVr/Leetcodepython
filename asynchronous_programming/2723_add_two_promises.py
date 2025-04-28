"""
LeetCode Question #2723: Add Two Promises

Problem Statement:
Given two promises `promise1` and `promise2`, return a new promise. 
When both promises resolve, the returned promise should resolve with the sum of the two values. 
If either promise rejects, the returned promise should reject with the same reason.

Example 1:
Input: 
promise1 = Promise.resolve(2)
promise2 = Promise.resolve(5)
Output: Promise that resolves to 7

Example 2:
Input: 
promise1 = Promise.reject("Error")
promise2 = Promise.resolve(5)
Output: Promise that rejects with "Error"

Constraints:
- Both promises are guaranteed to either resolve with a number or reject with a string.
"""

# Python Solution
import asyncio

async def add_two_promises(promise1, promise2):
    """
    This function takes two promises (asyncio Futures) and returns a new promise (Future).
    The returned promise resolves with the sum of the two values if both promises resolve.
    If either promise rejects, the returned promise rejects with the same reason.
    """
    try:
        # Wait for both promises to resolve
        result1, result2 = await asyncio.gather(promise1, promise2)
        # Return the sum of the resolved values
        return result1 + result2
    except Exception as e:
        # If any promise rejects, propagate the rejection
        raise e

# Example Test Cases
async def test_add_two_promises():
    # Test Case 1: Both promises resolve
    promise1 = asyncio.Future()
    promise2 = asyncio.Future()
    promise1.set_result(2)
    promise2.set_result(5)
    result = await add_two_promises(promise1, promise2)
    assert result == 7, f"Expected 7, but got {result}"

    # Test Case 2: One promise rejects
    promise1 = asyncio.Future()
    promise2 = asyncio.Future()
    promise1.set_exception(Exception("Error"))
    promise2.set_result(5)
    try:
        await add_two_promises(promise1, promise2)
    except Exception as e:
        assert str(e) == "Error", f"Expected 'Error', but got {str(e)}"

    # Test Case 3: Both promises reject
    promise1 = asyncio.Future()
    promise2 = asyncio.Future()
    promise1.set_exception(Exception("Error1"))
    promise2.set_exception(Exception("Error2"))
    try:
        await add_two_promises(promise1, promise2)
    except Exception as e:
        assert str(e) == "Error1", f"Expected 'Error1', but got {str(e)}"

    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    asyncio.run(test_add_two_promises())

"""
Time Complexity Analysis:
- The `asyncio.gather` function waits for both promises to resolve or reject.
- If both promises resolve, the time complexity is O(1) since we are only summing two numbers.
- If either promise rejects, the time complexity is still O(1) as the rejection is handled immediately.

Space Complexity Analysis:
- The space complexity is O(1) since we are not using any additional data structures.

Topic: Asynchronous Programming
"""