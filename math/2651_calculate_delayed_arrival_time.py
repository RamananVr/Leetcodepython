"""
LeetCode Problem #2651: Calculate Delayed Arrival Time

Problem Statement:
You are given a positive integer arrivalTime denoting the arrival time of a train in hours, and another positive integer delayedTime denoting the amount of delay in hours.

Return the time when the train will arrive at the station.

Note that the time in this problem is in 24-hour format.

Example 1:
Input: arrivalTime = 15, delayedTime = 5
Output: 20
Explanation: Arrival time of the train was 15:00 hours. It is delayed by 5 hours. So it will reach at 15:00 + 5:00 = 20:00 hours.

Example 2:
Input: arrivalTime = 13, delayedTime = 11
Output: 0
Explanation: Arrival time of the train was 13:00 hours. It is delayed by 11 hours. So it will reach at 13:00 + 11:00 = 24:00 hours. Since the time is in 24-hour format, 24:00 hours is represented as 00:00 hours.

Example 3:
Input: arrivalTime = 23, delayedTime = 5
Output: 4
Explanation: Arrival time of the train was 23:00 hours. It is delayed by 5 hours. So it will reach at 23:00 + 5:00 = 28:00 hours. Since the time is in 24-hour format, 28:00 hours is represented as 04:00 hours.

Constraints:
- 1 <= arrivalTime <= 23
- 1 <= delayedTime <= 24
"""

def findDelayedArrivalTime(arrivalTime: int, delayedTime: int) -> int:
    """
    Calculate the delayed arrival time in 24-hour format.
    
    Args:
        arrivalTime: Original arrival time (0-23)
        delayedTime: Delay amount in hours
        
    Returns:
        int: Delayed arrival time in 24-hour format (0-23)
    """
    return (arrivalTime + delayedTime) % 24

def findDelayedArrivalTimeAlternative(arrivalTime: int, delayedTime: int) -> int:
    """
    Alternative implementation with explicit overflow handling
    """
    total_time = arrivalTime + delayedTime
    
    # Handle 24-hour format wraparound
    if total_time >= 24:
        return total_time - 24
    else:
        return total_time

def findDelayedArrivalTimeVerbose(arrivalTime: int, delayedTime: int) -> int:
    """
    Verbose implementation showing step-by-step calculation
    """
    # Calculate total time
    total_hours = arrivalTime + delayedTime
    
    # Convert to 24-hour format
    # If total_hours >= 24, we need to wrap around
    delayed_arrival = total_hours % 24
    
    return delayed_arrival

def findDelayedArrivalTimeWithValidation(arrivalTime: int, delayedTime: int) -> int:
    """
    Implementation with input validation
    """
    # Validate inputs
    if not (1 <= arrivalTime <= 23):
        raise ValueError("arrivalTime must be between 1 and 23")
    if not (1 <= delayedTime <= 24):
        raise ValueError("delayedTime must be between 1 and 24")
    
    return (arrivalTime + delayedTime) % 24

def findDelayedArrivalTimeMultipleDays(arrivalTime: int, delayedTime: int) -> tuple:
    """
    Enhanced version that returns both delayed time and number of days passed
    """
    total_hours = arrivalTime + delayedTime
    days_passed = total_hours // 24
    delayed_arrival = total_hours % 24
    
    return delayed_arrival, days_passed

def findDelayedArrivalTimeString(arrivalTime: int, delayedTime: int) -> str:
    """
    Version that returns formatted time string
    """
    delayed_hour = (arrivalTime + delayedTime) % 24
    return f"{delayed_hour:02d}:00"

class TrainSchedule:
    """
    Class to handle multiple train schedules and delays
    """
    
    def __init__(self):
        self.trains = {}
    
    def add_train(self, train_id: str, arrival_time: int):
        """Add a train to the schedule"""
        self.trains[train_id] = arrival_time
    
    def calculate_delayed_arrival(self, train_id: str, delay: int) -> int:
        """Calculate delayed arrival for a specific train"""
        if train_id not in self.trains:
            raise ValueError(f"Train {train_id} not found")
        
        original_time = self.trains[train_id]
        return (original_time + delay) % 24
    
    def get_all_delayed_arrivals(self, delay: int) -> dict:
        """Calculate delayed arrivals for all trains"""
        return {
            train_id: (arrival_time + delay) % 24
            for train_id, arrival_time in self.trains.items()
        }

