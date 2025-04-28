"""
LeetCode Problem #1622: Fancy Sequence

Problem Statement:
Design an object that supports the following operations:
1. `append(val)`: Appends an integer `val` to the sequence.
2. `addAll(inc)`: Increments all existing values in the sequence by an integer `inc`.
3. `multAll(m)`: Multiplies all existing values in the sequence by an integer `m`.
4. `getIndex(idx)`: Gets the current value at index `idx` (0-indexed) of the sequence modulo 10^9 + 7. 
   If the index is greater or equal to the length of the sequence, return -1.

Implement the `Fancy` class:
- `Fancy()` Initializes the object with an empty sequence.
- `void append(int val)` Appends an integer `val` to the sequence.
- `void addAll(int inc)` Increments all existing values in the sequence by an integer `inc`.
- `void multAll(int m)` Multiplies all existing values in the sequence by an integer `m`.
- `int getIndex(int idx)` Returns the current value at index `idx` modulo 10^9 + 7, or -1 if the index is invalid.

Constraints:
- 1 <= val, inc, m <= 100
- 0 <= idx < 10^5
- At most 10^5 calls will be made to `append`, `addAll`, `multAll`, and `getIndex`.

"""

# Python Solution
class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.sequence = []
        self.add = 0
        self.mult = 1

    def append(self, val: int) -> None:
        # Reverse the effect of the current add and mult operations
        adjusted_val = (val - self.add) * pow(self.mult, -1, self.MOD) % self.MOD
        self.sequence.append(adjusted_val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.add = (self.add * m) % self.MOD
        self.mult = (self.mult * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.sequence):
            return -1
        # Apply the current add and mult operations to the stored value
        return (self.sequence[idx] * self.mult + self.add) % self.MOD


# Example Test Cases
if __name__ == "__main__":
    fancy = Fancy()
    fancy.append(2)  # Sequence: [2]
    fancy.addAll(3)  # Sequence: [5]
    fancy.append(7)  # Sequence: [5, 7]
    fancy.multAll(2) # Sequence: [10, 14]
    print(fancy.getIndex(0))  # Output: 10
    fancy.addAll(3)  # Sequence: [13, 17]
    fancy.append(10) # Sequence: [13, 17, 10]
    fancy.multAll(2) # Sequence: [26, 34, 20]
    print(fancy.getIndex(0))  # Output: 26
    print(fancy.getIndex(1))  # Output: 34
    print(fancy.getIndex(2))  # Output: 20
    print(fancy.getIndex(3))  # Output: -1 (index out of bounds)

"""
Time and Space Complexity Analysis:

1. `append(val)`:
   - Time Complexity: O(1), as we are simply appending a value to the list.
   - Space Complexity: O(1), no additional space is used apart from the input.

2. `addAll(inc)`:
   - Time Complexity: O(1), as we are just updating the `add` variable.
   - Space Complexity: O(1), no additional space is used.

3. `multAll(m)`:
   - Time Complexity: O(1), as we are just updating the `add` and `mult` variables.
   - Space Complexity: O(1), no additional space is used.

4. `getIndex(idx)`:
   - Time Complexity: O(1), as we are performing a constant number of operations to compute the result.
   - Space Complexity: O(1), no additional space is used.

Overall:
- Time Complexity (per operation): O(1)
- Space Complexity: O(n), where `n` is the number of elements in the sequence.

Topic: Math, Modular Arithmetic, Design
"""