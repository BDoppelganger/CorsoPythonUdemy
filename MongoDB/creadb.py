import pymongo
from pymongo import MongoClient

#eseguire connessione con MongoDB
client = MongoClient('local', 27017)

#creare database chiamandolo testdb
db = client.testdb

#creare collection persone
persone_coll = db.persone

#creare indici per query con nome e cognome e computer
persone_coll.create_index([("nome", pymongo.ASCENDING)])
persone_coll.create_index([("cognome", pymongo.ASCENDING)])
persone_coll.create_index([("computer", pymongo.ASCENDING)])

#crea un documento
p1 = {"nome": "Mario", "cognome": "Rossi", "eta": 30, "computer": ["asus", "apple"]}

#inserire documento nella collection
persone_coll.insert_one(p1)

#crea un documento
p2 = {"nome": "Giuseppe", "cognome": "Verdi", "eta": 45, "computer": ["apple"]}

#inserire documento nella collection
persone_coll.insert_one(p2)