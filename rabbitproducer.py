from pika import BlockingConnection, ConnectionParameters, PlainCredentials

connection_params = ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=PlainCredentials(username="user", password="password")
)

def main():
    with BlockingConnection(connection_params) as connecton:
        with connecton.channel() as ch:
            ch.queue_declare(queue="test-messages")
            ch.basic_publish(
                exchange="",
                routing_key="test-messages",
                body="Hello RabbitMQ!",
            ) # type: ignore
            print("Message sent!")

if __name__ == "__main__":
    main()
