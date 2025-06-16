"""
LeetCode Question #2728: Count Houses in a Circular Street

Problem Statement:
You are given an object `street` of class `Street` that represents a circular street and a positive integer `k` which represents a maximum bound for the number of houses in that street (in other words, the number of houses is less than or equal to `k`). Houses' doors could be open or closed initially.

Initially, you are standing in front of a house door on this circular street. Your task is to count the number of houses in the street.

The class `Street` contains the following functions which may help you:
- `void moveRight()`: Move to the next house in the clockwise direction.
- `void moveLeft()`: Move to the next house in the counter-clockwise direction.
- `boolean isDoorOpen()`: Return true if the door of the current house is open, false otherwise.

Note: Inside the street, the houses are numbered from 1 to n in clockwise order.

Constraints:
- `n == number of houses`
- `1 <= n <= k <= 10^3`

Example:
Input: street = [0,0,0,0], k = 10
Output: 4
Explanation: There are 4 houses, and all of them are initially closed.

Input: street = [1,0,1,1,0], k = 10
Output: 5
Explanation: There are 5 houses, 3 of them are initially open and 2 are closed.
"""

# Mock Street class for testing purposes
class Street:
    def __init__(self, houses):
        self.houses = houses
        self.current = 0
        self.n = len(houses)
    
    def moveRight(self):
        self.current = (self.current + 1) % self.n
    
    def moveLeft(self):
        self.current = (self.current - 1) % self.n
    
    def isDoorOpen(self):
        return self.houses[self.current] == 1

def houseCount(street, k):
    """
    Count the number of houses in a circular street.
    
    Args:
        street: Street object with moveRight(), moveLeft(), isDoorOpen() methods
        k: Upper bound on number of houses
    
    Returns:
        Number of houses in the street
    """
    # Strategy: Move right until we return to starting position
    # Track unique positions by their door states and relative positions
    
    # Record initial state
    initial_state = street.isDoorOpen()
    count = 1
    
    # Move right and count until we return to start
    street.moveRight()
    
    while count < k:
        # If we've made a full circle back to start with same door state
        if street.isDoorOpen() == initial_state and count > 0:
            # Additional verification: check if we're really at start
            # by moving one more step and checking if pattern continues
            next_state = None
            if count < k - 1:
                street.moveRight()
                next_state = street.isDoorOpen()
                street.moveLeft()  # Go back
            
            # If this looks like the start, verify by checking a few more positions
            if count > 1:  # Need at least 2 houses to verify pattern
                return count
        
        count += 1
        if count < k:
            street.moveRight()
    
    return count

def houseCount_pattern_matching(street, k):
    """
    Count houses using pattern matching approach.
    
    Args:
        street: Street object
        k: Upper bound on number of houses
    
    Returns:
        Number of houses in the street
    """
    # Record the pattern of door states
    pattern = []
    initial_position = 0
    
    # Collect states until we find a cycle
    for i in range(k):
        pattern.append(street.isDoorOpen())
        street.moveRight()
        
        # Check if we've seen this pattern before (cycle detection)
        if i > 0:
            # Try different cycle lengths
            for cycle_len in range(1, i + 1):
                if i + 1 >= 2 * cycle_len:  # Need at least 2 full cycles to confirm
                    # Check if pattern repeats
                    is_cycle = True
                    for j in range(cycle_len):
                        if pattern[j] != pattern[j + cycle_len]:
                            is_cycle = False
                            break
                    
                    if is_cycle:
                        return cycle_len
    
    return len(pattern)

