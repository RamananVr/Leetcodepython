"""
LeetCode Question #2723: Add Two Promises

Problem Statement:
Given two promises `promise1` and `promise2`, return a new promise. `promise1` and `promise2` will both resolve to a number. The returned promise should resolve to the sum of the two numbers.

Constraints:
- `promise1` and `promise2` are promises that resolve to numbers

Example:
Input: promise1 = new Promise(resolve => setTimeout(() => resolve(2), 20)), 
       promise2 = new Promise(resolve => setTimeout(() => resolve(5), 60))
Output: 7
Explanation: The two input promises resolve to the values of 2 and 5 respectively. The returned promise should resolve to a value of 2 + 5 = 7. The returned promise should resolve after both the input promises resolve.

Input: promise1 = new Promise(resolve => setTimeout(() => resolve(10), 50)), 
       promise2 = new Promise(resolve => setTimeout(() => resolve(-12), 30))
Output: -2
Explanation: The two input promises resolve to the values of 10 and -12 respectively. The returned promise should resolve to a value of 10 + (-12) = -2.
"""

async def addTwoPromises(promise1, promise2):
    """
    Add the results of two promises when they resolve.
    
    Args:
        promise1: Promise that resolves to a number
        promise2: Promise that resolves to a number
    
    Returns:
        Promise that resolves to the sum of the two numbers
    """
    # Wait for both promises to resolve
    value1 = await promise1
    value2 = await promise2
    
    # Return the sum
    return value1 + value2

def addTwoPromises_promise_all(promise1, promise2):
    """
    Use Promise.all equivalent to wait for both promises.
    
    Args:
        promise1: Promise that resolves to a number
        promise2: Promise that resolves to a number
    
    Returns:
        Promise that resolves to the sum
    """
    import asyncio
    
    async def sum_promises():
        results = await asyncio.gather(promise1, promise2)
        return results[0] + results[1]
    
    return sum_promises()

def addTwoPromises_manual_implementation(promise1, promise2):
    """
    Manual implementation without using built-in promise utilities.
    
    Args:
        promise1: Promise that resolves to a number
        promise2: Promise that resolves to a number
    
    Returns:
        Promise that resolves to the sum
    """
    import asyncio
    
    async def manual_add():
        # Manually wait for each promise
        result1 = None
        result2 = None
        
        # Create tasks for concurrent execution
        task1 = asyncio.create_task(promise1)
        task2 = asyncio.create_task(promise2)
        
        # Wait for both to complete
        result1 = await task1
        result2 = await task2
        
        return result1 + result2
    
    return manual_add()

def addTwoPromises_callback_style(promise1, promise2):
    """
    Callback-style implementation for educational purposes.
    
    Args:
        promise1: Promise that resolves to a number
        promise2: Promise that resolves to a number
    
    Returns:
        Promise that resolves to the sum
    """
    import asyncio
    
    class PromiseSum:
        def __init__(self):
            self.value1 = None
            self.value2 = None
            self.resolved_count = 0
            self.result = None
            self.future = asyncio.Future()
        
        async def add_promises(self, p1, p2):
            # Handle first promise
            try:
                self.value1 = await p1
                self.resolved_count += 1
                self._check_completion()
            except Exception as e:
                self.future.set_exception(e)
                return
            
            # Handle second promise
            try:
                self.value2 = await p2
                self.resolved_count += 1
                self._check_completion()
            except Exception as e:
                self.future.set_exception(e)
                return
            
            return await self.future
        
        def _check_completion(self):
            if self.resolved_count == 2:
                self.result = self.value1 + self.value2
                self.future.set_result(self.result)
    
    promise_sum = PromiseSum()
    return promise_sum.add_promises(promise1, promise2)

def addTwoPromises_concurrent(promise1, promise2):
    """
    Concurrent execution ensuring both promises run in parallel.
    
    Args:
        promise1: Promise that resolves to a number
        promise2: Promise that resolves to a number
    
    Returns:
        Promise that resolves to the sum
    """
    import asyncio
    
    async def concurrent_add():
        # Run promises concurrently
        results = await asyncio.gather(
            promise1,
            promise2,
            return_exceptions=True
        )
        
        # Check for exceptions
        for result in results:
            if isinstance(result, Exception):
                raise result
        
        return results[0] + results[1]
    
    return concurrent_add()

