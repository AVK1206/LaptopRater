"""This script is designed to scrape product information.

It extracts details such as
the product title and rating for laptops listed on the site.
"""

import time
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


def collect_products(
        base_url: str = foxtrot_url) -> list[dict]:
    """Collects products from the provided base URL. It iterates
    through  the pages, scraping product titles and ratings
    and stops when pages are over.
    """
    all_products = []
    current_page = 1
    is_first_page = True
    first_page_data = None

    driver = webdriver.Chrome()

    try:
        while True:
            url = f"{base_url}page={current_page}"
            print(f"[INFO] Requesting URL: {url}")

            driver.get(url)

            items = WebDriverWait(driver, 10).until(
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
            time.sleep(1)

    finally:
        driver.quit()

    return all_products
