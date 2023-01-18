from confluent_kafka.admin import AdminClient, NewTopic

login = AdminClient({'bootstrap.servers': 'localhost:9092'})
data = NewTopic("new_row", num_partitions=3, replication_factor=1)

topic = login.create_topics([data])

for data, f in topic.items():
    f.result()
    print(f"New Topic {data} created")
