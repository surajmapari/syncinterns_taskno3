import string
import random

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.characters = string.ascii_letters + string.digits
        self.base_url = 'https://bit.ly/'

    def shorten_url(self, original_url):
        if original_url in self.url_mapping:
            return self.url_mapping[original_url]

        shortcode = self.generate_shortcode()
        shortened_url = self.base_url + shortcode
        self.url_mapping[original_url] = shortened_url

        return shortened_url

    def generate_shortcode(self):
        shortcode_length = 6
        shortcode = ''.join(random.choice(self.characters) for _ in range(shortcode_length))
        return shortcode

# Usage example
shortener = URLShortener()

while True:
    # Take original URL from the user
    original_url = input("Enter the original URL (or 'quit' to exit): ")

    if original_url.lower() == 'quit':
        break

    # Shorten the URL
    shortened_url = shortener.shorten_url(original_url)
    print('Shortened URL:', shortened_url)
    print()

print('Program ended.')
