from confluent_kafka import Producer

producer_config = {
    'bootstrap.servers':'localhost:9092',
    'acks':'all',
    'enable.idempotence': True,
    'retries': 5,
    'delivery.timeout.ms': 1000,
}

producer = Producer(producer_config)

def producer_callback(*args):
    for arg in args:
        print(arg)

def main():
    for i in range(5):
        producer.produce(
            topic='multi-partition',
            key=f"{i}",
            value="Hello Kafka!",
            callback=producer_callback,
        )

    producer.flush()

if __name__ == '__main__':
    main()
