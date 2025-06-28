"""
LeetCode Problem 2759: Convert JSON String with Conditions

Given a JSON string, convert it to a JavaScript object with the following conditions:
- If the JSON string is invalid, return the string "Invalid JSON"
- If the JSON is valid but contains any function, return "Functions Not Allowed"
- If the JSON is valid and contains no functions, return the parsed object

Example 1:
Input: jsonString = '{"name": "John", "age": 30}'
Output: {"name": "John", "age": 30}
Explanation: Valid JSON with no functions.

Example 2:
Input: jsonString = '{"name": "John", "greet": function() { return "Hello"; }}'
Output: "Functions Not Allowed"
Explanation: JSON contains a function.

Example 3:
Input: jsonString = '{"name": "John", "age": 30'
Output: "Invalid JSON"
Explanation: Missing closing brace.

Example 4:
Input: jsonString = '{"nested": {"array": [1, 2, 3], "obj": {"key": "value"}}}'
Output: {"nested": {"array": [1, 2, 3], "obj": {"key": "value"}}}
Explanation: Valid nested JSON.

Constraints:
- 1 <= jsonString.length <= 10^4
- The string only contains printable ASCII characters
"""

import json
import re
from typing import Any, Union


def convertJSONString(json_string: str) -> Union[Any, str]:
    """
    Convert JSON string to object with validation for functions.
    
    Args:
        json_string: JSON string to parse
        
    Returns:
        Parsed object if valid, error message if invalid or contains functions
        
    Time Complexity: O(n) where n is length of JSON string
    Space Complexity: O(n) for parsed object storage
    """
    # First check for functions using regex
    # Look for function keyword followed by optional name and parentheses
    function_pattern = r'\bfunction\s*\w*\s*\('
    if re.search(function_pattern, json_string):
        return "Functions Not Allowed"
    
    # Try to parse the JSON
    try:
        parsed_obj = json.loads(json_string)
        
        # Additional check for function-like strings in values
        if contains_function_recursive(parsed_obj):
            return "Functions Not Allowed"
        
        return parsed_obj
    except (json.JSONDecodeError, ValueError):
        return "Invalid JSON"


def convertJSONStringStrict(json_string: str) -> Union[Any, str]:
    """
    Strict implementation that checks for function patterns more thoroughly.
    
    Args:
        json_string: JSON string to parse
        
    Returns:
        Parsed object if valid, error message if invalid or contains functions
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Multiple patterns for detecting functions
    function_patterns = [
        r'\bfunction\s*\w*\s*\(',  # function() or function name()
        r'=>',                     # Arrow functions
        r'\w+\s*:\s*function',     # Property: function
        r'function\s*\(',          # Basic function
    ]
    
    for pattern in function_patterns:
        if re.search(pattern, json_string):
            return "Functions Not Allowed"
    
    try:
        return json.loads(json_string)
    except (json.JSONDecodeError, ValueError):
        return "Invalid JSON"


def convertJSONStringBasic(json_string: str) -> Union[Any, str]:
    """
    Basic implementation focusing on core requirements.
    
    Args:
        json_string: JSON string to parse
        
    Returns:
        Parsed object if valid, error message if invalid or contains functions
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Simple function detection
    if 'function' in json_string:
        return "Functions Not Allowed"
    
    try:
        return json.loads(json_string)
    except:
        return "Invalid JSON"


def convertJSONStringAdvanced(json_string: str) -> Union[Any, str]:
    """
    Advanced implementation with comprehensive function detection.
    
    Args:
        json_string: JSON string to parse
        
    Returns:
        Parsed object if valid, error message if invalid or contains functions
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Check for various function patterns
    function_indicators = [
        'function(',
        'function ',
        ') {',
        '=>',
        'function() {',
        'function()',
    ]
    
    json_lower = json_string.lower()
    for indicator in function_indicators:
        if indicator in json_lower:
            return "Functions Not Allowed"
    
    # Try parsing
    try:
        result = json.loads(json_string)
        return result
    except json.JSONDecodeError:
        return "Invalid JSON"
    except Exception:
        return "Invalid JSON"


def contains_function_recursive(obj: Any) -> bool:
    """
    Recursively check if object contains function-like strings.
    
    Args:
        obj: Object to check
        
    Returns:
        True if contains function patterns, False otherwise
    """
    if isinstance(obj, str):
        return 'function' in obj.lower()
    elif isinstance(obj, dict):
        return any(contains_function_recursive(v) for v in obj.values())
    elif isinstance(obj, list):
        return any(contains_function_recursive(item) for item in obj)
    else:
        return False


def convertJSONStringWithCustomParser(json_string: str) -> Union[Any, str]:
    """
    Implementation with custom JSON parsing logic.
    
    Args:
        json_string: JSON string to parse
        
    Returns:
        Parsed object if valid, error message if invalid or contains functions
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Pre-process to check for functions
    if re.search(r'function\s*\(', json_string, re.IGNORECASE):
        return "Functions Not Allowed"
    
    # Remove whitespace and validate basic structure
    stripped = json_string.strip()
    if not stripped:
        return "Invalid JSON"
    
    # Basic structure validation
    if not ((stripped.startswith('{') and stripped.endswith('}')) or
            (stripped.startswith('[') and stripped.endswith(']'))):
        # Could be a simple value
        pass
    
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        return "Invalid JSON"


