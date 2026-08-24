from pika import BlockingConnection, ConnectionParameters, PlainCredentials
from pika.channel import Channel

connection_params = ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=PlainCredentials(username="user", password="password")
)

def consumer_callback(ch: Channel, method, properties, body):
    msg = body.decode("utf-8")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(msg)

def main():
    with BlockingConnection(connection_params) as connecton:
        with connecton.channel() as ch:
            ch.queue_declare(queue="test-messages")
            ch.basic_consume(
                queue="test-messages",
                on_message_callback=consumer_callback,
            )
            print("Жду сообщений")
            try:
                ch.start_consuming()
            except KeyboardInterrupt:
                print("Stopping")

if __name__ == "__main__":
    main()
