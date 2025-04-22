"""
LeetCode Question #251: Flatten 2D Vector

Problem Statement:
Design and implement an iterator to flatten a 2D vector. It should support the `next` and `hasNext` operations.

Implement the `Vector2D` class:
- `Vector2D(vector: List[List[int]])` initializes the object with the 2D vector `vector`.
- `next() -> int` returns the next element in the flattened 2D vector and moves the pointer forward.
- `hasNext() -> bool` returns `true` if there are still elements in the flattened vector, and `false` otherwise.

Constraints:
- `0 <= vector.length <= 10^5`
- `0 <= vector[i].length <= 500`
- `-10^5 <= vector[i][j] <= 10^5`

Example:
Input:
vector = [[1,2],[3],[4,5,6]]
Vector2D iterator = new Vector2D(vector);
iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return true
iterator.next(); // return 5
iterator.hasNext(); // return true
iterator.next(); // return 6
iterator.hasNext(); // return false
"""

# Python Solution
class Vector2D:
    def __init__(self, vector: list[list[int]]):
        self.vector = vector
        self.outer = 0  # Pointer to the outer list
        self.inner = 0  # Pointer to the inner list

    def next(self) -> int:
        if not self.hasNext():
            raise Exception("No more elements")
        result = self.vector[self.outer][self.inner]
        self.inner += 1
        return result

    def hasNext(self) -> bool:
        while self.outer < len(self.vector):
            if self.inner < len(self.vector[self.outer]):
                return True
            self.outer += 1
            self.inner = 0
        return False


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    vector = [[1, 2], [3], [4, 5, 6]]
    iterator = Vector2D(vector)
    assert iterator.next() == 1
    assert iterator.next() == 2
    assert iterator.next() == 3
    assert iterator.hasNext() == True
    assert iterator.next() == 4
    assert iterator.hasNext() == True
    assert iterator.next() == 5
    assert iterator.hasNext() == True
    assert iterator.next() == 6
    assert iterator.hasNext() == False

    # Test Case 2
    vector = [[], [1], [], [2, 3]]
    iterator = Vector2D(vector)
    assert iterator.next() == 1
    assert iterator.hasNext() == True
    assert iterator.next() == 2
    assert iterator.hasNext() == True
    assert iterator.next() == 3
    assert iterator.hasNext() == False

    # Test Case 3
    vector = [[]]
    iterator = Vector2D(vector)
    assert iterator.hasNext() == False

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

Time Complexity:
- `next()`: O(1) amortized. In the worst case, we may need to skip empty inner lists, but this is handled efficiently.
- `hasNext()`: O(1) amortized. It skips empty inner lists in constant time.

Space Complexity:
- O(1): The solution uses constant extra space for pointers (`outer` and `inner`).

Topic: Iterators
"""