
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://kvishva27:kvishva27@cluster0.uvtb8qo.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)