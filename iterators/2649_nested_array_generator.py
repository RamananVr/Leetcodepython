"""
LeetCode Problem #2649: Nested Array Generator

Problem Statement:
Given a multi-dimensional array of integers, return a generator object which yields integers in the same order as inorder traversal.

A multi-dimensional array is a recursive data structure that contains integers or other multi-dimensional arrays.

Inorder traversal visits the nodes in the following order: left, root, right.

Example 1:
Input: arr = [[[6]],[1,3],2]
Output: [6, 1, 3, 2]
Explanation:
The generator should yield 6, then 1, then 3, then 2.

Example 2:
Input: arr = []
Output: []
Explanation: There are no integers so the generator doesn't yield anything.

Constraints:
- 0 <= arr.flat().length <= 10^5
- 0 <= arr.flat()[i] <= 10^9
- maxNestingDepth <= 10^5
"""

from typing import Generator, List, Union, Any

def inorderTraversal(arr: List[Union[int, List]]) -> Generator[int, None, None]:
    """
    Generator that yields integers from nested array in inorder traversal.
    
    Args:
        arr: Multi-dimensional array containing integers or nested arrays
        
    Yields:
        int: Next integer in inorder traversal
    """
    for item in arr:
        if isinstance(item, int):
            yield item
        elif isinstance(item, list):
            # Recursively yield from nested array
            yield from inorderTraversal(item)

def inorderTraversalIterative(arr: List[Union[int, List]]) -> Generator[int, None, None]:
    """
    Iterative implementation using stack to avoid deep recursion
    """
    stack = [arr]
    
    while stack:
        current = stack.pop()
        
        if isinstance(current, int):
            yield current
        elif isinstance(current, list):
            # Add items in reverse order to maintain left-to-right traversal
            for item in reversed(current):
                stack.append(item)

def inorderTraversalWithIndex(arr: List[Union[int, List]]) -> Generator[tuple, None, None]:
    """
    Enhanced version that yields both value and path indices
    """
    def traverse(current_arr: List, path: List[int] = None):
        if path is None:
            path = []
        
        for i, item in enumerate(current_arr):
            current_path = path + [i]
            if isinstance(item, int):
                yield (item, current_path)
            elif isinstance(item, list):
                yield from traverse(item, current_path)
    
    for item in traverse(arr):
        yield item

class NestedArrayIterator:
    """
    Class-based iterator for nested arrays
    """
    
    def __init__(self, arr: List[Union[int, List]]):
        self.stack = []
        self._flatten_to_stack(arr)
    
    def _flatten_to_stack(self, arr: List[Union[int, List]]):
        """Flatten array and add to stack in reverse order"""
        for item in reversed(arr):
            if isinstance(item, int):
                self.stack.append(item)
            elif isinstance(item, list):
                self._flatten_to_stack(item)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.stack:
            raise StopIteration
        return self.stack.pop()

def inorderTraversalDFS(arr: List[Union[int, List]]) -> Generator[int, None, None]:
    """
    DFS-based approach with explicit recursion control
    """
    def dfs(current):
        if isinstance(current, int):
            yield current
        elif isinstance(current, list):
            for element in current:
                yield from dfs(element)
    
    yield from dfs(arr)

def inorderTraversalFlattened(arr: List[Union[int, List]]) -> List[int]:
    """
    Non-generator version that returns flattened list for comparison
    """
    result = []
    
    def flatten(current_arr):
        for item in current_arr:
            if isinstance(item, int):
                result.append(item)
            elif isinstance(item, list):
                flatten(item)
    
    flatten(arr)
    return result

