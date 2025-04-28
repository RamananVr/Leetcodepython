"""
LeetCode Problem #2671: Frequency Tracker

Problem Statement:
Design a data structure that keeps track of the frequency of elements in an array. The data structure should support the following operations:

1. `add(number)`: Add `number` to the data structure.
2. `deleteOne(number)`: Delete one occurrence of `number` from the data structure. If `number` does not exist in the data structure, do nothing.
3. `hasFrequency(frequency)`: Check if there is any number in the data structure that occurs exactly `frequency` times. Return `True` if such a number exists, otherwise return `False`.

Implement the `FrequencyTracker` class:
- `FrequencyTracker()`: Initializes the FrequencyTracker object.
- `add(number)`: Adds `number` to the data structure.
- `deleteOne(number)`: Deletes one occurrence of `number` from the data structure.
- `hasFrequency(frequency)`: Returns `True` if there is a number with the exact frequency `frequency`, otherwise returns `False`.

Constraints:
- `1 <= number <= 10^5`
- `1 <= frequency <= 10^5`
- At most `2 * 10^5` calls will be made to `add`, `deleteOne`, and `hasFrequency`.

"""

class FrequencyTracker:
    def __init__(self):
        # Dictionary to store the frequency of each number
        self.num_freq = {}
        # Dictionary to store the count of frequencies
        self.freq_count = {}

    def add(self, number: int) -> None:
        # Get the current frequency of the number
        current_freq = self.num_freq.get(number, 0)
        
        # Update the frequency count for the current frequency
        if current_freq > 0:
            self.freq_count[current_freq] -= 1
            if self.freq_count[current_freq] == 0:
                del self.freq_count[current_freq]
        
        # Increment the frequency of the number
        new_freq = current_freq + 1
        self.num_freq[number] = new_freq
        
        # Update the frequency count for the new frequency
        if new_freq in self.freq_count:
            self.freq_count[new_freq] += 1
        else:
            self.freq_count[new_freq] = 1

    def deleteOne(self, number: int) -> None:
        # Check if the number exists in the data structure
        if number not in self.num_freq or self.num_freq[number] == 0:
            return
        
        # Get the current frequency of the number
        current_freq = self.num_freq[number]
        
        # Update the frequency count for the current frequency
        self.freq_count[current_freq] -= 1
        if self.freq_count[current_freq] == 0:
            del self.freq_count[current_freq]
        
        # Decrement the frequency of the number
        new_freq = current_freq - 1
        if new_freq == 0:
            del self.num_freq[number]
        else:
            self.num_freq[number] = new_freq
        
        # Update the frequency count for the new frequency
        if new_freq > 0:
            if new_freq in self.freq_count:
                self.freq_count[new_freq] += 1
            else:
                self.freq_count[new_freq] = 1

    def hasFrequency(self, frequency: int) -> bool:
        # Check if the frequency exists in the frequency count dictionary
        return frequency in self.freq_count and self.freq_count[frequency] > 0


# Example Test Cases
if __name__ == "__main__":
    # Initialize the FrequencyTracker object
    tracker = FrequencyTracker()

    # Test Case 1: Add numbers and check frequencies
    tracker.add(1)
    tracker.add(1)
    tracker.add(2)
    assert tracker.hasFrequency(2) == True  # 1 appears twice
    assert tracker.hasFrequency(1) == True  # 2 appears once
    assert tracker.hasFrequency(3) == False  # No number appears 3 times

    # Test Case 2: Delete numbers and check frequencies
    tracker.deleteOne(1)
    assert tracker.hasFrequency(2) == False  # 1 no longer appears twice
    assert tracker.hasFrequency(1) == True  # 1 and 2 both appear once

    # Test Case 3: Delete a number that doesn't exist
    tracker.deleteOne(3)  # No effect
    assert tracker.hasFrequency(1) == True

    # Test Case 4: Add and delete to create specific frequencies
    tracker.add(2)
    tracker.add(2)
    assert tracker.hasFrequency(3) == True  # 2 appears three times
    tracker.deleteOne(2)
    assert tracker.hasFrequency(3) == False  # 2 no longer appears three times

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. `add(number)`:
   - Time Complexity: O(1), as dictionary operations (get, set, increment) are O(1).
   - Space Complexity: O(1) additional space per call.

2. `deleteOne(number)`:
   - Time Complexity: O(1), as dictionary operations (get, set, decrement) are O(1).
   - Space Complexity: O(1) additional space per call.

3. `hasFrequency(frequency)`:
   - Time Complexity: O(1), as it checks for the existence of a key in a dictionary.
   - Space Complexity: O(1) additional space per call.

Overall:
- Time Complexity: O(1) per operation.
- Space Complexity: O(n), where n is the number of unique numbers in the data structure.

Topic: Hash Table
"""