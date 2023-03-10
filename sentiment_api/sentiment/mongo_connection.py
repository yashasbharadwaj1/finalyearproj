from urllib.parse import quote_plus
#from dotenv import dotenv_values

#config = dotenv_values(".env")
# pymongo import
from pymongo import MongoClient

# Mongo db connection setup
passw = "jaishriram@24"
usname = "hema"
#passw = config['MONGODB_PWD']
#usname = config['NAME']
name = quote_plus(usname)
password = quote_plus(passw)
connection_string = f"mongodb+srv://{name}:{password}@cluster0.erb6pk2.mongodb.net/test"
client = MongoClient(connection_string)
databases = client.list_database_names()
# print(databases)

db = client["moviereview"]
mydata = db["datacollection"]
commentsdata = db["comments"]

__all__ = ["client", "db", "mydata", "commentsdata"]
