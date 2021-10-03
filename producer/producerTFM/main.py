from faker import Faker
from kafka import KafkaProducer
import json
import time

fake = Faker()
filename = "/home/adrian/Downloads/LOGS/TR_CL_diselsw_s39ac1.log"

def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1 == 1:
        with open(filename) as file_in:
            document = None
            for line in file_in:
                if line.startswith("2021"):
                    if document is None:
                        document = line
                    else:
                        producer.send("registered_user", document)
                        document = line
                else:
                    document = document + "\n" + line
            time.sleep(1)
            producer.send("registered_user", document)