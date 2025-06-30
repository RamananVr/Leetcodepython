"""
LeetCode Problem 2785: Sort Vowels in a String

Given a string s, return a string where all the vowels of s are sorted in non-decreasing order. Also, preserve the original positions of consonants.

Vowels are 'a', 'e', 'i', 'o', 'u' and their uppercase counterparts.

Constraints:
- 1 <= s.length <= 10^5
- s consists only of letters of the English alphabet in uppercase and lowercase.

Example 1:
Input: s = "lEetcOde"
Output: "lEOtceede"
Explanation: 'E', 'e', 'O', 'e' are the vowels in s; after sorting the vowels, s becomes "lEOtcede".

Example 2:
Input: s = "lYmpH"
Output: "lYmpH"
Explanation: There are no vowels in s (all characters in s are consonants), so we return s.
"""

def sort_vowels(s):
    """
    Optimized solution using two-pass approach
    
    Time Complexity: O(n + k log k) where k is number of vowels
    Space Complexity: O(n + k)
    """
    if not s:
        return s
    
    vowels = set('aeiouAEIOU')
    
    # First pass: extract vowels and their positions
    vowel_chars = []
    vowel_positions = []
    
    for i, char in enumerate(s):
        if char in vowels:
            vowel_chars.append(char)
            vowel_positions.append(i)
    
    # Sort the vowels
    vowel_chars.sort()
    
    # Second pass: reconstruct string
    result = list(s)
    for i, pos in enumerate(vowel_positions):
        result[pos] = vowel_chars[i]
    
    return ''.join(result)

def sort_vowels_optimized(s):
    """
    Most optimized solution with single allocation
    
    Time Complexity: O(n + k log k)
    Space Complexity: O(n)
    """
    vowels = set('aeiouAEIOU')
    result = list(s)
    vowel_chars = []
    
    # Extract vowels and replace with placeholder
    for i in range(len(s)):
        if s[i] in vowels:
            vowel_chars.append(s[i])
            result[i] = None  # Placeholder
    
    # Sort vowels
    vowel_chars.sort()
    
    # Fill back the sorted vowels
    vowel_idx = 0
    for i in range(len(result)):
        if result[i] is None:
            result[i] = vowel_chars[vowel_idx]
            vowel_idx += 1
    
    return ''.join(result)

def sort_vowels_counting_sort(s):
    """
    Ultra-optimized using counting sort for vowels
    
    Time Complexity: O(n)
    Space Complexity: O(1) - fixed size for vowel counts
    """
    # Vowel order for counting sort
    vowel_order = 'AEIOUaeiou'
    vowel_to_idx = {v: i for i, v in enumerate(vowel_order)}
    
    # Count each vowel
    vowel_counts = [0] * len(vowel_order)
    result = list(s)
    
    # First pass: count vowels and mark positions
    for i, char in enumerate(s):
        if char in vowel_to_idx:
            vowel_counts[vowel_to_idx[char]] += 1
            result[i] = None  # Mark vowel position
    
    # Create sorted vowel sequence
    sorted_vowels = []
    for i, count in enumerate(vowel_counts):
        sorted_vowels.extend([vowel_order[i]] * count)
    
    # Second pass: fill vowels back
    vowel_idx = 0
    for i in range(len(result)):
        if result[i] is None:
            result[i] = sorted_vowels[vowel_idx]
            vowel_idx += 1
    
    return ''.join(result)

def sort_vowels_in_place_simulation(s):
    """
    Simulated in-place approach (strings are immutable in Python)
    
    Time Complexity: O(n + k log k)
    Space Complexity: O(n)
    """
    vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    chars = list(s)
    
    # Collect vowels and their indices
    vowels_with_indices = []
    for i, char in enumerate(chars):
        if char in vowel_set:
            vowels_with_indices.append((char, i))
    
    # Sort vowels only
    vowels_with_indices.sort(key=lambda x: x[0])
    
    # Place sorted vowels back
    for i, (vowel, original_idx) in enumerate(vowels_with_indices):
        # Find the i-th vowel position in the string
        vowel_pos_count = 0
        for j, char in enumerate(chars):
            if char in vowel_set:
                if vowel_pos_count == i:
                    chars[j] = vowel
                    break
                vowel_pos_count += 1
    
    return ''.join(chars)

# Test cases
def test_sort_vowels():
    test_cases = [
        ("lEetcOde", "lEOtceede"),
        ("lYmpH", "lYmpH"),
        ("", ""),
        ("aEiOu", "aEiOu"),  # Already sorted
        ("uOiEa", "aEiOu"),  # Reverse order
        ("bcdfg", "bcdfg"),  # No vowels
        ("aeiou", "aeiou"),  # Only vowels, sorted
        ("uoiea", "aeiou"),  # Only vowels, unsorted
        ("Programming", "Pregramming"),  # Mixed case
        ("QuickSort", "QeickSort"),  # Real word example
        ("Python", "Python"),  # Single vowel
        ("AaEeIiOoUu", "AaEeIiOoUu"),  # All vowels sorted
        ("UuOoIiEeAa", "AaEeIiOoUu"),  # All vowels reverse
    ]
    
    approaches = [
        ("Two-pass", sort_vowels),
        ("Optimized", sort_vowels_optimized),
        ("Counting Sort", sort_vowels_counting_sort),
        ("In-place Sim", sort_vowels_in_place_simulation)
    ]
    
    for approach_name, func in approaches:
        print(f"Testing {approach_name} approach:")
        all_passed = True
        
        for s, expected in test_cases:
            try:
                result = func(s)
                passed = result == expected
                if not passed:
                    all_passed = False
                
                print(f"  Input: '{s}'")
                print(f"  Expected: '{expected}', Got: '{result}'")
                print(f"  {'✓' if passed else '✗'}")
            except Exception as e:
                print(f"  Input: '{s}'")
                print(f"  Error: {e}")
                print(f"  ✗")
                all_passed = False
        
        print(f"  Overall: {'✓ All Passed' if all_passed else '✗ Some Failed'}\n")

def benchmark_performance():
    """Quick performance test with longer strings"""
    import time
    
    # Create test string with many vowels
    test_string = "aEiOuBcDfGhJkLmNpQrStVwXyZ" * 1000
    
    approaches = [
        ("Two-pass", sort_vowels),
        ("Optimized", sort_vowels_optimized),
        ("Counting Sort", sort_vowels_counting_sort)
    ]
    
    print("Performance Benchmark (1000x repeated pattern):")
    for name, func in approaches:
        start = time.time()
        result = func(test_string)
        end = time.time()
        print(f"  {name}: {end - start:.4f} seconds")

if __name__ == "__main__":
    test_sort_vowels()
    print("\n" + "="*50)
    benchmark_performance()

"""
Topics: String, Sorting, Two Pointers
Difficulty: Medium

Key Insights:
1. Extract vowels, sort them, then place back in original vowel positions
2. Counting sort can optimize since there are only 10 possible vowels
3. Two-pass approach: collect vowels, then reconstruct string
4. Preserve consonant positions while sorting vowels
5. ASCII order naturally gives correct vowel sorting (A < E < I < O < U < a < e < i < o < u)

Companies: Microsoft, Google, Amazon, Apple
"""
