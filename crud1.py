import pymongo

client = pymongo.MongoClient()

mydb=client["mydb"]

mycol=mydb["people"]

data={'name':'shiv','age':'29'}

datalist=[{'name':'shiv','age':'30'},{'sandy':'43'},{'shivaji':'31'}]

mycol.insert_many(datalist)


mycol.insert_one(data)

print(client.list_database_names())

for x in mycol.find():
    print(x)

