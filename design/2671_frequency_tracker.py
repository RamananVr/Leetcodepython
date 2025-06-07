"""
LeetCode Question #2671: Frequency Tracker

Problem Statement:
Design a data structure that keeps track of the values in it and answers some queries regarding their frequencies.

Implement the FrequencyTracker class:
- FrequencyTracker(): Initializes the FrequencyTracker object with an empty array initially.
- void add(int number): Adds number to the data structure.
- void deleteOne(int number): Deletes one occurrence of number from the data structure. The data structure may not contain number, and in this case nothing is deleted.
- bool hasFrequency(int frequency): Returns true if there is a number in the data structure that occurs frequency number of times, otherwise, it returns false.

Examples:
Example 1:
Input
["FrequencyTracker", "add", "add", "hasFrequency"]
[[], [3], [3], [2]]
Output
[null, null, null, true]
Explanation
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(3); // data structure becomes [3]
frequencyTracker.add(3); // data structure becomes [3, 3]
frequencyTracker.hasFrequency(2); // returns true, because 3 occurs 2 times

Example 2:
Input
["FrequencyTracker", "add", "deleteOne", "hasFrequency"]
[[], [1], [1], [1]]
Output
[null, null, null, false]
Explanation
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(1); // data structure becomes [1]
frequencyTracker.deleteOne(1); // data structure becomes []
frequencyTracker.hasFrequency(1); // returns false, because the data structure is empty

Constraints:
- 1 <= number <= 10^5
- 1 <= frequency <= 10^5
- At most 2 * 10^5 calls will be made to add, deleteOne, and hasFrequency in total.
"""

from collections import defaultdict

class FrequencyTracker:
    """
    A data structure that tracks frequencies of numbers efficiently.
    
    Uses two hash maps:
    1. num_count: tracks count of each number
    2. freq_count: tracks how many numbers have each frequency
    """
    
    def __init__(self):
        # Maps number -> its current count
        self.num_count = defaultdict(int)
        # Maps frequency -> how many numbers have this frequency
        self.freq_count = defaultdict(int)
    
    def add(self, number: int) -> None:
        """Add a number to the tracker."""
        old_freq = self.num_count[number]
        new_freq = old_freq + 1
        
        # Update number count
        self.num_count[number] = new_freq
        
        # Update frequency count
        if old_freq > 0:
            self.freq_count[old_freq] -= 1
            if self.freq_count[old_freq] == 0:
                del self.freq_count[old_freq]
        
        self.freq_count[new_freq] += 1
    
    def deleteOne(self, number: int) -> None:
        """Delete one occurrence of a number."""
        if number not in self.num_count or self.num_count[number] == 0:
            return
        
        old_freq = self.num_count[number]
        new_freq = old_freq - 1
        
        # Update frequency count
        self.freq_count[old_freq] -= 1
        if self.freq_count[old_freq] == 0:
            del self.freq_count[old_freq]
        
        if new_freq > 0:
            self.num_count[number] = new_freq
            self.freq_count[new_freq] += 1
        else:
            del self.num_count[number]
    
    def hasFrequency(self, frequency: int) -> bool:
        """Check if any number has the given frequency."""
        return frequency in self.freq_count and self.freq_count[frequency] > 0

class FrequencyTrackerSimple:
    """
    Simpler implementation that recalculates frequencies each time.
    Less efficient but easier to understand.
    """
    
    def __init__(self):
        self.numbers = defaultdict(int)
    
    def add(self, number: int) -> None:
        self.numbers[number] += 1
    
    def deleteOne(self, number: int) -> None:
        if number in self.numbers and self.numbers[number] > 0:
            self.numbers[number] -= 1
            if self.numbers[number] == 0:
                del self.numbers[number]
    
    def hasFrequency(self, frequency: int) -> bool:
        # Count how many numbers have the given frequency
        return frequency in self.numbers.values()

class FrequencyTrackerWithList:
    """
    Alternative implementation using a list to store numbers.
    Less efficient but matches the problem description more literally.
    """
    
    def __init__(self):
        self.numbers = []
    
    def add(self, number: int) -> None:
        self.numbers.append(number)
    
    def deleteOne(self, number: int) -> None:
        if number in self.numbers:
            self.numbers.remove(number)
    
    def hasFrequency(self, frequency: int) -> bool:
        from collections import Counter
        counter = Counter(self.numbers)
        return frequency in counter.values()

# Test Cases
if __name__ == "__main__":
    print("Testing FrequencyTracker:")
    
    # Test case 1
    ft = FrequencyTracker()
    ft.add(3)
    ft.add(3)
    result1 = ft.hasFrequency(2)
    print(f"Test 1: hasFrequency(2) after adding 3 twice = {result1}, expected = True, {'✓' if result1 else '✗'}")
    
    # Test case 2
    ft2 = FrequencyTracker()
    ft2.add(1)
    ft2.deleteOne(1)
    result2 = ft2.hasFrequency(1)
    print(f"Test 2: hasFrequency(1) after adding 1 and deleting 1 = {result2}, expected = False, {'✓' if not result2 else '✗'}")
    
    # Additional test cases
    print("\nAdditional test cases:")
    ft3 = FrequencyTracker()
    
    # Add multiple numbers with different frequencies
    ft3.add(1)  # 1 appears 1 time
    ft3.add(2)  # 2 appears 1 time
    ft3.add(2)  # 2 appears 2 times
    ft3.add(3)  # 3 appears 1 time
    ft3.add(3)  # 3 appears 2 times
    ft3.add(3)  # 3 appears 3 times
    
    print(f"hasFrequency(1): {ft3.hasFrequency(1)}, expected: True")  # 1 appears once
    print(f"hasFrequency(2): {ft3.hasFrequency(2)}, expected: True")  # 2 appears twice
    print(f"hasFrequency(3): {ft3.hasFrequency(3)}, expected: True")  # 3 appears thrice
    print(f"hasFrequency(4): {ft3.hasFrequency(4)}, expected: False")  # No number appears 4 times
    
    # Delete and check again
    ft3.deleteOne(3)  # 3 now appears 2 times
    print(f"After deleting one 3: hasFrequency(3): {ft3.hasFrequency(3)}, expected: False")
    print(f"After deleting one 3: hasFrequency(2): {ft3.hasFrequency(2)}, expected: True")  # Now 2 and 3 both appear twice
    
    print("\nTesting simple implementation:")
    ft_simple = FrequencyTrackerSimple()
    ft_simple.add(3)
    ft_simple.add(3)
    result_simple = ft_simple.hasFrequency(2)
    print(f"Simple implementation hasFrequency(2): {result_simple}, expected: True")

"""
Time and Space Complexity Analysis:

Optimized Implementation (FrequencyTracker):
- add(): O(1) average time
- deleteOne(): O(1) average time  
- hasFrequency(): O(1) average time
- Space: O(n) where n is the number of unique numbers

Simple Implementation (FrequencyTrackerSimple):
- add(): O(1)
- deleteOne(): O(1)
- hasFrequency(): O(n) where n is the number of unique numbers
- Space: O(n)

List Implementation (FrequencyTrackerWithList):
- add(): O(1)
- deleteOne(): O(n) where n is the total number of elements
- hasFrequency(): O(n)
- Space: O(n)

Key Insights:
1. The main challenge is efficiently tracking both numbers and their frequencies
2. Using two hash maps allows O(1) operations for all methods
3. We need to maintain consistency between num_count and freq_count
4. Deleting zero-count entries prevents memory leaks

Topic: Design, Hash Map, Data Structure
"""
