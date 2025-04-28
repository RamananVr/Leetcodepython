"""
LeetCode Problem #2469: Convert the Temperature

Problem Statement:
You are given a non-negative floating point number `celsius`, that denotes the temperature in Celsius.

You should convert Celsius into two other temperature units:
1. Kelvin (K): The formula to convert Celsius to Kelvin is `kelvin = celsius + 273.15`.
2. Fahrenheit (°F): The formula to convert Celsius to Fahrenheit is `fahrenheit = celsius * 1.80 + 32.00`.

Return the conversion results as an array `result = [kelvin, fahrenheit]`.

Example:
Input: celsius = 36.50
Output: [309.65000, 97.70000]

Input: celsius = 122.11
Output: [395.26000, 251.79800]

Constraints:
- 0 <= celsius <= 1000
- The output should be rounded to 5 decimal places.
"""

# Python Solution
def convertTemperature(celsius: float) -> list[float]:
    """
    Converts the given temperature in Celsius to Kelvin and Fahrenheit.

    Args:
    celsius (float): The temperature in Celsius.

    Returns:
    list[float]: A list containing the temperature in Kelvin and Fahrenheit.
    """
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    return [round(kelvin, 5), round(fahrenheit, 5)]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    celsius = 36.50
    print(convertTemperature(celsius))  # Expected Output: [309.65000, 97.70000]

    # Test Case 2
    celsius = 122.11
    print(convertTemperature(celsius))  # Expected Output: [395.26000, 251.79800]

    # Test Case 3
    celsius = 0.0
    print(convertTemperature(celsius))  # Expected Output: [273.15000, 32.00000]

    # Test Case 4
    celsius = 1000.0
    print(convertTemperature(celsius))  # Expected Output: [1273.15000, 1832.00000]

    # Test Case 5
    celsius = 25.0
    print(convertTemperature(celsius))  # Expected Output: [298.15000, 77.00000]

"""
Time Complexity Analysis:
- The solution performs a constant number of arithmetic operations (addition, multiplication) and rounding.
- Therefore, the time complexity is O(1).

Space Complexity Analysis:
- The solution uses a constant amount of space to store intermediate results (kelvin, fahrenheit).
- Therefore, the space complexity is O(1).

Topic: Math
"""