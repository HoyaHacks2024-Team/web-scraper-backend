from pymongo import MongoClient
import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=env_path)


client = MongoClient(os.getenv("CONNECTION_STRING"))
db = client.get_database(os.getenv("DB_NAME"))
records = db.monster

example = {
    'name': 'nam',
    'roll':1,
}

records.insert_one(example)

print(records.count_documents({}))

print(records.find_one({'nam'}))