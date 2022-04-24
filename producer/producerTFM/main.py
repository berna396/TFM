import now as now
from faker import Faker
from kafka import KafkaProducer
from random import randrange
import json
from datetime import datetime

fake = Faker()
filename = "/home/adrian/Downloads/LOGS/TR_CL_diselsw_s39ac1.log"


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


# producer = KafkaProducer(bootstrap_servers=['192.168.1.63:9092'],
#                         value_serializer=json_serializer)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    for i in range(0, 1000000):
        with open(filename, encoding='latin-1') as file_in:
            document = None
            for line in file_in:
                if line.startswith("2021"):
                    if document is None:
                        document = line
                    else:
                        print(document)
                        producer.send("registered_user", document)
                        document = line
                else:
                    document = document + "\n" + line
            producer.send("registered_user", document)
#    print("Current Time =", datetime.now().time())
#    producer.send("registered_user", "prueba4")
