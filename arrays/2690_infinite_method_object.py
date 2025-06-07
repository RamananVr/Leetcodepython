"""
LeetCode Question #2690: Infinite Method Object

Problem Statement:
Write a function that returns an object that can be called an infinite number of times.

- Calling obj.method() should return "Hello World".
- The object should be able to be called infinitely many times.
- Every time you call obj.method(), it should return the same result: "Hello World".

Examples:
Example 1:
Input: 
const obj = createInfiniteObject();
console.log(obj.method()); // "Hello World"
console.log(obj.method()); // "Hello World"
console.log(obj.method()); // "Hello World"

Example 2:
Input:
const obj = createInfiniteObject();
for (let i = 0; i < 1000000; i++) {
    console.log(obj.method()); // "Hello World" (1 million times)
}

Constraints:
- The function should work indefinitely
- Memory usage should be constant
- Each call should return exactly "Hello World"
"""

class InfiniteMethodObject:
    """
    Simple implementation of infinite method object.
    
    This object can be called infinitely and always returns "Hello World".
    """
    
    def method(self) -> str:
        """Always returns 'Hello World'."""
        return "Hello World"

def createInfiniteObject() -> InfiniteMethodObject:
    """
    Factory function to create an infinite method object.
    
    Returns:
        InfiniteMethodObject that can be called infinitely
    """
    return InfiniteMethodObject()

class InfiniteMethodObjectWithCounter:
    """
    Enhanced version that tracks how many times it's been called.
    """
    
    def __init__(self):
        self.call_count = 0
    
    def method(self) -> str:
        """Returns 'Hello World' and increments counter."""
        self.call_count += 1
        return "Hello World"
    
    def get_call_count(self) -> int:
        """Returns number of times method has been called."""
        return self.call_count
    
    def reset_counter(self) -> None:
        """Resets the call counter to 0."""
        self.call_count = 0

class InfiniteMethodObjectWithTimestamp:
    """
    Version that includes timestamp information.
    """
    
    def __init__(self):
        self.first_call_time = None
        self.last_call_time = None
        self.call_count = 0
    
    def method(self) -> str:
        """Returns 'Hello World' and updates timestamp info."""
        import time
        current_time = time.time()
        
        if self.first_call_time is None:
            self.first_call_time = current_time
        
        self.last_call_time = current_time
        self.call_count += 1
        
        return "Hello World"
    
    def get_stats(self) -> dict:
        """Returns statistics about method calls."""
        return {
            'call_count': self.call_count,
            'first_call_time': self.first_call_time,
            'last_call_time': self.last_call_time,
            'total_duration': (
                self.last_call_time - self.first_call_time 
                if self.first_call_time and self.last_call_time 
                else 0
            )
        }

class InfiniteMethodObjectWithCustomMessage:
    """
    Flexible version that allows custom message configuration.
    """
    
    def __init__(self, message: str = "Hello World"):
        self.message = message
        self.call_count = 0
    
    def method(self) -> str:
        """Returns the configured message."""
        self.call_count += 1
        return self.message
    
    def set_message(self, new_message: str) -> None:
        """Updates the message to return."""
        self.message = new_message
    
    def get_call_count(self) -> int:
        """Returns call count."""
        return self.call_count

class ThreadSafeInfiniteMethodObject:
    """
    Thread-safe version for concurrent access.
    """
    
    def __init__(self):
        import threading
        self.call_count = 0
        self.lock = threading.Lock()
    
    def method(self) -> str:
        """Thread-safe method that returns 'Hello World'."""
        with self.lock:
            self.call_count += 1
        return "Hello World"
    
    def get_call_count(self) -> int:
        """Thread-safe getter for call count."""
        with self.lock:
            return self.call_count

# JavaScript-like implementation using function closures
def createInfiniteObjectJS():
    """
    JavaScript-style implementation using closures.
    
    Returns a dictionary that mimics JavaScript object behavior.
    """
    call_count = [0]  # Use list to make it mutable in closure
    
    def method():
        call_count[0] += 1
        return "Hello World"
    
    return {
        'method': method,
        'get_call_count': lambda: call_count[0]
    }

def createInfiniteObjectGenerator():
    """
    Generator-based approach (different pattern but interesting).
    
    Returns an object that uses a generator internally.
    """
    def hello_world_generator():
        while True:
            yield "Hello World"
    
    class GeneratorBasedObject:
        def __init__(self):
            self.generator = hello_world_generator()
        
        def method(self):
            return next(self.generator)
    
    return GeneratorBasedObject()

# Performance testing utilities
def performance_test(obj, num_calls: int = 1000000):
    """
    Test performance of infinite method object.
    
    Args:
        obj: Object to test
        num_calls: Number of times to call the method
    
    Returns:
        Dictionary with performance metrics
    """
    import time
    import tracemalloc
    
    # Start memory tracking
    tracemalloc.start()
    
    start_time = time.time()
    
    # Make the calls
    for i in range(num_calls):
        result = obj.method()
        if result != "Hello World":
            raise ValueError(f"Unexpected result: {result}")
    
    end_time = time.time()
    
    # Get memory usage
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return {
        'num_calls': num_calls,
        'total_time': end_time - start_time,
        'calls_per_second': num_calls / (end_time - start_time),
        'memory_current': current,
        'memory_peak': peak,
        'time_per_call_ns': (end_time - start_time) * 1_000_000_000 / num_calls
    }

