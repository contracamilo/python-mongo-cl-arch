import os

from pymongo import MongoClient, ASCENDING
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")


def get_mongo_client():
    return MongoClient(os.getenv('MONGODB_URI'))


def get_note_collection():
    client = get_mongo_client()
    collection = client["note_manager_db"]["notes"]
    create_indexes(collection)
    return collection


def create_indexes(collection):
    collection.create_index([("title", ASCENDING)], unique=True)
