import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# Function to clean a string by removing special characters
def clean_filename(filename):
    return ''.join(e for e in filename if e.isalnum() or e in ('.', '_'))

# Function to extract image URLs from a URL and save them to a text file
def save_image_urls(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all image tags in the HTML
    img_tags = soup.find_all('img')

    # Extract image URLs and save them to the output file
    with open(output_file, 'w') as file:
        for img in img_tags:
            img_url = img.get('src')
            if img_url:
                # Create an absolute URL if the img_url is relative
                img_url = urljoin(url, img_url)
                file.write(img_url + '\n')
                print(f"Image URL: {img_url}")

# URL of the website containing images
url = 'https://example.com'  # Replace this with the URL you want to scrape images from

# Output file to save image URLs
output_file = 'images.txt'

# Call the function to extract image URLs from the specified URL and save them to the output file
save_image_urls(url, output_file)