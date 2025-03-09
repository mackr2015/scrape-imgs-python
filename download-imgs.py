import os
import requests
from requests.exceptions import Timeout, RequestException


# Create the 'images' directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Open the file containing the URLs and read them
with open('image-links.txt', 'r') as file:

    # Read all the links from the file (assuming each link is on a new line)
    links = file.readlines()

    # Loop through each link, download the image, and save it
    for link in links:

        # Try to download the image
        try:
            # Get the image response from the URL
            response = requests.get(link, stream=True, timeout=20)

            # Check if the request was successful
            if response.status_code == 200:
                # Extract the image name from the URL (e.g., 'image1.jpg')
                image_name = link.split('/')[-1]
                # Define the file path where the image will be saved
                image_path = os.path.join('images', image_name)

                # Open the file and write the image content to it
                with open(image_path, 'wb') as img_file:
                    for chunk in response.iter_content(1024):
                        img_file.write(chunk)

                print(f"Downloaded: {image_name}")
            else:
                print(f"Failed to download {link} (Status Code: {response.status_code})")
                
        except Timeout:
            print(f"Timeout occurred while downloading {link}. Retrying...")

        except Exception as e:
            print(f"Error downloading {link}: {e}")