# Test Cases
if __name__ == "__main__":
    print("Testing Infinite Method Object implementations:")
    
    # Test basic implementation
    print("\n1. Basic Implementation:")
    obj1 = createInfiniteObject()
    for i in range(5):
        result = obj1.method()
        print(f"Call {i+1}: {result}")
    
    # Test with counter
    print("\n2. Implementation with Counter:")
    obj2 = InfiniteMethodObjectWithCounter()
    for i in range(3):
        result = obj2.method()
        print(f"Call {i+1}: {result} (Total calls: {obj2.get_call_count()})")
    
    # Test with timestamp
    print("\n3. Implementation with Timestamp:")
    obj3 = InfiniteMethodObjectWithTimestamp()
    for i in range(3):
        result = obj3.method()
        print(f"Call {i+1}: {result}")
        if i == 2:  # Show stats after last call
            stats = obj3.get_stats()
            print(f"Stats: {stats}")
    
    # Test with custom message
    print("\n4. Implementation with Custom Message:")
    obj4 = InfiniteMethodObjectWithCustomMessage("Custom Hello!")
    print(f"Call 1: {obj4.method()}")
    obj4.set_message("Updated Message!")
    print(f"Call 2: {obj4.method()}")
    
    # Test JavaScript-style implementation
    print("\n5. JavaScript-style Implementation:")
    obj5 = createInfiniteObjectJS()
    for i in range(3):
        result = obj5['method']()
        print(f"Call {i+1}: {result} (Total: {obj5['get_call_count']()})")
    
    # Test generator-based implementation
    print("\n6. Generator-based Implementation:")
    obj6 = createInfiniteObjectGenerator()
    for i in range(3):
        result = obj6.method()
        print(f"Call {i+1}: {result}")
    
    # Performance comparison
    print("\n7. Performance Comparison:")
    test_objects = [
        ("Basic", createInfiniteObject()),
        ("With Counter", InfiniteMethodObjectWithCounter()),
        ("JavaScript-style", createInfiniteObjectJS()),
        ("Generator-based", createInfiniteObjectGenerator())
    ]
    
    num_calls = 100000
    print(f"Performance test with {num_calls:,} calls:")
    
    for name, obj in test_objects:
        try:
            if name == "JavaScript-style":
                # Special handling for dictionary-based object
                start_time = time.time()
                for _ in range(num_calls):
                    obj['method']()
                end_time = time.time()
                calls_per_sec = num_calls / (end_time - start_time)
            else:
                metrics = performance_test(obj, num_calls)
                calls_per_sec = metrics['calls_per_second']
            
            print(f"{name}: {calls_per_sec:,.0f} calls/second")
        except Exception as e:
            print(f"{name}: Error - {e}")
    
    # Thread safety test
    print("\n8. Thread Safety Test:")
    import threading
    import time
    
    thread_safe_obj = ThreadSafeInfiniteMethodObject()
    
    def worker(worker_id, num_calls):
        for _ in range(num_calls):
            result = thread_safe_obj.method()
            assert result == "Hello World"
    
    # Create multiple threads
    threads = []
    calls_per_thread = 1000
    num_threads = 5
    
    start_time = time.time()
    
    for i in range(num_threads):
        thread = threading.Thread(target=worker, args=(i, calls_per_thread))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    
    total_calls = thread_safe_obj.get_call_count()
    expected_calls = num_threads * calls_per_thread
    
    print(f"Expected calls: {expected_calls}")
    print(f"Actual calls: {total_calls}")
    print(f"Thread safety test: {'PASSED' if total_calls == expected_calls else 'FAILED'}")
    print(f"Total time: {end_time - start_time:.3f} seconds")

"""
Time and Space Complexity Analysis:

Basic Implementation:
Time Complexity: O(1) per method call
Space Complexity: O(1) constant memory usage

With Counter Implementation:
Time Complexity: O(1) per method call
Space Complexity: O(1) constant memory (counter is just an integer)

With Timestamp Implementation:
Time Complexity: O(1) per method call
Space Complexity: O(1) constant memory

Thread-Safe Implementation:
Time Complexity: O(1) per method call (lock acquisition is typically O(1))
Space Complexity: O(1) constant memory

Generator-Based Implementation:
Time Complexity: O(1) per method call
Space Complexity: O(1) constant memory (generator state is minimal)

Key Design Principles:
1. Constant memory usage regardless of call count
2. Consistent O(1) time complexity per call
3. Thread safety when needed
4. Extensibility for additional features
5. Simple, maintainable code

Real-World Applications:
- API endpoints that return constant responses
- Mock objects for testing
- Placeholder implementations during development
- Rate limiting and monitoring wrappers
- Caching layer interfaces

Performance Considerations:
- Method calls should be as fast as possible
- Memory usage should not grow with call count
- Thread safety adds minimal overhead when needed
- Generator approach is memory efficient but slightly slower

Design Patterns Used:
- Factory pattern (createInfiniteObject)
- Singleton-like behavior (constant response)
- Decorator pattern (enhanced versions)
- Closure pattern (JavaScript-style implementation)

Topic: Object-Oriented Design, Factory Pattern, Performance Optimization, Thread Safety
"""
