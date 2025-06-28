"""
LeetCode Problem 2795: Parallel Execution of Promises for Specific Duration

Given an array of asynchronous functions functions and a timeout time t, return a new function that executes all functions in parallel but terminates execution after t milliseconds.

The returned function should:
- Execute all functions in parallel
- Return a promise that resolves when all functions complete or when the timeout is reached
- If timeout occurs, reject with "Time Limit Exceeded"
- If all functions complete within time, resolve with array of results

Constraints:
- 1 <= functions.length <= 10
- 1 <= t <= 1000
- functions[i] returns a Promise

Example 1:
Input: functions = [() => new Promise(res => setTimeout(res, 100))], t = 50
Output: Promise rejects with "Time Limit Exceeded"

Example 2:
Input: functions = [() => new Promise(res => setTimeout(() => res(1), 100))], t = 200
Output: Promise resolves with [1]

Topics: Promises, Asynchronous Programming, JavaScript, Concurrency
"""

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from typing import List, Callable, Any

class Solution:
    def promiseAllWithTimeout(self, functions: List[Callable], t: int):
        """
        Approach 1: Python asyncio simulation of Promise.all with timeout
        
        Use asyncio to run all functions in parallel with a timeout.
        
        Time: O(min(t, max_function_time))
        Space: O(n) for storing function results
        """
        async def execute_with_timeout():
            # Convert functions to async tasks
            tasks = []
            for func in functions:
                # Wrap function to make it async if needed
                if asyncio.iscoroutinefunction(func):
                    tasks.append(func())
                else:
                    # For regular functions, run in executor
                    loop = asyncio.get_event_loop()
                    tasks.append(loop.run_in_executor(None, func))
            
            try:
                # Wait for all tasks with timeout
                results = await asyncio.wait_for(
                    asyncio.gather(*tasks), 
                    timeout=t / 1000.0  # Convert ms to seconds
                )
                return {"status": "resolved", "results": results}
            except asyncio.TimeoutError:
                return {"status": "rejected", "error": "Time Limit Exceeded"}
        
        return execute_with_timeout()
    
    def promiseAllWithTimeout_threading(self, functions: List[Callable], t: int):
        """
        Approach 2: Using ThreadPoolExecutor with timeout
        
        Execute functions in parallel using threads with timeout control.
        
        Time: O(min(t, max_function_time))
        Space: O(n)
        """
        class PromiseResult:
            def __init__(self):
                self.resolved = False
                self.rejected = False
                self.results = None
                self.error = None
        
        result = PromiseResult()
        
        def execute():
            try:
                with ThreadPoolExecutor(max_workers=len(functions)) as executor:
                    # Submit all functions
                    futures = [executor.submit(func) for func in functions]
                    
                    # Wait for completion with timeout
                    results = []
                    start_time = time.time()
                    
                    for future in futures:
                        remaining_time = (t / 1000.0) - (time.time() - start_time)
                        if remaining_time <= 0:
                            result.rejected = True
                            result.error = "Time Limit Exceeded"
                            return result
                        
                        try:
                            res = future.result(timeout=remaining_time)
                            results.append(res)
                        except TimeoutError:
                            result.rejected = True
                            result.error = "Time Limit Exceeded"
                            return result
                    
                    result.resolved = True
                    result.results = results
                    return result
                    
            except Exception as e:
                result.rejected = True
                result.error = str(e)
                return result
        
        return execute()
    
    def promiseAllWithTimeout_simple(self, functions: List[Callable], t: int):
        """
        Approach 3: Simple simulation for testing
        
        Execute functions sequentially but with overall timeout tracking.
        
        Time: O(sum of function times) or O(t), whichever is smaller
        Space: O(n)
        """
        class SimplePromise:
            def __init__(self):
                self.resolved = False
                self.rejected = False
                self.value = None
                self.error = None
        
        promise = SimplePromise()
        start_time = time.time() * 1000  # Convert to milliseconds
        results = []
        
        try:
            for func in functions:
                current_time = time.time() * 1000
                if current_time - start_time >= t:
                    promise.rejected = True
                    promise.error = "Time Limit Exceeded"
                    return promise
                
                # Execute function (simulate async behavior)
                result = func()
                results.append(result)
            
            promise.resolved = True
            promise.value = results
            return promise
            
        except Exception as e:
            promise.rejected = True
            promise.error = str(e)
            return promise
    
    def promiseAllWithTimeout_race_condition(self, functions: List[Callable], t: int):
        """
        Approach 4: Race condition between completion and timeout
        
        Simulate Promise.race between Promise.all and timeout.
        
        Time: O(min(t, max_function_time))
        Space: O(n)
        """
        import threading
        import queue
        
        result_queue = queue.Queue()
        
        def execute_all():
            try:
                results = []
                threads = []
                thread_results = [None] * len(functions)
                
                def run_function(idx, func):
                    thread_results[idx] = func()
                
                # Start all function threads
                for i, func in enumerate(functions):
                    thread = threading.Thread(target=run_function, args=(i, func))
                    thread.start()
                    threads.append(thread)
                
                # Wait for all threads to complete
                for thread in threads:
                    thread.join()
                
                result_queue.put({"status": "resolved", "results": thread_results})
                
            except Exception as e:
                result_queue.put({"status": "rejected", "error": str(e)})
        
        def timeout_handler():
            time.sleep(t / 1000.0)
            result_queue.put({"status": "rejected", "error": "Time Limit Exceeded"})
        
        # Start execution and timeout threads
        exec_thread = threading.Thread(target=execute_all)
        timeout_thread = threading.Thread(target=timeout_handler)
        
        exec_thread.start()
        timeout_thread.start()
        
        # Get the first result (either completion or timeout)
        result = result_queue.get()
        
        return result

