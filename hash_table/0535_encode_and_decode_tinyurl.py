"""
LeetCode Question #535: Encode and Decode TinyURL

Problem Statement:
TinyURL is a URL shortening service where you enter a URL such as 
https://leetcode.com/problems/design-tinyurl and it returns a short URL 
such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and 
decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. 
You just need to ensure that a URL can be encoded to a tiny URL and the 
tiny URL can be decoded to the original URL.

Implement the `Codec` class:
- `Codec()` Initializes the object of the system.
- `encode(longUrl: str) -> str` Encodes a URL to a shortened URL.
- `decode(shortUrl: str) -> str` Decodes a shortened URL to its original URL. 
  It is guaranteed that the given shortUrl is a valid shortened URL and 
  was encoded by the same object.

Example:
    Input:
        url = "https://leetcode.com/problems/design-tinyurl"
    Output:
        codec = Codec()
        codec.decode(codec.encode(url)) -> "https://leetcode.com/problems/design-tinyurl"

Constraints:
- All URLs are valid.
- The length of the URLs is at most 10^4.
"""

# Solution
import random
import string

class Codec:
    def __init__(self):
        # Dictionary to store mappings between original URLs and shortened URLs
        self.url_map = {}
        self.short_to_long = {}
        self.base_url = "http://tinyurl.com/"
    
    def _generate_short_key(self):
        """Generates a random 6-character key for the shortened URL."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.url_map:
            # If the URL is already encoded, return the existing short URL
            return self.url_map[longUrl]
        
        # Generate a unique short key
        short_key = self._generate_short_key()
        while short_key in self.short_to_long:
            short_key = self._generate_short_key()
        
        # Create the short URL
        shortUrl = self.base_url + short_key
        
        # Store the mappings
        self.url_map[longUrl] = shortUrl
        self.short_to_long[shortUrl] = longUrl
        
        return shortUrl
    
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.short_to_long[shortUrl]

# Example Test Cases
if __name__ == "__main__":
    codec = Codec()
    
    # Test Case 1
    url = "https://leetcode.com/problems/design-tinyurl"
    encoded_url = codec.encode(url)
    decoded_url = codec.decode(encoded_url)
    print(f"Original URL: {url}")
    print(f"Encoded URL: {encoded_url}")
    print(f"Decoded URL: {decoded_url}")
    assert decoded_url == url
    
    # Test Case 2
    url2 = "https://example.com/some/long/path"
    encoded_url2 = codec.encode(url2)
    decoded_url2 = codec.decode(encoded_url2)
    print(f"Original URL: {url2}")
    print(f"Encoded URL: {encoded_url2}")
    print(f"Decoded URL: {decoded_url2}")
    assert decoded_url2 == url2
    
    # Test Case 3: Encoding the same URL multiple times
    encoded_url3 = codec.encode(url)
    print(f"Encoded URL (again): {encoded_url3}")
    assert encoded_url3 == encoded_url

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - `encode`: O(1) on average for generating a random key and storing mappings.
   - `decode`: O(1) for retrieving the original URL from the dictionary.

2. Space Complexity:
   - The space complexity is O(n), where n is the number of URLs stored. 
     This is due to the dictionaries `url_map` and `short_to_long` storing mappings.

Topic: Hash Table
"""