def inorderTraversalWithTypes(arr: List[Any]) -> Generator[tuple, None, None]:
    """
    Generator that yields both value and type information
    """
    for item in arr:
        if isinstance(item, int):
            yield (item, 'int')
        elif isinstance(item, list):
            yield ('start_array', 'control')
            yield from inorderTraversalWithTypes(item)
            yield ('end_array', 'control')
        else:
            yield (item, type(item).__name__)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic nested array
    print("Test Case 1: Basic nested array")
    arr1 = [[[6]],[1,3],2]
    gen1 = inorderTraversal(arr1)
    result1 = list(gen1)
    print(f"Input: {arr1}")
    print(f"Output: {result1}")  # Expected: [6, 1, 3, 2]
    
    # Test Case 2: Empty array
    print("\nTest Case 2: Empty array")
    arr2 = []
    gen2 = inorderTraversal(arr2)
    result2 = list(gen2)
    print(f"Input: {arr2}")
    print(f"Output: {result2}")  # Expected: []
    
    # Test Case 3: Single level array
    print("\nTest Case 3: Single level array")
    arr3 = [1, 2, 3, 4]
    gen3 = inorderTraversal(arr3)
    result3 = list(gen3)
    print(f"Input: {arr3}")
    print(f"Output: {result3}")  # Expected: [1, 2, 3, 4]
    
    # Test Case 4: Deep nesting
    print("\nTest Case 4: Deep nesting")
    arr4 = [1, [2, [3, [4, 5]], 6], 7]
    gen4 = inorderTraversal(arr4)
    result4 = list(gen4)
    print(f"Input: {arr4}")
    print(f"Output: {result4}")  # Expected: [1, 2, 3, 4, 5, 6, 7]
    
    # Test Case 5: Mixed nesting levels
    print("\nTest Case 5: Mixed nesting levels")
    arr5 = [[1, 2], 3, [4, [5, 6]], 7]
    gen5 = inorderTraversal(arr5)
    result5 = list(gen5)
    print(f"Input: {arr5}")
    print(f"Output: {result5}")  # Expected: [1, 2, 3, 4, 5, 6, 7]
    
    # Test Case 6: Iterative vs Recursive comparison
    print("\nTest Case 6: Iterative vs Recursive comparison")
    arr6 = [[[1, 2]], [3, [4]], 5]
    
    gen_recursive = inorderTraversal(arr6)
    result_recursive = list(gen_recursive)
    
    gen_iterative = inorderTraversalIterative(arr6)
    result_iterative = list(gen_iterative)
    
    print(f"Recursive result: {result_recursive}")
    print(f"Iterative result: {result_iterative}")
    print(f"Results match: {result_recursive == result_iterative}")
    
    # Test Case 7: Class-based iterator
    print("\nTest Case 7: Class-based iterator")
    arr7 = [[1, [2, 3]], 4, [5]]
    iterator = NestedArrayIterator(arr7)
    result7 = list(iterator)
    print(f"Input: {arr7}")
    print(f"Class-based result: {result7}")  # Expected: [1, 2, 3, 4, 5]
    
    # Test Case 8: Generator with indices
    print("\nTest Case 8: Generator with path indices")
    arr8 = [[1, 2], [3, [4]]]
    gen_with_indices = inorderTraversalWithIndex(arr8)
    result8 = list(gen_with_indices)
    print(f"Input: {arr8}")
    print(f"With indices: {result8}")
    
    # Test Case 9: Performance test with large array
    print("\nTest Case 9: Performance test")
    import time
    
    # Create large nested array
    large_arr = []
    for i in range(1000):
        if i % 10 == 0:
            large_arr.append([i, i+1])
        else:
            large_arr.append(i)
    
    start_time = time.time()
    gen_large = inorderTraversal(large_arr)
    result_large = list(gen_large)
    end_time = time.time()
    
    print(f"Processed {len(result_large)} elements in {end_time - start_time:.4f}s")

"""
Time and Space Complexity Analysis:

Time Complexity:
- inorderTraversal(): O(n) where n is total number of integers in nested array
- inorderTraversalIterative(): O(n) - each element processed once
- Each approach visits every element exactly once

Space Complexity:
- inorderTraversal(): O(d) where d is maximum nesting depth (recursion stack)
- inorderTraversalIterative(): O(n) in worst case for stack storage
- NestedArrayIterator: O(n) for storing flattened elements

The recursive approach is generally more memory-efficient for deeply nested structures,
while the iterative approach can handle very deep nesting without stack overflow.

Topic: Generator, Iterator, Nested Data Structures, Tree Traversal, Recursion
"""
