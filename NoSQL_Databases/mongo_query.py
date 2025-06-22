from pymongo import MongoClient

user = 'root'
password = 'Hsg3zwHUOVOyyL98ASHb3HTg'
host = 'mongo'

connecturl = f"mongodb://{user}:{password}@{host}:27017/?authSource=admin"

connection = MongoClient(connecturl)

db = connection.training

collection = db.python

doc = {"lab":"Accessing mongodb using python", "Subject":"No SQL Databases"}

print("Inserting a document into collection.")
db.collection.insert_one(doc)
# query for all documents in 'training' database and 'python' collection
docs = db.collection.find()
print("Printing the documents in the collection.")
for document in docs:
    print(document)
# close the server connecton
print("Closing the connection.")
connection.close()