def simulateMultipleDelays(arrivalTime: int, delays: list) -> list:
    """
    Simulate multiple consecutive delays
    """
    current_time = arrivalTime
    results = []
    
    for delay in delays:
        current_time = (current_time + delay) % 24
        results.append(current_time)
    
    return results

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic case without overflow
    print("Test Case 1: No time overflow")
    arrivalTime1, delayedTime1 = 15, 5
    result1 = findDelayedArrivalTime(arrivalTime1, delayedTime1)
    print(f"Arrival: {arrivalTime1}, Delay: {delayedTime1}, Result: {result1}")  # Expected: 20
    
    # Test Case 2: Exactly 24 hours (midnight)
    print("\nTest Case 2: Exactly midnight")
    arrivalTime2, delayedTime2 = 13, 11
    result2 = findDelayedArrivalTime(arrivalTime2, delayedTime2)
    print(f"Arrival: {arrivalTime2}, Delay: {delayedTime2}, Result: {result2}")  # Expected: 0
    
    # Test Case 3: Time overflow
    print("\nTest Case 3: Time overflow")
    arrivalTime3, delayedTime3 = 23, 5
    result3 = findDelayedArrivalTime(arrivalTime3, delayedTime3)
    print(f"Arrival: {arrivalTime3}, Delay: {delayedTime3}, Result: {result3}")  # Expected: 4
    
    # Test Case 4: Maximum delay
    print("\nTest Case 4: Maximum delay")
    arrivalTime4, delayedTime4 = 1, 24
    result4 = findDelayedArrivalTime(arrivalTime4, delayedTime4)
    print(f"Arrival: {arrivalTime4}, Delay: {delayedTime4}, Result: {result4}")  # Expected: 1
    
    # Test Case 5: Minimum values
    print("\nTest Case 5: Minimum values")
    arrivalTime5, delayedTime5 = 1, 1
    result5 = findDelayedArrivalTime(arrivalTime5, delayedTime5)
    print(f"Arrival: {arrivalTime5}, Delay: {delayedTime5}, Result: {result5}")  # Expected: 2
    
    # Test Case 6: Alternative implementations comparison
    print("\nTest Case 6: Compare implementations")
    test_cases = [(15, 5), (13, 11), (23, 5), (22, 3), (10, 15)]
    
    for arrival, delay in test_cases:
        result_main = findDelayedArrivalTime(arrival, delay)
        result_alt = findDelayedArrivalTimeAlternative(arrival, delay)
        result_verbose = findDelayedArrivalTimeVerbose(arrival, delay)
        
        print(f"Arrival: {arrival}, Delay: {delay}")
        print(f"  Main: {result_main}, Alt: {result_alt}, Verbose: {result_verbose}")
        assert result_main == result_alt == result_verbose, "Results don't match!"
    
    # Test Case 7: Enhanced features
    print("\nTest Case 7: Enhanced features")
    arrival7, delay7 = 20, 15
    time_and_days = findDelayedArrivalTimeMultipleDays(arrival7, delay7)
    time_string = findDelayedArrivalTimeString(arrival7, delay7)
    print(f"Arrival: {arrival7}, Delay: {delay7}")
    print(f"  Time and days: {time_and_days}")  # (11, 1)
    print(f"  Formatted time: {time_string}")  # "11:00"
    
    # Test Case 8: Train schedule class
    print("\nTest Case 8: Train schedule management")
    schedule = TrainSchedule()
    schedule.add_train("Express101", 14)
    schedule.add_train("Local202", 18)
    schedule.add_train("Night303", 22)
    
    delay_hours = 6
    all_delays = schedule.get_all_delayed_arrivals(delay_hours)
    print(f"All trains with {delay_hours}h delay: {all_delays}")
    
    # Test Case 9: Multiple consecutive delays
    print("\nTest Case 9: Multiple consecutive delays")
    initial_arrival = 10
    consecutive_delays = [2, 3, 8, 5]
    multiple_results = simulateMultipleDelays(initial_arrival, consecutive_delays)
    print(f"Initial arrival: {initial_arrival}")
    print(f"Consecutive delays: {consecutive_delays}")
    print(f"Results after each delay: {multiple_results}")
    
    # Test Case 10: Edge cases
    print("\nTest Case 10: Edge cases")
    edge_cases = [
        (23, 1),   # Late night with small delay
        (1, 23),   # Early morning with large delay
        (12, 12),  # Noon with 12-hour delay
        (23, 24),  # Latest time with max delay
    ]
    
    for arrival, delay in edge_cases:
        result = findDelayedArrivalTime(arrival, delay)
        print(f"Arrival: {arrival:2d}, Delay: {delay:2d}, Result: {result:2d}")

"""
Time and Space Complexity Analysis:

Time Complexity:
- findDelayedArrivalTime(): O(1) - simple arithmetic and modulo operation
- All alternative implementations: O(1) - constant time operations
- Class operations: O(1) for single train, O(n) for all trains where n is number of trains
- Multiple delays simulation: O(k) where k is number of delays

Space Complexity:
- All main functions: O(1) - only using constant extra space
- TrainSchedule class: O(n) where n is number of trains stored
- Multiple delays: O(k) for storing results where k is number of delays

The problem is fundamentally simple requiring only modular arithmetic.
The modulo operation (%) handles the 24-hour format wraparound elegantly.

Key insights:
1. 24-hour format naturally maps to modulo 24 arithmetic
2. Any time >= 24 wraps around to 0-23 range
3. The operation is commutative: (a + b) % 24 = ((a % 24) + (b % 24)) % 24

Topic: Mathematics, Modular Arithmetic, Time Calculation
"""
