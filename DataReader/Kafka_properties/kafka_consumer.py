# hackathon/Kafka_properties/kafka_consumer.py
from kafka import KafkaConsumer
import Kafka_properties.kafka_config as kafka_config
import json

def create_consumer(topic):
    return KafkaConsumer(
        topic,
        bootstrap_servers=kafka_config.KAFKA_BOOTSTRAP_SERVERS,
        security_protocol=kafka_config.KAFKA_SECURITY_PROTOCOL,
        sasl_mechanism=kafka_config.KAFKA_SASL_MECHANISM,
        sasl_plain_username=kafka_config.KAFKA_SASL_USERNAME,
        sasl_plain_password=kafka_config.KAFKA_SASL_PASSWORD,
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        group_id='group_id',
        auto_offset_reset='earliest'
    )

def consume_messages(topic):
    consumer = create_consumer(topic)
    for message in consumer:
        print(f"Received message: {message.value}")
