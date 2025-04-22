"""
LeetCode Question #534: Design TinyURL

Problem Statement:
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design a class to encode a URL and decode a tiny URL.

Implement the `Codec` class:
- `Codec()` Initializes the object of the system.
- `encode(longUrl: str) -> str` Returns a tiny URL for the given long URL.
- `decode(shortUrl: str) -> str` Returns the original long URL for the given short URL. It is guaranteed that the given short URL was encoded by the same object.

Example:
    Input: url = "https://leetcode.com/problems/design-tinyurl"
    Output: "https://leetcode.com/problems/design-tinyurl"

Constraints:
- All URLs are guaranteed to be valid.
"""

import random
import string

class Codec:
    def __init__(self):
        # Dictionary to store mappings between long URLs and short URLs
        self.url_map = {}
        self.reverse_map = {}
        self.base_url = "http://tinyurl.com/"
        self.key_length = 6  # Length of the random key for the short URL

    def _generate_key(self):
        """Generates a random key for the short URL."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=self.key_length))

    def encode(self, longUrl: str) -> str:
        """Encodes a long URL into a short URL."""
        if longUrl in self.url_map:
            # If the URL is already encoded, return the existing short URL
            return self.url_map[longUrl]
        
        # Generate a unique key for the short URL
        key = self._generate_key()
        while key in self.reverse_map:
            key = self._generate_key()
        
        shortUrl = self.base_url + key
        self.url_map[longUrl] = shortUrl
        self.reverse_map[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a short URL back into the original long URL."""
        return self.reverse_map.get(shortUrl, "")


# Example Test Cases
if __name__ == "__main__":
    codec = Codec()
    
    # Test Case 1
    long_url = "https://leetcode.com/problems/design-tinyurl"
    short_url = codec.encode(long_url)
    assert codec.decode(short_url) == long_url
    print(f"Original URL: {long_url}")
    print(f"Shortened URL: {short_url}")
    print(f"Decoded URL: {codec.decode(short_url)}")
    
    # Test Case 2
    another_url = "https://example.com/some/long/path"
    another_short_url = codec.encode(another_url)
    assert codec.decode(another_short_url) == another_url
    print(f"Original URL: {another_url}")
    print(f"Shortened URL: {another_short_url}")
    print(f"Decoded URL: {codec.decode(another_short_url)}")
    
    # Test Case 3: Encoding the same URL multiple times
    repeated_short_url = codec.encode(long_url)
    assert repeated_short_url == short_url  # Should return the same short URL
    print(f"Repeated Shortened URL: {repeated_short_url}")

"""
Time and Space Complexity Analysis:

1. Encoding:
   - Time Complexity: O(1) on average for generating a random key and storing the mappings.
   - Space Complexity: O(n), where n is the number of URLs stored in the system.

2. Decoding:
   - Time Complexity: O(1) for retrieving the original URL from the dictionary.
   - Space Complexity: O(n), where n is the number of URLs stored in the system.

Topic: Hash Table
"""