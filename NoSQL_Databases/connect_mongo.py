from pymongo import MongoClient

user = 'root'
password = 'Hsg3zwHUOVOyyL98ASHb3HTg'
host = 'mongo'

connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

connection = MongoClient(connecturl)

dbs = connection.list_database_names()

for db in dbs:
    print(db)

connection.close()