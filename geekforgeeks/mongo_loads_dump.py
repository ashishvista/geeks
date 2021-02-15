import pymongo
import json
from bson.json_util import dumps
from bson.json_util import loads

myclient = pymongo.MongoClient("mongodb://miraah:TERi0Maa0Ka0$akInaaka@localhost:27027/staging?authSource=admin")
mydb = myclient["staging"]
mycol = mydb["catalive"]

docs= mycol.find({"status":"History"},{"title":1}).limit(10)
for doc in docs:
    print(doc)

docsArray= list(mycol.find({"status":"History"},{"title":1,"_id":1}).limit(10))
print(list(docsArray))
myclient.close()


with open('data.json', 'w', encoding='utf-8') as f:
    f.write(dumps(docsArray))

with open('data.json', 'r', encoding='utf-8') as f:
    dd=loads(f.read())
    print(dd)
    mycol = mydb["ttt"]
    mycol.insert_many(dd)


