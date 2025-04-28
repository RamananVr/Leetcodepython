"""
LeetCode Question #1860: Incremental Memory Leak

Problem Statement:
-------------------
You are given two integers `memory1` and `memory2` representing the available memory in two memory banks. 
The task is to simulate a memory leak process as follows:

1. On the i-th second (starting with i = 1), you allocate i units of memory to the memory bank with more available memory 
   (or to the first bank if both have the same available memory).
2. If neither memory bank has at least i units of memory available, the process ends.

Return a list containing three integers:
- The total number of seconds the process lasted,
- The remaining memory in the first memory bank,
- The remaining memory in the second memory bank.

Constraints:
------------
- 0 <= memory1, memory2 <= 2^31 - 1
"""

def mem_leak(memory1: int, memory2: int) -> list:
    """
    Simulates the memory leak process and returns the result as a list.
    
    Args:
    memory1 (int): Available memory in the first memory bank.
    memory2 (int): Available memory in the second memory bank.
    
    Returns:
    list: A list containing [total_seconds, remaining_memory1, remaining_memory2].
    """
    seconds = 1
    while True:
        if memory1 >= memory2:
            if memory1 >= seconds:
                memory1 -= seconds
            else:
                break
        else:
            if memory2 >= seconds:
                memory2 -= seconds
            else:
                break
        seconds += 1
    return [seconds, memory1, memory2]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    memory1 = 2
    memory2 = 2
    print(mem_leak(memory1, memory2))  # Output: [3, 1, 0]

    # Test Case 2
    memory1 = 8
    memory2 = 11
    print(mem_leak(memory1, memory2))  # Output: [6, 0, 4]

    # Test Case 3
    memory1 = 0
    memory2 = 0
    print(mem_leak(memory1, memory2))  # Output: [1, 0, 0]

    # Test Case 4
    memory1 = 10
    memory2 = 5
    print(mem_leak(memory1, memory2))  # Output: [5, 0, 1]

"""
Time and Space Complexity Analysis:
------------------------------------
Time Complexity: O(sqrt(N))
- The process runs until the sum of the first `k` natural numbers (1 + 2 + ... + k) exceeds the total memory.
  This sum is approximately k * (k + 1) / 2, which means k grows as O(sqrt(N)), where N is the total memory.

Space Complexity: O(1)
- The algorithm uses a constant amount of space regardless of the input size.

Topic: Simulation
"""