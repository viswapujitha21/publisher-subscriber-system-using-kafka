from pubsub import pub
import sys
import requests
import json
import subprocess
import sqlite3
import os
from collections import OrderedDict

contentDictionary = OrderedDict()
contentDictionary[1] = []
contentDictionary[2] = []
contentDictionary[3] = []
contentDictionary[4] = []
contentDictionary[5] = []
contentDictionary[6] = []
contentDictionary[7] = []
contentDictionary[8] = []
contentDictionary[9] = []
contentDictionary[10] = []

#Get data from database
def getDBData(tableName):
    mydb = sqlite3.connect('/tmp/database.db')
    mycursor = mydb.cursor()
    sqlCommand = 'SELECT * FROM '+tableName
    mycursor.execute(sqlCommand)
    myresult = mycursor.fetchall()
    return myresult

#Insert data into database
def insertDBData(tableName, param1, param2, param3, param4):
    mydb = sqlite3.connect('/tmp/database.db')
    mycursor = mydb.cursor()
    if(tableName=="user"):
        sqlCommand = "INSERT INTO `user` (`Id`, `Name`, `Username`, `Password`) VALUES ('"+str(param1)+"', '"+param2+"', '"+param3+"', '"+param4+"');"
        print(sqlCommand)
    mycursor.execute(sqlCommand)
    mydb.commit()

#Update table in database
def updateDBData(tableName, param1):
    mydb = sqlite3.connect('/tmp/database.db')
    mycursor = mydb.cursor()
    if(tableName=="user_login"):
        sqlCommand = "UPDATE user SET Authenticate='true' WHERE Id='"+param1+"'"
    if(tableName=="user_logout"):
        sqlCommand = "UPDATE user SET Authenticate='false' WHERE Id='"+str(param1)+"'"
    mycursor.execute(sqlCommand)
    mydb.commit()

def getTopicList():
    topicList = ["delhi", "mumbai", "chennai"]
    return topicList

#Get real data and publish messages of the topic
def notify(topicList):
    for item in topicList:
        url = "https://indianrailways.p.rapidapi.com/findstations.php"
        querystring = {"station":item}
        headers = {
            'x-rapidapi-host': "indianrailways.p.rapidapi.com",
            'x-rapidapi-key': "45efc8d234mshdf58075678e3d40p132999jsnda9beebfaa12"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        pub.sendMessage(item,  arg={'headline': 'New Content', 'news': response.text})

#Listener functions
def listener_1(arg):
    global contentDictionary
    contentDictionary[1].append(arg['headline']+"\n")
    contentDictionary[1].append(arg['news']+"\n") 

def listener_2(arg):
    global contentDictionary
    contentDictionary[2].append(arg['headline']+"\n")
    contentDictionary[2].append(arg['news']+"\n") 

def listener_3(arg):
    global contentDictionary
    contentDictionary[3].append(arg['headline']+"\n")
    contentDictionary[3].append(arg['news']+"\n")

def listener_4(arg):
    global contentDictionary
    contentDictionary[4].append(arg['headline']+"\n")
    contentDictionary[4].append(arg['news']+"\n") 

def listener_5(arg):
    global contentDictionary
    contentDictionary[5].append(arg['headline']+"\n")
    contentDictionary[5].append(arg['news']+"\n")

def listener_6(arg):
    global contentDictionary
    contentDictionary[6].append(arg['headline']+"\n")
    contentDictionary[6].append(arg['news']+"\n")

def listener_7(arg):
    global contentDictionary
    contentDictionary[7].append(arg['headline']+"\n")
    contentDictionary[7].append(arg['news']+"\n")

def listener_8(arg):
    global contentDictionary
    contentDictionary[8].append(arg['headline']+"\n")
    contentDictionary[8].append(arg['news']+"\n")

def listener_9(arg):
    global contentDictionary
    contentDictionary[9].append(arg['headline']+"\n")
    contentDictionary[9].append(arg['news']+"\n")

def listener_10(arg):
    global contentDictionary
    contentDictionary[10].append(arg['headline']+"\n")
    contentDictionary[10].append(arg['news']+"\n") 

#Unsubscribe to a topic
def subscribe(topicList, name, listenerId):
    global contentDictionary
    for topic in topicList:
        if(listenerId=="1"):
            pub.subscribe(listener_1, topic)
            contentDictionary[1].append(name + " has subscribed to " + topic+"\n")
        elif(listenerId=="2"):
            pub.subscribe(listener_2, topic)
            contentDictionary[2].append(name + " has subscribed to " + topic+"\n")
        elif(listenerId=="3"):
            pub.subscribe(listener_3, topic)
            contentDictionary[3].append(name + " has subscribed to " + topic+"\n")
        elif(listenerId=="4"):
            pub.subscribe(listener_4, topic)
            contentDictionary[4].append(name + " has subscribed to " + topic+"\n")
        elif(listenerId=="5"):
            pub.subscribe(listener_5, topic)
            contentDictionary[5].append(name + " has subscribed to " + topic+"\n")
        elif(listenerId=="6"):
            pub.subscribe(listener_6, topic)
            contentDictionary[6].append(name + " has subscribed to " + topic+"\n")
        elif(listenerId=="7"):
            pub.subscribe(listener_7, topic)
            contentDictionary[7].append(name + " has subscribed to " + topic+"\n")
        elif(listenerId=="8"):
            pub.subscribe(listener_8, topic)
            contentDictionary[8].append(name + " has subscribed to " + topic+"\n")
        elif(listenerId=="9"):
            pub.subscribe(listener_9, topic)
            contentDictionary[9].append(name + " has subscribed to " + topic+"\n")
        elif(listenerId=="10"):
            pub.subscribe(listener_10, topic)
            contentDictionary[10].append(name + " has subscribed to " + topic+"\n")

#Unsubscribe to a topic
def unsubscribe(topicList, name, listenerId):
    global contentDictionary
    for topic in topicList:
        if(listenerId=="1"):
            pub.unsubscribe(listener_1, topic)
            contentDictionary[1].append(name + " has unsubscribe to " + topic+"\n")
        elif(listenerId=="2"):
            pub.unsubscribe(listener_2, topic)
            contentDictionary[2].append(name + " has unsubscribe to " + topic+"\n")
        elif(listenerId=="3"):
            pub.unsubscribe(listener_3, topic)
            contentDictionary[3].append(name + " has unsubscribe to " + topic+"\n")
        elif(listenerId=="4"):
            pub.unsubscribe(listener_4, topic)
            contentDictionary[4].append(name + " has unsubscribe to " + topic+"\n")
        elif(listenerId=="5"):
            pub.unsubscribe(listener_5, topic)
            contentDictionary[5].append(name + " has unsubscribe to " + topic+"\n")
        elif(listenerId=="6"):
            pub.unsubscribe(listener_6, topic)
            contentDictionary[6].append(name + " has unsubscribe to " + topic+"\n")
        elif(listenerId=="7"):
            pub.unsubscribe(listener_7, topic)
            contentDictionary[7].append(name + " has unsubscribe to " + topic+"\n")
        elif(listenerId=="8"):
            pub.unsubscribe(listener_8, topic)
            contentDictionary[8].append(name + " has unsubscribe to " + topic+"\n")
        elif(listenerId=="9"):
            pub.unsubscribe(listener_9, topic)
            contentDictionary[9].append(name + " has unsubscribe to " + topic+"\n")
        elif(listenerId=="10"):
            pub.unsubscribe(listener_10, topic)
            contentDictionary[10].append(name + " has unsubscribe to " + topic+"\n")

def getContentDictionary(listenerId):
    global contentDictionary
    return contentDictionary[listenerId]