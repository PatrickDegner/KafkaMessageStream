from confluent_kafka import Consumer
import json

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'message_stream',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['new_row'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print(f'Consumer error: {msg.error()}')
        continue

    print(f'Consumed message: {json.loads(msg.value())}')

consumer.close()