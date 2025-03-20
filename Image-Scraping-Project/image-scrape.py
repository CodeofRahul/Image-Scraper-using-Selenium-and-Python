import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

def download_images(url, download_folder = 'images'):
    """
    Downloads all images from a given URL and saves them to a specified folder.

    Args:
        url (str): The URL of the webpage to scrape images from.
        download_folder (str, optional): The folder to save the downloaded images. Defaults to 'images'.
    """
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for bad status codes

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all image tags
        images = soup.find_all('img')

        # Create the download folder if it doesn't exist
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # Iterate through each image tag and download the image
        for img in images:
            # Get the image source URL
            src = img.get('src')
            if src:
                # Construct the absolute URL if the source is relative
                src = urllib.parse.urljoin(url, src)

                try:
                    # Fetch the image content
                    img_response = requests.get(src)
                    img_response.raise_for_status() # Raise exception for bad status codes

                    # Extract the image name from the URL
                    img_name = os.path.basename(urllib.parse.urlparse(src).path)

                    # Remove query parameters from the image name
                    img_name = img_name.split('?')[0]

                    # Construct the full image path
                    img_path = os.path.join(download_folder, img_name)

                    # Save the image to the file system
                    with open(img_path,'wb') as f:
                        f.write(img_response.content)
                    
                    # Print a message indicating the image was downloaded
                    print(f"Downloaded {img_path}")
                except requests.exceptions.RequestException as e:
                        print(f"Error downloading image from {src}: {e}")
                except Exception as e:
                    print(f"An error occurred while processing image from {src}: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

# Get the folder name from the user
foldername = input("Enter Folder name to save images : ")

# Get the URL from the user
url = input("Enter url to Download images : ")

# Call the download_images function with user input
download_images(download_folder=foldername, url=url)
