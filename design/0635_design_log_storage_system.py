"""
LeetCode Question #635: Design Log Storage System

Problem Statement:
You are given several logs, where each log contains a unique ID and a timestamp. 
Timestamp is a string that has the following format: "Year:Month:Day:Hour:Minute:Second", 
for example, "2017:01:01:23:59:59". All domains are zero-padded decimal numbers.

Implement the LogSystem class:
1. LogSystem() Initializes the LogSystem object.
2. void put(int id, string timestamp) Stores the given log (id, timestamp) in the system.
3. List<Integer> retrieve(string start, string end, string granularity) Returns the IDs of all logs 
   whose timestamps are within the range from start to end inclusive. The granularity parameter 
   (e.g., "Year", "Month", "Day", etc.) determines the level of precision for the comparison. 
   For example, if granularity is "Year", consider only the year when comparing timestamps.

Granularity levels are:
- "Year": Consider only the year (e.g., "2017").
- "Month": Consider up to the month (e.g., "2017:01").
- "Day": Consider up to the day (e.g., "2017:01:01").
- "Hour": Consider up to the hour (e.g., "2017:01:01:23").
- "Minute": Consider up to the minute (e.g., "2017:01:01:23:59").
- "Second": Consider the entire timestamp (e.g., "2017:01:01:23:59:59").

Constraints:
- 1 <= id <= 500
- The timestamp follows the format "Year:Month:Day:Hour:Minute:Second".
- All timestamps are unique.
- The range of years is [2000, 2017].
- The retrieve method will be called at most 10,000 times.

"""

class LogSystem:
    def __init__(self):
        # Initialize a list to store logs as (id, timestamp) tuples
        self.logs = []
        # Define the granularity mapping to the number of characters to consider
        self.granularity_map = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19
        }

    def put(self, id: int, timestamp: str) -> None:
        # Append the log as a tuple (id, timestamp) to the logs list
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> list:
        # Determine the number of characters to consider based on granularity
        granularity_length = self.granularity_map[granularity]
        # Truncate the start and end timestamps to the required granularity
        start = start[:granularity_length]
        end = end[:granularity_length]
        # Filter and return the IDs of logs within the range
        return [
            log_id
            for log_id, timestamp in self.logs
            if start <= timestamp[:granularity_length] <= end
        ]


# Example Test Cases
if __name__ == "__main__":
    # Initialize the LogSystem
    log_system = LogSystem()

    # Add logs
    log_system.put(1, "2017:01:01:23:59:59")
    log_system.put(2, "2017:01:01:22:59:59")
    log_system.put(3, "2016:01:01:00:00:00")

    # Retrieve logs with different granularities
    print(log_system.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"))  # Output: [1, 2, 3]
    print(log_system.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"))  # Output: [2]
    print(log_system.retrieve("2017:01:01:23:59:59", "2017:01:01:23:59:59", "Second"))  # Output: [1]

"""
Time and Space Complexity Analysis:

1. put() Method:
   - Time Complexity: O(1), as appending to a list is an O(1) operation.
   - Space Complexity: O(1), as no additional space is used apart from storing the log.

2. retrieve() Method:
   - Time Complexity: O(n), where n is the number of logs stored. This is because we iterate through all logs to filter the relevant ones.
   - Space Complexity: O(k), where k is the number of logs that match the criteria, as we store their IDs in the result list.

Overall:
- Time Complexity: O(n) for retrieve, O(1) for put.
- Space Complexity: O(n) for storing logs, O(k) for the result of retrieve.

Topic: Design
"""