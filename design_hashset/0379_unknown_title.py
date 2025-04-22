"""
LeetCode Problem #379: Design Phone Directory

Problem Statement:
Design a phone directory that provides the following functionalities:
1. get(): Provide a number which is not assigned to anyone. Return -1 if no number is available.
2. check(number): Check if a number is available or not.
3. release(number): Recycle or release a number.

Implement the PhoneDirectory class:
- PhoneDirectory(int maxNumbers): Initializes the phone directory with the maximum number of numbers that can be stored in the directory.
- int get(): Provides a number that is not assigned to anyone. Returns -1 if no number is available.
- bool check(int number): Returns true if the number is available and false if it is already assigned.
- void release(int number): Recycles or releases the number.

Constraints:
- 1 <= maxNumbers <= 10^4
- 0 <= number < maxNumbers
- At most 2 * 10^4 calls will be made to get, check, and release.
"""

class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        """
        Initialize the phone directory with the maximum number of numbers.
        """
        self.available = set(range(maxNumbers))  # Set of available numbers
        self.assigned = set()  # Set of assigned numbers

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        Returns -1 if no number is available.
        """
        if not self.available:
            return -1
        number = self.available.pop()
        self.assigned.add(number)
        return number

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        Returns True if the number is available, False otherwise.
        """
        return number in self.available

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number in self.assigned:
            self.assigned.remove(number)
            self.available.add(number)


# Example Test Cases
if __name__ == "__main__":
    # Initialize the phone directory with a maximum of 3 numbers: 0, 1, and 2.
    directory = PhoneDirectory(3)

    # Test Case 1: Get a number
    print(directory.get())  # Output: 0 (or any available number)

    # Test Case 2: Get another number
    print(directory.get())  # Output: 1 (or any available number)

    # Test Case 3: Check if a number is available
    print(directory.check(2))  # Output: True (2 is available)

    # Test Case 4: Get another number
    print(directory.get())  # Output: 2 (or any available number)

    # Test Case 5: Check if a number is available
    print(directory.check(2))  # Output: False (2 is now assigned)

    # Test Case 6: Release a number
    directory.release(2)

    # Test Case 7: Check if the released number is available
    print(directory.check(2))  # Output: True (2 is now available again)

    # Test Case 8: Get a number after releasing
    print(directory.get())  # Output: 2 (or any available number)


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - get(): O(1) on average, as set operations (pop and add) are O(1).
   - check(): O(1), as checking membership in a set is O(1).
   - release(): O(1), as adding/removing from a set is O(1).

2. Space Complexity:
   - O(maxNumbers), as we store up to maxNumbers in the `available` and `assigned` sets.

Topic: Design, HashSet
"""