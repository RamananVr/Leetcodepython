"""
LeetCode Problem #1501: Countries You Can Safely Invest In

Problem Statement:
You are given a table `Person` with the following structure:

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
| country     | varchar |

id is the primary key for this table. Each row of this table contains the id, name, and country of a person.

You are also given a table `Friend` with the following structure:

| Column Name | Type |
|-------------|------|
| person1_id  | int  |
| person2_id  | int  |

(person1_id, person2_id) is the primary key for this table. Each row of this table indicates that person1_id and person2_id are friends.

Write an SQL query to find the countries where all the people are friends with at least one person from the same country.

Return the result table in any order.

The query result format is in the following example.

Example Input:
Person table:
| id | name  | country |
|----|-------|---------|
| 1  | Alice | USA     |
| 2  | Bob   | USA     |
| 3  | Carol | Canada  |
| 4  | David | Canada  |
| 5  | Eve   | Canada  |

Friend table:
| person1_id | person2_id |
|------------|------------|
| 1          | 2          |
| 2          | 3          |
| 3          | 4          |
| 4          | 5          |

Example Output:
| country |
|---------|
| USA     |
| Canada  |

Explanation:
- In the USA, Alice and Bob are friends, so the USA is a valid country.
- In Canada, Carol, David, and Eve are all friends with at least one person from Canada, so Canada is a valid country.
"""

# Python Solution
def countries_you_can_safely_invest_in(person, friend):
    """
    This function simulates the SQL query to find countries where all people are friends
    with at least one person from the same country.

    :param person: List of dictionaries representing the Person table.
    :param friend: List of dictionaries representing the Friend table.
    :return: List of countries that satisfy the condition.
    """
    from collections import defaultdict

    # Step 1: Build a mapping of person_id to country
    person_to_country = {p['id']: p['country'] for p in person}

    # Step 2: Build a graph of friendships
    friendships = defaultdict(set)
    for f in friend:
        friendships[f['person1_id']].add(f['person2_id'])
        friendships[f['person2_id']].add(f['person1_id'])

    # Step 3: Check each country
    countries = set(p['country'] for p in person)
    valid_countries = set()

    for country in countries:
        # Get all people in this country
        people_in_country = {p['id'] for p in person if p['country'] == country}

        # Check if every person in this country has at least one friend in the same country
        is_valid = True
        for person_id in people_in_country:
            if not friendships[person_id] & people_in_country:
                is_valid = False
                break

        if is_valid:
            valid_countries.add(country)

    return list(valid_countries)


# Example Test Cases
if __name__ == "__main__":
    # Example Input
    person = [
        {"id": 1, "name": "Alice", "country": "USA"},
        {"id": 2, "name": "Bob", "country": "USA"},
        {"id": 3, "name": "Carol", "country": "Canada"},
        {"id": 4, "name": "David", "country": "Canada"},
        {"id": 5, "name": "Eve", "country": "Canada"},
    ]

    friend = [
        {"person1_id": 1, "person2_id": 2},
        {"person1_id": 2, "person2_id": 3},
        {"person1_id": 3, "person2_id": 4},
        {"person1_id": 4, "person2_id": 5},
    ]

    # Expected Output: ['USA', 'Canada']
    print(countries_you_can_safely_invest_in(person, friend))


# Time and Space Complexity Analysis
"""
Time Complexity:
- Building the person_to_country map: O(n), where n is the number of people.
- Building the friendships graph: O(m), where m is the number of friendships.
- Checking each country:
  - For each country, we iterate over all people in that country and their friendships.
  - In the worst case, this is O(n + m).
Overall: O(n + m).

Space Complexity:
- person_to_country map: O(n).
- friendships graph: O(m).
- people_in_country set: O(n) in the worst case.
Overall: O(n + m).
"""

# Topic: Graphs