from pymongo import MongoClient
import json

with open("appsettings.json") as user_file:
      file_contents = user_file.read()

appsettings = json.loads(file_contents)

def connection():

    client = MongoClient(appsettings["ConnectionStrings"]["url"])
    database = client[appsettings["ConnectionStrings"]["database"]]
    collection = database[appsettings["ConnectionStrings"]["collection"]]
    
    return collection

def sequences():

  client = MongoClient(appsettings["ConnectionStringsSequences"]["url"])
  database = client[appsettings["ConnectionStringsSequences"]["database"]]
  collection = database[appsettings["ConnectionStringsSequences"]["collection"]]
    
  return collection