from django.shortcuts import render
from django.http import JsonResponse

from pymongo import MongoClient

import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=env_path)

def store_data(data):

    client = MongoClient(os.getenv("CONNECTION_STRING"))
    db = client.get_database(os.getenv("DB_NAME"))
    collection = db.monster

    collection.insert_one(data)
    
    client.close()

    return 0
    