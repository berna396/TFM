from datetime import datetime
from pymongo import MongoClient
import smtplib

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    server = smtplib.SMTP('imap.gmail.com', 587)
    server.starttls()
    server.login('testalertingtfm@gmail.com', 'testalerting')
    server.sendmail('testalertingTFM@gmail.com', 'testalertingTFM@gmail.com', 'prueba')



    client = MongoClient("mongodb://mongo:mongo@127.0.0.1:27017")
    print("Connection Successful")
    mydb = client["alerting"]
    mycol = mydb["alert"]

    mydict = {"type": "unknown", "text": "prueba", "date" : datetime.now()}

    x = mycol.insert_one(mydict)
    client.close

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
