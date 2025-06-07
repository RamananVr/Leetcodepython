"""
LeetCode Question #2686: Immediate Food Delivery III

Problem Statement:
Table: Delivery
+-----------------------------+
| Column Name                 | Type    |
+-----------------------------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+
delivery_id is the primary key of this table.
The table holds information about food delivery to customers that made orders at some date and have a preference for their delivery date (either immediate or scheduled).

If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

Write an SQL query to find the percentage of immediate orders on each unique order_date, rounded to 2 decimal places.

Return the result table ordered by order_date in ascending order.

Examples:
Example 1:
Input: 
Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 2           | 2019-08-01 | 2019-08-01                  |
| 3           | 3           | 2019-08-01 | 2019-08-01                  |
| 4           | 4           | 2019-08-02 | 2019-08-02                  |
| 5           | 5           | 2019-08-02 | 2019-08-03                  |
| 6           | 6           | 2019-08-02 | 2019-08-02                  |
| 7           | 7           | 2019-08-03 | 2019-08-03                  |
+-------------+-------------+------------+-----------------------------+

Output: 
+------------+----------------------+
| order_date | immediate_percentage |
+------------+----------------------+
| 2019-08-01 | 66.67                |
| 2019-08-02 | 66.67                |
| 2019-08-03 | 100.00               |
+------------+----------------------+

Explanation: 
- On 2019-08-01 there were 3 orders, 2 of them were immediate, so percentage = 2/3 * 100 = 66.67
- On 2019-08-02 there were 3 orders, 2 of them were immediate, so percentage = 2/3 * 100 = 66.67
- On 2019-08-03 there was 1 order, 1 of them was immediate, so percentage = 1/1 * 100 = 100.00

Constraints:
- 1 <= delivery_id <= 500
- 1 <= customer_id <= 100
- order_date and customer_pref_delivery_date are valid dates between 2019-01-01 and 2019-12-31.
"""

# This is a SQL problem, but we'll provide Python simulation and SQL solutions

def immediate_food_delivery_iii(delivery_data):
    """
    Python simulation of the SQL query.
    
    Args:
        delivery_data: List of tuples (delivery_id, customer_id, order_date, customer_pref_delivery_date)
    
    Returns:
        List of tuples (order_date, immediate_percentage)
    """
    from collections import defaultdict
    from datetime import datetime
    
    # Group by order_date
    date_stats = defaultdict(lambda: {'total': 0, 'immediate': 0})
    
    for delivery_id, customer_id, order_date, pref_date in delivery_data:
        # Convert string dates to datetime objects if needed
        if isinstance(order_date, str):
            order_date = datetime.strptime(order_date, '%Y-%m-%d').date()
        if isinstance(pref_date, str):
            pref_date = datetime.strptime(pref_date, '%Y-%m-%d').date()
        
        date_stats[order_date]['total'] += 1
        if order_date == pref_date:
            date_stats[order_date]['immediate'] += 1
    
    # Calculate percentages
    result = []
    for order_date in sorted(date_stats.keys()):
        stats = date_stats[order_date]
        percentage = (stats['immediate'] / stats['total']) * 100
        result.append((order_date.strftime('%Y-%m-%d'), round(percentage, 2)))
    
    return result

def create_sql_solution():
    """
    Returns the SQL solution for the problem.
    """
    sql_query = """
    SELECT 
        order_date,
        ROUND(
            (SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100.0) 
            / COUNT(*), 
            2
        ) AS immediate_percentage
    FROM Delivery
    GROUP BY order_date
    ORDER BY order_date;
    """
    return sql_query

def create_alternative_sql_solutions():
    """
    Alternative SQL approaches.
    """
    
    # Solution 1: Using AVG with CASE
    solution1 = """
    SELECT 
        order_date,
        ROUND(
            AVG(CASE WHEN order_date = customer_pref_delivery_date THEN 100.0 ELSE 0.0 END), 
            2
        ) AS immediate_percentage
    FROM Delivery
    GROUP BY order_date
    ORDER BY order_date;
    """
    
    # Solution 2: Using subquery
    solution2 = """
    SELECT 
        order_date,
        ROUND(
            (immediate_count * 100.0) / total_count,
            2
        ) AS immediate_percentage
    FROM (
        SELECT 
            order_date,
            COUNT(*) as total_count,
            SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) as immediate_count
        FROM Delivery
        GROUP BY order_date
    ) AS stats
    ORDER BY order_date;
    """
    
    # Solution 3: Using window functions
    solution3 = """
    SELECT DISTINCT
        order_date,
        ROUND(
            (SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) 
             OVER (PARTITION BY order_date) * 100.0) 
            / COUNT(*) OVER (PARTITION BY order_date),
            2
        ) AS immediate_percentage
    FROM Delivery
    ORDER BY order_date;
    """
    
    return {
        "avg_case": solution1,
        "subquery": solution2,
        "window_function": solution3
    }

