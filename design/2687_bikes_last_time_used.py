"""
LeetCode Question #2687: Bikes Last Time Used

Problem Statement:
Table: Bikes
+---------------+----------+
| Column Name   | Type     |
+---------------+----------+
| bike_id       | int      |
| last_used     | datetime |
+---------------+----------+
bike_id is the primary key of this table.
Each row contains the bike id and the last time the bike was used.

Write an SQL query to find the latest time each bike was used.

Return the result table ordered by bike_id in ascending order.

Examples:
Example 1:
Input: 
Bikes table:
+---------+---------------------+
| bike_id | last_used           |
+---------+---------------------+
| W00576  | 2012-03-25 11:30:00 |
| W00300  | 2012-03-25 10:30:00 |
| W00455  | 2012-03-26 14:30:00 |
| W00576  | 2012-03-25 12:30:00 |
| W00576  | 2012-03-25 13:30:00 |
+---------+---------------------+

Output: 
+---------+---------------------+
| bike_id | last_used           |
+---------+---------------------+
| W00300  | 2012-03-25 10:30:00 |
| W00455  | 2012-03-26 14:30:00 |
| W00576  | 2012-03-25 13:30:00 |
+---------+---------------------+

Explanation: 
- W00300 was used only once.
- W00455 was used only once.
- W00576 was used 3 times, the latest time was 2012-03-25 13:30:00.

Constraints:
- 1 <= bike_id count <= 1000
- last_used contains valid datetime values.
"""

# This is a SQL problem, but we'll provide Python simulation and SQL solutions

def bikes_last_time_used(bikes_data):
    """
    Python simulation of the SQL query.
    
    Args:
        bikes_data: List of tuples (bike_id, last_used)
    
    Returns:
        List of tuples (bike_id, latest_last_used) sorted by bike_id
    """
    from collections import defaultdict
    from datetime import datetime
    
    # Track the latest usage time for each bike
    bike_latest = defaultdict(lambda: None)
    
    for bike_id, last_used in bikes_data:
        # Convert string to datetime if needed
        if isinstance(last_used, str):
            last_used = datetime.strptime(last_used, '%Y-%m-%d %H:%M:%S')
        
        # Update if this is the first time we see this bike or if this time is later
        if bike_latest[bike_id] is None or last_used > bike_latest[bike_id]:
            bike_latest[bike_id] = last_used
    
    # Sort by bike_id and return
    result = []
    for bike_id in sorted(bike_latest.keys()):
        latest_time = bike_latest[bike_id]
        if isinstance(latest_time, datetime):
            latest_time = latest_time.strftime('%Y-%m-%d %H:%M:%S')
        result.append((bike_id, latest_time))
    
    return result

def create_sql_solution():
    """
    Returns the SQL solution for the problem.
    """
    sql_query = """
    SELECT 
        bike_id,
        MAX(last_used) AS last_used
    FROM Bikes
    GROUP BY bike_id
    ORDER BY bike_id;
    """
    return sql_query

def create_alternative_sql_solutions():
    """
    Alternative SQL approaches.
    """
    
    # Solution 1: Using window function
    solution1 = """
    SELECT DISTINCT
        bike_id,
        FIRST_VALUE(last_used) OVER (
            PARTITION BY bike_id 
            ORDER BY last_used DESC
        ) AS last_used
    FROM Bikes
    ORDER BY bike_id;
    """
    
    # Solution 2: Using correlated subquery
    solution2 = """
    SELECT 
        b1.bike_id,
        b1.last_used
    FROM Bikes b1
    WHERE b1.last_used = (
        SELECT MAX(b2.last_used)
        FROM Bikes b2
        WHERE b2.bike_id = b1.bike_id
    )
    ORDER BY b1.bike_id;
    """
    
    # Solution 3: Using ROW_NUMBER
    solution3 = """
    SELECT 
        bike_id,
        last_used
    FROM (
        SELECT 
            bike_id,
            last_used,
            ROW_NUMBER() OVER (
                PARTITION BY bike_id 
                ORDER BY last_used DESC
            ) as rn
        FROM Bikes
    ) ranked
    WHERE rn = 1
    ORDER BY bike_id;
    """
    
    # Solution 4: Using RANK (handles ties differently)
    solution4 = """
    SELECT 
        bike_id,
        last_used
    FROM (
        SELECT 
            bike_id,
            last_used,
            RANK() OVER (
                PARTITION BY bike_id 
                ORDER BY last_used DESC
            ) as rnk
        FROM Bikes
    ) ranked
    WHERE rnk = 1
    ORDER BY bike_id;
    """
    
    return {
        "window_function": solution1,
        "correlated_subquery": solution2,
        "row_number": solution3,
        "rank": solution4
    }

