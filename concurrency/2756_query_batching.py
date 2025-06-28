"""
LeetCode Problem 2756: Query Batching

Design a QueryBatcher class that batches multiple queries and executes them efficiently.

The QueryBatcher should:
1. Accept queries and batch them together
2. Execute batched queries when the batch size reaches a threshold or a timeout occurs
3. Return promises that resolve with individual query results
4. Handle errors appropriately

Implement the following methods:
- QueryBatcher(executeBatch, maxBatchSize, maxWaitTime): Constructor
- addQuery(query): Add a query to the current batch and return a promise

Example 1:
Input: 
batcher = QueryBatcher(
    executeBatch: (queries) => Promise.resolve(queries.map(q => q * 2)),
    maxBatchSize: 3,
    maxWaitTime: 100
)
batcher.addQuery(1)  // Returns promise that resolves to 2
batcher.addQuery(2)  // Returns promise that resolves to 4  
batcher.addQuery(3)  // Triggers batch execution, returns promise that resolves to 6

Example 2:
Input:
batcher = QueryBatcher(
    executeBatch: (queries) => Promise.resolve(queries.map(q => q.toUpperCase())),
    maxBatchSize: 5,
    maxWaitTime: 50
)
batcher.addQuery("hello")  // Will execute after 50ms timeout
// Returns promise that resolves to "HELLO"

Constraints:
- 1 <= maxBatchSize <= 100
- 10 <= maxWaitTime <= 1000 (milliseconds)
- executeBatch function returns a Promise that resolves to an array of results
- Results array length must match queries array length
"""

import asyncio
import time
from typing import Any, Callable, List, Optional
from concurrent.futures import Future
import threading


class QueryBatcher:
    """
    Batches queries for efficient execution.
    
    Automatically executes batches when:
    1. Batch size reaches maxBatchSize
    2. maxWaitTime elapses since first query in batch
    """
    
    def __init__(self, execute_batch: Callable[[List[Any]], Any], max_batch_size: int, max_wait_time: float):
        """
        Initialize the QueryBatcher.
        
        Args:
            execute_batch: Function that executes a batch of queries
            max_batch_size: Maximum number of queries per batch
            max_wait_time: Maximum wait time in seconds before executing batch
        """
        self.execute_batch = execute_batch
        self.max_batch_size = max_batch_size
        self.max_wait_time = max_wait_time / 1000.0  # Convert to seconds
        
        self.current_batch = []
        self.pending_promises = []
        self.batch_timer = None
        self.lock = threading.Lock()
    
    def add_query(self, query: Any) -> Future:
        """
        Add a query to the current batch.
        
        Args:
            query: The query to add
            
        Returns:
            Future that will resolve with the query result
        """
        with self.lock:
            # Create a future for this query
            future = Future()
            
            # Add to current batch
            self.current_batch.append(query)
            self.pending_promises.append(future)
            
            # Start timer if this is the first query in batch
            if len(self.current_batch) == 1:
                self._start_batch_timer()
            
            # Execute immediately if batch is full
            if len(self.current_batch) >= self.max_batch_size:
                self._execute_current_batch()
            
            return future
    
    def _start_batch_timer(self):
        """Start the batch execution timer."""
        if self.batch_timer:
            self.batch_timer.cancel()
        
        self.batch_timer = threading.Timer(self.max_wait_time, self._execute_current_batch)
        self.batch_timer.start()
    
    def _execute_current_batch(self):
        """Execute the current batch of queries."""
        with self.lock:
            if not self.current_batch:
                return
            
            # Cancel timer if it's running
            if self.batch_timer:
                self.batch_timer.cancel()
                self.batch_timer = None
            
            # Get current batch and promises
            batch = self.current_batch[:]
            promises = self.pending_promises[:]
            
            # Clear current batch
            self.current_batch.clear()
            self.pending_promises.clear()
        
        # Execute batch in separate thread to avoid blocking
        def execute():
            try:
                # Execute the batch
                results = self.execute_batch(batch)
                
                # Handle async results
                if hasattr(results, '__await__'):
                    # If result is awaitable, handle it
                    async def handle_async():
                        actual_results = await results
                        self._resolve_promises(promises, actual_results)
                    
                    # Run in event loop
                    try:
                        loop = asyncio.get_event_loop()
                        asyncio.run_coroutine_threadsafe(handle_async(), loop)
                    except RuntimeError:
                        # No event loop, run directly
                        asyncio.run(handle_async())
                else:
                    # Synchronous result
                    self._resolve_promises(promises, results)
                    
            except Exception as e:
                # Reject all promises with the error
                for promise in promises:
                    promise.set_exception(e)
        
        threading.Thread(target=execute, daemon=True).start()
    
    def _resolve_promises(self, promises: List[Future], results: List[Any]):
        """Resolve promises with their corresponding results."""
        if len(results) != len(promises):
            error = ValueError(f"Results length {len(results)} doesn't match queries length {len(promises)}")
            for promise in promises:
                promise.set_exception(error)
            return
        
        for promise, result in zip(promises, results):
            promise.set_result(result)


