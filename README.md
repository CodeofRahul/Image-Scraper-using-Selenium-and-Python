[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Selenium](https://img.shields.io/badge/Selenium-4A29A8?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Automation](https://img.shields.io/badge/Automation-007EC7?style=for-the-badge&logo=automation&logoColor=white)](https://en.wikipedia.org/wiki/Automation)

# Image-Scraper-using-Selenium-and-Python

This project is a web image scraper that uses Selenium and Python to automate image extraction from Google Images. It scrolls through the page, collects high-quality images, and downloads them efficiently. The script is designed with error handling and retry mechanisms to ensure robustness.

✨ **Features**

* **Automated Web Scraping:** Uses Selenium to interact with the browser and fetch images dynamically.
* **Smart Scrolling:** Automatically scrolls to load more images.
* **Image Filtering:** Filters out low-resolution and placeholder images.
* **Base64 & Direct Image Support:** Handles both direct image URLs and base64-encoded images.
* **Retry Mechanism:** Retries failed downloads to improve success rate.
* **Customizable Settings:** Modify search queries, scroll limits, and number of images easily.

📂 **Project Structure**

🛠️ **Setup & Installation**

Follow these steps to get started:

1️⃣ **Install Dependencies**

Make sure you have Python 3.x installed, then run:

```bash
pip install selenium requests webdriver-manager
```
2️⃣ **Run the Script**

Modify the `search_term` in `Image_Scrape.py` to your desired query and execute:

```bash
Image_Scrape.py
```

3️⃣ **View Downloaded Images**

The images will be saved in the `scraped_images` folder inside the specified directory.

🏗️ **How It Works**

- **Initialize WebDriver:** Sets up ChromeDriver with necessary configurations.
- **Navigate to Google Images:** Searches for the specified term.
- **Scroll Down:** Loads more images dynamically.
- **Scrape Image URLs:** Extracts valid image links.
- **Download Images:** Saves images in a local folder.
- **Exit Browser:** Closes WebDriver after execution.

🔍 **Code Breakdown**

- `create_driver()`: Sets up a headless Chrome browser for scraping.
- `scroll_down()`: Scrolls the page to load more images.
- `scrape_all_images()`: Extracts image URLs while filtering out placeholders.
- `save_image()`: Downloads images and saves them efficiently.
- `scrap_and_save_images()`: Combines all functions to scrape and store images.
