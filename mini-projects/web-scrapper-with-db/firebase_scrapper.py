# pip install bs4
# pip install requests
from bs4 import BeautifulSoup
import requests
import pyrebase
import json

firebase_config = {
    'apiKey': "AIzaSyBfePZU1LMCmrwxFqLYXiQF_n132SdZhC4",
    'authDomain': "fruitsbase.firebaseapp.com",
    'projectId': "fruitsbase",
    'storageBucket': "fruitsbase.appspot.com",
    'messagingSenderId': "445383361070",
    'appId': "1:445383361070:web:4210d09aabe8622619d5bf",
    'measurementId': "G-QCV1XJRVHR",

    # Add this line
    'databaseURL':'https://fruitsbase-default-rtdb.firebaseio.com/'
}
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()
# db.child("fruit").set({"name":"olma"})

def getDataAndWriteData():
    url = "https://statusycitaty.ru/statusyi-o-sebe/statusyi-pro-sebya-smeshnyie.html"
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")
    notes = soup.findAll("div", class_="stickynote", )
    slist = []
    for i in notes:
        slist.append(i.p.text)

    for x in range(len(slist)):
        item = slist[x]
        db.child("notes").push(
            {f"id{x}": f"{item}"}
        )
    print("Successfully")

def writeDataToJson():
    d = db.child("notes").get()
    data = []
    for i,k in d.val().items():
        data.append(k)
    notesDict = {}
    for x in range(len(data) - 1):
        notesDict.update(data[x])
        if len(notesDict) != 0:
            jdata = json.dumps(notesDict)
            return jdata
notes = writeDataToJson()

print(type(notes))
print(notes)
# print(type(soup))
# print(dir(soup))
