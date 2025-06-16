"""
2739. Total Distance Traveled

A truck has two fuel tanks. You are given two integers, mainTank and additionalTank, representing the fuel in the main tank and the additional tank in liters, respectively.

The truck has a mileage of 10 km per liter. Whenever the truck travels 50 km, if the main tank has at least 5 liters of fuel, the truck will transfer 1 liter of fuel from the additional tank to the main tank.

Return the maximum distance the truck can travel.

Note that the truck can only travel as long as the main tank has fuel.

Example 1:
Input: mainTank = 5, additionalTank = 10
Output: 60
Explanation: 
The truck travels 50 km, then 1 liter of fuel is transferred from additional to main tank.
Now, main tank has 1 liter and additional tank has 9 liters.
The truck travels 10 km and runs out of fuel.
Total distance = 50 + 10 = 60 km.

Example 2:
Input: mainTank = 1, additionalTank = 2
Output: 10
Explanation: 
The truck travels 10 km and runs out of fuel.

Constraints:
- 1 <= mainTank, additionalTank <= 100
"""

def distance_traveled(mainTank: int, additionalTank: int) -> int:
    """
    Calculate maximum distance truck can travel with fuel transfer rules.
    
    Args:
        mainTank: Initial fuel in main tank (liters)
        additionalTank: Initial fuel in additional tank (liters)
        
    Returns:
        int: Maximum distance that can be traveled (km)
        
    Time Complexity: O(mainTank) - simulation based on fuel consumption
    Space Complexity: O(1) - constant extra space
    """
    distance = 0
    
    while mainTank > 0:
        if mainTank >= 5:
            # Travel 50 km (consumes 5 liters)
            distance += 50
            mainTank -= 5
            
            # Transfer 1 liter from additional to main if available
            if additionalTank > 0:
                mainTank += 1
                additionalTank -= 1
        else:
            # Travel remaining distance with remaining fuel
            distance += mainTank * 10
            mainTank = 0
    
    return distance