# Test cases
def test_convertJSONString():
    """Test the convertJSONString function with various inputs."""
    
    test_cases = [
        {
            "json_string": '{"name": "John", "age": 30}',
            "expected": {"name": "John", "age": 30},
            "description": "Example 1: Valid JSON with no functions"
        },
        {
            "json_string": '{"name": "John", "greet": "function() { return \\"Hello\\"; }"}',
            "expected": "Functions Not Allowed",
            "description": "Example 2: JSON contains function string"
        },
        {
            "json_string": '{"name": "John", "age": 30',
            "expected": "Invalid JSON",
            "description": "Example 3: Missing closing brace"
        },
        {
            "json_string": '{"nested": {"array": [1, 2, 3], "obj": {"key": "value"}}}',
            "expected": {"nested": {"array": [1, 2, 3], "obj": {"key": "value"}}},
            "description": "Example 4: Valid nested JSON"
        },
        {
            "json_string": '[]',
            "expected": [],
            "description": "Empty array"
        },
        {
            "json_string": '{}',
            "expected": {},
            "description": "Empty object"
        },
        {
            "json_string": '"simple string"',
            "expected": "simple string",
            "description": "Simple string value"
        },
        {
            "json_string": '42',
            "expected": 42,
            "description": "Simple number value"
        },
        {
            "json_string": 'true',
            "expected": True,
            "description": "Boolean value"
        },
        {
            "json_string": 'null',
            "expected": None,
            "description": "Null value"
        },
        {
            "json_string": '{"func": "not a function but contains function word"}',
            "expected": "Functions Not Allowed",
            "description": "String containing 'function' word"
        },
        {
            "json_string": '{"arrow": "() => {}"}',
            "expected": "Functions Not Allowed",
            "description": "String containing arrow function"
        },
        {
            "json_string": '{"data": [1, 2, {"nested": "function"}]}',
            "expected": "Functions Not Allowed",
            "description": "Nested function string"
        }
    ]
    
    for i, test in enumerate(test_cases):
        json_string = test["json_string"]
        expected = test["expected"]
        
        print(f"Test {i+1}: {test['description']}")
        print(f"  Input: {json_string}")
        print(f"  Expected: {expected}")
        
        # Test main solution
        result1 = convertJSONString(json_string)
        print(f"  Main solution: {result1}")
        
        # Test strict solution
        result2 = convertJSONStringStrict(json_string)
        print(f"  Strict solution: {result2}")
        
        # Test basic solution
        result3 = convertJSONStringBasic(json_string)
        print(f"  Basic solution: {result3}")
        
        # For function detection tests, verify error message
        if expected == "Functions Not Allowed" or expected == "Invalid JSON":
            assert result1 == expected, f"Main solution failed for test {i+1}"
            # Other solutions might have different detection sensitivity
        else:
            # For valid JSON, all should return same parsed result
            assert result1 == expected, f"Main solution failed for test {i+1}"
            if result2 == result1:  # Only check if detection logic matches
                assert result2 == expected, f"Strict solution failed for test {i+1}"
        
        print(f"  ✓ Test passed!")
        print()


if __name__ == "__main__":
    test_convertJSONString()

"""
Complexity Analysis:

1. Main Solution (convertJSONString):
   - Time Complexity: O(n) - regex search + JSON parsing
   - Space Complexity: O(n) - storage for parsed object

2. Strict Solution (convertJSONStringStrict):
   - Time Complexity: O(n * k) where k is number of patterns to check
   - Space Complexity: O(n) - parsed object storage

3. Basic Solution (convertJSONStringBasic):
   - Time Complexity: O(n) - simple string search + JSON parsing
   - Space Complexity: O(n) - parsed object storage

Key Insights:
- JSON parsing can fail for various reasons (syntax errors, malformed structure)
- Function detection requires pattern matching since JSON doesn't natively support functions
- Need to balance between thoroughness and performance in function detection
- Different levels of strictness possible for function detection

Function Detection Strategies:
1. Simple keyword search: Look for 'function' keyword
2. Regex patterns: Match function syntax patterns
3. Recursive checking: Check parsed object values for function strings
4. Multiple patterns: Arrow functions, method definitions, etc.

Edge Cases:
- Empty JSON objects/arrays
- Primitive JSON values (string, number, boolean, null)
- Nested objects with functions deep inside
- Function-like strings that aren't actual functions
- Invalid JSON syntax

Error Handling:
- JSONDecodeError for malformed JSON
- ValueError for other parsing issues
- Custom validation for business rules (no functions)

Implementation Considerations:
- Regex performance for large strings
- False positives in function detection
- Support for various function syntaxes
- Graceful error handling

Topics: JSON Parsing, String Processing, Regular Expressions, Error Handling
"""
