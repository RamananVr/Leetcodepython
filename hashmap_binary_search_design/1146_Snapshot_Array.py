"""
LeetCode Problem #1146: Snapshot Array

Problem Statement:
Implement a SnapshotArray that supports the following interface:
- SnapshotArray(int length): Initializes an array-like data structure with the given length. Initially, each element equals 0.
- void set(index, val): Sets the element at the given index to be equal to val.
- int snap(): Takes a snapshot of the array and returns the snap_id: the total number of times snap() has been called minus 1.
- int get(index, snap_id): Returns the value at the given index at the time we took the snapshot with the given snap_id.

Constraints:
- 1 <= length <= 5 * 10^4
- 0 <= index < length
- 0 <= snap_id < (the total number of times snap() has been called)
- 0 <= val <= 10^9
- At most 5 * 10^4 calls will be made to set, snap, and get.

"""

class SnapshotArray:
    def __init__(self, length: int):
        """
        Initialize the SnapshotArray with the given length.
        Each index will store a list of tuples (snap_id, value) to track changes efficiently.
        """
        self.snap_id = 0
        self.data = [{} for _ in range(length)]  # Each index stores a dictionary {snap_id: value}

    def set(self, index: int, val: int) -> None:
        """
        Set the value at the given index to val for the current snap_id.
        """
        self.data[index][self.snap_id] = val

    def snap(self) -> int:
        """
        Take a snapshot and return the current snap_id.
        """
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        """
        Get the value at the given index for the specified snap_id.
        If the exact snap_id is not found, return the value from the most recent snap_id before it.
        """
        while snap_id not in self.data[index] and snap_id >= 0:
            snap_id -= 1
        return self.data[index].get(snap_id, 0)


# Example Test Cases
if __name__ == "__main__":
    # Initialize a SnapshotArray of length 3
    snapshot_array = SnapshotArray(3)

    # Set values and take snapshots
    snapshot_array.set(0, 5)  # Set index 0 to 5
    snap_id_1 = snapshot_array.snap()  # Take a snapshot, snap_id = 0
    snapshot_array.set(0, 6)  # Set index 0 to 6
    snap_id_2 = snapshot_array.snap()  # Take another snapshot, snap_id = 1

    # Get values from snapshots
    print(snapshot_array.get(0, snap_id_1))  # Output: 5 (value at index 0 in snap_id 0)
    print(snapshot_array.get(0, snap_id_2))  # Output: 6 (value at index 0 in snap_id 1)
    print(snapshot_array.get(1, snap_id_1))  # Output: 0 (index 1 was never set, so default is 0)


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - `set(index, val)`: O(1) on average, as we are simply updating a dictionary for the given index and snap_id.
   - `snap()`: O(1), as we are just incrementing the snap_id counter.
   - `get(index, snap_id)`: O(snap_id) in the worst case, as we may need to iterate backward to find the most recent snap_id with a value.

2. Space Complexity:
   - The space complexity is O(n + k), where n is the length of the array and k is the total number of `set` operations. Each `set` operation stores a value for a specific snap_id.

Topic: HashMap, Binary Search, Design
"""