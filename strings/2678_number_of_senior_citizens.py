# filepath: q:\source\AgentGeneratedLeetcode\design\2678_number_of_senior_citizens.py
"""
LeetCode Question #2678: Number of Senior Citizens

Problem Statement:
You are given a 0-indexed array of strings details. Each element of details provides information about a given passenger compressed into a string of length 15. The system is such that:

- The first ten characters consist of the phone number of passengers.
- The next character denotes the gender of the person.
- The following two characters are used to indicate the age of the person.
- The last two characters determine the seat allotted to that person.

You are given that the passengers are senior citizens if their age is strictly greater than 60.

Return the number of passengers who are senior citizens.

Examples:
Example 1:
Input: details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
Output: 2
Explanation: The passengers at indices 0, 1, and 2 have ages 75, 92, and 40 respectively.
Since the ages of passengers at indices 0 and 1 are greater than 60, the answer is 2.

Example 2:
Input: details = ["1313579440F2036","2921522980M5644"]
Output: 0
Explanation: None of the passengers are senior citizens.

Constraints:
- 1 <= details.length <= 100
- details[i].length == 15
- details[i] consists of digits and an uppercase English letter.
- Each phone number consists of exactly 10 digits.
- Each age consists of exactly 2 digits and are a valid age.
- Each seat consists of exactly 2 digits.
"""

from typing import List

def countSeniors(details: List[str]) -> int:
    """
    Count passengers who are senior citizens (age > 60).
    
    Time: O(n) where n is the number of passengers
    Space: O(1) - only using constant extra space
    """
    count = 0
    
    for detail in details:
        # Extract age from positions 11-12 (0-indexed)
        age_str = detail[11:13]
        age = int(age_str)
        
        if age > 60:
            count += 1
    
    return count

def countSeniorsVerbose(details: List[str]) -> int:
    """
    Verbose version that extracts all components.
    
    Time: O(n)
    Space: O(1)
    """
    count = 0
    
    for detail in details:
        # Parse the detail string
        phone = detail[:10]          # Characters 0-9
        gender = detail[10]          # Character 10
        age_str = detail[11:13]      # Characters 11-12
        seat = detail[13:15]         # Characters 13-14
        
        age = int(age_str)
        
        # Check if senior citizen
        if age > 60:
            count += 1
    
    return count

def countSeniorsOneLinear(details: List[str]) -> int:
    """
    One-liner functional approach.
    
    Time: O(n)
    Space: O(1)
    """
    return sum(1 for detail in details if int(detail[11:13]) > 60)

def countSeniorsWithValidation(details: List[str]) -> int:
    """
    Version with input validation.
    
    Time: O(n)
    Space: O(1)
    """
    if not details:
        return 0
    
    count = 0
    
    for i, detail in enumerate(details):
        # Validate string length
        if len(detail) != 15:
            raise ValueError(f"Invalid detail string at index {i}: expected length 15, got {len(detail)}")
        
        try:
            # Extract and validate age
            age_str = detail[11:13]
            
            # Check if age characters are digits
            if not age_str.isdigit():
                raise ValueError(f"Invalid age format at index {i}: '{age_str}' is not numeric")
            
            age = int(age_str)
            
            # Validate age range (assuming reasonable age limits)
            if age < 0 or age > 120:
                raise ValueError(f"Invalid age at index {i}: {age} is out of reasonable range")
            
            if age > 60:
                count += 1
                
        except (ValueError, IndexError) as e:
            raise ValueError(f"Error processing detail at index {i}: {e}")
    
    return count

def countSeniorsWithBreakdown(details: List[str]) -> tuple:
    """
    Return count along with breakdown of all passengers.
    
    Time: O(n)
    Space: O(n) for breakdown storage
    """
    senior_count = 0
    breakdown = []
    
    for i, detail in enumerate(details):
        phone = detail[:10]
        gender = detail[10]
        age = int(detail[11:13])
        seat = detail[13:15]
        
        is_senior = age > 60
        if is_senior:
            senior_count += 1
        
        passenger_info = {
            "index": i,
            "phone": phone,
            "gender": gender,
            "age": age,
            "seat": seat,
            "is_senior": is_senior
        }
        breakdown.append(passenger_info)
    
    return senior_count, breakdown

def countSeniorsListComprehension(details: List[str]) -> int:
    """
    Using list comprehension approach.
    
    Time: O(n)
    Space: O(n) for intermediate list (can be optimized with generator)
    """
    ages = [int(detail[11:13]) for detail in details]
    return len([age for age in ages if age > 60])

def countSeniorsGenerator(details: List[str]) -> int:
    """
    Memory-efficient generator approach.
    
    Time: O(n)
    Space: O(1)
    """
    return sum(1 for detail in details if int(detail[11:13]) > 60)

# Test Cases
if __name__ == "__main__":
    test_cases = [
        (["7868190130M7522", "5303914400F9211", "9273338290F4010"], 2),
        (["1313579440F2036", "2921522980M5644"], 0),
        (["9751302862F0693", "3888560693F7262", "5485983835F0649", "2580974299F6042", "9976672161M6561", "0234451011F8013"], 4),
        (["1234567890M6100"], 0),  # Age exactly 61, should count
        (["1234567890M6101"], 1),  # Age 61, should count
        (["1234567890M5999"], 0),  # Age 59, should not count
        (["1234567890M0001"], 0),  # Age 0, should not count
        (["1234567890M9999"], 1),  # Age 99, should count
    ]
    
    print("Testing main approach:")
    for details, expected in test_cases:
        result = countSeniors(details)
        print(f"Details: {details}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing verbose approach:")
    for details, expected in test_cases:
        result = countSeniorsVerbose(details)
        print(f"Details: {details}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing one-liner approach:")
    for details, expected in test_cases:
        result = countSeniorsOneLinear(details)
        print(f"Details: {details}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing breakdown approach:")
    details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
    count, breakdown = countSeniorsWithBreakdown(details)
    print(f"Senior count: {count}")
    print("Passenger breakdown:")
    for passenger in breakdown:
        print(f"  Index {passenger['index']}: Age {passenger['age']}, Gender {passenger['gender']}, Senior: {passenger['is_senior']}")
    
    print("\nTesting validation:")
    try:
        countSeniorsWithValidation(["invalid_length"])
    except ValueError as e:
        print(f"Caught expected error: {e}")

"""
Time and Space Complexity Analysis:

All Main Approaches:
Time Complexity: O(n) where n is the number of passenger details
Space Complexity: O(1) - only using constant extra space for counting

Breakdown Approach:
Time Complexity: O(n) - single pass through details
Space Complexity: O(n) - storing breakdown information for each passenger

List Comprehension Approach:
Time Complexity: O(n) - creating intermediate list and filtering
Space Complexity: O(n) - intermediate list storage

Generator Approach:
Time Complexity: O(n) - single pass through details
Space Complexity: O(1) - no intermediate storage

Key Insights:
1. String slicing is used to extract specific information from fixed-format strings
2. The age is always at positions 11-12 (0-indexed) in the 15-character string
3. Senior citizen threshold is strictly greater than 60 (age > 60)
4. Input validation is important for robust solutions
5. Functional programming approaches can provide concise solutions

String Format:
Position:  0123456789012345
Format:    PPPPPPPPPPGAASS
Where:     P = Phone digit (10 chars)
           G = Gender (1 char) 
           A = Age digit (2 chars)
           S = Seat digit (2 chars)

Topic: String Processing, Array Iteration, Data Parsing
"""