def addTwoPromises_with_timeout(promise1, promise2, timeout=10):
    """
    Add promises with timeout handling.
    
    Args:
        promise1: Promise that resolves to a number
        promise2: Promise that resolves to a number
        timeout: Maximum time to wait in seconds
    
    Returns:
        Promise that resolves to the sum or raises TimeoutError
    """
    import asyncio
    
    async def add_with_timeout():
        try:
            results = await asyncio.wait_for(
                asyncio.gather(promise1, promise2),
                timeout=timeout
            )
            return results[0] + results[1]
        except asyncio.TimeoutError:
            raise TimeoutError(f"Promises did not resolve within {timeout} seconds")
    
    return add_with_timeout()

# Example Test Cases and Simulation
if __name__ == "__main__":
    import asyncio
    import time
    
    # Helper function to create delayed promises
    async def delayed_promise(value, delay):
        await asyncio.sleep(delay / 1000)  # Convert to seconds
        return value
    
    async def run_tests():
        # Test Case 1
        promise1 = delayed_promise(2, 20)
        promise2 = delayed_promise(5, 60)
        result = await addTwoPromises(promise1, promise2)
        print(f"Test 1 - Expected: 7, Got: {result}")
        assert result == 7
        
        # Test Case 2
        promise1 = delayed_promise(10, 50)
        promise2 = delayed_promise(-12, 30)
        result = await addTwoPromises(promise1, promise2)
        print(f"Test 2 - Expected: -2, Got: {result}")
        assert result == -2
        
        # Test Case 3 - Zero values
        promise1 = delayed_promise(0, 10)
        promise2 = delayed_promise(0, 10)
        result = await addTwoPromises(promise1, promise2)
        print(f"Test 3 - Expected: 0, Got: {result}")
        assert result == 0
        
        # Test Case 4 - Large numbers
        promise1 = delayed_promise(1000000, 5)
        promise2 = delayed_promise(2000000, 5)
        result = await addTwoPromises(promise1, promise2)
        print(f"Test 4 - Expected: 3000000, Got: {result}")
        assert result == 3000000
        
        # Test Case 5 - Negative numbers
        promise1 = delayed_promise(-50, 15)
        promise2 = delayed_promise(-25, 25)
        result = await addTwoPromises(promise1, promise2)
        print(f"Test 5 - Expected: -75, Got: {result}")
        assert result == -75
        
        # Test timing (promises should run concurrently)
        start_time = time.time()
        promise1 = delayed_promise(1, 100)  # 100ms
        promise2 = delayed_promise(2, 100)  # 100ms
        result = await addTwoPromises(promise1, promise2)
        end_time = time.time()
        elapsed = (end_time - start_time) * 1000  # Convert to ms
        
        print(f"Test 6 - Concurrent execution: {elapsed:.0f}ms (should be ~100ms, not ~200ms)")
        assert result == 3
        assert elapsed < 150  # Should be close to 100ms, not 200ms
        
        # Test different implementations produce same results
        promise1 = delayed_promise(15, 20)
        promise2 = delayed_promise(25, 30)
        
        results = await asyncio.gather(
            addTwoPromises(promise1, delayed_promise(25, 30)),
            addTwoPromises_promise_all(delayed_promise(15, 20), delayed_promise(25, 30)),
            addTwoPromises_concurrent(delayed_promise(15, 20), delayed_promise(25, 30))
        )
        
        for i, result in enumerate(results):
            assert result == 40, f"Implementation {i} failed"
        
        print("All test cases passed!")
    
    # Run the async tests
    asyncio.run(run_tests())

"""
Time and Space Complexity Analysis:

Async/Await Solution:
1. Time Complexity: O(max(T1, T2))
   - Where T1 and T2 are the resolution times of promise1 and promise2
   - Promises execute concurrently, so total time is the maximum, not sum

2. Space Complexity: O(1)
   - Only stores the two resolved values temporarily
   - No additional data structures needed

Promise.all Equivalent (asyncio.gather):
1. Time Complexity: O(max(T1, T2))
   - Same as async/await, runs promises concurrently
   - gather waits for all promises to complete

2. Space Complexity: O(1)
   - Minimal additional space for result collection

Manual Implementation:
1. Time Complexity: O(max(T1, T2))
   - Tasks are created and run concurrently
   - Similar performance to built-in methods

2. Space Complexity: O(1)
   - Additional task objects, but constant space

Key Insights:
- Promises execute concurrently when awaited together
- Using await sequentially would be O(T1 + T2) instead
- asyncio.gather is preferred for multiple promises
- Error handling propagates from either promise
- Timeout can be added for reliability

Real-world Considerations:
- Handle promise rejection gracefully
- Consider timeout for long-running promises
- Use asyncio.gather for multiple promises
- Async/await provides clean, readable code

Topic: Asynchronous Programming, Promises, Concurrency, Error Handling
"""
