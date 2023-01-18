from confluent_kafka import Producer
import json
import time
import random

names = ['John', 'Emma', 'Emily', 'Jacob', 'Michael', 'Madison', 'Olivia', 'William', 'Ava', 'Isabella']
lastname = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
age = [i for i in range(18, 100)]

producer = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_msg(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} in partition {msg.partition()}')
        print(f'Offset: {msg.offset()}')

for i in range(20):
    data = {'id': i, 'Firstname': random.choice(names), 'Lastname': random.choice(lastname), 'Age': random.choice(age)}
    producer.produce('new_row', json.dumps(data), callback=delivery_msg)
    producer.poll(0)
    time.sleep(1)

producer.flush()