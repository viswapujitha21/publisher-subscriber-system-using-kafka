import json 
from kafka import KafkaConsumer

def consumer(topicName):
    consumer = KafkaConsumer(
        topicName,
        bootstrap_servers='localhost:29092',
        auto_offset_reset='earliest'
    )
    for message in consumer:
        print(json.loads(message.value))
    consumer.close()