import time 
import json 
import random 
from kafka import KafkaProducer

def serializer(message):
    return json.dumps(message).encode('utf-8')

def producer(topicName):
    producer = KafkaProducer(
            bootstrap_servers=['localhost:29092'],
            value_serializer=serializer
        )

    producer.send(topicName, topicName+" is a new topic")
    time_to_sleep = random.randint(1, 11)
    time.sleep(time_to_sleep)