def analyze_bike_usage_patterns(bikes_data):
    """
    Additional analysis of bike usage patterns.
    """
    from collections import defaultdict, Counter
    from datetime import datetime, timedelta
    
    bike_usage = defaultdict(list)
    
    # Group all usage times by bike
    for bike_id, last_used in bikes_data:
        if isinstance(last_used, str):
            last_used = datetime.strptime(last_used, '%Y-%m-%d %H:%M:%S')
        bike_usage[bike_id].append(last_used)
    
    # Sort usage times for each bike
    for bike_id in bike_usage:
        bike_usage[bike_id].sort()
    
    analysis = {}
    
    for bike_id, usage_times in bike_usage.items():
        usage_count = len(usage_times)
        first_used = usage_times[0]
        last_used = usage_times[-1]
        
        # Calculate usage duration
        total_duration = last_used - first_used if usage_count > 1 else timedelta(0)
        
        # Calculate average time between uses
        if usage_count > 1:
            intervals = []
            for i in range(1, len(usage_times)):
                interval = usage_times[i] - usage_times[i-1]
                intervals.append(interval.total_seconds() / 3600)  # Convert to hours
            avg_interval = sum(intervals) / len(intervals)
        else:
            avg_interval = 0
        
        analysis[bike_id] = {
            'usage_count': usage_count,
            'first_used': first_used.strftime('%Y-%m-%d %H:%M:%S'),
            'last_used': last_used.strftime('%Y-%m-%d %H:%M:%S'),
            'total_duration_days': total_duration.days,
            'avg_interval_hours': round(avg_interval, 2) if avg_interval > 0 else 0,
            'usage_frequency': 'High' if usage_count >= 3 else 'Medium' if usage_count == 2 else 'Low'
        }
    
    return analysis

def create_extended_queries():
    """
    Additional useful queries for bike usage analysis.
    """
    
    queries = {
        # Find bikes used multiple times
        "multiple_usage": """
        SELECT 
            bike_id,
            COUNT(*) as usage_count,
            MIN(last_used) as first_used,
            MAX(last_used) as last_used
        FROM Bikes
        GROUP BY bike_id
        HAVING COUNT(*) > 1
        ORDER BY usage_count DESC, bike_id;
        """,
        
        # Find most recently used bikes
        "most_recent": """
        SELECT 
            bike_id,
            MAX(last_used) as last_used
        FROM Bikes
        GROUP BY bike_id
        ORDER BY MAX(last_used) DESC
        LIMIT 5;
        """,
        
        # Usage by day
        "usage_by_day": """
        SELECT 
            DATE(last_used) as usage_date,
            COUNT(DISTINCT bike_id) as unique_bikes_used,
            COUNT(*) as total_usages
        FROM Bikes
        GROUP BY DATE(last_used)
        ORDER BY usage_date;
        """,
        
        # Bikes with usage gaps
        "usage_gaps": """
        WITH bike_usage_ranked AS (
            SELECT 
                bike_id,
                last_used,
                LAG(last_used) OVER (PARTITION BY bike_id ORDER BY last_used) as prev_used
            FROM Bikes
        )
        SELECT 
            bike_id,
            last_used,
            prev_used,
            TIMESTAMPDIFF(HOUR, prev_used, last_used) as hours_gap
        FROM bike_usage_ranked
        WHERE prev_used IS NOT NULL
        AND TIMESTAMPDIFF(HOUR, prev_used, last_used) > 24
        ORDER BY bike_id, last_used;
        """
    }
    
    return queries

