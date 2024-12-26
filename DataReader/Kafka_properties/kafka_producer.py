from kafka import KafkaProducer
import  kafka_config
import json

def create_producer():
    return KafkaProducer(
        bootstrap_servers=kafka_config.KAFKA_BOOTSTRAP_SERVERS,
        security_protocol=kafka_config.KAFKA_SECURITY_PROTOCOL,
        sasl_mechanism=kafka_config.KAFKA_SASL_MECHANISM,
        sasl_plain_username=kafka_config.KAFKA_SASL_USERNAME,
        sasl_plain_password=kafka_config.KAFKA_SASL_PASSWORD,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

def send_message(topic, message):
    producer = create_producer()
    producer.send(topic, message)
    producer.flush()
    print(f"Message sent to topic {topic}: {message}")
