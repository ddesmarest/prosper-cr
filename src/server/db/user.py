import pprint
from pymongo import MongoClient

class User:
    def __init__( self, name, collection):
        self.collection = collection
        self.id = self.collection.insert_one( { 'name':name } ).inserted_id
        self.data = None
    def ensure_data(self):
        if self.data is None:
            self.data = self.collection.find_one( { '_id': self.id } )
    def get_name( self ):
        self.ensure_data()
        return self.data['name']