def analyze_delivery_patterns(delivery_data):
    """
    Additional analysis of delivery patterns.
    """
    from collections import defaultdict, Counter
    
    # Customer analysis
    customer_preferences = defaultdict(lambda: {'immediate': 0, 'scheduled': 0})
    date_patterns = Counter()
    
    for delivery_id, customer_id, order_date, pref_date in delivery_data:
        if isinstance(order_date, str):
            from datetime import datetime
            order_date = datetime.strptime(order_date, '%Y-%m-%d').date()
            pref_date = datetime.strptime(pref_date, '%Y-%m-%d').date()
        
        if order_date == pref_date:
            customer_preferences[customer_id]['immediate'] += 1
            date_patterns[order_date] += 1
        else:
            customer_preferences[customer_id]['scheduled'] += 1
    
    # Calculate customer preference ratios
    customer_analysis = {}
    for customer_id, prefs in customer_preferences.items():
        total = prefs['immediate'] + prefs['scheduled']
        immediate_ratio = prefs['immediate'] / total if total > 0 else 0
        customer_analysis[customer_id] = {
            'total_orders': total,
            'immediate_ratio': immediate_ratio,
            'preference': 'immediate' if immediate_ratio >= 0.5 else 'scheduled'
        }
    
    return {
        'customer_analysis': customer_analysis,
        'popular_immediate_dates': date_patterns.most_common()
    }

# Test Cases
if __name__ == "__main__":
    # Test data from the example
    test_data = [
        (1, 1, '2019-08-01', '2019-08-02'),
        (2, 2, '2019-08-01', '2019-08-01'),
        (3, 3, '2019-08-01', '2019-08-01'),
        (4, 4, '2019-08-02', '2019-08-02'),
        (5, 5, '2019-08-02', '2019-08-03'),
        (6, 6, '2019-08-02', '2019-08-02'),
        (7, 7, '2019-08-03', '2019-08-03')
    ]
    
    expected_result = [
        ('2019-08-01', 66.67),
        ('2019-08-02', 66.67),
        ('2019-08-03', 100.00)
    ]
    
    print("Testing Python simulation:")
    result = immediate_food_delivery_iii(test_data)
    print("Result:", result)
    print("Expected:", expected_result)
    print("Match:", result == expected_result)
    
    print("\nSQL Solution:")
    print(create_sql_solution())
    
    print("\nAlternative SQL Solutions:")
    alternatives = create_alternative_sql_solutions()
    for name, query in alternatives.items():
        print(f"\n{name.replace('_', ' ').title()}:")
        print(query)
    
    print("\nDelivery Pattern Analysis:")
    analysis = analyze_delivery_patterns(test_data)
    print("Customer Analysis:", analysis['customer_analysis'])
    print("Popular Immediate Dates:", analysis['popular_immediate_dates'])
    
    # Additional test cases
    print("\nAdditional Test Cases:")
    
    # All immediate orders
    test_all_immediate = [
        (1, 1, '2019-08-01', '2019-08-01'),
        (2, 2, '2019-08-01', '2019-08-01'),
        (3, 3, '2019-08-02', '2019-08-02')
    ]
    
    result_all_immediate = immediate_food_delivery_iii(test_all_immediate)
    print("All immediate orders:", result_all_immediate)
    
    # All scheduled orders
    test_all_scheduled = [
        (1, 1, '2019-08-01', '2019-08-02'),
        (2, 2, '2019-08-01', '2019-08-03'),
        (3, 3, '2019-08-02', '2019-08-04')
    ]
    
    result_all_scheduled = immediate_food_delivery_iii(test_all_scheduled)
    print("All scheduled orders:", result_all_scheduled)

"""
Time and Space Complexity Analysis:

Python Simulation:
Time Complexity: O(n log n) - where n is number of deliveries (due to sorting)
Space Complexity: O(d) - where d is number of distinct order dates

SQL Query:
Time Complexity: O(n log n) - GROUP BY and ORDER BY operations
Space Complexity: O(d) - intermediate grouping results

Key SQL Concepts:
1. GROUP BY for aggregating data by order_date
2. CASE WHEN for conditional counting
3. Aggregate functions (COUNT, SUM, AVG)
4. ROUND for formatting decimal places
5. ORDER BY for result sorting

Alternative Approaches:
1. Using AVG with CASE - more concise but same logic
2. Subquery approach - separates calculation steps
3. Window functions - useful for more complex analytics

Business Insights:
- Immediate delivery preference indicates customer urgency
- Date patterns can reveal business trends
- Customer behavior analysis for targeted marketing
- Operational planning based on delivery preferences

SQL Best Practices:
- Use meaningful column aliases
- Handle division by zero (though not needed here due to GROUP BY)
- Consider indexing on order_date for performance
- Use appropriate data types for dates

Topic: SQL, Database Queries, Aggregation, Percentage Calculations, Date Analysis
"""
