"""
LeetCode Problem #2525: Categorize Box According to Criteria

Problem Statement:
You are given four integers `length`, `width`, `height`, and `mass` which represent a box's dimensions and mass respectively.

The box is categorized based on the following criteria:

1. A box is considered "Bulky" if any of the following conditions are true:
   - Any of the dimensions of the box (length, width, or height) is greater than or equal to 10^4.
   - The volume of the box (length * width * height) is greater than or equal to 10^9.

2. A box is considered "Heavy" if its mass is greater than or equal to 100.

3. A box is categorized based on the following rules:
   - If the box is both "Bulky" and "Heavy", the category is "Both".
   - If the box is neither "Bulky" nor "Heavy", the category is "Neither".
   - If the box is "Bulky" but not "Heavy", the category is "Bulky".
   - If the box is "Heavy" but not "Bulky", the category is "Heavy".

Return the category of the box as a string.

Constraints:
- 1 <= length, width, height <= 10^5
- 1 <= mass <= 10^3
"""

def categorizeBox(length: int, width: int, height: int, mass: int) -> str:
    # Check if the box is "Bulky"
    bulky = length >= 10**4 or width >= 10**4 or height >= 10**4 or (length * width * height) >= 10**9
    
    # Check if the box is "Heavy"
    heavy = mass >= 100
    
    # Determine the category based on the conditions
    if bulky and heavy:
        return "Both"
    elif not bulky and not heavy:
        return "Neither"
    elif bulky:
        return "Bulky"
    else:  # heavy is True
        return "Heavy"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Both Bulky and Heavy
    print(categorizeBox(10000, 10000, 10000, 150))  # Output: "Both"

    # Test Case 2: Neither Bulky nor Heavy
    print(categorizeBox(10, 10, 10, 50))  # Output: "Neither"

    # Test Case 3: Bulky but not Heavy
    print(categorizeBox(10000, 10, 10, 50))  # Output: "Bulky"

    # Test Case 4: Heavy but not Bulky
    print(categorizeBox(10, 10, 10, 150))  # Output: "Heavy"

    # Test Case 5: Edge case for volume
    print(categorizeBox(1000, 1000, 1000, 99))  # Output: "Bulky"

    # Test Case 6: Edge case for mass
    print(categorizeBox(10, 10, 10, 100))  # Output: "Heavy"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution performs a constant number of operations (comparisons and arithmetic calculations) regardless of the input size.
- Therefore, the time complexity is O(1).

Space Complexity:
- The solution uses a constant amount of extra space for variables.
- Therefore, the space complexity is O(1).

Topic: Conditional Logic
"""