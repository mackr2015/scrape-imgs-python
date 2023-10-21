import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# Function to clean a string by removing special characters
def clean_filename(filename):
    return ''.join(e for e in filename if e.isalnum() or e in ('.', '_'))


# Function to download images from a URL and save their URLs in a Word document
def download_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all image tags in the HTML
    img_tags = soup.find_all('img')
    
    # Create the "images" directory if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')
    
    
    # Extract image URLs and download them
    for img in img_tags:
        img_url = img.get('src')
        if img_url:
            # Create an absolute URL if the img_url is relative
            img_url = urljoin(url, img_url)
            img_data = requests.get(img_url).content
            # Extract the image file name from the URL
            
            img_filename = os.path.join('images/', clean_filename(os.path.basename(img_url)))
            # check if img filename exists
            if not img_filename:
                with open(img_filename, 'wb') as img_file:
                    img_file.write(img_data)
                print(f"Downloaded: {img_filename}")
           

    
    

# URL of the website containing images
url = 'https://example.com'
# Call the function to download images from the specified URL and save their URLs in the Word document
download_images(url)
