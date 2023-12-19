"""This script is designed to insert product information
into a MongoDB database.

The script uses the "pymongo" library to interact with MongoDB
and leverages the "collect_products" function from
the "parsing.parser" module for data scraping.
"""

from pymongo import MongoClient
from parsing.parser import collect_products


def insert_info_in_mongodb(products: list[dict]) -> None:
    """ Inserts a list of product information into
    the MongoDB database.

    The function connects to the MongoDB server, drops the
    existing collection if it exists, and inserts the new data.
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client["laptops"]
    collection = db["ratings"]

    try:
        collection.drop()
        print("[INFO] Existing collection dropped.")
        collection.insert_many(products)
        print(f"[INFO] Inserted {len(products)} products into MongoDB.")
    except Exception as error:
        print(f"[ERROR] Error inserting data: {error}")


insert_info_in_mongodb(collect_products())