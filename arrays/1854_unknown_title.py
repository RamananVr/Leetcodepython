"""
LeetCode Problem #1854: Maximum Population Year

Problem Statement:
You are given a 2D integer array `logs` where each `logs[i] = [birthi, deathi]` indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if `birthi <= x < deathi`. Note that the person is not counted in the population in the year they die.

Return the earliest year with the maximum population.

Constraints:
- 1 <= logs.length <= 100
- 1950 <= birthi < deathi <= 2050
"""

def maximumPopulation(logs):
    """
    Finds the earliest year with the maximum population.

    :param logs: List[List[int]] - A list of birth and death years for individuals.
    :return: int - The earliest year with the maximum population.
    """
    # Create an array to track population changes for years 1950 to 2050
    population_changes = [0] * 101  # 101 because 2050 - 1950 + 1 = 101

    # Update population changes based on birth and death years
    for birth, death in logs:
        population_changes[birth - 1950] += 1  # Increment population for birth year
        population_changes[death - 1950] -= 1  # Decrement population for death year

    # Calculate the running population and find the year with the maximum population
    max_population = 0
    current_population = 0
    earliest_year = 1950

    for year in range(101):
        current_population += population_changes[year]
        if current_population > max_population:
            max_population = current_population
            earliest_year = 1950 + year

    return earliest_year

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    logs1 = [[1993, 1999], [2000, 2010]]
    print(maximumPopulation(logs1))  # Output: 1993

    # Test Case 2
    logs2 = [[1950, 1961], [1960, 1971], [1970, 1981]]
    print(maximumPopulation(logs2))  # Output: 1960

    # Test Case 3
    logs3 = [[2000, 2005], [2001, 2003], [2002, 2004]]
    print(maximumPopulation(logs3))  # Output: 2002

    # Test Case 4
    logs4 = [[1980, 1990], [1975, 1985], [1970, 1980], [1965, 1975]]
    print(maximumPopulation(logs4))  # Output: 1975

"""
Time Complexity:
- O(n + y), where n is the number of logs and y is the range of years (101 in this case).
  - We iterate through the logs to update the population changes (O(n)).
  - We then iterate through the years to calculate the running population (O(y)).

Space Complexity:
- O(y), where y is the range of years (101 in this case).
  - We use an array of size 101 to store population changes.

Topic: Arrays
"""