def test_promise_all_with_timeout():
    """Test the promise all with timeout solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Function that takes too long
    def slow_function():
        time.sleep(0.1)  # 100ms
        return 1
    
    result1 = solution.promiseAllWithTimeout_simple([slow_function], 50)
    assert result1.rejected == True
    assert result1.error == "Time Limit Exceeded"
    
    # Test case 2: Function that completes in time
    def fast_function():
        time.sleep(0.05)  # 50ms
        return 42
    
    result2 = solution.promiseAllWithTimeout_simple([fast_function], 200)
    assert result2.resolved == True
    assert result2.value == [42]
    
    # Test case 3: Multiple functions, all complete in time
    def func1():
        time.sleep(0.02)  # 20ms
        return "first"
    
    def func2():
        time.sleep(0.03)  # 30ms
        return "second"
    
    result3 = solution.promiseAllWithTimeout_simple([func1, func2], 100)
    assert result3.resolved == True
    assert result3.value == ["first", "second"]
    
    # Test case 4: Multiple functions, one takes too long
    def func_fast():
        time.sleep(0.01)  # 10ms
        return "fast"
    
    def func_slow():
        time.sleep(0.08)  # 80ms
        return "slow"
    
    result4 = solution.promiseAllWithTimeout_simple([func_fast, func_slow], 50)
    assert result4.rejected == True
    
    # Test case 5: No functions
    result5 = solution.promiseAllWithTimeout_simple([], 100)
    assert result5.resolved == True
    assert result5.value == []
    
    # Test case 6: Function that throws error
    def error_function():
        raise ValueError("Function error")
    
    result6 = solution.promiseAllWithTimeout_simple([error_function], 100)
    assert result6.rejected == True
    
    # Test case 7: Very short timeout
    def normal_function():
        return "done"
    
    result7 = solution.promiseAllWithTimeout_simple([normal_function], 1)
    # May or may not timeout depending on execution speed
    
    # Test threading approach
    result8 = solution.promiseAllWithTimeout_threading([fast_function], 200)
    assert result8.resolved == True
    
    print("All promise all with timeout tests passed!")

if __name__ == "__main__":
    test_promise_all_with_timeout()
