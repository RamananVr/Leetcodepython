"""
LeetCode Problem 2810: Faulty Keyboard

Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it reverses the string that you have written. Typing other characters works as expected.

You are given a 0-indexed string s representing the final string that appeared on your screen.

Return the original string that you must have typed.

Constraints:
- 1 <= s.length <= 100
- s consists only of lowercase English letters.
- s does not contain the character 'i'.

Example 1:
Input: s = "string"
Output: "rtsng"
Explanation: The original string was "rtsng". When we type 'r', 't', 's', we get "rts". When we type 'i', the string gets reversed and becomes "str". When we type 'n', 'g', we get "string".

Example 2:
Input: s = "poiinter"
Output: "ponter"
Explanation: The original string was "ponter". When we type 'p', 'o', we get "po". When we type 'i', the string gets reversed and becomes "op". When we type 'i', the string gets reversed and becomes "po". When we type 'n', 't', 'e', 'r', we get "ponter".
"""

def faulty_keyboard(s):
    """
    Approach 1: Stack-based Simulation
    
    Use a stack to simulate the typing process in reverse.
    
    Time Complexity: O(n^2) in worst case
    Space Complexity: O(n)
    """
    result = []
    
    # Process characters from right to left
    reverse_mode = False
    
    for char in reversed(s):
        if char == 'i':
            reverse_mode = not reverse_mode
        else:
            if reverse_mode:
                result.append(char)
            else:
                result.insert(0, char)
    
    return ''.join(result)

def faulty_keyboard_deque(s):
    """
    Approach 2: Deque for Efficient Operations
    
    Use deque for O(1) insertion at both ends.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    from collections import deque
    
    result = deque()
    reverse_mode = False
    
    # Process characters from right to left
    for char in reversed(s):
        if char == 'i':
            reverse_mode = not reverse_mode
        else:
            if reverse_mode:
                result.appendleft(char)
            else:
                result.append(char)
    
    return ''.join(result)

def faulty_keyboard_two_pointers(s):
    """
    Approach 3: Two Pointers with Reversal Tracking
    
    Track reversal state and build result accordingly.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(s)
    result = [''] * n
    left, right = 0, n - 1
    reverse_count = 0
    
    # Count total number of 'i's to determine final orientation
    for char in s:
        if char == 'i':
            reverse_count += 1
    
    # Determine if we need to reverse at the end
    final_reversed = reverse_count % 2 == 1
    
    # Build the original string
    original = []
    current_reversed = False
    
    for char in reversed(s):
        if char == 'i':
            current_reversed = not current_reversed
        else:
            if current_reversed != final_reversed:
                original.append(char)
            else:
                original.insert(0, char)
    
    return ''.join(original)

def faulty_keyboard_segment_based(s):
    """
    Approach 4: Segment-based Processing
    
    Split string into segments between 'i' characters.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    segments = []
    current_segment = []
    
    # Split into segments
    for char in s:
        if char == 'i':
            if current_segment:
                segments.append(''.join(current_segment))
                current_segment = []
            segments.append('i')
        else:
            current_segment.append(char)
    
    if current_segment:
        segments.append(''.join(current_segment))
    
    # Process segments in reverse order
    result = []
    reversed_state = False
    
    for segment in reversed(segments):
        if segment == 'i':
            reversed_state = not reversed_state
        else:
            if reversed_state:
                result.extend(list(segment))
            else:
                result = list(segment) + result
    
    return ''.join(result)

def faulty_keyboard_recursive(s):
    """
    Approach 5: Recursive Solution
    
    Recursively process the string by finding 'i' characters.
    
    Time Complexity: O(n^2) in worst case
    Space Complexity: O(n) for recursion stack
    """
    def solve(string, start, end, reversed_state):
        if start > end:
            return []
        
        # Find the next 'i' from the current position
        next_i = -1
        for i in range(start, end + 1):
            if string[i] == 'i':
                next_i = i
                break
        
        if next_i == -1:
            # No more 'i', return the remaining characters
            chars = [string[i] for i in range(start, end + 1)]
            return chars if not reversed_state else chars[::-1]
        
        # Process the part before 'i'
        before_chars = [string[i] for i in range(start, next_i)]
        if reversed_state:
            before_chars = before_chars[::-1]
        
        # Process the part after 'i' with flipped state
        after_chars = solve(string, next_i + 1, end, not reversed_state)
        
        if reversed_state:
            return after_chars + before_chars
        else:
            return before_chars + after_chars
    
    result_chars = solve(s, 0, len(s) - 1, False)
    return ''.join(result_chars)

def faulty_keyboard_optimized(s):
    """
    Approach 6: Most Optimized Solution
    
    Single pass with smart direction tracking.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    from collections import deque
    
    result = deque()
    add_to_front = False
    
    # Process from right to left to undo the typing
    for char in reversed(s):
        if char == 'i':
            add_to_front = not add_to_front
        else:
            if add_to_front:
                result.appendleft(char)
            else:
                result.append(char)
    
    return ''.join(result)

