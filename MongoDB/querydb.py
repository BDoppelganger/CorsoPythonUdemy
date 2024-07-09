import pymongo
from pymongo import MongoClient

#eseguire connessione con MongoDB
client = MongoClient('local', 27017)

#creare database chiamandolo testdb
db = client.testdb

#accedere alla collection persone
persone_coll = db.persone

p = persone_coll.find_one() #ritrnare il primo doc
print(p)

#richiedere persone che possiedono computer apple
persone = persone_coll.find({"computer": "apple"})

for persona in persone:
    print(persona)
    
#modificare età giuseppe verdi
res = persone_coll.update_one({"nome": "Giuseppe"}, {"$set": {"eta": 50}})
p = persone_coll.find_one({"nome": "Giuseppe"})
print(p)

#filtro che trova il primo documento che abbia nome > Giuseppe
persona = persone_coll.find_one({"nome": {"$gt": "Giuseppe"}})
print(persona)
