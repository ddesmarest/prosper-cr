from pymongo import MongoClient
import datetime
import pprint
client = MongoClient()
db = client.test_database
posts = db.posts


post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

post_id = posts.insert_one(post).inserted_id
print post_id
print  db.collection_names(include_system_collections=False)

for post in posts.find():
    pprint.pprint(post)