# Test Cases
if __name__ == "__main__":
    # Test data from the example
    test_data = [
        ('W00576', '2012-03-25 11:30:00'),
        ('W00300', '2012-03-25 10:30:00'),
        ('W00455', '2012-03-26 14:30:00'),
        ('W00576', '2012-03-25 12:30:00'),
        ('W00576', '2012-03-25 13:30:00')
    ]
    
    expected_result = [
        ('W00300', '2012-03-25 10:30:00'),
        ('W00455', '2012-03-26 14:30:00'),
        ('W00576', '2012-03-25 13:30:00')
    ]
    
    print("Testing Python simulation:")
    result = bikes_last_time_used(test_data)
    print("Result:", result)
    print("Expected:", expected_result)
    print("Match:", result == expected_result)
    
    print("\nMain SQL Solution:")
    print(create_sql_solution())
    
    print("\nAlternative SQL Solutions:")
    alternatives = create_alternative_sql_solutions()
    for name, query in alternatives.items():
        print(f"\n{name.replace('_', ' ').title()}:")
        print(query)
    
    print("\nBike Usage Pattern Analysis:")
    analysis = analyze_bike_usage_patterns(test_data)
    for bike_id, stats in analysis.items():
        print(f"Bike {bike_id}: {stats}")
    
    print("\nExtended Analysis Queries:")
    extended_queries = create_extended_queries()
    for name, query in extended_queries.items():
        print(f"\n{name.replace('_', ' ').title()}:")
        print(query)
    
    # Additional test cases
    print("\nAdditional Test Cases:")
    
    # Single usage per bike
    test_single_usage = [
        ('B001', '2012-03-25 10:00:00'),
        ('B002', '2012-03-25 11:00:00'),
        ('B003', '2012-03-25 12:00:00')
    ]
    
    result_single = bikes_last_time_used(test_single_usage)
    print("Single usage per bike:", result_single)
    
    # Same bike, same time (edge case)
    test_same_time = [
        ('B001', '2012-03-25 10:00:00'),
        ('B001', '2012-03-25 10:00:00'),
        ('B002', '2012-03-25 11:00:00')
    ]
    
    result_same_time = bikes_last_time_used(test_same_time)
    print("Same time usage:", result_same_time)

"""
Time and Space Complexity Analysis:

Python Simulation:
Time Complexity: O(n log k) - where n is number of records, k is number of unique bikes
Space Complexity: O(k) - storing latest time for each unique bike

SQL Query (GROUP BY + MAX):
Time Complexity: O(n log k) - GROUP BY operation with sorting
Space Complexity: O(k) - intermediate grouping results

Window Function Approach:
Time Complexity: O(n log n) - sorting within each partition
Space Complexity: O(n) - window function overhead

Correlated Subquery:
Time Complexity: O(n²) - subquery executed for each row
Space Complexity: O(1) - no additional storage needed

Key SQL Concepts:
1. GROUP BY with aggregate functions (MAX)
2. Window functions (FIRST_VALUE, ROW_NUMBER, RANK)
3. Correlated subqueries for row-by-row comparison
4. ORDER BY for result sorting
5. DISTINCT for eliminating duplicates

Performance Considerations:
- GROUP BY + MAX is typically most efficient
- Window functions good for complex requirements
- Correlated subqueries can be slow on large datasets
- Proper indexing on (bike_id, last_used) recommended

Business Applications:
- Fleet management and maintenance scheduling
- Usage pattern analysis for bike sharing
- Predictive maintenance based on usage frequency
- Customer behavior analysis
- Resource allocation optimization

Advanced Analytics:
- Usage frequency classification
- Idle time analysis
- Peak usage periods identification
- Bike lifecycle management
- Demand forecasting

Topic: SQL, Database Queries, Aggregation, Window Functions, Time Series Analysis
"""
