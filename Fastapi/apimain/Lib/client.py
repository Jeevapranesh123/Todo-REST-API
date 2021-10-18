import pymongo

client=pymongo.MongoClient(host="mongodb",
                            port=27017,
                            username="root",
                            password="pass",
                            authSource="admin")