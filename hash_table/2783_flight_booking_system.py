"""
LeetCode Problem 2783: Flight Booking System

You are implementing a flight booking system. You are given an integer n representing the number of flights numbered from 1 to n.

You have the following operations:
- book(flightNumber, passenger): Book passenger on the given flight
- cancel(flightNumber, passenger): Cancel booking for passenger on the given flight
- getBookings(flightNumber): Return the list of passengers booked on the flight

Constraints:
- 1 <= n <= 10^5
- 1 <= flightNumber <= n
- 1 <= passenger <= 10^6
- At most 2 * 10^4 calls will be made to book, cancel, and getBookings

Example:
Input: n = 3
["book", 1, 101], ["book", 1, 102], ["book", 2, 101], ["getBookings", 1], ["cancel", 1, 101], ["getBookings", 1]
Output: [null, null, null, [101, 102], null, [102]]
"""

class FlightBookingSystem:
    """
    Optimized Flight Booking System using Hash Map
    
    Time Complexity:
    - book: O(1)
    - cancel: O(1) 
    - getBookings: O(k) where k is number of passengers on flight
    
    Space Complexity: O(total_bookings)
    """
    
    def __init__(self, n):
        self.n = n
        # flight_number -> set of passengers
        self.bookings = {}
    
    def book(self, flight_number, passenger):
        """Book a passenger on the given flight"""
        if flight_number < 1 or flight_number > self.n:
            return False
        
        if flight_number not in self.bookings:
            self.bookings[flight_number] = set()
        
        self.bookings[flight_number].add(passenger)
        return True
    
    def cancel(self, flight_number, passenger):
        """Cancel booking for passenger on the given flight"""
        if flight_number < 1 or flight_number > self.n:
            return False
        
        if flight_number in self.bookings:
            self.bookings[flight_number].discard(passenger)
            # Clean up empty flights
            if not self.bookings[flight_number]:
                del self.bookings[flight_number]
            return True
        
        return False
    
    def get_bookings(self, flight_number):
        """Get all passengers booked on the flight"""
        if flight_number < 1 or flight_number > self.n:
            return []
        
        if flight_number in self.bookings:
            return sorted(list(self.bookings[flight_number]))
        
        return []
    
    def get_flight_count(self, flight_number):
        """Get number of passengers on flight"""
        if flight_number in self.bookings:
            return len(self.bookings[flight_number])
        return 0
    
    def get_total_bookings(self):
        """Get total number of bookings across all flights"""
        return sum(len(passengers) for passengers in self.bookings.values())

# Alternative implementation with detailed tracking
class DetailedFlightBookingSystem:
    """
    Alternative implementation with passenger details tracking
    """
    
    def __init__(self, n):
        self.n = n
        self.flight_passengers = {}  # flight -> {passenger: booking_time}
        self.passenger_flights = {}  # passenger -> {flight: booking_time}
        self.booking_counter = 0
    
    def book(self, flight_number, passenger):
        if flight_number < 1 or flight_number > self.n:
            return False
        
        # Initialize if needed
        if flight_number not in self.flight_passengers:
            self.flight_passengers[flight_number] = {}
        if passenger not in self.passenger_flights:
            self.passenger_flights[passenger] = {}
        
        # Book the flight
        self.booking_counter += 1
        self.flight_passengers[flight_number][passenger] = self.booking_counter
        self.passenger_flights[passenger][flight_number] = self.booking_counter
        
        return True
    
    def cancel(self, flight_number, passenger):
        if (flight_number in self.flight_passengers and 
            passenger in self.flight_passengers[flight_number]):
            
            del self.flight_passengers[flight_number][passenger]
            del self.passenger_flights[passenger][flight_number]
            
            # Clean up empty entries
            if not self.flight_passengers[flight_number]:
                del self.flight_passengers[flight_number]
            if not self.passenger_flights[passenger]:
                del self.passenger_flights[passenger]
            
            return True
        
        return False
    
    def get_bookings(self, flight_number):
        if flight_number in self.flight_passengers:
            # Return passengers sorted by booking time
            passengers_with_time = [
                (time, passenger) 
                for passenger, time in self.flight_passengers[flight_number].items()
            ]
            return [passenger for time, passenger in sorted(passengers_with_time)]
        return []
    
    def get_passenger_flights(self, passenger):
        """Get all flights for a passenger"""
        if passenger in self.passenger_flights:
            return list(self.passenger_flights[passenger].keys())
        return []

# Test cases
def test_flight_booking_system():
    print("Testing Flight Booking System:")
    
    # Test basic functionality
    fbs = FlightBookingSystem(3)
    
    # Test booking
    print(f"Book flight 1, passenger 101: {fbs.book(1, 101)}")
    print(f"Book flight 1, passenger 102: {fbs.book(1, 102)}")
    print(f"Book flight 2, passenger 101: {fbs.book(2, 101)}")
    
    # Test getting bookings
    print(f"Bookings for flight 1: {fbs.get_bookings(1)}")
    print(f"Bookings for flight 2: {fbs.get_bookings(2)}")
    print(f"Bookings for flight 3: {fbs.get_bookings(3)}")
    
    # Test cancellation
    print(f"Cancel flight 1, passenger 101: {fbs.cancel(1, 101)}")
    print(f"Bookings for flight 1 after cancellation: {fbs.get_bookings(1)}")
    
    # Test edge cases
    print(f"Book invalid flight 0: {fbs.book(0, 101)}")
    print(f"Book invalid flight 4: {fbs.book(4, 101)}")
    print(f"Cancel non-existent booking: {fbs.cancel(1, 999)}")
    
    print(f"Total bookings: {fbs.get_total_bookings()}")
    
    print("\n" + "="*50)
    
    # Test detailed system
    print("Testing Detailed Flight Booking System:")
    dfbs = DetailedFlightBookingSystem(2)
    
    dfbs.book(1, 201)
    dfbs.book(1, 202)
    dfbs.book(2, 201)
    
    print(f"Flight 1 bookings: {dfbs.get_bookings(1)}")
    print(f"Passenger 201 flights: {dfbs.get_passenger_flights(201)}")
    
    dfbs.cancel(1, 201)
    print(f"Flight 1 bookings after cancel: {dfbs.get_bookings(1)}")
    print(f"Passenger 201 flights after cancel: {dfbs.get_passenger_flights(201)}")

if __name__ == "__main__":
    test_flight_booking_system()

"""
Topics: Hash Map, Design, System Design
Difficulty: Medium

Key Insights:
1. Use hash map for O(1) book/cancel operations
2. Set data structure prevents duplicate bookings
3. Clean up empty flights to save memory
4. Return sorted passenger list for consistency
5. Can extend with booking timestamps and detailed tracking

Companies: Booking.com, Expedia, Airbnb, Airlines
"""
