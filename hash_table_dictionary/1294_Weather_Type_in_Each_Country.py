"""
LeetCode Problem #1294: Weather Type in Each Country

Problem Statement:
You are given a list of countries, where each country is represented as a string. Each country has a weather type associated with it, which is either "Sunny", "Rainy", or "Cloudy". You are also given a list of queries, where each query asks for the weather type of a specific country.

Write a function `weatherTypeInEachCountry(countries: List[str], weather: List[str], queries: List[str]) -> List[str]` that returns a list of weather types corresponding to the queried countries. If a country in the query does not exist in the list of countries, return "Unknown" for that query.

Constraints:
- The length of `countries` and `weather` is the same.
- 1 <= len(countries), len(weather), len(queries) <= 10^4
- Each country name and weather type is a string of length between 1 and 100.
- The weather type is guaranteed to be one of "Sunny", "Rainy", or "Cloudy".
- Queries may contain country names not present in the `countries` list.

Example:
Input:
countries = ["USA", "Canada", "Mexico"]
weather = ["Sunny", "Rainy", "Cloudy"]
queries = ["USA", "Mexico", "India"]

Output:
["Sunny", "Cloudy", "Unknown"]
"""

from typing import List

def weatherTypeInEachCountry(countries: List[str], weather: List[str], queries: List[str]) -> List[str]:
    # Create a dictionary to map countries to their weather types
    country_weather_map = {country: weather_type for country, weather_type in zip(countries, weather)}
    
    # Process each query and return the corresponding weather type or "Unknown"
    return [country_weather_map.get(query, "Unknown") for query in queries]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    countries = ["USA", "Canada", "Mexico"]
    weather = ["Sunny", "Rainy", "Cloudy"]
    queries = ["USA", "Mexico", "India"]
    print(weatherTypeInEachCountry(countries, weather, queries))  # Output: ["Sunny", "Cloudy", "Unknown"]

    # Test Case 2
    countries = ["France", "Germany", "Italy"]
    weather = ["Rainy", "Cloudy", "Sunny"]
    queries = ["Germany", "Italy", "Spain"]
    print(weatherTypeInEachCountry(countries, weather, queries))  # Output: ["Cloudy", "Sunny", "Unknown"]

    # Test Case 3
    countries = ["Japan", "China", "Korea"]
    weather = ["Sunny", "Rainy", "Cloudy"]
    queries = ["China", "Korea", "Japan", "India"]
    print(weatherTypeInEachCountry(countries, weather, queries))  # Output: ["Rainy", "Cloudy", "Sunny", "Unknown"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Creating the dictionary `country_weather_map` takes O(n), where n is the length of the `countries` list.
- Processing the queries takes O(m), where m is the length of the `queries` list.
- Overall time complexity: O(n + m).

Space Complexity:
- The dictionary `country_weather_map` requires O(n) space to store the mapping of countries to weather types.
- The output list requires O(m) space to store the results for the queries.
- Overall space complexity: O(n + m).
"""

# Topic: Hash Table / Dictionary