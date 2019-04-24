import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["Dev"]

dblist = client.list_database_names()  # get list of all databases
print(dblist)

mycol = mydb["customers"]