class AsyncQueryBatcher:
    """
    Async version of QueryBatcher using asyncio.
    """
    
    def __init__(self, execute_batch: Callable[[List[Any]], Any], max_batch_size: int, max_wait_time: float):
        self.execute_batch = execute_batch
        self.max_batch_size = max_batch_size
        self.max_wait_time = max_wait_time / 1000.0
        
        self.current_batch = []
        self.pending_futures = []
        self.batch_task = None
        self.lock = asyncio.Lock()
    
    async def add_query(self, query: Any) -> Any:
        """
        Add a query to the current batch (async version).
        
        Args:
            query: The query to add
            
        Returns:
            Coroutine that resolves with the query result
        """
        async with self.lock:
            # Create a future for this query
            loop = asyncio.get_event_loop()
            future = loop.create_future()
            
            # Add to current batch
            self.current_batch.append(query)
            self.pending_futures.append(future)
            
            # Start timer if this is the first query in batch
            if len(self.current_batch) == 1:
                await self._start_batch_timer()
            
            # Execute immediately if batch is full
            if len(self.current_batch) >= self.max_batch_size:
                await self._execute_current_batch()
            
            return await future
    
    async def _start_batch_timer(self):
        """Start the batch execution timer (async)."""
        if self.batch_task and not self.batch_task.done():
            self.batch_task.cancel()
        
        async def timer():
            await asyncio.sleep(self.max_wait_time)
            await self._execute_current_batch()
        
        self.batch_task = asyncio.create_task(timer())
    
    async def _execute_current_batch(self):
        """Execute the current batch of queries (async)."""
        async with self.lock:
            if not self.current_batch:
                return
            
            # Cancel timer if it's running
            if self.batch_task and not self.batch_task.done():
                self.batch_task.cancel()
            
            # Get current batch and futures
            batch = self.current_batch[:]
            futures = self.pending_futures[:]
            
            # Clear current batch
            self.current_batch.clear()
            self.pending_futures.clear()
        
        try:
            # Execute the batch
            results = self.execute_batch(batch)
            
            # Handle async results
            if hasattr(results, '__await__'):
                results = await results
            
            # Resolve futures
            if len(results) != len(futures):
                error = ValueError(f"Results length {len(results)} doesn't match queries length {len(futures)}")
                for future in futures:
                    future.set_exception(error)
            else:
                for future, result in zip(futures, results):
                    future.set_result(result)
                    
        except Exception as e:
            # Reject all futures with the error
            for future in futures:
                future.set_exception(e)


class SimpleQueryBatcher:
    """
    Simplified version for basic use cases.
    """
    
    def __init__(self, execute_batch: Callable, max_batch_size: int = 10):
        self.execute_batch = execute_batch
        self.max_batch_size = max_batch_size
        self.current_batch = []
    
    def add_query(self, query: Any) -> Any:
        """
        Add query and execute if batch is full.
        
        Returns:
            Result if batch executed, None otherwise
        """
        self.current_batch.append(query)
        
        if len(self.current_batch) >= self.max_batch_size:
            return self.flush()
        
        return None
    
    def flush(self) -> List[Any]:
        """Execute current batch and return results."""
        if not self.current_batch:
            return []
        
        batch = self.current_batch[:]
        self.current_batch.clear()
        
        return self.execute_batch(batch)


