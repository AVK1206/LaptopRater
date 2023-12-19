"""This FastAPI application provides an API endpoint to retrieve
data from a MongoDB database. The data includes
laptop titles and their corresponding ratings.
"""

from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel


app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["laptops"]
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
async def get_laptop_ratings() -> list[LaptopRating]:
    """This endpoint retrieves ratings for laptops based on
    optional query parameters.
    """
    query_title = {"title": {"$regex": "Lenovo", "$options": "i"}}
    query_rating = {"rating": 5}
    query_combined = {"title": {"$regex": "asus", "$options": "i"},
                      "rating": 4}

    laptop_ratings = [LaptopRating.from_mongo(document) for document in
                      collection.find()]
    return laptop_ratings
