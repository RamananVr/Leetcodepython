"""
LeetCode Problem #2650: Design Cancellable Function

Problem Statement:
Sometimes you have a long running task and you may want to cancel it before it completes. To aid in this goal, write a function cancellable that accepts a generator function as input and returns an array of two values:

1. A cancel function.
2. A promise that resolves to the value the generator function was supposed to return.

You may assume the generator function will only yield promises. It is your function's responsibility to pass the resolved values back to the generator and to handle when the promise rejects.

If the cancel function is called before the generator finishes, your function should return a promise that resolves to the string "Cancelled". Otherwise, it should return a promise that resolves to the value returned by the generator function.

Example 1:
Input: 
generatorFunction = async function*() {
    return 42;
}
cancelTimeMs = 100
Output: {"resolved": 42, "time": 0}
Explanation: The generator immediately returned 42. Since cancelTimeMs = 100 and the generator completed at t=0ms, it was not cancelled.

Example 2:
Input:
generatorFunction = async function*() {
    const msg = yield new Promise(res => setTimeout(() => res("Hello"), 100));
    throw `Error: ${msg}`;
}
cancelTimeMs = 50
Output: {"resolved": "Cancelled", "time": 50}
Explanation: The function was cancelled at t=50ms. At this point, the generator had yielded a promise that would resolve to "Hello" in 100ms.

Example 3:
Input:
generatorFunction = async function*() {
    const msg = yield new Promise(res => setTimeout(() => res("Hello"), 100));
    return `${msg} World`;
}
cancelTimeMs = 150
Output: {"resolved": "Hello World", "time": 100}
Explanation: The function was not cancelled. The first yielded promise resolved with "Hello" at t=100ms, then the generator returned "Hello World".

Constraints:
- The generator function will only yield promises
- cancelTimeMs is a positive integer
"""

import asyncio
from typing import Callable, Any, Tuple, Coroutine, AsyncGenerator
import time

async def cancellable(generator_func: Callable[[], AsyncGenerator], cancel_time_ms: int) -> dict:
    """
    Create a cancellable function that can interrupt a generator function.
    
    Args:
        generator_func: Async generator function to execute
        cancel_time_ms: Time in milliseconds after which to cancel
        
    Returns:
        dict: Result containing 'resolved' value and 'time' taken
    """
    start_time = time.time() * 1000  # Convert to milliseconds
    
    # Create the generator
    gen = generator_func()
    
    # Create cancel task
    async def cancel_after_delay():
        await asyncio.sleep(cancel_time_ms / 1000)  # Convert ms to seconds
        return "Cancelled"
    
    cancel_task = asyncio.create_task(cancel_after_delay())
    
    # Execute generator
    async def run_generator():
        try:
            current_value = None
            while True:
                try:
                    if current_value is None:
                        # First iteration - call next() without sending value
                        promise = await gen.__anext__()
                    else:
                        # Send resolved value back to generator
                        promise = await gen.asend(current_value)
                    
                    # Wait for the yielded promise
                    current_value = await promise
                    
                except StopAsyncIteration as e:
                    # Generator finished normally
                    return e.value if hasattr(e, 'value') else current_value
                    
        except Exception as e:
            # Generator threw an exception
            raise e
    
    generator_task = asyncio.create_task(run_generator())
    
    # Race between generator completion and cancellation
    try:
        done, pending = await asyncio.wait(
            {generator_task, cancel_task},
            return_when=asyncio.FIRST_COMPLETED
        )
        
        # Cancel remaining tasks
        for task in pending:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
        
        # Get the result from the completed task
        completed_task = done.pop()
        result = await completed_task
        
        end_time = time.time() * 1000
        elapsed_time = int(end_time - start_time)
        
        return {
            "resolved": result,
            "time": elapsed_time
        }
        
    except Exception as e:
        end_time = time.time() * 1000
        elapsed_time = int(end_time - start_time)
        
        return {
            "resolved": str(e),
            "time": elapsed_time
        }

def cancellable_sync_version(generator_func: Callable, cancel_time_ms: int) -> Tuple[Callable, Any]:
    """
    Synchronous version that returns cancel function and result
    """
    cancelled = False
    result = None
    
    def cancel():
        nonlocal cancelled
        cancelled = True
        return "Cancelled"
    
    def execute():
        nonlocal result, cancelled
        if cancelled:
            return "Cancelled"
        
        try:
            gen = generator_func()
            current_value = None
            
            while not cancelled:
                try:
                    if current_value is None:
                        yielded = next(gen)
                    else:
                        yielded = gen.send(current_value)
                    
                    # Simulate async operation
                    time.sleep(0.01)  # Small delay to allow cancellation
                    current_value = yielded
                    
                except StopIteration as e:
                    result = e.value if hasattr(e, 'value') else current_value
                    break
                    
            return "Cancelled" if cancelled else result
            
        except Exception as e:
            return str(e)
    
    return cancel, execute

