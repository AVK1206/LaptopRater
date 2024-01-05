"""This script is designed to scrape product information.

It extracts details such as
the product title and rating for laptops listed on the site.
"""

import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


foxtrot_url = "https://www.foxtrot.com.ua/uk/shop/noutbuki.html?"


def clean_title(title: str) -> str:
    """Cleans the product title by removing the words what not need."""
    title = re.sub(r'^Ноутбук\s+', '', title)
    title = re.sub(r'\s+\([^)]*\)', '', title)

    return title


def setup_selenium():
    """Set up Selenium with Chrome in headless mode."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-features=VizDisplayCompositor")

    driver = webdriver.Chrome(options=chrome_options)
    return driver


def collect_products(driver, base_url: str = foxtrot_url) -> list[dict]:
    """Collects products from the provided base URL. It iterates
    through  the pages, scraping product titles and ratings
    and stops when pages are over.
    """
    all_products = []
    current_page = 1
    is_first_page = True
    first_page_data = None

    try:
        while True:
            url = f"{base_url}page={current_page}"
            print(f"[INFO] Requesting URL: {url}")

            driver.get(url)

            items = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, 'div.card__body')))

            if is_first_page:
                first_page_data = [item.text for item in items]
                is_first_page = False

            elif [item.text for item in items] == first_page_data:
                print("[INFO] All pages are parsed")
                break

            print(f"[INFO] Processing page {current_page}...")
            for item in items:
                product_data = {}
                title_element = item.find_element(By.CSS_SELECTOR,
                                                  'a.card__title')

                cleaned_title = clean_title(title_element.text.strip())
                product_data["title"] = cleaned_title

                rating_html = item.find_element(By.CSS_SELECTOR,
                                                'div.card__rating') \
                    .get_attribute("outerHTML")

                soup = BeautifulSoup(rating_html, 'html.parser')
                stars = soup.select('i.icon_orange')
                rating = len(stars)

                product_data["rating"] = rating

                all_products.append(product_data)

            current_page += 1

    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")

    return all_products


if __name__ == "__main__":
    driver = setup_selenium()
    products = collect_products(driver)
    driver.quit()
