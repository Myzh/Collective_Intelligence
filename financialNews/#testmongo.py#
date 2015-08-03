#!/usr/bin/env python

from pymongo import MongoClient

client=MongoClient('localhost',27017)

db=client.finance
collection=db.cnnews
#posts=[{"_id":1,"name":"haha1"},{"_id":2,"name":"haha2"}]
#collection.insert_many(posts)
print collection
#print collection.find_one()
result=collection.find_one({"_id":1})
print result
re=collection.find_one({"_id":10})
print re

