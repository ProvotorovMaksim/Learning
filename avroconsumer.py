from confluent_kafka import Consumer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer
from confluent_kafka.serialization import SerializationContext, StringDeserializer, MessageField

schema_registry_config = {
    "url": "http://127.0.0.1:8081"
}

schema_registry_client = SchemaRegistryClient(schema_registry_config)

avro_deserializer = AvroDeserializer(
    schema_registry_client, # type: ignore
    )

consumer_config = {
    'bootstrap.servers':'localhost:29092',
    "group.id":'test-consumer-group',
    "auto.offset.reset":'earliest'
}

def main():
    with Consumer(consumer_config) as consumer:
        consumer.subscribe(topics=["multi-partition"])
        try:
            while True:
                msg = consumer.poll(1.0)
                if msg == None:
                        continue
                if msg.error():
                    print(f"{msg.error()}")
                    continue
                key = msg.key().decode("utf-8") if msg.key() else None
                value = avro_deserializer(msg.value(), SerializationContext("users-avro", MessageField.VALUE))
                print(f"Сообщение получено: {key}: {value}")
        except KeyboardInterrupt:
            print("Stopping")
        finally:
            consumer.close()
        consumer.close()

if __name__ == "__main__":
    main()