def faulty_keyboard_simulation(s):
    """
    Approach 7: Direct Simulation for Verification
    
    Simulate the actual typing process to verify our solution.
    """
    def simulate_typing(original_string):
        """Simulate typing the original string with faulty keyboard"""
        screen = ""
        for char in original_string:
            if char == 'i':
                screen = screen[::-1]  # Reverse the string
            else:
                screen += char
        return screen
    
    # This is used for testing/verification
    # We would need to search for the original string that produces s
    # This is computationally expensive for large inputs
    pass

# Test cases
def test_faulty_keyboard():
    test_cases = [
        ("string", "rtsng"),
        ("poiinter", "ponter"),
        ("abc", "abc"),
        ("dcba", "dcba"),
        ("a", "a"),
        ("iworld", "dlrow"),
        ("worldi", "dlrow"),
        ("hello", "hello"),
        ("test", "test")
    ]
    
    approaches = [
        ("Stack-based", faulty_keyboard),
        ("Deque", faulty_keyboard_deque),
        ("Two Pointers", faulty_keyboard_two_pointers),
        ("Segment-based", faulty_keyboard_segment_based),
        ("Recursive", faulty_keyboard_recursive),
        ("Optimized", faulty_keyboard_optimized)
    ]
    
    for approach_name, func in approaches:
        print(f"Testing {approach_name} approach:")
        all_passed = True
        
        for s, expected in test_cases:
            try:
                result = func(s)
                passed = result == expected
                if not passed:
                    all_passed = False
                
                print(f"  Input: '{s}'")
                print(f"  Expected: '{expected}', Got: '{result}'")
                print(f"  {'✓' if passed else '✗'}")
            except Exception as e:
                print(f"  Input: '{s}'")
                print(f"  Error: {e}")
                print(f"  ✗")
                all_passed = False
        
        print(f"  Overall: {'✓ All Passed' if all_passed else '✗ Some Failed'}\n")

def verify_solution():
    """Verify our solutions by simulating the typing process"""
    def simulate_typing(original):
        """Simulate the faulty keyboard typing"""
        screen = ""
        for char in original:
            if char == 'i':
                screen = screen[::-1]
            else:
                screen += char
        return screen
    
    test_cases = [
        ("string", "rtsng"),
        ("poiinter", "ponter")
    ]
    
    print("Verification by simulation:")
    for expected_screen, original in test_cases:
        simulated = simulate_typing(original)
        print(f"Original: '{original}' -> Screen: '{simulated}' (Expected: '{expected_screen}')")
        print(f"{'✓' if simulated == expected_screen else '✗'}")

if __name__ == "__main__":
    test_faulty_keyboard()
    print("\n" + "="*50)
    verify_solution()

"""
Topics: String, Stack, Deque, Simulation
Difficulty: Easy

Key Insights:
1. Process the string in reverse to undo the typing
2. Track reversal state as we encounter 'i' characters
3. Use deque for efficient insertion at both ends
4. Each 'i' toggles the insertion direction
5. The problem is about reconstructing the original input sequence

Companies: Google, Microsoft, Amazon, Apple
"""
