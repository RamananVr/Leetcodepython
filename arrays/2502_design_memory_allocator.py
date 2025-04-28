"""
LeetCode Question #2502: Design Memory Allocator

Problem Statement:
You are tasked with designing a memory allocator that can allocate and free memory blocks. The memory allocator should support the following operations:

1. `allocate(size: int, mID: int) -> int`: Allocates a contiguous block of memory of size `size` and associates it with the memory ID `mID`. Returns the starting index of the allocated block if successful, or -1 if it cannot allocate the block.

2. `free(mID: int) -> int`: Frees all memory blocks associated with the memory ID `mID`. Returns the total size of the freed memory.

The memory allocator operates on a memory array of fixed size `n`, initialized with all elements set to 0 (representing free memory). Memory blocks are allocated contiguously, and the allocator should find the first available block that fits the requested size.

Constraints:
- `1 <= n <= 1000`
- `1 <= size <= n`
- `1 <= mID <= 1000`
- At most `1000` calls will be made to `allocate` and `free`.

"""

class MemoryAllocator:
    def __init__(self, n: int):
        """
        Initializes the memory allocator with a memory array of size n.
        """
        self.memory = [0] * n  # Memory array initialized to 0 (free memory)
        self.n = n  # Size of the memory array

    def allocate(self, size: int, mID: int) -> int:
        """
        Allocates a contiguous block of memory of the given size and associates it with mID.
        Returns the starting index of the allocated block if successful, or -1 if allocation fails.
        """
        for i in range(self.n - size + 1):  # Check all possible starting indices
            if all(self.memory[j] == 0 for j in range(i, i + size)):  # Check if block is free
                for j in range(i, i + size):  # Allocate the block
                    self.memory[j] = mID
                return i  # Return the starting index
        return -1  # Allocation failed

    def free(self, mID: int) -> int:
        """
        Frees all memory blocks associated with the given mID.
        Returns the total size of the freed memory.
        """
        freed_size = 0
        for i in range(self.n):
            if self.memory[i] == mID:  # Free the block
                self.memory[i] = 0
                freed_size += 1
        return freed_size


# Example Test Cases
if __name__ == "__main__":
    # Initialize memory allocator with size 10
    allocator = MemoryAllocator(10)

    # Test allocate
    print(allocator.allocate(3, 1))  # Expected: 0 (allocates memory at index 0)
    print(allocator.allocate(2, 2))  # Expected: 3 (allocates memory at index 3)
    print(allocator.allocate(5, 3))  # Expected: -1 (not enough contiguous space)

    # Test free
    print(allocator.free(1))  # Expected: 3 (frees memory associated with mID 1)
    print(allocator.allocate(5, 3))  # Expected: 0 (allocates memory at index 0 after freeing mID 1)
    print(allocator.free(2))  # Expected: 2 (frees memory associated with mID 2)

# Time and Space Complexity Analysis
# Time Complexity:
# - `allocate`: O(n * size), where `n` is the size of the memory array and `size` is the requested block size.
#   This is because we iterate over the memory array and check for a contiguous free block.
# - `free`: O(n), where `n` is the size of the memory array. We iterate over the memory array to free blocks.

# Space Complexity:
# - The space complexity is O(n), where `n` is the size of the memory array. This is the space required to store the memory array.

# Topic: Arrays