#!/usr/bin/env python

import sys, urllib, urllib2, pymongo
from pymongo import MongoClient
reload(sys)
sys.setdefaultencoding("utf-8")


#setup localhost mongodb conenctor
mongoClient=MongoClient('localhost',27017)
db=mongoClient.finance
collection=db.cnnews

#def parseSinaFinance():
sinaURL="http://finance.sina.com.cn"
response=urllib2.urlopen(sinaURL)
sinaHTML=response.read()

sec1Con=[]
# section1=sinaHTML.split('blk_yw_2')[-1].split('</ul>')[0].split('<li>')[1:-1]

# for item in section1:
#     url=item.split('href="')[1].split('"')[0]
#     date=url.split('/')[-2]
#     uid=url.split('/')[-1].rstrip('.shtml')
#     uuid=date+'-'+uid
#     name=item.split('>')[1].rstrip("</a")
#     name=name.decode('utf-8','ignore')

#     if collection.find_one({"_id":uuid})==None:
#         sec1Con.append({"_id":uuid,"date":date,"uid":uid,"date":date,"name":name,"url":url,"source":"Sina Finance"})


# section2=sinaHTML.split('blk_yw_3')[-1].split('</ul>')[0].split('<li>')[1:-1]
# for item in section2:
#     url=item.split('href="')[1].split('"')[0]
#     date=url.split('/')[-2]
#     uid=url.split('/')[-1].rstrip('.shtml')
#     uuid=date+'-'+uid
#     name=item.split('>')[1].rstrip("</a")
#     name=name.decode('utf-8','ignore')

#     if collection.find_one({"_id":uuid})==None:
#         sec1Con.append({"_id":uuid,"date":date,"uid":uid,"date":date,"name":name,"url":url,"source":"Sina Finance"})

section3=sinaHTML.split('blk_yw_4')[-1].split('</ul>')[0].split('<li>')[1:-1]
for item in section3:
    url=item.split('href="')[1].split('"')[0]
    date=url.split('/')[-2]
    uid=url.split('/')[-1].rstrip('.shtml')
    uuid=date+'-'+uid
    name=item.split('>')[1].rstrip("</a")
#    name=name.decode('utf-8','ignore')

    if collection.find_one({"_id":uuid})==None:
        sec1Con.append({"_id":uuid,"date":date,"uid":uid,"date":date,"name":name,"url":url,"source":"Sina Finance"})

#collection.insert_many(sec1Con)

print sec1Con
#for item in sec1Con:
#    print item

