from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def collect_products(
        base_url="https://www.foxtrot.com.ua/uk/shop/noutbuki.html?"):
    all_products = []
    current_page = 1

    driver = webdriver.Chrome()

    try:
        for _ in range(30):
            url = f"{base_url}page={current_page}"
            print(f"[INFO] Requesting URL: {url}")

            driver.get(url)

            items = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, 'div.card__body')))

            print(f"[INFO] Processing page {current_page}...")
            for item in items:
                product_data = {}
                title_element = item.find_element(By.CSS_SELECTOR,
                                                  'a.card__title')
                product_data[
                    "title"] = title_element.text.strip()

                rating_html = item.find_element(By.CSS_SELECTOR,
                                                'div.card__rating') \
                    .get_attribute("outerHTML")

                soup = BeautifulSoup(rating_html, 'html.parser')
                stars = soup.select('i.icon_orange')
                rating = len(stars)

                product_data["rating"] = rating

                all_products.append(product_data)

            current_page += 1

    finally:
        driver.quit()

    return all_products


products = collect_products()
print(products)
