from confluent_kafka import Producer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import SerializationContext, MessageField
import json

user_schema_str = """
{
    "type": "record",
    "name": "User",
    "fields": [
        {"name": "user_id", "type": "int"},
        {"name": "action", "type": "string"},
        {"name": "timestamp", "type": "long"}
    ]
}
"""

schema_registry_config = {
    "url": "http://127.0.0.1:8081"
}

schema_registry_client = SchemaRegistryClient(schema_registry_config)


avro_serializer = AvroSerializer(
    schema_registry_client, # type: ignore
    user_schema_str,
)

producer_config = {
    "bootstrap.servers": "localhost:29092",
    "acks": "all",
    "enable.idempotence": True,
    "retries": 5,
    "delivery.timeout.ms": 1000,
}

producer = Producer(producer_config)

message = {
    "user_id": 1,
    "action": "created",
    "timestamp": 121243241
}

def producer_callback(*args):
    for arg in args:
        print(arg)

def main():
    producer.produce(
        topic="multi-partition",
        key="key",
        value=avro_serializer(message, SerializationContext("users-avro", MessageField.VALUE)),
        callback=producer_callback,
    )
    producer.flush()

if __name__ == "__main__":
    main()