class CancellableTask:
    """
    Class-based approach for cancellable tasks
    """
    
    def __init__(self, generator_func: Callable):
        self.generator_func = generator_func
        self.cancelled = False
        self.result = None
        self.start_time = None
    
    def cancel(self):
        """Cancel the task"""
        self.cancelled = True
        return "Cancelled"
    
    async def execute(self, cancel_time_ms: int = None):
        """Execute the generator function"""
        self.start_time = time.time() * 1000
        
        # Set up auto-cancel if specified
        if cancel_time_ms:
            async def auto_cancel():
                await asyncio.sleep(cancel_time_ms / 1000)
                self.cancel()
            
            asyncio.create_task(auto_cancel())
        
        try:
            gen = self.generator_func()
            current_value = None
            
            while not self.cancelled:
                try:
                    if current_value is None:
                        promise = await gen.__anext__()
                    else:
                        promise = await gen.asend(current_value)
                    
                    if self.cancelled:
                        break
                        
                    current_value = await promise
                    
                except StopAsyncIteration as e:
                    self.result = e.value if hasattr(e, 'value') else current_value
                    break
            
            end_time = time.time() * 1000
            elapsed = int(end_time - self.start_time)
            
            return {
                "resolved": "Cancelled" if self.cancelled else self.result,
                "time": elapsed
            }
            
        except Exception as e:
            end_time = time.time() * 1000
            elapsed = int(end_time - self.start_time)
            
            return {
                "resolved": str(e),
                "time": elapsed
            }

# Example Test Cases
async def test_cancellable():
    """Test cases for cancellable function"""
    
    # Test Case 1: Immediate return
    print("Test Case 1: Immediate return")
    async def immediate_generator():
        return 42
    
    result1 = await cancellable(immediate_generator, 100)
    print(f"Result 1: {result1}")  # Expected: {"resolved": 42, "time": ~0}
    
    # Test Case 2: Cancelled before completion
    print("\nTest Case 2: Cancelled before completion")
    async def slow_generator():
        msg = yield asyncio.sleep(0.1, result="Hello")  # 100ms delay
        raise Exception(f"Error: {msg}")
    
    result2 = await cancellable(slow_generator, 50)  # Cancel after 50ms
    print(f"Result 2: {result2}")  # Expected: {"resolved": "Cancelled", "time": ~50}
    
    # Test Case 3: Completes before cancellation
    print("\nTest Case 3: Completes before cancellation")
    async def normal_generator():
        msg = yield asyncio.sleep(0.1, result="Hello")  # 100ms delay
        return f"{msg} World"
    
    result3 = await cancellable(normal_generator, 150)  # Cancel after 150ms
    print(f"Result 3: {result3}")  # Expected: {"resolved": "Hello World", "time": ~100}
    
    # Test Case 4: Multiple yields
    print("\nTest Case 4: Multiple yields")
    async def multi_yield_generator():
        first = yield asyncio.sleep(0.05, result="First")  # 50ms
        second = yield asyncio.sleep(0.05, result="Second")  # 50ms
        return f"{first} and {second}"
    
    result4 = await cancellable(multi_yield_generator, 200)
    print(f"Result 4: {result4}")  # Expected: completes normally
    
    # Test Case 5: Exception handling
    print("\nTest Case 5: Exception in generator")
    async def error_generator():
        await asyncio.sleep(0.02)  # 20ms
        raise ValueError("Test error")
    
    result5 = await cancellable(error_generator, 100)
    print(f"Result 5: {result5}")  # Expected: error message
    
    # Test Case 6: Class-based approach
    print("\nTest Case 6: Class-based approach")
    async def class_test_generator():
        result = yield asyncio.sleep(0.08, result="Class test")
        return f"Completed: {result}"
    
    task = CancellableTask(class_test_generator)
    result6 = await task.execute(150)
    print(f"Result 6: {result6}")

if __name__ == "__main__":
    # Run async test cases
    asyncio.run(test_cancellable())

"""
Time and Space Complexity Analysis:

Time Complexity:
- Cancellable execution: O(n) where n is number of yields in generator
- Each yield operation adds constant overhead for task management
- Cancellation check: O(1) per iteration

Space Complexity:
- Generator state: O(1) for generator object
- Task management: O(1) for cancel task and generator task
- Overall: O(1) additional space beyond generator's own space requirements

The implementation efficiently handles cancellation through asyncio task racing,
allowing immediate termination when cancel conditions are met.

Key Features:
1. Proper async/await handling
2. Generator state management with send()
3. Exception propagation
4. Timing measurement
5. Clean task cancellation

Topic: Async Programming, Generators, Concurrency, Task Management
"""
