import pymongo
client = pymongo.MongoClient("mongodb+srv://Dharavath_ramdas:Ramdas123@cluster0.dyoaqq5.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"ramdas",
    "email" : "dramdas1505@gmail.com",
    "surname":"dharavath"

}

db1 = client['mangotest']
coll= db1['test']
coll.insert_one(d)