"""
LeetCode Problem #2166: Design Bitset

Problem Statement:
A Bitset is a data structure that can store a binary string of size `size`. 
You can set the value of each bit to either 0 or 1.

Implement the Bitset class:
- `Bitset(int size)` Initializes the Bitset with size bits, all of which are 0.
- `void fix(int idx)` Sets the bit at index `idx` to 1. If the bit is already 1, it does nothing.
- `void unfix(int idx)` Sets the bit at index `idx` to 0. If the bit is already 0, it does nothing.
- `void flip()` Flips the values of each bit in the Bitset (i.e., all 0s become 1s, and all 1s become 0s).
- `boolean all()` Checks if the value of each bit in the Bitset is 1. Returns true if it satisfies the condition, false otherwise.
- `boolean one()` Checks if there is at least one bit in the Bitset with value 1. Returns true if it satisfies the condition, false otherwise.
- `int count()` Returns the total number of bits in the Bitset that have the value 1.
- `String toString()` Returns the current composition of the Bitset as a binary string.

Constraints:
- 1 <= size <= 10^5
- 0 <= idx < size
- At most 10^5 calls will be made to fix, unfix, flip, all, one, count, and toString.

"""

class Bitset:
    def __init__(self, size: int):
        self.size = size
        self.bits = [0] * size  # Initialize all bits to 0
        self.flipped = False   # Track whether the bits are flipped
        self.count_ones = 0    # Track the number of 1s in the Bitset

    def fix(self, idx: int) -> None:
        if not self.flipped and self.bits[idx] == 0:
            self.bits[idx] = 1
            self.count_ones += 1
        elif self.flipped and self.bits[idx] == 1:
            self.bits[idx] = 0
            self.count_ones += 1

    def unfix(self, idx: int) -> None:
        if not self.flipped and self.bits[idx] == 1:
            self.bits[idx] = 0
            self.count_ones -= 1
        elif self.flipped and self.bits[idx] == 0:
            self.bits[idx] = 1
            self.count_ones -= 1

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.count_ones = self.size - self.count_ones

    def all(self) -> bool:
        return self.count_ones == self.size

    def one(self) -> bool:
        return self.count_ones > 0

    def count(self) -> int:
        return self.count_ones

    def toString(self) -> str:
        if not self.flipped:
            return ''.join(str(bit) for bit in self.bits)
        else:
            return ''.join(str(1 - bit) for bit in self.bits)


# Example Test Cases
if __name__ == "__main__":
    # Initialize a Bitset of size 5
    bitset = Bitset(5)
    
    # Test fix
    bitset.fix(3)
    print(bitset.toString())  # Output: "00010"
    
    # Test unfix
    bitset.unfix(3)
    print(bitset.toString())  # Output: "00000"
    
    # Test flip
    bitset.flip()
    print(bitset.toString())  # Output: "11111"
    
    # Test all
    print(bitset.all())  # Output: True
    
    # Test one
    print(bitset.one())  # Output: True
    
    # Test count
    print(bitset.count())  # Output: 5
    
    # Test toString
    print(bitset.toString())  # Output: "11111"

"""
Time Complexity Analysis:
- `fix` and `unfix`: O(1) for each operation since we directly access the bit at the given index.
- `flip`: O(1) since we only toggle the `flipped` flag and update the count of 1s.
- `all` and `one`: O(1) since they only check the count of 1s.
- `count`: O(1) since it directly returns the count of 1s.
- `toString`: O(size) since it constructs the binary string representation of the Bitset.

Space Complexity:
- O(size) for storing the bits array.

Topic: Design, Bit Manipulation
"""