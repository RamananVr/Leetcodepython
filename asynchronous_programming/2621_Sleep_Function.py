"""
LeetCode Problem #2621: Sleep Function

Problem Statement:
Write an asynchronous function `sleep` that takes in a positive integer `millis` (in milliseconds) and resolves a promise after the specified number of milliseconds.

The function should pause execution for the given duration and then resolve.

Example:
Input: sleep(100)
Output: A promise that resolves after 100ms.

Constraints:
- `millis` is a positive integer.
"""

import asyncio

# Solution
async def sleep(millis: int) -> None:
    """
    Asynchronous function that pauses execution for the given duration in milliseconds.

    Args:
    millis (int): The number of milliseconds to sleep.

    Returns:
    None
    """
    await asyncio.sleep(millis / 1000)

# Example Test Cases
async def test_sleep():
    """
    Test cases for the sleep function.
    """
    import time

    print("Test Case 1: Sleep for 100ms")
    start_time = time.time()
    await sleep(100)
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    print(f"Elapsed Time: {elapsed_time:.2f}ms (Expected: ~100ms)")

    print("Test Case 2: Sleep for 500ms")
    start_time = time.time()
    await sleep(500)
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    print(f"Elapsed Time: {elapsed_time:.2f}ms (Expected: ~500ms)")

    print("Test Case 3: Sleep for 1000ms")
    start_time = time.time()
    await sleep(1000)
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    print(f"Elapsed Time: {elapsed_time:.2f}ms (Expected: ~1000ms)")

# Time and Space Complexity Analysis
"""
Time Complexity:
The time complexity of the `sleep` function is O(1) because the function itself does not perform any operations that depend on the input size. It simply waits for the specified duration.

Space Complexity:
The space complexity is O(1) because the function does not use any additional data structures or memory that scales with the input size.
"""

# Topic
# Topic: Asynchronous Programming

# To run the test cases, use the following code:
# import asyncio
# asyncio.run(test_sleep())