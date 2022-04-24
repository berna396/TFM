from faker import Faker
from kafka import KafkaProducer
from random import randrange
import json
import time

fake = Faker()
filename = "/home/adrian/Downloads/LOGS/TR_CL_diselsw_s39ac1.log"


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


#producer = KafkaProducer(bootstrap_servers=['192.168.1.63:9092'],
#                         value_serializer=json_serializer)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    for x in range(100):
        producer.send("registered_user", "holi")

