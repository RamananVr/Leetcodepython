"""
LeetCode Problem #1146: Snapshot Array

Problem Statement:
Implement a SnapshotArray that supports the following interface:
- SnapshotArray(int length): Initializes an array-like data structure with the given length. Initially, each element equals 0.
- void set(index, val): Sets the element at the given index to be equal to val.
- int snap(): Takes a snapshot of the array and returns the snap_id: the total number of times snap() has been called minus 1.
- int get(index, snap_id): Returns the value at the given index, at the time we took the snapshot with the given snap_id.

Constraints:
- 1 <= length <= 5 * 10^4
- 0 <= index < length
- 0 <= val <= 10^9
- 0 <= snap_id < (the total number of times snap() has been called)
- At most 5 * 10^4 calls will be made to set, snap, and get.

"""

class SnapshotArray:
    def __init__(self, length: int):
        """
        Initialize the SnapshotArray with the given length.
        Each index will store a list of (snap_id, value) pairs.
        """
        self.snap_id = 0
        self.data = [{} for _ in range(length)]  # Dictionary to store snap_id -> value for each index

    def set(self, index: int, val: int) -> None:
        """
        Set the value at the given index to val.
        """
        self.data[index][self.snap_id] = val

    def snap(self) -> int:
        """
        Take a snapshot and return the snap_id.
        """
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        """
        Get the value at the given index for the specified snap_id.
        """
        if snap_id not in self.data[index]:
            return 0