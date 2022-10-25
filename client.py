import sys

import pika
import logging
import socket


def send_data_to_server(id: str, dna: str):
    """Send id and DNA of person to server"""
    logging.debug("start sending data to server")
    client_socket = socket.socket()
    client_socket.connect(('localhost', 5000))
    message = dna + ' ' + id
    client_socket.send(message.encode())
    client_socket.close()
    logging.debug("finish sending data to server")


def execute_client():
    """Main executing client"""

    # First part of client work
    logging.debug("start sending DNA")
    print("Enter id: ", flush=True, end='')
    id = sys.stdin.readline()[:-1]
    print("Enter DNA: ", flush=True, end='')
    DNA = sys.stdin.readline()[:-1]

    # Second part of client work
    logging.debug("open rabbit channel for giving hospital messages")
    params = pika.ConnectionParameters(host='localhost')
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='logs', queue=queue_name)

    def callback(_0, _1, _2, msg):
        """Printing essential messages"""
        msg = str(msg)[2:-1]
        logging.debug(f"Message recieved. Message is {msg}")
        if id in msg:
            print(msg)

    send_data_to_server(id=id, dna=DNA)
    while True:
        logging.debug("wait hospital messages")
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            logging.debug("keyboard intertupt")
            channel.stop_consuming()
            break
        except Exception:
            channel.stop_consuming()
            logging.warning("exception")

    logging.debug("close rabbit channel")
    channel.close()


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.getLogger("pika").propagate = False
    execute_client()