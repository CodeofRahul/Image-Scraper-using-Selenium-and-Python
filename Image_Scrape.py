# Import necessary libraries for web scraping and image downloading


import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import base64
import time

# Function to set up and create a Selenium WebDriver
# Configures Chrome options to run without unnecessary overhead
# Installs and manages ChromeDriver automatically

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")   # Disables GPU hardware acceleration
    options.add_argument("--no-sandbox")    # Bypasses OS security restrictions
    options.add_argument("--disable-dev-shm-usage")  # Prevents memory issues in containers
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Function to scroll down the webpage to load more images
# Scrolls incrementally with pauses to allow content loading

def scroll_down(driver, scroll_pause_time=2, scroll_limit=2):
    last_height = driver.execute_script("return document.body.scrollHeight")  # Get initial scroll height
    for i in range(scroll_limit):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll to bottom
        time.sleep(scroll_pause_time)  # Pause to allow content to load
        new_height = driver.execute_script("return document.body.scrollHeight")  # Get new height
        if new_height == last_height:  # Stop if no new content loads
            break
        last_height = new_height

# Function to scrape all image URLs from the webpage
# Filters images based on size to avoid thumbnails and low-quality images

def scrape_all_images(driver):
    try:
        images = driver.find_elements(By.TAG_NAME, 'img')  # Locate all image elements
        image_urls = []
        for img in images:
            image_url = img.get_attribute('src') or img.get_attribute('data-src')  # Get image URL
            if image_url and "data:image/gif" not in image_url:  # Exclude placeholder images
                width = int(img.get_attribute('width') or 0)
                height = int(img.get_attribute('height') or 0)
                if width >= 100 and height >= 100:  # Consider only images larger than 100x100 pixels
                    image_urls.append(image_url)
        return image_urls
    except Exception as e:
        print(f"Error scraping images {e}")
        return []

# Function to download and save images from URLs
# Supports both base64-encoded images and direct URLs

def save_image(image_url, folder_name, file_name, retry_count=3):
    try:
        file_path = os.path.join(folder_name, f"{file_name}.jpg")

        # If the image is base64-encoded, decode and save it
        if image_url.startswith('data:image/'):
            header, encoded = image_url.split(',', 1)
            image_data = base64.b64decode(encoded)
            with open(file_path, 'wb') as f:
                f.write(image_data)

        # Otherwise, download image via HTTP request
        else:
            for attempt in range(retry_count):  # Retry mechanism for failed downloads
                response = requests.get(image_url, timeout=10)
                if response.status_code == 200:  # If successful, save image
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    break
                else:
                    print(f"Failed attempt {attempt+1} for image: {image_url}")
                    time.sleep(2)  # Wait before retrying
    except Exception as e:
        print(f"Error saving image {file_name}: {e}")

# Main function to scrape and save images
# Creates a folder, initializes WebDriver, searches for images, and saves them

def scrap_and_save_images(base_folder, num_image = 10):
    folder_path = os.path.join(base_folder, "scraped_images")  # Define save folder path

    if not os.path.exists(folder_path):  # Create folder if it doesn't exist
        os.makedirs(folder_path)
    driver = create_driver()  # Initialize WebDriver
    search_term = "MS Dhoni"  # Search query for Google Images
    driver.get(f"https://www.google.com/search?q={search_term}&tbm=isch")  # Open Google Images
    time.sleep(5)  # Allow page to load

    scroll_down(driver)  # Scroll to load more images
    image_urls = scrape_all_images(driver)  # Extract image URLs
    image_urls = image_urls[:num_image]  # Limit number of images to save

    for index, image_url in enumerate(image_urls, start=1):
        file_name = f"{search_term}_{index}"  # Naming convention for saved images
        save_image(image_url, folder_path, file_name)  # Save each image

    print(f"Finished scraping!")
    driver.quit()  # Close WebDriver

# Entry point of the script
if __name__ == "__main__":
    base_folder = r"F:\Web-Scrape\Scrape_image"  # Define base folder for saving images
    scrap_and_save_images(base_folder, num_image=10)  # Start scraping process
