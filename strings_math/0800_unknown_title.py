"""
LeetCode Problem #800: Similar RGB Color

Problem Statement:
The red-green-blue color "#ABCDEF" can be written as "#AABBCC" in shorthand. 
For example, "#15c" is shorthand for "#1155cc". 

The similarity between two colors "#ABCDEF" and "#UVWXYZ" is defined as 
-(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2. 

Given the color "#ABCDEF", return the color that is most similar to it, 
which has a shorthand (i.e., it can be represented as some "#AABBCC").

Example 1:
Input: color = "#09f166"
Output: "#11ee66"

Note:
1. color is a string of length 7.
2. color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from '0' to 'f'.
3. Any answer which has the same (highest) similarity as the best answer will be accepted.
4. All inputs and outputs should use lowercase letters, and the output is 7 characters.
"""

# Solution
def similarRGB(color: str) -> str:
    def closest_shorthand_component(component: str) -> str:
        # Convert the component to an integer
        value = int(component, 16)
        # Find the closest shorthand value (0x00, 0x11, ..., 0xFF)
        closest = round(value / 17) * 17
        # Convert back to hexadecimal and format as two characters
        return f"{closest:02x}"

    # Extract the three components of the color
    r, g, b = color[1:3], color[3:5], color[5:7]
    # Find the closest shorthand for each component
    return f"#{closest_shorthand_component(r)}{closest_shorthand_component(g)}{closest_shorthand_component(b)}"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    color1 = "#09f166"
    print(similarRGB(color1))  # Expected Output: "#11ee66"

    # Test Case 2
    color2 = "#4e3f2a"
    print(similarRGB(color2))  # Expected Output: "#554433"

    # Test Case 3
    color3 = "#abcdef"
    print(similarRGB(color3))  # Expected Output: "#aabbcc"

    # Test Case 4
    color4 = "#000000"
    print(similarRGB(color4))  # Expected Output: "#000000"

    # Test Case 5
    color5 = "#ffffff"
    print(similarRGB(color5))  # Expected Output: "#ffffff"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function processes each of the three color components (R, G, B) independently.
- For each component, the operations (conversion to integer, rounding, and formatting) are O(1).
- Therefore, the overall time complexity is O(1).

Space Complexity:
- The function uses a constant amount of space for intermediate variables and calculations.
- No additional data structures are used, so the space complexity is O(1).
"""

# Topic: Strings, Math