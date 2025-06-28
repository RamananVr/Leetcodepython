"""
LeetCode Problem 2776: Convert Callback Based Function to Promise Based Function

Write a function that converts a callback-based function to a Promise-based function.

The callback-based function follows the Node.js convention where the last parameter is a callback function that takes an error as the first parameter and the result as the second parameter.

Your function should return a new function that returns a Promise.

Constraints:
- The original function follows Node.js callback convention: callback(error, result)
- 1 <= arguments.length <= 100
- 0 <= callback executions <= 1

Example 1:
Input: fn = (callback) => { callback(null, 42) }
Output: A function that returns Promise.resolve(42)

Example 2:
Input: fn = (n, callback) => { 
    if (n < 0) callback(new Error("negative"))
    else callback(null, n * 2)
}
Output: A function that returns Promise.resolve(n * 2) for n >= 0, Promise.reject(Error) for n < 0

Topics: Promises, Asynchronous Programming, JavaScript, Functions
"""

class Solution:
    def promisify(self, fn):
        """
        Approach 1: Standard Promisify Implementation
        
        Convert a callback-based function to Promise-based.
        The returned function captures all arguments except the callback,
        then wraps the original function call in a Promise.
        
        Time: O(1) for function creation
        Space: O(1) for closure variables
        """
        def promisified(*args):
            """
            Return a Promise that resolves/rejects based on callback result.
            
            This is a Python simulation of JavaScript Promise behavior.
            In actual JavaScript, this would return a real Promise object.
            """
            from concurrent.futures import Future
            import threading
            
            future = Future()
            
            def callback(error, result=None):
                if error is not None:
                    future.set_exception(error)
                else:
                    future.set_result(result)
            
            try:
                # Call the original function with args + callback
                fn(*args, callback)
            except Exception as e:
                future.set_exception(e)
            
            return future
        
        return promisified
    
    def promisify_simple(self, fn):
        """
        Approach 2: Simplified Promise simulation
        
        For testing purposes, use a simpler Promise-like object.
        
        Time: O(1)
        Space: O(1)
        """
        class SimplePromise:
            def __init__(self):
                self.resolved = False
                self.rejected = False
                self.value = None
                self.error = None
            
            def resolve(self, value):
                self.resolved = True
                self.value = value
                return self
            
            def reject(self, error):
                self.rejected = True
                self.error = error
                return self
            
            def then(self, on_resolve=None, on_reject=None):
                if self.resolved and on_resolve:
                    return on_resolve(self.value)
                elif self.rejected and on_reject:
                    return on_reject(self.error)
                return self
        
        def promisified(*args):
            promise = SimplePromise()
            
            def callback(error, result=None):
                if error is not None:
                    promise.reject(error)
                else:
                    promise.resolve(result)
            
            try:
                fn(*args, callback)
            except Exception as e:
                promise.reject(e)
            
            return promise
        
        return promisified
    
    def promisify_with_executor(self, fn):
        """
        Approach 3: Promise with executor pattern
        
        Simulate JavaScript Promise constructor with executor function.
        
        Time: O(1)
        Space: O(1)
        """
        class PromiseExecutor:
            def __init__(self, executor):
                self.resolved = False
                self.rejected = False
                self.value = None
                self.error = None
                
                def resolve(value):
                    if not self.resolved and not self.rejected:
                        self.resolved = True
                        self.value = value
                
                def reject(error):
                    if not self.resolved and not self.rejected:
                        self.rejected = True
                        self.error = error
                
                try:
                    executor(resolve, reject)
                except Exception as e:
                    reject(e)
        
        def promisified(*args):
            def executor(resolve, reject):
                def callback(error, result=None):
                    if error is not None:
                        reject(error)
                    else:
                        resolve(result)
                
                fn(*args, callback)
            
            return PromiseExecutor(executor)
        
        return promisified

def test_promisify():
    """Test the promisify solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Simple successful callback
    def simple_fn(callback):
        callback(None, 42)
    
    promisified_simple = solution.promisify_simple(simple_fn)
    result1 = promisified_simple()
    assert result1.resolved == True
    assert result1.value == 42
    
    # Test case 2: Function with parameters
    def multiply_fn(n, callback):
        if n < 0:
            callback(Exception("negative number"))
        else:
            callback(None, n * 2)
    
    promisified_multiply = solution.promisify_simple(multiply_fn)
    
    # Test positive case
    result2 = promisified_multiply(5)
    assert result2.resolved == True
    assert result2.value == 10
    
    # Test negative case
    result3 = promisified_multiply(-3)
    assert result3.rejected == True
    assert isinstance(result3.error, Exception)
    
    # Test case 3: Function with multiple parameters
    def add_fn(a, b, callback):
        try:
            result = a + b
            callback(None, result)
        except Exception as e:
            callback(e)
    
    promisified_add = solution.promisify_simple(add_fn)
    result4 = promisified_add(3, 7)
    assert result4.resolved == True
    assert result4.value == 10
    
    # Test case 4: Function that throws error
    def error_fn(callback):
        raise ValueError("Something went wrong")
    
    promisified_error = solution.promisify_simple(error_fn)
    result5 = promisified_error()
    assert result5.rejected == True
    assert isinstance(result5.error, ValueError)
    
    # Test case 5: Function with no parameters
    def no_param_fn(callback):
        callback(None, "success")
    
    promisified_no_param = solution.promisify_simple(no_param_fn)
    result6 = promisified_no_param()
    assert result6.resolved == True
    assert result6.value == "success"
    
    # Test case 6: Function that calls callback with error
    def callback_error_fn(should_error, callback):
        if should_error:
            callback(RuntimeError("callback error"))
        else:
            callback(None, "ok")
    
    promisified_callback_error = solution.promisify_simple(callback_error_fn)
    result7 = promisified_callback_error(True)
    assert result7.rejected == True
    
    result8 = promisified_callback_error(False)
    assert result8.resolved == True
    assert result8.value == "ok"
    
    # Test with executor approach
    promisified_executor = solution.promisify_with_executor(simple_fn)
    result9 = promisified_executor()
    assert result9.resolved == True
    assert result9.value == 42
    
    print("All promisify tests passed!")

if __name__ == "__main__":
    test_promisify()