def distance_traveled_optimized(mainTank: int, additionalTank: int) -> int:
    """
    Optimized calculation using mathematical approach to minimize simulation.
    
    Args:
        mainTank: Initial fuel in main tank (liters)
        additionalTank: Initial fuel in additional tank (liters)
        
    Returns:
        int: Maximum distance that can be traveled (km)
        
    Time Complexity: O(1) - mathematical calculation
    Space Complexity: O(1) - constant space
    """
    distance = 0
    
    # Calculate how many times we can do the 50km + transfer cycle
    transfers = min(mainTank // 5, additionalTank)
    
    # Each transfer cycle: use 5 liters, travel 50km, gain 1 liter
    # Net fuel consumption per cycle: 4 liters
    # Distance per cycle: 50 km
    distance += transfers * 50
    mainTank -= transfers * 4  # Net fuel consumed
    additionalTank -= transfers
    
    # Travel remaining distance with remaining main tank fuel
    distance += mainTank * 10
    
    return distance

def distance_traveled_simulation(mainTank: int, additionalTank: int) -> int:
    """
    Step-by-step simulation for clear understanding of the process.
    
    Args:
        mainTank: Initial fuel in main tank (liters)
        additionalTank: Initial fuel in additional tank (liters)
        
    Returns:
        int: Maximum distance that can be traveled (km)
        
    Time Complexity: O(mainTank) - detailed simulation
    Space Complexity: O(1) - constant space
    """
    total_distance = 0
    
    while mainTank > 0:
        if mainTank >= 5 and additionalTank > 0:
            # Complete a 50km segment with transfer
            total_distance += 50
            mainTank -= 5  # Consume 5 liters for 50km
            mainTank += 1  # Transfer 1 liter from additional
            additionalTank -= 1
        elif mainTank >= 5:
            # Can travel 50km but no additional fuel to transfer
            total_distance += 50
            mainTank -= 5
        else:
            # Less than 5 liters, travel as far as possible
            total_distance += mainTank * 10
            mainTank = 0
    
    return total_distance

def distance_traveled_mathematical(mainTank: int, additionalTank: int) -> int:
    """
    Mathematical approach calculating transfers directly.
    
    Args:
        mainTank: Initial fuel in main tank (liters)
        additionalTank: Initial fuel in additional tank (liters)
        
    Returns:
        int: Maximum distance that can be traveled (km)
        
    Time Complexity: O(1) - direct mathematical calculation
    Space Complexity: O(1) - constant space
    """
    # Each complete cycle consumes 4 liters net (5 used, 1 transferred)
    # and covers 50 km
    
    # Calculate maximum number of complete transfer cycles
    max_cycles = min(mainTank // 5, additionalTank)
    
    # After max_cycles transfers:
    # - Distance covered: max_cycles * 50
    # - Main tank remaining: mainTank - max_cycles * 4
    # - Additional tank remaining: additionalTank - max_cycles
    
    distance_from_cycles = max_cycles * 50
    remaining_main = mainTank - max_cycles * 4
    
    # Travel remaining distance with leftover fuel
    remaining_distance = remaining_main * 10
    
    return distance_from_cycles + remaining_distance

# Test cases
def test_distance_traveled():
    test_cases = [
        # Basic test cases
        (5, 10, 60),    # Example 1
        (1, 2, 10),     # Example 2
        
        # Edge cases
        (1, 0, 10),     # No additional fuel
        (4, 5, 40),     # Less than 5 in main, can't transfer
        (5, 0, 50),     # Exactly 5 in main, no additional
        (10, 1, 110),   # Multiple transfers possible
        
        # Boundary cases
        (5, 1, 60),     # Exactly one transfer possible
        (9, 1, 100),    # Almost two cycles but only one transfer
        (10, 2, 120),   # Exactly two transfers
        
        # Large values
        (50, 10, 560),  # Many transfers
        (25, 5, 270),   # Multiple cycles
        (100, 20, 1080), # Large input
        
        # No transfers possible
        (3, 10, 30),    # Main tank too small for any transfers
        (2, 0, 20),     # Very small main tank
        
        # Optimal transfer scenarios
        (20, 4, 240),   # Exactly 4 transfers (20/5 = 4, additionalTank = 4)
        (15, 10, 190),  # Limited by main tank capacity for transfers
    ]
    
    print("Testing distance_traveled function:")
    for i, (mainTank, additionalTank, expected) in enumerate(test_cases):
        result1 = distance_traveled(mainTank, additionalTank)
        result2 = distance_traveled_optimized(mainTank, additionalTank)
        result3 = distance_traveled_simulation(mainTank, additionalTank)
        result4 = distance_traveled_mathematical(mainTank, additionalTank)
        
        print(f"Test {i+1}: mainTank={mainTank}, additionalTank={additionalTank}")
        print(f"  Expected: {expected}")
        print(f"  Basic Simulation: {result1}")
        print(f"  Optimized: {result2}")
        print(f"  Detailed Simulation: {result3}")
        print(f"  Mathematical: {result4}")
        
        assert result1 == expected, f"Basic failed for test case {i+1}"
        assert result2 == expected, f"Optimized failed for test case {i+1}"
        assert result3 == expected, f"Simulation failed for test case {i+1}"
        assert result4 == expected, f"Mathematical failed for test case {i+1}"
        print(f"  ✓ All passed\n")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_distance_traveled()

"""
Time Complexity Analysis:
- Basic Simulation: O(mainTank) - loops based on fuel consumption
- Optimized: O(1) - mathematical calculation with minimal loops
- Detailed Simulation: O(mainTank) - step by step process
- Mathematical: O(1) - direct formula application

Space Complexity Analysis:
- All solutions: O(1) - using constant extra space

Key Insights:
1. The truck travels 50km per 5 liters (10 km/liter rate)
2. Transfer happens when main tank has ≥5 liters after traveling 50km
3. Each transfer cycle effectively consumes 4 liters net (5 used, 1 gained)
4. We can calculate the number of complete cycles mathematically
5. Remaining fuel after cycles determines final distance

Transfer Logic:
- Travel 50km (consume 5L) → if additionalTank > 0, transfer 1L to main
- Net consumption per cycle: 4L from main, 1L from additional
- Continue until main tank can't support another 50km trip

Topics: Simulation, Math, Greedy
"""
