"""This script is designed to insert product information
into a MongoDB database.

The script uses the "pymongo" library to interact with MongoDB
and leverages the "collect_products" function from
the "parsing.parser" module for data scraping.
"""

from pymongo import MongoClient
from parsing.parser import collect_products, setup_selenium


def insert_info_in_mongodb(products: list[dict]) -> None:
    """Inserts a list of product information into
    the MongoDB database.

    The function connects to the MongoDB server, drops the
    existing collection if it exists, and inserts the new data.
    """
    client = MongoClient("mongodb://mongodb:27017/")
    db = client["lappy"]
    collection = db["ratings"]

    try:
        collection.drop()
        print("[INFO] Existing collection dropped.")
        collection.insert_many(products)
        print(f"[INFO] Inserted {len(products)} products into MongoDB.")
    except Exception as error:
        print(f"[ERROR] Error inserting data: {error}")


if __name__ == "__main__":
    driver = setup_selenium()
    products = collect_products(driver)
    driver.quit()
    insert_info_in_mongodb(products)
