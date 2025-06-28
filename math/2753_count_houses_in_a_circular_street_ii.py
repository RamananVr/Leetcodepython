"""
LeetCode Problem 2753: Count Houses in a Circular Street II

You are given an object street of class Street that represents a circular street and a positive integer k. There are houses numbered from 0 to n - 1.

Initially, you are standing in front of house 0. You can perform one of the following operations any number of times:
- Move to the next house: street.moveRight()
- Move to the previous house: street.moveLeft()
- Check if the current house is painted: street.isDoorOpen()

Note that the street is circular, which means the next house of house n - 1 is house 0, and the previous house of house 0 is house n - 1.

The street object has the following methods:
- void moveRight(): Move to the next house in the circular street.
- void moveLeft(): Move to the previous house in the circular street.
- boolean isDoorOpen(): Return true if the door is open (house is painted), false otherwise.

It is guaranteed that exactly k houses are painted, and they are evenly distributed. For example, if n = 6 and k = 3, then houses 0, 2, and 4 are painted.

Return the number of houses in the street (the length of the array).

Example 1:
Input: street = [1,0,1,0,1,0], k = 3
Output: 6
Explanation: There are 6 houses, and exactly 3 of them are painted (houses 0, 2, 4).
Since k = 3 and the houses are evenly distributed, the distance between painted houses is 6/3 = 2.

Example 2:
Input: street = [1,0,0,1,0,0], k = 2  
Output: 6
Explanation: There are 6 houses, and exactly 2 of them are painted (houses 0, 3).
Since k = 2 and the houses are evenly distributed, the distance between painted houses is 6/2 = 3.

Constraints:
- n == street.length
- 2 <= n <= 10^4
- k == number of painted houses
- 1 <= k <= n/2
- Exactly k houses are painted and evenly distributed
- The input is generated such that there is exactly one valid answer
"""

class Street:
    """Mock Street class for testing purposes."""
    
    def __init__(self, houses):
        self.houses = houses
        self.n = len(houses)
        self.current = 0
    
    def moveRight(self):
        """Move to the next house in the circular street."""
        self.current = (self.current + 1) % self.n
    
    def moveLeft(self):
        """Move to the previous house in the circular street."""
        self.current = (self.current - 1) % self.n
    
    def isDoorOpen(self):
        """Return true if current house is painted."""
        return self.houses[self.current] == 1


def houseCount(street: Street, k: int) -> int:
    """
    Find the number of houses in a circular street.
    
    Since painted houses are evenly distributed, we can find the distance
    between consecutive painted houses and multiply by k.
    
    Strategy:
    1. Find the distance between first two painted houses
    2. Total houses = distance * k
    
    Args:
        street: Street object with moveRight(), moveLeft(), isDoorOpen() methods
        k: Number of painted houses
        
    Returns:
        Total number of houses in the street
        
    Time Complexity: O(n/k) on average
    Space Complexity: O(1)
    """
    # Start at house 0, find next painted house
    moves = 0
    
    # Move right until we find the next painted house
    while True:
        street.moveRight()
        moves += 1
        if street.isDoorOpen():
            break
    
    # Distance between consecutive painted houses
    distance = moves
    
    # Total houses = distance * k (since houses are evenly distributed)
    return distance * k


def houseCountValidation(street: Street, k: int) -> int:
    """
    Alternative approach that validates the answer by making a full circle.
    
    Args:
        street: Street object
        k: Number of painted houses
        
    Returns:
        Total number of houses in the street
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Count painted houses in a full circle to validate
    painted_count = 0
    total_moves = 0
    
    # Count painted house at starting position
    if street.isDoorOpen():
        painted_count += 1
    
    # Make a full circle
    while True:
        street.moveRight()
        total_moves += 1
        
        if street.isDoorOpen():
            painted_count += 1
        
        # If we've seen k painted houses and we're back at start
        if painted_count == k + 1:  # +1 because we double-counted starting house
            break
    
    return total_moves


def houseCountOptimal(street: Street, k: int) -> int:
    """
    Most efficient approach using mathematical property.
    
    Since houses are evenly distributed, we only need to find the
    distance to the next painted house.
    
    Args:
        street: Street object
        k: Number of painted houses
        
    Returns:
        Total number of houses in the street
        
    Time Complexity: O(n/k) expected
    Space Complexity: O(1)
    """
    moves = 0
    
    # Move right until we find the next painted house
    while True:
        street.moveRight()
        moves += 1
        if street.isDoorOpen():
            break
    
    # Since houses are evenly distributed, total = moves * k
    return moves * k


def houseCountTwoPointer(street: Street, k: int) -> int:
    """
    Two-pointer approach: find distance between two painted houses.
    
    Args:
        street: Street object
        k: Number of painted houses
        
    Returns:
        Total number of houses in the street
        
    Time Complexity: O(n/k)
    Space Complexity: O(1)
    """
    # Assume we start at a painted house (house 0)
    first_painted = 0 if street.isDoorOpen() else None
    
    if first_painted is None:
        # Find first painted house
        moves = 0
        while not street.isDoorOpen():
            street.moveRight()
            moves += 1
        first_painted = moves
    
    # Find next painted house
    moves = 0
    while True:
        street.moveRight()
        moves += 1
        if street.isDoorOpen():
            break
    
    # Distance between consecutive painted houses
    distance = moves
    
    return distance * k


def houseCountBruteForce(street: Street, k: int) -> int:
    """
    Brute force: count all houses by making a complete circle.
    
    Args:
        street: Street object
        k: Number of painted houses
        
    Returns:
        Total number of houses in the street
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    painted_houses = []
    total_houses = 0
    
    # Record starting position
    start_painted = street.isDoorOpen()
    if start_painted:
        painted_houses.append(0)
    
    # Make a complete circle
    while True:
        street.moveRight()
        total_houses += 1
        
        if street.isDoorOpen():
            painted_houses.append(total_houses)
        
        # Check if we're back to start
        if len(painted_houses) > 1 and street.isDoorOpen() == start_painted:
            # Verify we found exactly k painted houses
            if len(painted_houses) == k + 1:  # +1 for double counting start
                break
    
    return total_houses