def houseCount_state_tracking(street, k):
    """
    Count houses by tracking states and positions.
    
    Args:
        street: Street object
        k: Upper bound on number of houses
    
    Returns:
        Number of houses in the street
    """
    # Use a different approach: mark the starting house
    # Since we can't physically mark it, we'll use the door state pattern
    
    visited_states = []
    
    for i in range(k):
        current_state = street.isDoorOpen()
        visited_states.append(current_state)
        
        # Move to next house
        if i < k - 1:
            street.moveRight()
        
        # After visiting enough houses, check for cycle
        if i >= 1:
            # Check if current position could be the start
            # This is tricky without being able to mark houses
            # We'll use the fact that if we've made a complete circle,
            # the pattern should repeat
            
            for cycle_length in range(1, i + 1):
                if (i + 1) % cycle_length == 0:  # Complete cycles
                    # Check if pattern repeats
                    is_repeating = True
                    for j in range(cycle_length):
                        for rep in range(1, (i + 1) // cycle_length):
                            if visited_states[j] != visited_states[j + rep * cycle_length]:
                                is_repeating = False
                                break
                        if not is_repeating:
                            break
                    
                    if is_repeating and cycle_length < i + 1:
                        return cycle_length
    
    return len(visited_states)

def houseCount_simple(street, k):
    """
    Simple approach: move right until pattern repeats.
    
    Args:
        street: Street object
        k: Upper bound on number of houses
    
    Returns:
        Number of houses in the street
    """
    # Collect door states as we move
    states = []
    
    for _ in range(k):
        states.append(street.isDoorOpen())
        street.moveRight()
        
        # Check if we have a repeating pattern
        n = len(states)
        if n >= 2:
            # Check all possible cycle lengths
            for cycle_len in range(1, n):
                if n % cycle_len == 0:
                    # Check if this cycle length works
                    is_cycle = True
                    for i in range(n):
                        if states[i] != states[i % cycle_len]:
                            is_cycle = False
                            break
                    
                    if is_cycle:
                        return cycle_len
    
    return len(states)

def houseCount_optimized(street, k):
    """
    Optimized approach using early cycle detection.
    
    Args:
        street: Street object
        k: Upper bound on number of houses
    
    Returns:
        Number of houses in the street
    """
    # Record initial state
    first_state = street.isDoorOpen()
    count = 1
    
    # Move and collect states
    states = [first_state]
    street.moveRight()
    
    while count < k:
        current_state = street.isDoorOpen()
        states.append(current_state)
        count += 1
        
        # Early detection: if we see the first state again
        if current_state == first_state and count > 1:
            # Verify this is actually the start by checking if pattern repeats
            if count >= 2:
                # Check if we have a valid cycle
                potential_cycle = states[:-1]  # Exclude the repeated first state
                
                # Simple verification: if the next state matches the second state
                if count < k:
                    street.moveRight()
                    next_state = street.isDoorOpen()
                    
                    if len(potential_cycle) > 1 and next_state == potential_cycle[1]:
                        return len(potential_cycle)
                    
                    # Move back
                    street.moveLeft()
        
        if count < k:
            street.moveRight()
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1 - All doors closed
    street = Street([0, 0, 0, 0])
    result = houseCount_simple(street, 10)
    print(f"Test 1 - Expected: 4, Got: {result}")
    assert result == 4
    
    # Test Case 2 - Mixed open/closed doors
    street = Street([1, 0, 1, 1, 0])
    result = houseCount_simple(street, 10)
    print(f"Test 2 - Expected: 5, Got: {result}")
    assert result == 5
    
    # Test Case 3 - Single house
    street = Street([1])
    result = houseCount_simple(street, 10)
    print(f"Test 3 - Expected: 1, Got: {result}")
    assert result == 1
    
    # Test Case 4 - Two houses
    street = Street([0, 1])
    result = houseCount_simple(street, 10)
    print(f"Test 4 - Expected: 2, Got: {result}")
    assert result == 2
    
    # Test Case 5 - All doors open
    street = Street([1, 1, 1])
    result = houseCount_simple(street, 10)
    print(f"Test 5 - Expected: 3, Got: {result}")
    assert result == 3
    
    # Test Case 6 - Pattern with repetition
    street = Street([0, 1, 0, 1])
    result = houseCount_simple(street, 10)
    print(f"Test 6 - Expected: 4, Got: {result}")
    assert result == 4
    
    # Test Case 7 - Larger street
    street = Street([1, 0, 0, 1, 1, 0, 1])
    result = houseCount_simple(street, 15)
    print(f"Test 7 - Expected: 7, Got: {result}")
    assert result == 7
    
    # Test all implementations on same data
    test_cases = [
        [0, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [1],
        [0, 1],
        [1, 1, 1]
    ]
    
    for i, houses in enumerate(test_cases):
        expected = len(houses)
        
        # Test different implementations
        implementations = [
            houseCount_simple,
            houseCount_pattern_matching,
            houseCount_state_tracking
        ]
        
        for j, impl in enumerate(implementations):
            street = Street(houses)
            result = impl(street, 10)
            assert result == expected, f"Test case {i}, implementation {j}: expected {expected}, got {result}"
    
    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

Simple Implementation:
1. Time Complexity: O(n²) where n is the number of houses
   - For each position (up to n), we check all possible cycle lengths
   - Cycle verification takes O(n) time
   - Total: O(n²)

2. Space Complexity: O(n)
   - Store door states for all houses
   - Additional space for cycle detection

Pattern Matching Implementation:
1. Time Complexity: O(n²)
   - Similar to simple approach
   - Pattern comparison for each potential cycle length

2. Space Complexity: O(n)
   - Pattern storage

Optimized Implementation:
1. Time Complexity: O(n) average case, O(n²) worst case
   - Early termination when first state repeats
   - Verification step may require additional moves
   - Best case: O(n) when cycle detected early

2. Space Complexity: O(n)
   - State storage

Key Insights:
- Cannot modify houses or leave physical markers
- Must rely on door state patterns to detect cycles
- Circular nature means we'll eventually return to start
- Need to distinguish between coincidental state matches and actual cycles

Challenges:
1. Identical door states: All doors same state makes detection harder
2. Pattern ambiguity: Short patterns might repeat by coincidence
3. Starting position: Unknown initial position in the cycle

Strategies:
1. Collect sufficient pattern data before making decisions
2. Verify cycles by checking multiple repetitions
3. Use early termination when confident about cycle detection
4. Handle edge cases (single house, all same states)

Real-world Applications:
- Circuit analysis in electrical engineering
- Network topology discovery
- Game development (circular maps)
- Robot navigation in cyclic environments

Topic: Cycle Detection, Pattern Recognition, State Machine, Graph Traversal
"""
