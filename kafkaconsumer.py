from confluent_kafka import Consumer

consumer_config = {
    'bootstrap.servers':'localhost:9092',
    "group.id":'test-consumer-group',
    "auto.offset.reset":'earliest'
}

def consumer_callback(*args):
    for arg in args:
        print(arg)

def main():
    with Consumer(consumer_config) as consumer:
        consumer.subscribe(
            topics=['multi-partition'],
        )
        try:
            while True:
                msg = consumer.poll(2.0)
                if msg == None:
                    continue
                if msg.error():
                    print(f"{msg.error()}")
                    continue
                key = msg.key().decode('utf-8') if msg.key() else None
                value = msg.value().decode('utf-8') if msg.value() else None
                print(f"Сообщение получено: {key}: {value}")
        except KeyboardInterrupt:
            print("Stopping")
        finally:
            consumer.close()
        consumer.close()


if __name__ == '__main__':
    main()
