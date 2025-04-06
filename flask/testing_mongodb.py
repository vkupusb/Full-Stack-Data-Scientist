
from pymongo import MongoClient


uri = "mongodb+srv://cluster0.uvtb8qo.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='D:/Learning/MongoDB/Authentication file')

db = client['testDB']
collection = db['testCol']
doc_count = collection.count_documents({})
print(doc_count)
