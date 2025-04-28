"""
LeetCode Problem #895: Maximum Frequency Stack

Problem Statement:
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:
- FreqStack() Initializes the object.
- void push(int val) Pushes an integer val onto the stack.
- int pop() Removes and returns the most frequent element in the stack.
  - If there is a tie for the most frequent element, the element closest to the top of the stack is removed and returned.

Constraints:
- 0 <= val <= 10^9
- At most 2 * 10^4 calls will be made to push and pop.

Example:
Input:
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output:
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation:
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5, 7]
freqStack.push(5); // The stack is [5, 7, 5]
freqStack.push(7); // The stack is [5, 7, 5, 7]
freqStack.push(4); // The stack is [5, 7, 5, 7, 4]
freqStack.push(5); // The stack is [5, 7, 5, 7, 4, 5]
freqStack.pop();   // Returns 5, as 5 is the most frequent. The stack becomes [5, 7, 5, 7, 4]
freqStack.pop();   // Returns 7, as 7 is the most frequent. The stack becomes [5, 7, 5, 4]
freqStack.pop();   // Returns 5, as 5 is the most frequent. The stack becomes [5, 7, 4]
freqStack.pop();   // Returns 4, as 4 is the most frequent. The stack becomes [5, 7]
"""

# Python Solution
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)  # Maps each value to its frequency
        self.group = defaultdict(list)  # Maps frequency to a stack of values
        self.max_freq = 0  # Tracks the current maximum frequency

    def push(self, val: int) -> None:
        self.freq[val] += 1
        freq = self.freq[val]
        if freq > self.max_freq:
            self.max_freq = freq
        self.group[freq].append(val)

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val

# Example Test Cases
if __name__ == "__main__":
    freqStack = FreqStack()
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(4)
    freqStack.push(5)
    print(freqStack.pop())  # Output: 5
    print(freqStack.pop())  # Output: 7
    print(freqStack.pop())  # Output: 5
    print(freqStack.pop())  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- push(val): O(1) - Incrementing frequency and appending to the group stack are constant time operations.
- pop(): O(1) - Removing the most frequent element and updating the frequency are constant time operations.

Space Complexity:
- O(n) - The space required for `freq` and `group` dictionaries is proportional to the number of unique elements in the stack.

Topic: Stack, Hash Table
"""