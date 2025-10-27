# crud.py
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, host='localhost', port=27017, db='aac'):
        try:
            self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}/{db}')
            self.database = self.client[db]
            print("Connected to MongoDB successfully!")
        except ConnectionFailure as e:
            print(f"Could not connect to MongoDB: {e}")

    def create(self, data, collection="animals"):
        if data:
            try:
                result = self.database[collection].insert_one(data)
                return result.acknowledged
            except OperationFailure as e:
                print("Create failed:", e)
        return False

    def read(self, query, collection="animals"):
        try:
            return list(self.database[collection].find(query))
        except OperationFailure as e:
            print("Read failed:", e)
            return []

    def update(self, query, new_data, collection="animals"):
        try:
            result = self.database[collection].update_many(query, {"$set": new_data})
            return result.modified_count
        except OperationFailure as e:
            print("Update failed:", e)
            return 0

    def delete(self, query, collection="animals"):
        try:
            result = self.database[collection].delete_many(query)
            return result.deleted_count
        except OperationFailure as e:
            print("Delete failed:", e)
            return 0