# Test cases
def test_houseCount():
    """Test the houseCount function with various inputs."""
    
    test_cases = [
        {
            "houses": [1,0,1,0,1,0],
            "k": 3,
            "expected": 6,
            "description": "Example 1: 3 painted houses evenly distributed"
        },
        {
            "houses": [1,0,0,1,0,0],
            "k": 2,
            "expected": 6,
            "description": "Example 2: 2 painted houses evenly distributed"
        },
        {
            "houses": [1,0,0,0,1,0,0,0],
            "k": 2,
            "expected": 8,
            "description": "8 houses with 2 painted, distance = 4"
        },
        {
            "houses": [1,0,1,0],
            "k": 2,
            "expected": 4,
            "description": "4 houses with 2 painted, distance = 2"
        },
        {
            "houses": [1,1],
            "k": 2,
            "expected": 2,
            "description": "Minimum case: 2 houses, both painted"
        },
        {
            "houses": [1,0,0,0,0,1,0,0,0,0],
            "k": 2,
            "expected": 10,
            "description": "10 houses with 2 painted, distance = 5"
        }
    ]
    
    for i, test in enumerate(test_cases):
        houses = test["houses"]
        k = test["k"]
        expected = test["expected"]
        
        print(f"Test {i+1}: {test['description']}")
        print(f"  Houses pattern: {houses}")
        print(f"  Painted houses (k): {k}")
        print(f"  Expected: {expected}")
        
        # Test main solution
        street1 = Street(houses)
        result1 = houseCount(street1, k)
        print(f"  Main approach: {result1}")
        
        # Test optimal solution
        street2 = Street(houses)
        result2 = houseCountOptimal(street2, k)
        print(f"  Optimal approach: {result2}")
        
        # Test validation approach (for smaller inputs)
        if len(houses) <= 20:
            street3 = Street(houses)
            result3 = houseCountValidation(street3, k)
            print(f"  Validation approach: {result3}")
            assert result3 == expected, f"Validation approach failed for test {i+1}"
        
        # Verify results
        assert result1 == expected, f"Main approach failed for test {i+1}"
        assert result2 == expected, f"Optimal approach failed for test {i+1}"
        
        print(f"  ✓ All solutions passed!")
        print()


if __name__ == "__main__":
    test_houseCount()

"""
Complexity Analysis:

1. Main Approach (houseCount):
   - Time Complexity: O(n/k) - distance between painted houses is n/k
   - Space Complexity: O(1) - only using constant extra space

2. Optimal Approach (houseCountOptimal):
   - Time Complexity: O(n/k) - same as main approach
   - Space Complexity: O(1) - constant space

3. Validation Approach (houseCountValidation):
   - Time Complexity: O(n) - makes complete circle to verify
   - Space Complexity: O(1) - constant space

4. Brute Force (houseCountBruteForce):
   - Time Complexity: O(n) - visits every house
   - Space Complexity: O(k) - stores painted house positions

Key Insights:
- Since painted houses are evenly distributed, distance between consecutive painted houses is n/k
- We only need to find the distance to the next painted house from our starting position
- Total houses = distance_between_painted_houses * k
- This leverages the mathematical property of even distribution

Algorithm:
1. Start at house 0 (or any position)
2. Move right until finding the next painted house
3. Count the moves (this gives us the spacing)
4. Multiply by k to get total houses

Edge Cases:
- Minimum case: 2 houses
- All painted houses are adjacent (k = n/2)
- Large spacing between painted houses
- Starting at painted vs unpainted house

Optimization:
- The key insight is that we don't need to visit all houses
- Mathematical property of even distribution allows us to extrapolate
- Expected time is much better than O(n) in most cases

Topics: Math, Circular Array, Pattern Recognition, Greedy Algorithms
"""
