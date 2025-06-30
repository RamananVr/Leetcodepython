"""
LeetCode Problem 2788: Split Strings by Separator

Given an array of strings words and a character separator, split each string in words by separator.

Return an array of strings containing the new strings formed after the splits, excluding empty strings.

Notes:
- separator is used to determine where the split should occur, but it is not included in the resulting strings.
- A split may result in more than two strings.
- The resulting strings must maintain their original order.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 20
- Characters in words[i] are either lowercase English letters or characters from the string ".,;$#@".
- separator is a character from the string ".,;$#@".

Example 1:
Input: words = ["one.two.three","four.five","six"], separator = "."
Output: ["one","two","three","four","five","six"]

Example 2:
Input: words = ["$easy$","$problem$"], separator = "$"
Output: ["easy","problem"]

Example 3:
Input: words = ["|||"], separator = "|"
Output: []
Explanation: In this example, we split as follows:
- "|||" splits to ["", "", "", ""].
Since we exclude empty strings, the final answer is [].
"""

def split_words_by_separator(words, separator):
    """
    Optimized solution using list comprehension and built-in split
    
    Time Complexity: O(total_characters)
    Space Complexity: O(total_characters)
    """
    result = []
    
    for word in words:
        # Split by separator and filter out empty strings
        parts = word.split(separator)
        for part in parts:
            if part:  # Only add non-empty strings
                result.append(part)
    
    return result

def split_words_by_separator_manual(words, separator):
    """
    Manual implementation without using built-in split
    
    Time Complexity: O(total_characters)
    Space Complexity: O(total_characters)
    """
    result = []
    
    for word in words:
        current_part = ""
        
        for char in word:
            if char == separator:
                # Found separator, add current part if not empty
                if current_part:
                    result.append(current_part)
                    current_part = ""
            else:
                current_part += char
        
        # Add the last part if not empty
        if current_part:
            result.append(current_part)
    
    return result

def split_words_by_separator_optimized(words, separator):
    """
    Most optimized solution using generator and filter
    
    Time Complexity: O(total_characters)
    Space Complexity: O(total_characters)
    """
    def split_and_filter(word):
        """Generator that yields non-empty parts"""
        for part in word.split(separator):
            if part:
                yield part
    
    result = []
    for word in words:
        result.extend(split_and_filter(word))
    
    return result

def split_words_by_separator_one_liner(words, separator):
    """
    One-liner solution using list comprehension
    
    Time Complexity: O(total_characters)
    Space Complexity: O(total_characters)
    """
    return [part for word in words for part in word.split(separator) if part]

def split_words_by_separator_functional(words, separator):
    """
    Functional programming approach
    
    Time Complexity: O(total_characters)
    Space Complexity: O(total_characters)
    """
    from functools import reduce
    from operator import add
    
    # Split each word and flatten the results
    split_words = [word.split(separator) for word in words]
    flattened = reduce(add, split_words, [])
    
    # Filter out empty strings
    return list(filter(None, flattened))

def split_words_by_separator_itertools(words, separator):
    """
    Using itertools for a different approach
    
    Time Complexity: O(total_characters)
    Space Complexity: O(total_characters)
    """
    import itertools
    
    # Split all words and chain them together
    all_parts = itertools.chain.from_iterable(
        word.split(separator) for word in words
    )
    
    # Filter out empty strings
    return [part for part in all_parts if part]

# Test cases
def test_split_words_by_separator():
    test_cases = [
        (["one.two.three","four.five","six"], ".", ["one","two","three","four","five","six"]),
        (["$easy$","$problem$"], "$", ["easy","problem"]),
        (["|||"], "|", []),
        (["hello", "world"], ".", ["hello", "world"]),  # No separator in strings
        (["a.b.c", "", "d.e"], ".", ["a", "b", "c", "d", "e"]),  # Empty string in input
        ([".a.b.", "c..d"], ".", ["a", "b", "c", "d"]),  # Leading/trailing separators
        (["abc"], "x", ["abc"]),  # Separator not in string
        ([""], ".", []),  # Empty string input
        (["a;b;c", "d#e#f"], ";", ["a", "b", "c", "d#e#f"]),  # Different separator
        (["one$two$$three", "four$"], "$", ["one", "two", "three", "four"]),  # Multiple consecutive separators
    ]
    
    approaches = [
        ("Built-in Split", split_words_by_separator),
        ("Manual", split_words_by_separator_manual),
        ("Optimized", split_words_by_separator_optimized),
        ("One-liner", split_words_by_separator_one_liner),
        ("Functional", split_words_by_separator_functional),
        ("Itertools", split_words_by_separator_itertools)
    ]
    
    for approach_name, func in approaches:
        print(f"Testing {approach_name} approach:")
        all_passed = True
        
        for words, separator, expected in test_cases:
            try:
                result = func(words[:], separator)  # Pass copy to avoid modification
                passed = result == expected
                if not passed:
                    all_passed = False
                
                print(f"  Input: words={words}, separator='{separator}'")
                print(f"  Expected: {expected}")
                print(f"  Got: {result}")
                print(f"  {'✓' if passed else '✗'}")
            except Exception as e:
                print(f"  Input: words={words}, separator='{separator}'")
                print(f"  Error: {e}")
                print(f"  ✗")
                all_passed = False
        
        print(f"  Overall: {'✓ All Passed' if all_passed else '✗ Some Failed'}\n")

def test_edge_cases():
    """Test additional edge cases"""
    print("Testing Edge Cases:")
    
    edge_cases = [
        # All separators
        (["...", ";;;", "$$$"], ".", ["", "", "", ";;;", "$$$"]),
        # Mixed with empty results
        (["a..b", "c.d"], ".", ["a", "b", "c", "d"]),
        # Single character strings
        (["a", "b", "c"], ".", ["a", "b", "c"]),
        # All empty after split
        ([".", "..", "..."], ".", []),
    ]
    
    for words, separator, expected in edge_cases:
        result = split_words_by_separator(words, separator)
        passed = result == expected
        print(f"  Input: {words}, sep='{separator}'")
        print(f"  Expected: {expected}, Got: {result}")
        print(f"  {'✓' if passed else '✗'}")

def benchmark_performance():
    """Quick performance comparison"""
    import time
    
    # Create large test case
    words = ["a.b.c.d.e.f.g.h.i.j"] * 1000
    separator = "."
    
    approaches = [
        ("Built-in Split", split_words_by_separator),
        ("Manual", split_words_by_separator_manual),
        ("One-liner", split_words_by_separator_one_liner),
    ]
    
    print("Performance Benchmark (1000 words):")
    for name, func in approaches:
        start = time.time()
        result = func(words, separator)
        end = time.time()
        print(f"  {name}: {end - start:.4f} seconds, result length: {len(result)}")

if __name__ == "__main__":
    test_split_words_by_separator()
    print("\n" + "="*50)
    test_edge_cases()
    print("\n" + "="*50)
    benchmark_performance()

"""
Topics: String, Array, String Manipulation
Difficulty: Easy

Key Insights:
1. Use built-in split() method for simplicity and efficiency
2. Filter out empty strings after splitting
3. Maintain original order of non-empty parts
4. Handle consecutive separators properly (they create empty strings)
5. One-liner possible with list comprehension

Companies: Google, Microsoft, Amazon, Apple
"""
