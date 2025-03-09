import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# URL of the website containing images
web_url = input("Please provide a valid website url: ").lower()

while not web_url.strip():
    print("Input cannot be empty. Please try again.")
    web_url = input("Please provide a valid website URL: ").lower()

# Check if any of the specified substrings are in the user input
if 'http://' in web_url or 'https://' in web_url:

    # Function to clean a string by removing special characters
    def clean_filename(filename):
        return ''.join(e for e in filename if e.isalnum() or e in ('.', '_'))

    # Function to extract image URLs from a URL and save them to a text file
    def save_image_urls(web_url, output_file):
        response = requests.get(web_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all image tags in the HTML
        img_tags = soup.find_all('img')

        # Extract image URLs and save them to the output file
        with open(output_file, 'w') as file:
            for img in img_tags:
                img_url = img.get('src')
                if img_url:
                    # Create an absolute URL if the img_url is relative
                    img_url = urljoin(web_url, img_url)
                    file.write(img_url + '\n')
                    print(f"Image URL: {img_url}")



    # Output file to save image URLs
    output_file = 'image-links.txt'

    # Call the function to extract image URLs from the specified URL and save them to the output file
    save_image_urls(web_url, output_file)

else: 
    # user input doesn't contain a valid url 
    print("your input doesn't contain a valid website url. Try using http:// or https:// before a website url.")


