"""This FastAPI application provides an API endpoint to retrieve
data from a MongoDB database. The data includes
laptop titles and their corresponding ratings.
"""

from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

app = FastAPI()

client = MongoClient("mongodb://mongodb:27017/")
db = client["lappy"]
collection = db["ratings"]


class LaptopRating(BaseModel):
    """Pydantic model representing a laptop rating."""
    id: str
    title: str
    rating: int

    @classmethod
    def from_mongo(cls, document: dict) -> "LaptopRating":
        """Converts a MongoDB document to a LaptopRating instance."""
        document['id'] = str(document['_id'])
        return cls(**document)


@app.get("/laptop_ratings", response_model=list[LaptopRating])
async def get_laptop_ratings(title: str = None, rating: int = None) -> list[
    LaptopRating]:
    """This endpoint retrieves ratings for laptops based on
    optional query parameters.
    """
    query = {}
    if title:
        query["title"] = {"$regex": title, "$options": "i"}
    if rating:
        query["rating"] = rating

    laptop_ratings = [LaptopRating.from_mongo(document) for document in
                      collection.find(query).sort("title", 1)]

    return laptop_ratings
