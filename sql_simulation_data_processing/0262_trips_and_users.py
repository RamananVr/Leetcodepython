"""
LeetCode Question #262: Trips and Users

Problem Statement:
The `Trips` table holds all taxi trips. Each trip has a unique Id, while `Client_Id` and `Driver_Id` are both foreign keys referencing the `Users` table. `Status` is an ENUM type with values ('completed', 'cancelled', 'ongoing'). `Request_at` is the day the trip was requested.

The `Users` table holds all users. Each user has a unique `Users_Id`, and `Banned` is an ENUM type with values ('Yes', 'No').

Write an SQL query to find the cancellation rate of requests made by unbanned users between "2013-10-01" and "2013-10-03". The cancellation rate is defined as the number of trips with `Status = 'cancelled'` divided by the total number of trips in the specified period.

Return the result table with a single column named `Cancellation Rate`.

Note: This problem is SQL-based, but for the sake of this Python implementation, we will simulate the solution using Python.

Python Solution:
Since this problem is SQL-based, we will simulate the solution using Python by processing the data in a tabular format (e.g., using pandas).
"""

import pandas as pd

# Simulated data for Trips table
trips_data = [
    {"Id": 1, "Client_Id": 1, "Driver_Id": 10, "Status": "completed", "Request_at": "2013-10-01"},
    {"Id": 2, "Client_Id": 2, "Driver_Id": 11, "Status": "cancelled", "Request_at": "2013-10-01"},
    {"Id": 3, "Client_Id": 3, "Driver_Id": 12, "Status": "completed", "Request_at": "2013-10-02"},
    {"Id": 4, "Client_Id": 4, "Driver_Id": 13, "Status": "cancelled", "Request_at": "2013-10-02"},
    {"Id": 5, "Client_Id": 5, "Driver_Id": 14, "Status": "completed", "Request_at": "2013-10-03"},
    {"Id": 6, "Client_Id": 6, "Driver_Id": 15, "Status": "cancelled", "Request_at": "2013-10-03"},
]

# Simulated data for Users table
users_data = [
    {"Users_Id": 1, "Banned": "No"},
    {"Users_Id": 2, "Banned": "No"},
    {"Users_Id": 3, "Banned": "No"},
    {"Users_Id": 4, "Banned": "Yes"},
    {"Users_Id": 5, "Banned": "No"},
    {"Users_Id": 6, "Banned": "No"},
]

# Convert data to pandas DataFrames
trips_df = pd.DataFrame(trips_data)
users_df = pd.DataFrame(users_data)

def calculate_cancellation_rate(trips_df, users_df, start_date, end_date):
    # Filter trips within the specified date range
    filtered_trips = trips_df[(trips_df["Request_at"] >= start_date) & (trips_df["Request_at"] <= end_date)]
    
    # Join trips with users to filter out banned users
    merged_df = filtered_trips.merge(users_df, left_on="Client_Id", right_on="Users_Id")
    unbanned_trips = merged_df[merged_df["Banned"] == "No"]
    
    # Calculate total trips and cancelled trips
    total_trips = len(unbanned_trips)
    cancelled_trips = len(unbanned_trips[unbanned_trips["Status"] == "cancelled"])
    
    # Calculate cancellation rate
    cancellation_rate = cancelled_trips / total_trips if total_trips > 0 else 0
    return round(cancellation_rate, 2)

# Example Test Cases
if __name__ == "__main__":
    start_date = "2013-10-01"
    end_date = "2013-10-03"
    result = calculate_cancellation_rate(trips_df, users_df, start_date, end_date)
    print(f"Cancellation Rate: {result}")  # Expected Output: 0.4

"""
Time and Space Complexity Analysis:
1. Time Complexity:
   - Filtering trips by date: O(n), where n is the number of rows in the Trips table.
   - Merging trips with users: O(n * m), where n is the number of rows in the Trips table and m is the number of rows in the Users table.
   - Filtering unbanned users: O(n).
   - Calculating cancellation rate: O(n).
   Overall: O(n * m), dominated by the merge operation.

2. Space Complexity:
   - Space required for the filtered and merged DataFrame: O(n + m).
   - Space required for intermediate computations: O(n).
   Overall: O(n + m).

Topic: SQL Simulation / Data Processing
"""