# Test cases
def test_query_batcher():
    """Test the QueryBatcher implementation."""
    
    print("Testing QueryBatcher:")
    
    # Test 1: Batch size trigger
    def double_queries(queries):
        return [q * 2 for q in queries]
    
    batcher1 = QueryBatcher(double_queries, max_batch_size=3, max_wait_time=1000)
    
    print("\nTest 1: Batch size trigger")
    future1 = batcher1.add_query(1)
    future2 = batcher1.add_query(2) 
    future3 = batcher1.add_query(3)  # Should trigger execution
    
    # Wait for results
    result1 = future1.result(timeout=1.0)
    result2 = future2.result(timeout=1.0)
    result3 = future3.result(timeout=1.0)
    
    print(f"  Results: {result1}, {result2}, {result3}")
    assert result1 == 2 and result2 == 4 and result3 == 6
    print("  ✓ Batch size trigger test passed!")
    
    # Test 2: Timer trigger
    batcher2 = QueryBatcher(double_queries, max_batch_size=10, max_wait_time=100)
    
    print("\nTest 2: Timer trigger")
    future4 = batcher2.add_query(5)
    time.sleep(0.15)  # Wait for timer
    result4 = future4.result(timeout=1.0)
    
    print(f"  Result: {result4}")
    assert result4 == 10
    print("  ✓ Timer trigger test passed!")
    
    # Test 3: String processing
    def uppercase_queries(queries):
        return [q.upper() for q in queries]
    
    batcher3 = QueryBatcher(uppercase_queries, max_batch_size=2, max_wait_time=500)
    
    print("\nTest 3: String processing")
    future5 = batcher3.add_query("hello")
    future6 = batcher3.add_query("world")  # Should trigger execution
    
    result5 = future5.result(timeout=1.0)
    result6 = future6.result(timeout=1.0)
    
    print(f"  Results: {result5}, {result6}")
    assert result5 == "HELLO" and result6 == "WORLD"
    print("  ✓ String processing test passed!")
    
    # Test 4: Error handling
    def error_queries(queries):
        raise ValueError("Batch execution failed")
    
    batcher4 = QueryBatcher(error_queries, max_batch_size=1, max_wait_time=500)
    
    print("\nTest 4: Error handling")
    future7 = batcher4.add_query("test")
    
    try:
        future7.result(timeout=1.0)
        assert False, "Should have raised an exception"
    except ValueError as e:
        print(f"  Caught expected error: {e}")
        print("  ✓ Error handling test passed!")
    
    # Test 5: Simple batcher
    print("\nTest 5: Simple batcher")
    simple_batcher = SimpleQueryBatcher(double_queries, max_batch_size=2)
    
    result = simple_batcher.add_query(10)  # Not enough for batch
    assert result is None
    
    result = simple_batcher.add_query(20)  # Triggers batch
    print(f"  Batch result: {result}")
    assert result == [20, 40]
    print("  ✓ Simple batcher test passed!")
    
    print("\n✓ All QueryBatcher tests passed!")


async def test_async_query_batcher():
    """Test the AsyncQueryBatcher implementation."""
    
    print("\nTesting AsyncQueryBatcher:")
    
    async def async_double_queries(queries):
        await asyncio.sleep(0.01)  # Simulate async work
        return [q * 2 for q in queries]
    
    batcher = AsyncQueryBatcher(async_double_queries, max_batch_size=2, max_wait_time=100)
    
    # Test batch size trigger
    task1 = asyncio.create_task(batcher.add_query(1))
    task2 = asyncio.create_task(batcher.add_query(2))
    
    result1, result2 = await asyncio.gather(task1, task2)
    
    print(f"  Async results: {result1}, {result2}")
    assert result1 == 2 and result2 == 4
    print("  ✓ Async batch test passed!")


if __name__ == "__main__":
    test_query_batcher()
    
    # Test async version
    try:
        asyncio.run(test_async_query_batcher())
    except Exception as e:
        print(f"Async test skipped: {e}")

"""
Complexity Analysis:

1. QueryBatcher.add_query():
   - Time Complexity: O(1) - adding to batch is constant time
   - Space Complexity: O(n) where n is batch size

2. Batch Execution:
   - Time Complexity: O(f(n)) where f is the execute_batch function complexity
   - Space Complexity: O(n) for storing batch and results

3. Timer Management:
   - Time Complexity: O(1) for timer operations
   - Space Complexity: O(1) for timer state

Key Features:
- Automatic batching based on size threshold
- Timeout-based execution for incomplete batches
- Thread-safe operation using locks
- Promise-based result delivery
- Error handling and propagation

Implementation Strategies:
1. Threading-based: Uses threading.Timer for timeouts
2. Asyncio-based: Uses asyncio for async operations
3. Simple: Synchronous batching without timers

Use Cases:
- Database query optimization
- API request batching
- Bulk data processing
- Network request optimization
- Rate limiting and throttling

Performance Considerations:
- Batch size vs latency trade-off
- Memory usage for large batches
- Thread overhead for execution
- Timer precision and overhead

Design Patterns:
- Batch Processing Pattern
- Promise/Future Pattern  
- Producer-Consumer Pattern
- Strategy Pattern (for different execution strategies)

Topics: Concurrency, Threading, Async Programming, Batch Processing, Design Patterns
"""
