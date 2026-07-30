from pymongo import MongoClient

from .config import MONGO_URI, MONGO_DATABASE

client = MongoClient(MONGO_URI)

db = client[MONGO_DATABASE]

comments_collection = db["comments"]
external_collection = db["external_information"]