#!/usr/bin/env python

import sys, urllib, urllib2, pymongo
from pymongo import MongoClient
reload(sys)
sys.setdefaultencoding("utf-8")

class SinaFinancialNews:

    #intialize section contents
    def __init__(self):
        self.secCon=[]
    #setup localhost mongodb conenctor
        mongoClient=MongoClient('localhost',27017)
        db=mongoClient.finance
        self.collection=db.cnnews

    #query html page
    def getHTMLNewsPage(self):
        sinaURL="http://finance.sina.com.cn"
        response=urllib2.urlopen(sinaURL)
        sinaHTML=response.read()
        return sinaHTML

    #find section header url, name uid with given section name
    #fine from m-list-container
    def getNewsFromSection(self,secName,sinaHTML):
        section=sinaHTML.split(secName)[-1].split('</ul>')[0].split('<li>')[1:-1]
        for item in section:
            url=item.split('href="')[1].split('"')[0].strip()
            date=url.split('/')[-2]
            uid=url.split('/')[-1].rstrip('.shtml')
            uuid=date+'-'+uid
            name=item.split('>')[1].rstrip("</a")
            name=name.decode('gbk').encode('utf-8')
            
            #confirm item not exist in mongo db
            if self.collection.find_one({"_id":uuid})==None:
                self.secCon.append({"_id":uuid,"date":date,"uid":uid,"date":date,"name":name,"url":url,"source":"Sina Finance"})
    
    #fine h3 news from blk_yw_1
    def getHeaderNewsFromNews(self,sinaHTML):
        section=sinaHTML.split('blk_yw_1')[-1].split('</div>')[0].split('href="')[1:]

        for item in section:
            url=item.split('"')[0].strip()
            if url.split('.')[-1]=='shtml':
                date=url.split('/')[-2]
                uid=url.split('/')[-1].rstrip('.shtml')
                uuid=date+'-'+uid
                name=item.split('>')[1].rstrip('</a>')
                name=name.decode('gbk').encode('utf-8')
                
                #confirm item not exist in mongo db
                if self.collection.find_one({"_id":uuid})==None:
                    self.secCon.append({"_id":uuid,"date":date,"uid":uid,"date":date,"name":name,"url":url,"source":"Sina Finance"})

        
    

    #get all items 
    def getAllSections(self):
        page=self.getHTMLNewsPage()

        #get news from blk_yw_1
        self.getHeaderNewsFromNews(page)

        for sec in ['blk_yw_2','blk_yw_3','blk_yw_4']:
            self.getNewsFromSection(sec,page)

    #print out extracted secCon which inserts into mongodb
    def printSection(self):
        print len(self.secCon)
        for item in self.secCon:
            print item["_id"]
            print item
            print ''
        print self.secCon

    def insertIntoMongo(self):
        if(len(self.secCon)>0):
            self.collection.insert_many(self.secCon)


#get sina finance news and insert into mongo
sina=SinaFinancialNews()
sina.getAllSections()
#sina.printSection()
sina.insertIntoMongo()
