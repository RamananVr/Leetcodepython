"""
LeetCode Question #595: Big Countries

Problem Statement:
A country is big if it has an area of at least 3 million square kilometers or a population of at least 25 million.

Write an SQL query to output the name, population, and area of the big countries.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Table: World
+-------------+------------+------------+--------------+
| name        | population | area       | continent    |
+-------------+------------+------------+--------------+
| Afghanistan | 25500100   | 652230     | Asia         |
| Albania     | 2831741    | 28748      | Europe       |
| Algeria     | 37100000   | 2381741    | Africa       |
| Andorra     | 78115      | 468        | Europe       |
| Angola      | 12878000   | 1246700    | Africa       |
+-------------+------------+------------+--------------+

Output:
+-------------+------------+------------+
| name        | population | area       |
+-------------+------------+------------+
| Afghanistan | 25500100   | 652230     |
| Algeria     | 37100000   | 2381741    |
+-------------+------------+------------+
"""

# Python Solution:
# Since this is an SQL problem, we will simulate the solution using Python for demonstration purposes.

# Define a function to filter big countries based on population and area.
def big_countries(world):
    """
    Filters the big countries based on population and area.

    Args:
    world (list of dict): A list of dictionaries representing the table 'World'.
                          Each dictionary contains 'name', 'population', 'area', and 'continent'.

    Returns:
    list of dict: A list of dictionaries containing 'name', 'population', and 'area' of big countries.
    """
    return [
        {"name": country["name"], "population": country["population"], "area": country["area"]}
        for country in world
        if country["population"] >= 25000000 or country["area"] >= 3000000
    ]

# Example Test Cases:
if __name__ == "__main__":
    # Input table
    world = [
        {"name": "Afghanistan", "population": 25500100, "area": 652230, "continent": "Asia"},
        {"name": "Albania", "population": 2831741, "area": 28748, "continent": "Europe"},
        {"name": "Algeria", "population": 37100000, "area": 2381741, "continent": "Africa"},
        {"name": "Andorra", "population": 78115, "area": 468, "continent": "Europe"},
        {"name": "Angola", "population": 12878000, "area": 1246700, "continent": "Africa"},
    ]

    # Expected output
    expected_output = [
        {"name": "Afghanistan", "population": 25500100, "area": 652230},
        {"name": "Algeria", "population": 37100000, "area": 2381741},
    ]

    # Test the function
    output = big_countries(world)
    print("Output:", output)
    print("Expected:", expected_output)
    assert output == expected_output, "Test case failed!"

# Time And Space Complexity Analysis:
# Time Complexity:
# The function iterates through the list of countries once, performing constant-time checks for each country.
# Therefore, the time complexity is O(n), where n is the number of countries in the input list.

# Space Complexity:
# The function creates a new list to store the filtered countries. In the worst case, all countries could be big,
# resulting in a space complexity of O(n), where n is the number of countries in the input list.

# Topic: SQL Simulation / Filtering