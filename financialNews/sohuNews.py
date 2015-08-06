#!/usr/bin/env python

import sys,urllib,urllib2,pymongo
from pymongo import MongoClient
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf-8')

class sohuNews:
    def __init__(self):
        self.contents=[]
        mongoClient=MongoClient('localhost',27017)
        db=mongoClient.finance
        self.connection=db.cnnews
        self.rss1="http://rss.business.sohu.com/rss/gongsixinwen.xml"
        self.rss=''

    def getRSS(self):
        response=urllib2.urlopen(self.rss1)
        self.rss=response.read()


    # def extractContent(self):
    #     root.Element("

sohu=sohuNews()
sohu.getRSS()
